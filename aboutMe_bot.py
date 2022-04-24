from flask import Blueprint, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    FollowEvent,

    TextSendMessage, 
    TemplateSendMessage, 
    ImageSendMessage, 
    StickerSendMessage,

    ButtonsTemplate, 
    PostbackTemplateAction
)

""" Self Defined Modules """
from utils.template import (
    main_template_send,
    options_template_send
)
from utils.postback import *
from utils.config import linebot_config
from utils.message_routine import (
    msg_IntroMyself,
    msg_NASA_Experience,
    msg_PA_Experience
)

aboutMe_bot = Blueprint('LINEBot', __name__)
line_bot_api = LineBotApi(linebot_config['LINE_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(linebot_config['LINE_CHANNEL_SECRET'])

@aboutMe_bot.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    # && get request body as text
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(FollowEvent)
def handle_new_following(event):
    line_bot_api.reply_message (
        event.reply_token,
        [
            TextSendMessage (
                text = msg_IntroMyself
            ),
            main_template_send
        ] 
    )

@handler.add(MessageEvent)
def handle_message(event):
    msg = event.message
    line_bot_api.reply_message (
        event.reply_token, 
        options_template_send
    )
    
@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data

    if data == postback_IntroToMyself:
        line_bot_api.reply_message (
            event.reply_token,
            [
                TextSendMessage (
                    text = msg_IntroMyself
                ),
                options_template_send
            ]
        )

    elif data == postback_RESUME:
        line_bot_api.reply_message (
            event.reply_token,
            [
                TextSendMessage (
                    text = '這是我的履歷',
                ),
                ImageSendMessage (
                    original_content_url = 'https://www.csie.ntu.edu.tw/~b08902016/resume.jpg',
                    preview_image_url = 'https://www.csie.ntu.edu.tw/~b08902016/resume.jpg'
                ),
                options_template_send
            ]
            )

    elif data == postback_NASA:
        line_bot_api.reply_message (
            event.reply_token,
            [
                TextSendMessage (
                    text = msg_NASA_Experience,
                ),
                TextSendMessage (
                    text = '這是我們DNS組的監控網站介面'
                ),
                ImageSendMessage (
                    original_content_url = 'https://www.csie.ntu.edu.tw/~b08902016/DNS_monitor.png',
                    preview_image_url = 'https://www.csie.ntu.edu.tw/~b08902016/DNS_monitor.png'
                ),
                options_template_send
            ]
            )
    
    elif data == postback_PA:
        line_bot_api.reply_message (
            event.reply_token,
            [
                TextSendMessage (
                    text = msg_PA_Experience,
                ),
                TextSendMessage (
                    text = '這是我去年十月擔任台大經濟系系卡的主控時，我的好朋友幫我拍的照片'
                ),
                ImageSendMessage (
                    original_content_url = 'https://www.csie.ntu.edu.tw/~b08902016/PA.jpg',
                    preview_image_url = 'https://www.csie.ntu.edu.tw/~b08902016/PA.jpg'
                ),
                options_template_send
            ]
            )
    