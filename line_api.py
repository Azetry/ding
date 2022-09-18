import sys

from fastapi import APIRouter, HTTPException, Request, Header
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import config
from chatbot import ChatBot



line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

api_routes = APIRouter()

chatbot = ChatBot()


@api_routes.post("/callback")
async def callback(request: Request, x_line_signature: str = Header(None)) -> str:
    """LINE Bot webhook callback
    Args:
        request (Request): Request Object.
        x_line_signature: Header Parameter used for validation 
    Raises:
        HTTPException: Invalid Signature Error
    Returns:
        str: OK
    """
    body = await request.body()

    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")

    return "OK"


@api_routes.get("/test")
async def test():
    return {'status': True}

# Message Event
@handler.add(MessageEvent, message=TextMessage)
def message_text(event) -> None:
    """Event - User sent text message
    Args:
        event (LINE Event Object): Refer to https://developers.line.biz/en/reference/messaging-api/#message-event
    """
    reply_token = event.reply_token

    # Get user sent message .
    user_id = event.source.user_id
    user_message = event.message.text

    msg = chatbot.response(user_id, user_message)
    messages = TextSendMessage(text=msg)
    line_bot_api.reply_message(reply_token=reply_token, messages=messages)