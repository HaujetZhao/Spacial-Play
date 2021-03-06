[中文](./README.md)　|　[English](./README_en.md) 

[Gitee](https://gitee.com/haujet/spacial-play)　|　[Github](https://github.com/HaujetZhao/Spacial-Play) 

# 空间播放

## ⭐ 简介

功能： 用 OpenAL 施加 HRTF（头相关传递函数）到音频文件上播放，模拟出真实的 3D 空间感。(仅 Windows 64bit 端可以开箱即用)

## 📝 背景

人有两个耳朵，却能定位来自三维空间的声音，这是因为声音在传到鼓膜之前，会经过肩膀、脑袋、头发、鼻子、耳廓、皮肤等一系列的反射和衍射，每个人特别的生理参数为传到耳朵的声音加了一层滤镜，同样一个声音，从不同方向传过来，就会有不同的效果，我们的大脑已经熟悉了这个滤镜，所以就可以轻松的从声音辨别方向。

但是从耳机里面播放的声音，由于没有经过这样的滤镜处理，就无法还原出3D空间感。所谓的 HiFi 耳机能够听到一个乐队在你身旁播放本身就是伪命题，因为如果声音没有头相关传递函数的处理，再贵的 HiFi 耳机也模拟不出声音在你前方播放的感觉。

但，如何快速得到某个人的全空间HRTF，这是个尚未解决的问题，由于每个人的头都长得不太一样，那么每个人的HRTF也应该不一样。

不过已经有一些研究人员测量了大量的 HRTF 数据，比如 [这里](http://recherche.ircam.fr/equipes/salles/listen/index.html) 这里公开的51个 HRTF 数据集（不过就我的实际测试，这些数据库只能模拟平面的前后左右，不能模拟上下空间感）

这个库中，我将上述51个HRTF 数据集，使用 [OpenAL Soft](https://openal-soft.org/) 转换成了 OpenAL 可以使用的 MHR 文件，然后就可以进行空间感的模拟。



## 💡 使用

需要提前安装上 FFmpeg、Python（3.8 以上版本）

先 `pip install -r requirements.txt` 安装依赖。

打开 `Spacial Play` 文件夹，有一个 `空间播放音乐.py` 的脚本，它的用法是：

```
python 空间播放音乐.py 音乐.mp3
```

先戴上耳机，然后再运行，你就会听到左右两个声道像是放到了两个喇叭里边在播放，然后这两个喇叭绕着你转。

当然你也有可能听不出是两个喇叭在绕着你转的感觉，因为每个人头相关传递函数是不一样的，在 `MinPHR` 中有 51 个 MHR 文件，每个文件有两个版本（前缀分别是 `01D` 和 `03D` ），比如 `01D_OpenAL_Soft_HRTF_IRC_1002_44100.mhr` 和 `03D_OpenAL_Soft_HRTF_IRC_1002_44100.mhr` ，他们都是同一个数据集转换来的，不过使用的是不同的 OpenAL Soft 版本，所以可能会有细微的表现不同，你可以全都试一下。

如何改变使用的 HRTF 函数呢？在 `MinPHR` 中选择一个 MHR 文件，复制他的文件名，用文本编辑器打开 `空间播放音乐.py`，在第二十五行，你会看到：

```python
MHR文件主名 = os.path.splitext('03D_OpenAL_Soft_HRTF_IRC_1014_44100.mhr')[0]
```

将里面那个文件名替换一下，保存，然后重新运行：

```
python 空间播放音乐.py 音乐.mp3
```

试一下更换  HRTF 函数后播放音乐的感觉，你可以多次筛选，找到最合适你的那个 HRTF 函数。

这个库只是玩一玩的性质，不具有什么生产效果。目前没有写入到文件的方法，只能实时听音频效果。不过你也可以这样处理一下你的视频声音，然后再将这个声音录制下来，放到你的视频创作中，让用耳机观看的用户有一种环绕的神奇感觉。

## 🔋 打赏

本软件完全开源，用爱发电，如果你愿意，可以以打赏的方式为我充电：

![sponsor](assets/Sponsor.png)

## 😀 交流

如果有软件方面的反馈可以提交 issues，或者加入 [QQ 群：1146626791](https://qm.qq.com/cgi-bin/qm/qr?k=DgiFh5cclAElnELH4mOxqWUBxReyEVpm&jump_from=webapi) 