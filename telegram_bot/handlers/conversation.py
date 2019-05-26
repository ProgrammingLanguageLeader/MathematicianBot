from functools import partial

from telegram.ext import ConversationHandler, CommandHandler
from telegram.ext import MessageHandler, Filters

from telegram_bot.handlers.commands.detailed_mode import \
    handle_detailed_mode_cmd
from telegram_bot.handlers.commands.examples import handle_examples_cmd
from telegram_bot.handlers.commands.help import handle_help_cmd
from telegram_bot.handlers.commands.simple_mode import handle_simple_mode_cmd
from telegram_bot.handlers.commands.start import handle_start_cmd
from telegram_bot.handlers.messages.manual_request import handle_manual_request
from telegram_bot.handlers.messages.start_menu import handle_start_menu
from telegram_bot.handlers.messages.wolfram_request import \
    handle_wolfram_request
from telegram_bot.handlers.utils.menu_entries import MenuEntry


def get_conversation_handler() -> ConversationHandler:
    return ConversationHandler(
        entry_points=[
            CommandHandler('start', handle_start_cmd),
            CommandHandler('help', handle_help_cmd),
            CommandHandler('examples', handle_examples_cmd),
            CommandHandler('simple_mode', handle_simple_mode_cmd),
            CommandHandler('detailed_mode', handle_detailed_mode_cmd),
            MessageHandler(Filters.all, handle_start_menu)
        ],
        states=get_conversation_states_with_handlers(),
        fallbacks=[]
    )


def get_conversation_states_with_handlers() -> dict:
    return {
        MenuEntry.START_MENU.value: [
            MessageHandler(Filters.text, handle_start_menu)
        ],
        MenuEntry.MANUAL_REQUEST.value: [
            MessageHandler(Filters.text, handle_manual_request)
        ],
        MenuEntry.INTEGRAL.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='integral')
            )
        ],
        MenuEntry.DERIVATIVE.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='derivative')
            )
        ],
        MenuEntry.LIMIT.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='limit')
            )
        ],
        MenuEntry.SUM.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='sum')
            )
        ],
        MenuEntry.PLOT.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='plot')
            )
        ],
        MenuEntry.EQUATION.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='equation')
            )
        ],
        MenuEntry.TAYLOR_SERIES.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='taylor series')
            )
        ],
        MenuEntry.EXTREMA.value: [
            MessageHandler(
                Filters.text,
                partial(handle_wolfram_request, prefix='extrema')
            )
        ],
    }
