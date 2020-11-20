from linebot import LineBotApi
from linebot.models import (TextMessage, TextSendMessage, ImageMessage, ImageSendMessage)

# リモートリポジトリに"ご自身のチャネルのアクセストークン"をpushするのは、避けてください。
# 理由は、そのアクセストークンがあれば、あなたになりすまして、プッシュ通知を送れてしまうからです。
import os

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def test_push():
    user_id = "U601f00f928b58cb599732d78ac1cc9df"

    messages = TextSendMessage(text=f"こんにちは😁\n\n" + f"最近はいかがお過ごしでしょうか?")
    line_bot_api.push_message(user_id, messages=messages)