# 第三方组件与许可

VideoToGif 使用下列第三方组件。作者自有源码不公开；第三方组件的版权、许可和相应权利不受影响。允许依据相应许可修改第三方库，以及为调试此类修改进行逆向工程。

| 组件 | 版本 | 许可证与版权资料 |
| --- | --- | --- |
| FFmpegKit | Android full 6.0-2 | LGPL-3.0；[LGPL 正文](third_party/ffmpeg-kit/COPYING.LGPLv3)、[GPL 正文](third_party/ffmpeg-kit/COPYING.GPLv3)；Copyright FFmpegKit / Taner Sener，详见上游源码版权头 |
| FFmpeg | n6.0 | LGPL-3.0-or-later（本发行构建）；Copyright FFmpeg developers，详见上游各源码文件 |
| Smart Exception common / java | 0.2.1 | [BSD-3-Clause，含 Taner Sener 版权声明](third_party/smart-exception-LICENSE) |
| Lucide / Feather 衍生图标 | 独立 SVG，对应官方修订 64502ae | [ISC / MIT，含各作者版权声明](third_party/lucide-LICENSE) |
| LLVM libc++ 及运行时支持 | Android LLVM 修订 87f1315dfbea7c137aa2e6d362dbb457e388158d | [libc++](third_party/llvm/libcxx-LICENSE.txt)、[libc++abi](third_party/llvm/libcxxabi-LICENSE.txt)、[libunwind](third_party/llvm/libunwind-LICENSE.txt)、[compiler-rt](third_party/llvm/compiler-rt-LICENSE.txt)：Apache-2.0 WITH LLVM-exception 及文件内列明的许可与版权 |

## FFmpegKit 包内外部组件

