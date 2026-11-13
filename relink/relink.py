"""Recombine VideoToGif application objects with interface-compatible LGPL libraries.
No source code, original signing key or Gradle build is needed. Output is unsigned.
"""
import argparse
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import zipfile

BASE_SHA256 = '31e1f5eb6d9b8abe625058fab17ae37aa14f118dc7f98e720abd0fef2aceb2e6'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('apk', 'aar', 'smart_common', 'smart_java', 'android_jar', 'build_tools', 'jdk', 'output'):
        parser.add_argument('--' + key.replace('_', '-'), required=True, type=Path)
    parser.add_argument('--objects', type=Path, default=Path(__file__).with_name('VideoToGif_1.0.0-application-objects.jar'))
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists; select a new filename.')
    if hashlib.sha256(args.apk.read_bytes()).hexdigest() != BASE_SHA256:
        parser.error('This object package is for the original 1.0.0 APK only.')
    java = args.jdk / 'bin' / ('java.exe' if os.name == 'nt' else 'java')
    align = args.build_tools / ('zipalign.exe' if os.name == 'nt' else 'zipalign')
    root = Path(__file__).resolve().parent.parent
    with tempfile.TemporaryDirectory(prefix='videotogif-relink-') as temp:
        temp = Path(temp)
        dex = temp / 'dex'
        dex.mkdir()
        with zipfile.ZipFile(args.aar) as aar, zipfile.ZipFile(args.apk) as original:
            classes = temp / 'ffmpegkit.jar'
            classes.write_bytes(aar.read('classes.jar'))
            natives = {}
            for name in aar.namelist():
                if name.startswith('jni/') and name.endswith('.so'):
                    if '..' in PurePosixPath(name).parts:
                        raise ValueError('Invalid native library path')
                    natives['lib/' + name[4:]] = name
            required = {n for n in original.namelist() if n.startswith('lib/') and n.endswith('.so')}
            if not required.issubset(natives):
                raise ValueError('Replacement AAR must supply all original ABI libraries: ' + str(sorted(required - natives.keys())))
            subprocess.run([str(java), '-cp', str(args.build_tools / 'lib/d8.jar'),
                            'com.android.tools.r8.D8', '--release', '--min-api', '26',
                            '--lib', str(args.android_jar), '--output', str(dex),
                            str(args.objects), str(classes), str(args.smart_common), str(args.smart_java)], check=True)
            raw = temp / 'recombined.apk'
            with zipfile.ZipFile(raw, 'w') as out:
                for item in original.infolist():
                    name = item.filename
                    if re.fullmatch(r'classes\d*\.dex', name) or name in required:
                        continue
                    if name.upper().startswith('META-INF/') and (name.upper().endswith(('.SF', '.RSA', '.DSA', '.EC')) or name.upper() == 'META-INF/MANIFEST.MF'):
                        continue
                    out.writestr(item, original.read(name))
                for file in sorted(dex.glob('*.dex')):
                    out.write(file, file.name, compress_type=zipfile.ZIP_STORED)
                for name, entry in sorted(natives.items()):
                    out.writestr(name, aar.read(entry), compress_type=zipfile.ZIP_STORED)
                # License delivery is independent of Android compiled resource names.
                for file in sorted((root / 'third_party').rglob('*')):
                    if file.is_file():
                        out.write(file, 'assets/third_party/' + file.relative_to(root / 'third_party').as_posix(), compress_type=zipfile.ZIP_DEFLATED)
                out.write(root / 'THIRD_PARTY_NOTICES.md', 'assets/third_party/THIRD_PARTY_NOTICES.md', compress_type=zipfile.ZIP_DEFLATED)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([str(align), '-P', '16', '4', str(raw), str(args.output)], check=True)
        subprocess.run([str(align), '-c', '-P', '16', '4', str(args.output)], check=True)
    print('Unsigned APK:', args.output.resolve())
    print('SHA256:', hashlib.sha256(args.output.read_bytes()).hexdigest())
    print('Sign with your own key before installation; this does not replace the original APK.')

if __name__ == '__main__':
    main()
