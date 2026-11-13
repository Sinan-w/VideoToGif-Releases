# LGPL 库重新链接

适用于 VideoToGif 1.1-r03。提供的 JAR 只包含应用 Java 对象代码及原包生成的资源 ID 对象，不包含 Java 源码。原 APK 提供界面、资源和 manifest；重新链接不需要作者签名密钥。

## 权利

允许使用、复制及分发本目录的对象代码，以便与修改后的 LGPL 库重新组合、重新链接，并安装、运行和分发所得组合。允许为调试第三方库修改而进行逆向工程。本授权不要求或代表作者自有源码公开。第三方部分遵循各自许可证。

## 输入

- 原版 `VideoToGif_1.1_Release_v03.apk`（校验值见发行说明）。
- 保持 Java/JNI 接口兼容的 FFmpegKit full AAR，包含原版全部 ABI 的库；可使用修改后的版本。
- Smart Exception common/java 0.2.1 JAR：从 [官方源码](https://github.com/tanersener/smart-exception/tree/v0.2.1) 构建，或使用其同版本发布件。
- Python 3、JDK 17、Android SDK API 36 的 android.jar、Build Tools 35.0.0（D8、zipalign、apksigner）。
- 本仓库完整的 `third_party`、`THIRD_PARTY_NOTICES.md` 和 `relink` 目录。

## 重组与安装

运行下列命令，将占位路径替换为本机路径。脚本只生成新的 unsigned 文件，不覆盖输入，也不访问密钥。

```text
python relink/relink.py --apk original.apk --aar modified-ffmpeg-kit-full.aar --smart-common smart-exception-common-0.2.1.jar --smart-java smart-exception-java-0.2.1.jar --android-jar SDK/platforms/android-36/android.jar --build-tools SDK/build-tools/35.0.0 --jdk JDK17 --output modified-unsigned.apk
```

脚本重新生成完整 DEX，同时替换 AAR 中的 native 库，并随包附上许可文件；仅替换 native .so 不足以替换 FFmpegKit 的 Java 部分。资源和界面沿用原 APK。

用自己的 Android 签名密钥签名，按工具提示输入密码，不把密码写入命令或文件：

```text
apksigner sign --ks YOUR_KEYSTORE --ks-key-alias YOUR_ALIAS --out modified-signed.apk modified-unsigned.apk
apksigner verify --verbose modified-signed.apk
adb install modified-signed.apk
```

自己的签名与原作者不同，无法直接覆盖原作者签名的安装；需在测试设备移除原安装后再安装，移除会删除应用数据。修改版仍须遵守所用第三方许可。请保留本目录与许可资料一同分发。
