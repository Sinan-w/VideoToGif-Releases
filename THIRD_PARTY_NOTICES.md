# 第三方组件与许可

VideoToGif 使用 FFmpegKit full 6.0-2、FFmpeg、libvpx 等组件和 Lucide 图标，自有源码的非公开状态不改变第三方许可权利。

- FFmpegKit 采用 LGPL v3，上游 https://github.com/arthenica/ffmpeg-kit/tree/v6.0 。
- FFmpeg 的实际许可依赖构建选项，说明 https://ffmpeg.org/legal.html 。
- full AAR 内的许可文本已原样保存在 third_party/ffmpeg-kit。
- 二进制包含 version3 和 libvpx 标志，未发现 enable-gpl、enable-nonfree 标志，此检查不等于已经履行全部分发条件。
- Smart Exception common/java 0.2.1 的对应许可来源仍需发布前核定。
- 图标许可见 third_party/lucide-LICENSE。

正式发布安装包之前，还需核实与实际二进制对应的 FFmpegKit/FFmpeg 及其外部库源码、构建信息、告知，以及 LGPL 要求的重链接或替换机制。当前仓库尚未公开提供 APK。
