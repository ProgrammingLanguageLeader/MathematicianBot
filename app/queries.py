from app.wolfram import make_query
from app.telegram_tools import send_typing, write_logs


@write_logs
@send_typing
def handle_query(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    answer = make_query(text)
    if answer.error or not answer.success:
        bot.send_message(
            chat_id=chat_id,
            text='Unsuccessful. Check your request and try again'
        )
        return
    for pod in answer.pods:
        title = pod.title
        bot.send_message(chat_id=chat_id, text=title)
        for sub in pod.subpods:
            text = sub.plaintext
            if text:
                bot.send_message(chat_id=chat_id, text=text)
            image_src = sub.img.src
            if image_src:
                bot.send_document(
                    chat_id=chat_id,
                    document=image_src,
                    timeout=15
                )
