from flask import Flask, request, abort
import os
from service.ChromeClawer import catchWeb
from service.Clawer import exchangeRate

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)

# Channel Access Token
# line_bot_api = LineBotApi("wPvQEPT/bzUmhPr5inpPojBSoRYynI1kL3DrFb8r9p7/fUjbnETltCxYNFwKpWSF3hDgx6quARgTNY3dV/jMhDEcPuVuvV4z5X79YvyZkQyvOBwRhmmImupatG2CjnJG4/MmBDJgFjfqsYCzi2sQOgdB04t89/1O/w1cDnyilFU=")
# Channel Secret
# handler = WebhookHandler("0ac24eb3d7c4a03eaf2f2ae125620f44")

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# 監聽所有來自 /callback 的 Post Request
@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print('on Call' + event.message.text)

    # if 'https://www.instagram.com' in event.message.text:
    #     # 返回含圖片Message
    #     imageUrl = ''
    #     imageUrl += imageInfo(event.message.text)

    #     if imageUrl != '':
    #         message = ImageSendMessage(
    #             original_content_url=imageUrl,
    #             preview_image_url=imageUrl
    #         )
    #         line_bot_api.reply_message(
    #             event.reply_token,
    #             message)
    # if '!妹子' in event.message.text:
    #     imageBase = getCk101Url('https://ck101.com/beauty/')
    #     imageUrl = getCk101Photo(imageBase)
    #     print('imageUrl' + imageUrl)
    #     if imageUrl != '':
    #         message = ImageSendMessage(
    #             original_content_url=imageUrl,
    #             preview_image_url=imageUrl
    #         )
    #         textMessage = TextSendMessage(text=imageBase)
    #         listMessage = [message,textMessage]

    #         line_bot_api.reply_message(
    #             event.reply_token,
    #             listMessage)

    # else:
        # 返回純文字Message
    outInfo = ''

    if '美金' in event.message.text:
         outInfo += exchangeRate("USD")

    print('outInfo:' + outInfo)

    if outInfo != '':
        message = TextSendMessage(text=outInfo)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
