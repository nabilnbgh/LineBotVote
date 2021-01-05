import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('mra4KD3HeDaq8f7i2sMAkWfMz+h8SpejlabC7F9NuJnbxN4jtfxXQ0Phnrm/CBtVnVU7Xn86gJ00Cc6IixFGAbUkHVjdjzgNb/YFMq/aRcGwPUK4482acdJ61Bwsir/Or8yPEXq5jp/A7V02tpmfxgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('05eb43ab3c41895b70ef09da7d2ab673')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if 'hello' in msg:
        message = TextSendMessage(text='cobain')
        line_bot_api.reply_message(event.reply_token,message)
    else :
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

