from flask import Blueprint, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage
from linebot.models import ButtonsTemplate, MessageTemplateAction

LINEBot = Blueprint('LINEBot', __name__)
line_bot_api = LineBotApi('EMd+ZQnh8L5ANSER5HurhuegPCunqKEtyGpTId22Z4dtamfe9CEG+HNpiEdLM1Kb7Oizvbq9D8Pf7EbwbCaozA9Xi0jn5G9vfZHr8qbMtU/a3m0/c1rWrEBbhGW+mmVhtKEUDWdDp248tftt4YC71gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fbecf5cd9498ea36fdde0501a085859d')

@LINEBot.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # LINEBot.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message

    if msg.text == '你好':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你好啊，最近過得如何？'))
        
    else:
        line_bot_api.reply_message(
            event.reply_token, TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='Menu',
                    text='請選擇地區',
                    actions=[
                        MessageTemplateAction(
                            label='台北市',
                            text='台北市'
                        ),
                        MessageTemplateAction(
                            label='台中市',
                            text='台中市'
                        ),
                        MessageTemplateAction(
                            label='高雄市',
                            text='高雄市'
                        )
                    ]
                ) 
            )
        )
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg.text))

