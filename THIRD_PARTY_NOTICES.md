# 第三方组件与许可

VideoToGif 使用下列第三方组件。作者自有源码不公开；第三方组件的版权、许可和相应权利不受影响。允许依据相应许可修改第三方库，以及为调试此类修改进行逆向工程。

| 组件 | 版本 | 许可证与版权资料 |
| --- | --- | --- |
| FFmpegKit | Android full 6.0-2 | LGPL-3.0；[LGPL 正文](third_party/ffmpeg-kit/COPYING.LGPLv3)、[GPL 正文](third_party/ffmpeg-kit/COPYING.GPLv3)；Copyright FFmpegKit / Taner Sener，详见上游源码版权头 |
| FFmpeg | n6.0 | LGPL-3.0-or-later（本发行构建）；Copyright FFmpeg developers，详见上游各源码文件 |
| Smart Exception common / java | 0.2.1 | [BSD-3-Clause，含 Taner Sener 版权声明](third_party/smart-exception-LICENSE) |
| Lucide / Feather 衍生图标 | 图标资源 | [ISC / MIT，含各作者版权声明](third_party/lucide-LICENSE) |
| LLVM libc++ 及运行时支持 | Android LLVM 修订 87f1315dfbea7c137aa2e6d362dbb457e388158d | [libc++](third_party/llvm/libcxx-LICENSE.txt)、[libc++abi](third_party/llvm/libcxxabi-LICENSE.txt)、[libunwind](third_party/llvm/libunwind-LICENSE.txt)、[compiler-rt](third_party/llvm/compiler-rt-LICENSE.txt)：Apache-2.0 WITH LLVM-exception 及文件内列明的许可与版权 |

## FFmpegKit 包内外部组件

以下文本保留 FFmpegKit AAR 所附许可及版权声明，覆盖直接及传递依赖。FreeType 使用 FTL 许可选项；libiconv 库使用 LGPL 许可，其所附 GPL 文件不表示本应用启用了 GPL 版 FFmpeg。

| 组件 | 许可 | 原文 |
| --- | --- | --- |
| cpu-features | Apache-2.0 | [许可及版权](third_party/ffmpeg-kit/license_cpu_features.txt) |
| dav1d | BSD-2-Clause | [许可及版权](third_party/ffmpeg-kit/license_dav1d.txt) |
| expat | MIT | [许可及版权](third_party/ffmpeg-kit/license_expat.txt) |
| fontconfig | MIT | [许可及版权](third_party/ffmpeg-kit/license_fontconfig.txt) |
| freetype | FTL | [许可及版权](third_party/ffmpeg-kit/license_freetype.txt) |
| fribidi | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_fribidi.txt) |
| giflib | MIT | [许可及版权](third_party/ffmpeg-kit/license_giflib.txt) |
| gmp | LGPL-3.0-or-later | [许可及版权](third_party/ffmpeg-kit/license_gmp.txt) |
| gnutls | LGPL-2.1-or-later（库） | [许可及版权](third_party/ffmpeg-kit/license_gnutls.txt) |
| harfbuzz | MIT 及文件内附加条款 | [许可及版权](third_party/ffmpeg-kit/license_harfbuzz.txt) |
| jpeg | IJG / BSD / zlib，见原文 | [许可及版权](third_party/ffmpeg-kit/license_jpeg.txt) |
| kvazaar | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_kvazaar.txt) |
| lame | LGPL-2.0-or-later | [许可及版权](third_party/ffmpeg-kit/license_lame.txt) |
| libass | ISC | [许可及版权](third_party/ffmpeg-kit/license_libass.txt) |
| libiconv | LGPL-2.1-or-later（库）；包内 GPL 文本另保留 | [许可及版权](third_party/ffmpeg-kit/license_libiconv.txt) |
| libilbc | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libilbc.txt) |
| libogg | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libogg.txt) |
| libpng | libpng 许可 | [许可及版权](third_party/ffmpeg-kit/license_libpng.txt) |
| libsndfile | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_libsndfile.txt) |
| libtheora | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libtheora.txt) |
| libuuid | Modified BSD | [许可及版权](third_party/ffmpeg-kit/license_libuuid.txt) |
| libvorbis | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libvorbis.txt) |
| libvpx | BSD-3-Clause 及专利授权 | [许可及版权](third_party/ffmpeg-kit/license_libvpx.txt) |
| libwebp | BSD-3-Clause 及专利授权 | [许可及版权](third_party/ffmpeg-kit/license_libwebp.txt) |
| libxml2 | MIT 及文件内附加条款 | [许可及版权](third_party/ffmpeg-kit/license_libxml2.txt) |
| nettle | LGPL-3.0-or-later / GPL-2.0-or-later 双许可（采用 LGPL） | [许可及版权](third_party/ffmpeg-kit/license_nettle.txt) |
| opencore-amr | Apache-2.0 | [许可及版权](third_party/ffmpeg-kit/license_opencore_amr.txt) |
| opus | BSD-3-Clause 及专利授权 | [许可及版权](third_party/ffmpeg-kit/license_opus.txt) |
| shine | LGPL-2.0-or-later | [许可及版权](third_party/ffmpeg-kit/license_shine.txt) |
| snappy | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_snappy.txt) |
| soxr | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_soxr.txt) |
| speex | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_speex.txt) |
| tiff | libtiff 许可 | [许可及版权](third_party/ffmpeg-kit/license_tiff.txt) |
| twolame | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_twolame.txt) |
| vo-amrwbenc | Apache-2.0 | [许可及版权](third_party/ffmpeg-kit/license_vo_amrwbenc.txt) |
| zimg | WTFPL-2.0 | [许可及版权](third_party/ffmpeg-kit/license_zimg.txt) |

FreeType 许可正文见 [FTL](third_party/ffmpeg-kit/freetype-FTL.TXT)。Portions of this software are copyright © 2023 The FreeType Project (www.freetype.org). All rights reserved.

libvpx 专利授权见 [PATENTS](third_party/ffmpeg-kit/libvpx-PATENTS)。

libiconv 的 LGPL 库许可补充见 [COPYING.LIB](third_party/ffmpeg-kit/libiconv-COPYING.LIB)。各许可的完整正文及文件内例外条款优先于本索引中的简称。

## 上游源码与构建资料

- [FFmpegKit v6.0](https://github.com/arthenica/ffmpeg-kit/tree/d6be56d7aec286eb3c292d6b23ff07a6b70d8693)：Android 构建脚本与 LGPL 许可。
- [FFmpegKit 外部依赖源码版本映射](https://github.com/arthenica/ffmpeg-kit/blob/d6be56d7aec286eb3c292d6b23ff07a6b70d8693/scripts/source.sh)。
- [FFmpeg n6.0](https://github.com/arthenica/FFmpeg/tree/n6.0)。
- [Smart Exception v0.2.1](https://github.com/tanersener/smart-exception/tree/v0.2.1)。
- LLVM 许可取自 [APK 所含运行库对应的 Android LLVM 修订](https://android.googlesource.com/toolchain/llvm-project/+/87f1315dfbea7c137aa2e6d362dbb457e388158d/)。
