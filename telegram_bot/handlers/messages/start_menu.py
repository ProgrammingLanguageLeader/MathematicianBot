from telegram_bot.handlers.commands.examples import handle_examples_cmd
from telegram_bot.handlers.commands.help import handle_help_cmd
from telegram_bot.handlers.messages.derivative import handle_derivative
from telegram_bot.handlers.messages.equation import handle_equation
from telegram_bot.handlers.messages.extrema import handle_extrema
from telegram_bot.handlers.messages.integral import handle_integral
from telegram_bot.handlers.messages.limit import handle_limit
from telegram_bot.handlers.messages.manual_request import handle_manual_request
from telegram_bot.handlers.messages.mode_toggling import handle_mode_toggling
from telegram_bot.handlers.messages.plot import handle_plot
from telegram_bot.handlers.messages.sum import handle_sum
from telegram_bot.handlers.messages.taylor_series import handle_taylor_series
from telegram_bot.handlers.messages.wolfram_request import \
    handle_wolfram_request
from telegram_bot.handlers.utils.decorators import send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@send_typing
@remember_new_user
def handle_start_menu(bot, update) -> int:
    text = update.message.text.lower()
    handlers_dict = {
        'examples': handle_examples_cmd,
        'help': handle_help_cmd,
        'toggle mode': handle_mode_toggling,
        'manual request': handle_manual_request,
        'integral': handle_integral,
        'derivative': handle_derivative,
        'limit': handle_limit,
        'sum': handle_sum,
        'plot': handle_plot,
        'equation': handle_equation,
        'extrema': handle_extrema,
        'taylor series': handle_taylor_series
    }
    if text in handlers_dict:
        handler = handlers_dict[text]
        return handler(bot, update) or MenuEntry.START_MENU.value
    return handle_wolfram_request(bot, update)
