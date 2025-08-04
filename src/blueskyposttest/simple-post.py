#!/usr/bin/env python3

import sys
from atproto import Client, client_utils

def main(handle, password) -> None:
    client = Client() #base_url='https://bsky.social'
    client.login(handle, password)
    print('ログイン成功！')

    post = client.send_post(text='APIから投稿してみるテスト。')
    print('ポスト成功！')
    print(post)


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 3: 
        print("Error: BlueSkyユーザのハンドルとパスワードを引数に渡してください。", file=sys.stderr)
        sys.exit(1)
#    print(sys.argv[1], sys.argv[2])
    main(sys.argv[1], sys.argv[2])

