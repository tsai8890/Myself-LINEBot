from pipes import Template
from linebot.models import (
    TemplateSendMessage,
    ButtonsTemplate, 
    PostbackTemplateAction,
    MessageAction
)
from utils.postback import *

main_template = ButtonsTemplate (
    title = '關於我',
    text = 'Intro to Myself',
    thumbnail_image_url = 'https://www.csie.ntu.edu.tw/~b08902016/selfie.jpg',
    actions = [
        PostbackTemplateAction (
            label = '關於我',
            data = postback_IntroToMyself
        ),

        PostbackTemplateAction (
            label = '我的履歷',
            data = postback_RESUME
        ),

        PostbackTemplateAction (
            label = '系上網管經驗',
            data = postback_NASA
        ),

        PostbackTemplateAction (
            label = '特殊經歷',
            data = postback_PA
        )
    ]
)

options_template = ButtonsTemplate (
    title = '關於我',
    text = 'Intro to Myself',
    actions = [
        PostbackTemplateAction (
            label = '關於我',
            data = postback_IntroToMyself
        ),

        PostbackTemplateAction (
            label = '我的履歷',
            data = postback_RESUME
        ),

        PostbackTemplateAction (
            label = '系上網管經驗',
            data = postback_NASA
        ),

        PostbackTemplateAction (
            label = '特殊經歷',
            data = postback_PA
        )
    ]
)

options_template_send = TemplateSendMessage (
    alt_text = '個人主頁',
    template = options_template
)


main_template_send = TemplateSendMessage (
    alt_text = '個人主頁',
    template = main_template
)