from telegram.ext import MessageHandler, Filters

from telegram_bot import logic
from telegram_bot.menu import MenuEntry


def get_states() -> dict:
    return {
        MenuEntry.START_MENU.value: [
            MessageHandler(Filters.text, logic.handle_start_menu),
            MessageHandler(Filters.all, logic.handle_other_messages)
        ],
        MenuEntry.MANUAL_QUERY.value: [
            MessageHandler(Filters.text, logic.handle_wolfram_request)
        ],
        MenuEntry.INTEGRAL.value: [
            MessageHandler(Filters.text, logic.handle_integral_query)
        ],
        MenuEntry.DERIVATIVE.value: [
            MessageHandler(Filters.text, logic.handle_derivative_query)
        ],
        MenuEntry.LIMIT.value: [
            MessageHandler(Filters.text, logic.handle_limit_query)
        ],
        MenuEntry.SUM.value: [
            MessageHandler(Filters.text, logic.handle_sum_query)
        ],
        MenuEntry.PLOT.value: [
            MessageHandler(Filters.text, logic.handle_plot_query)
        ],
        MenuEntry.EQUATION.value: [
            MessageHandler(Filters.text, logic.handle_equation_query)
        ],
        MenuEntry.TAYLOR_SERIES.value: [
            MessageHandler(
                Filters.text,
                logic.handle_taylor_series_query
            )
        ],
        MenuEntry.EXTREMA.value: [
            MessageHandler(Filters.text, logic.handle_extrema_query)
        ],
    }
