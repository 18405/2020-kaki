from linebot import LineBotApi
from linebot.models import (TextMessage, TextSendMessage, ImageMessage, ImageSendMessage)

import os

# リモートリポジトリに"ご自身のチャネルのアクセストークン"をpushするのは、避けてください。
# 理由は、そのアクセストークンがあれば、あなたになりすまして、プッシュ通知を送れてしまうからです。
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


# ====================================================================================================================================
# プッシュ通知用関数
# ====================================================================================================================================

# プッシュ通知送信 送信先LINEユーザー：userId
# # 指定のユーザーにプッシュ
# line_bot_api.push_message(userId, messages=messages)

# 毎朝報告？
def test_push1():
    imageUrl = 'https://taisoda-ezaki-lab.herokuapp.com/static/images/fish.png'
    thumUrl = 'https://taisoda-ezaki-lab.herokuapp.com/static/images/fish.png'
    # 全ユーザにプッシュ
    line_bot_api.broadcast(
        [TextSendMessage(text="今日の鯛の様子です！"), 
        ImageSendMessage(imageUrl, thumUrl)]
    )

# linelive通知？
def test_push2():
    t1 = "本日17時から、鯛のオンラインお料理教室「鯛の捌き方編」をライブ配信します。気軽にコメントお待ちしております。\n是非ご参加ください！\n\n"
    t1 += "【ご準備していただくもの】\n・注文した真鯛\n・まな板、包丁、キッチンペーパー、大きめのゴミ袋、ウロコとり\n・スマホまたはパソコン（ネット環境のあるもの）"
    t2 = "\n\n\n\n\nLINE LIVE　アプリで見る ↓\n"
    t2 += 'https://live.line.me'
    imageUrl = 'https://taisoda-ezaki-lab.herokuapp.com/static/images/cook.png'
    thumUrl = 'https://taisoda-ezaki-lab.herokuapp.com/static/images/cook.png'
    # 全ユーザにプッシュ
    line_bot_api.broadcast(
        [TextSendMessage(text=t1),
        TextSendMessage(text=t2),
        ImageSendMessage(imageUrl, thumUrl)]
    )

# まめ知識？
def test_push3():
    t = "知ってましたか？\n養殖魚の餌は、魚の成長具合によって変化するんですよ！"
    # 全ユーザにプッシュ
    line_bot_api.broadcast(
        TextSendMessage(text=t)
    )