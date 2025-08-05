[en](./README.md)

# BlueSky.API.Post

　BlueSkyのAPIで投稿する。

# 開発環境

* <time datetime="20250804233725">20250804233725</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2020-08-20 <small>[setup](http://ytyaru.hatenablog.com/entry/2020/10/06/111111)</small>
* bash 5.2.15(1)-release
* Python 3.11.2

# インストール

## anyenv

```sh
git clone https://github.com/anyenv/anyenv ~/.anyenv
echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(anyenv init -)"' >> ~/.bash_profile
anyenv install --init -y
```

## pyenv

```sh
anyenv install pyenv
exec $SHELL -l
```

## python

```sh
sudo apt install -y libsqlite3-dev libbz2-dev libncurses5-dev libgdbm-dev liblzma-dev libssl-dev tcl-dev tk-dev libreadline-dev
```

```sh
pyenv install -l
```
```sh
pyenv install 3.10.5
```


## このリポジトリ

```sh
git clone https://github.com/ytyaru/Python.BlueSky.API.Post.20250804233742
cd Python.BlueSky.API.Post.20250804233742/src
```
```sh
python -m venv blueskyposttest
cd blueskyposttest/
./bin/activate
```
```sh
pip install -r requirements.txt
```

# 使い方

## 実行

```sh
./main.py BlueSkyハンドル BlueSkyアプリパスワード
```

## 単体テスト

```sh
./test.py
```

<!--

# 注意

* 注意点など

-->

# 著者

　ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![BlueSky](http://www.google.com/s2/favicons?domain=bsky.app)](https://bsky.app/profile/ytyaru.bsky.social "BlueSky")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

<!--* [![twitter](http://www.google.com/s2/favicons?domain=twitter.com)](https://twitter.com/ytyaru1 "twitter")-->

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