版本和对应源码依据 FFmpegKit 官方 [Source v6.0](https://github.com/arthenica/ffmpeg-kit/wiki/Source-v6.0)；以下文本保留 AAR 所附版权声明，覆盖直接及传递依赖。FreeType 使用 FTL 许可选项；libiconv 库使用 LGPL 许可，其所附 GPL 文件不表示本应用启用了 GPL 版 FFmpeg。

| 组件 | v6.0 对应版本 | 许可 | 随附文本 | 官方源码 | 官方许可 |
| --- | --- | --- | --- | --- | --- |
| cpu-features | v0.8.0 | Apache-2.0 | [许可及版权](third_party/ffmpeg-kit/license_cpu_features.txt) | [源码](https://github.com/arthenica/cpu_features/tree/v0.8.0) | [许可](https://github.com/arthenica/cpu_features/blob/v0.8.0/LICENSE) |
| dav1d | 1.2.1 | BSD-2-Clause | [许可及版权](third_party/ffmpeg-kit/license_dav1d.txt) | [源码](https://github.com/arthenica/dav1d/tree/1.2.1) | [许可](https://github.com/arthenica/dav1d/blob/1.2.1/COPYING) |
| expat | R_2_5_0 | MIT | [许可及版权](third_party/ffmpeg-kit/license_expat.txt) | [源码](https://github.com/arthenica/libexpat/tree/R_2_5_0) | [许可](https://github.com/arthenica/libexpat/blob/R_2_5_0/expat/COPYING) |
| fontconfig | 2.14.2 | MIT | [许可及版权](third_party/ffmpeg-kit/license_fontconfig.txt) | [源码](https://github.com/arthenica/fontconfig/tree/2.14.2) | [许可](https://github.com/arthenica/fontconfig/blob/2.14.2/COPYING) |
| freetype | VER-2-13-0 | FTL | [许可及版权](third_party/ffmpeg-kit/license_freetype.txt) | [源码](https://github.com/arthenica/freetype2/tree/VER-2-13-0) | [许可](https://github.com/arthenica/freetype2/blob/VER-2-13-0/docs/FTL.TXT) |
| fribidi | v1.0.13 | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_fribidi.txt) | [源码](https://github.com/arthenica/fribidi/tree/v1.0.13) | [许可](https://github.com/arthenica/fribidi/blob/v1.0.13/COPYING) |
| giflib | 5.2.1 | MIT | [许可及版权](third_party/ffmpeg-kit/license_giflib.txt) | [源码](https://github.com/arthenica/giflib/tree/5.2.1) | [许可](https://github.com/arthenica/giflib/blob/5.2.1/COPYING) |
| gmp | v6.2.1 | LGPL-3.0-or-later | [许可及版权](third_party/ffmpeg-kit/license_gmp.txt) | [源码](https://github.com/arthenica/gmp/tree/v6.2.1) | [许可](https://github.com/arthenica/gmp/blob/v6.2.1/COPYING.LESSERv3) |
| gnutls | 3.7.9 | LGPL-2.1-or-later（库） | [许可及版权](third_party/ffmpeg-kit/license_gnutls.txt) | [源码](https://github.com/arthenica/gnutls/tree/3.7.9) | [许可](https://github.com/arthenica/gnutls/blob/3.7.9/doc/COPYING.LESSER) |
| harfbuzz | 8.0.1 | MIT 及文件内附加条款 | [许可及版权](third_party/ffmpeg-kit/license_harfbuzz.txt) | [源码](https://github.com/arthenica/harfbuzz/tree/8.0.1) | [许可](https://github.com/arthenica/harfbuzz/blob/8.0.1/COPYING) |
| jpeg | 3.0.0 | IJG / BSD / zlib，见原文 | [许可及版权](third_party/ffmpeg-kit/license_jpeg.txt) | [源码](https://github.com/arthenica/libjpeg-turbo/tree/3.0.0) | [许可](https://github.com/arthenica/libjpeg-turbo/blob/3.0.0/LICENSE.md) |
| kvazaar | v2.2.0 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_kvazaar.txt) | [源码](https://github.com/arthenica/kvazaar/tree/v2.2.0) | [许可](https://github.com/arthenica/kvazaar/blob/v2.2.0/LICENSE) |
| lame | RELEASE__3_100 | LGPL-2.0-or-later | [许可及版权](third_party/ffmpeg-kit/license_lame.txt) | [源码](https://github.com/arthenica/lame/tree/RELEASE__3_100) | [许可](https://github.com/arthenica/lame/blob/RELEASE__3_100/lame/COPYING) |
| libass | 0.17.1 | ISC | [许可及版权](third_party/ffmpeg-kit/license_libass.txt) | [源码](https://github.com/arthenica/libass/tree/0.17.1) | [许可](https://github.com/arthenica/libass/blob/0.17.1/COPYING) |
| libiconv | v1.17 | LGPL-2.1-or-later（库）；包内 GPL 文本另保留 | [许可及版权](third_party/ffmpeg-kit/license_libiconv.txt) | [源码](https://github.com/arthenica/libiconv/tree/v1.17) | [许可](https://github.com/arthenica/libiconv/blob/v1.17/COPYING.LIB) |
| libilbc | v3.0.4 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libilbc.txt) | [源码](https://github.com/arthenica/libilbc/tree/v3.0.4) | [许可](https://github.com/arthenica/libilbc/blob/v3.0.4/COPYING) |
| libogg | v1.3.5 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libogg.txt) | [源码](https://github.com/arthenica/ogg/tree/v1.3.5) | [许可](https://github.com/arthenica/ogg/blob/v1.3.5/COPYING) |
| libpng | v1.6.40 | libpng 许可 | [许可及版权](third_party/ffmpeg-kit/license_libpng.txt) | [源码](https://github.com/arthenica/libpng/tree/v1.6.40) | [许可](https://github.com/arthenica/libpng/blob/v1.6.40/LICENSE) |
| libsndfile | 1.2.0 | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_libsndfile.txt) | [源码](https://github.com/arthenica/libsndfile/tree/1.2.0) | [许可](https://github.com/arthenica/libsndfile/blob/1.2.0/COPYING) |
| libtheora | v1.1.1 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libtheora.txt) | [源码](https://github.com/arthenica/theora/tree/v1.1.1) | [许可](https://github.com/arthenica/theora/blob/v1.1.1/COPYING) |
| libuuid | libuuid-1.0.3 | Modified BSD | [许可及版权](third_party/ffmpeg-kit/license_libuuid.txt) | [源码](https://github.com/arthenica/libuuid/tree/libuuid-1.0.3) | [许可](https://github.com/arthenica/libuuid/blob/libuuid-1.0.3/COPYING) |
| libvorbis | v1.3.7 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_libvorbis.txt) | [源码](https://github.com/arthenica/vorbis/tree/v1.3.7) | [许可](https://github.com/arthenica/vorbis/blob/v1.3.7/COPYING) |
| libvpx | v1.13.0 | BSD-3-Clause 及专利授权 | [许可及版权](third_party/ffmpeg-kit/license_libvpx.txt) | [源码](https://github.com/arthenica/libvpx/tree/v1.13.0) | [许可](https://github.com/arthenica/libvpx/blob/v1.13.0/LICENSE) |
| libwebp | v1.3.1 | BSD-3-Clause 及专利授权 | [许可及版权](third_party/ffmpeg-kit/license_libwebp.txt) | [源码](https://github.com/arthenica/libwebp/tree/v1.3.1) | [许可](https://github.com/arthenica/libwebp/blob/v1.3.1/COPYING) |
| libxml2 | v2.11.4 | MIT 及文件内附加条款 | [许可及版权](third_party/ffmpeg-kit/license_libxml2.txt) | [源码](https://github.com/arthenica/libxml2/tree/v2.11.4) | [许可](https://github.com/arthenica/libxml2/blob/v2.11.4/Copyright) |
| nettle | nettle_3.8.1_release_20220727 | LGPL-3.0-or-later / GPL-2.0-or-later 双许可（采用 LGPL） | [许可及版权](third_party/ffmpeg-kit/license_nettle.txt) | [源码](https://github.com/arthenica/nettle/tree/nettle_3.8.1_release_20220727) | [许可](https://github.com/arthenica/nettle/blob/nettle_3.8.1_release_20220727/COPYING.LESSERv3) |
| opencore-amr | v0.1.6 | Apache-2.0 | [许可及版权](third_party/ffmpeg-kit/license_opencore_amr.txt) | [源码](https://github.com/arthenica/opencore-amr/tree/v0.1.6) | [许可](https://github.com/arthenica/opencore-amr/blob/v0.1.6/LICENSE) |
| opus | v1.4 | BSD-3-Clause 及专利授权 | [许可及版权](third_party/ffmpeg-kit/license_opus.txt) | [源码](https://github.com/arthenica/opus/tree/v1.4) | [许可](https://github.com/arthenica/opus/blob/v1.4/COPYING) |
| shine | 3.1.1 | LGPL-2.0-or-later | [许可及版权](third_party/ffmpeg-kit/license_shine.txt) | [源码](https://github.com/arthenica/shine/tree/3.1.1) | [许可](https://github.com/arthenica/shine/blob/3.1.1/COPYING) |
| snappy | 1.1.9 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_snappy.txt) | [源码](https://github.com/arthenica/snappy/tree/1.1.9) | [许可](https://github.com/arthenica/snappy/blob/1.1.9/COPYING) |
| soxr | 0.1.3 | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_soxr.txt) | [源码](https://github.com/arthenica/soxr/tree/0.1.3) | [许可](https://github.com/arthenica/soxr/blob/0.1.3/LICENCE) |
| speex | Speex-1.2.1 | BSD-3-Clause | [许可及版权](third_party/ffmpeg-kit/license_speex.txt) | [源码](https://github.com/arthenica/speex/tree/Speex-1.2.1) | [许可](https://github.com/arthenica/speex/blob/Speex-1.2.1/COPYING) |
| tiff | v4.1.0 | libtiff 许可 | [许可及版权](third_party/ffmpeg-kit/license_tiff.txt) | [源码](https://github.com/arthenica/libtiff/tree/v4.1.0) | [许可](https://github.com/arthenica/libtiff/blob/v4.1.0/COPYRIGHT) |
| twolame | 0.4.0 | LGPL-2.1-or-later | [许可及版权](third_party/ffmpeg-kit/license_twolame.txt) | [源码](https://github.com/arthenica/twolame/tree/0.4.0) | [许可](https://github.com/arthenica/twolame/blob/0.4.0/COPYING) |
| vo-amrwbenc | v0.1.3 | Apache-2.0 | [许可及版权](third_party/ffmpeg-kit/license_vo_amrwbenc.txt) | [源码](https://github.com/arthenica/vo-amrwbenc/tree/v0.1.3) | [许可](https://github.com/arthenica/vo-amrwbenc/blob/v0.1.3/COPYING) |
| zimg | release-3.0.5 | WTFPL-2.0 | [许可及版权](third_party/ffmpeg-kit/license_zimg.txt) | [源码](https://github.com/arthenica/zimg/tree/release-3.0.5) | [许可](https://github.com/arthenica/zimg/blob/release-3.0.5/COPYING) |

FreeType 许可正文见 [FTL](third_party/ffmpeg-kit/freetype-FTL.TXT)。Portions of this software are copyright © 2023 The FreeType Project (www.freetype.org). All rights reserved.

libvpx 专利授权见 [PATENTS](third_party/ffmpeg-kit/libvpx-PATENTS)。

libiconv 的 LGPL 库许可补充见 [COPYING.LIB](third_party/ffmpeg-kit/libiconv-COPYING.LIB)。各许可的完整正文及文件内例外条款优先于本索引中的简称。

## 上游源码与构建资料

- [FFmpegKit v6.0](https://github.com/arthenica/ffmpeg-kit/tree/d6be56d7aec286eb3c292d6b23ff07a6b70d8693)：Android 构建脚本与 LGPL 许可。
- [FFmpegKit 外部依赖源码版本映射](https://github.com/arthenica/ffmpeg-kit/blob/d6be56d7aec286eb3c292d6b23ff07a6b70d8693/scripts/source.sh)。
- [FFmpeg n6.0 官方基线](https://github.com/FFmpeg/FFmpeg/tree/n6.0)；[FFmpegKit 使用的 FFmpeg 源码](https://github.com/arthenica/FFmpeg/tree/n6.0)包含其协议扩展。
- [Smart Exception v0.2.1](https://github.com/tanersener/smart-exception/tree/v0.2.1)。
- LLVM 许可取自 [APK 所含运行库对应的 Android LLVM 修订](https://android.googlesource.com/toolchain/llvm-project/+/87f1315dfbea7c137aa2e6d362dbb457e388158d/)。

## 获取、构建与重新链接

原二进制的逐 ABI 配置参数见 [FFmpeg 构建参数](third_party/FFMPEG_BUILD.txt)。

可从上表各固定版本源码页面免费获取完整源码。对应 FFmpegKit 构建资料为 [Android 构建说明](https://github.com/arthenica/ffmpeg-kit/blob/d6be56d7aec286eb3c292d6b23ff07a6b70d8693/android/README.md)、[android.sh](https://github.com/arthenica/ffmpeg-kit/blob/d6be56d7aec286eb3c292d6b23ff07a6b70d8693/android.sh) 和 [构建脚本](https://github.com/arthenica/ffmpeg-kit/tree/d6be56d7aec286eb3c292d6b23ff07a6b70d8693/scripts)。full 包使用 `./android.sh --full`，不启用 `--enable-gpl`；原包使用 Android NDK r22b、FFmpeg n6.0。脚本负责获取依赖、应用构建补丁及生成 AAR。

应用对象代码、Java/native 库重新链接脚本、授权和自行签名安装方法见 [重新链接材料](relink/README.md)。这些材料允许使用修改后的接口兼容 LGPL 库重新组合应用，不需要取得 VideoToGif Java 源码或作者签名密钥。

## 其他官方许可入口

- [FFmpegKit v6.0 LGPL](https://github.com/arthenica/ffmpeg-kit/blob/d6be56d7aec286eb3c292d6b23ff07a6b70d8693/LICENSE)。
- [FFmpeg n6.0 LGPL](https://github.com/FFmpeg/FFmpeg/blob/n6.0/COPYING.LGPLv3)。
- [Smart Exception v0.2.1 BSD-3-Clause](https://github.com/tanersener/smart-exception/blob/v0.2.1/LICENSE)。
- [Lucide 官方许可](https://github.com/lucide-icons/lucide/blob/64502ae56389321a922bd498709d4184b0e61543/LICENSE)及[源码](https://github.com/lucide-icons/lucide/tree/64502ae56389321a922bd498709d4184b0e61543)：本发行使用独立 SVG，版本以所附资源内容为准，不绑定 npm 包版本；保留原有 ISC/MIT 版权声明。
- LLVM 运行库许可：[libc++ 对应修订](https://android.googlesource.com/toolchain/llvm-project/+/87f1315dfbea7c137aa2e6d362dbb457e388158d/libcxx/LICENSE.TXT)。

[libc++abi 官方许可](https://android.googlesource.com/toolchain/llvm-project/+/87f1315dfbea7c137aa2e6d362dbb457e388158d/libcxxabi/LICENSE.TXT)、[libunwind 官方许可](https://android.googlesource.com/toolchain/llvm-project/+/87f1315dfbea7c137aa2e6d362dbb457e388158d/libunwind/LICENSE.TXT)、[compiler-rt 官方许可](https://android.googlesource.com/toolchain/llvm-project/+/87f1315dfbea7c137aa2e6d362dbb457e388158d/compiler-rt/LICENSE.TXT)。

FFmpegKit 原包提供的[源码获取声明](third_party/ffmpeg-kit/source.txt)予以保留；对应版本入口以上表及 Source v6.0 为准。
