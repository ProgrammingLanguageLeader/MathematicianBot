from threading import Thread
from queue import Queue

from telegram.ext import CommandHandler, MessageHandler, Filters, \
    ConversationHandler, Dispatcher

import telegram_bot.logic as logic
from telegram_bot.menu import MenuEntry

from utils.singleton import Singleton


@Singleton
class DispatcherProxy(Dispatcher):
    def __init__(self, bot, *args, **kwargs):
        update_queue = Queue()
        super().__init__(bot, update_queue, *args, **kwargs)
        self._setup_dispatcher()
        self._start_thread()

    def _setup_dispatcher(self):
        conversation_handler = ConversationHandler(
            entry_points=[
                CommandHandler('start', logic.handle_start),
                MessageHandler(Filters.all, logic.handle_other_messages)
            ],
            states={
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
                    MessageHandler(Filters.text,
                                   logic.handle_taylor_series_query)
                ],
                MenuEntry.EXTREMA.value: [
                    MessageHandler(Filters.text, logic.handle_extrema_query)
                ],
                MenuEntry.TOGGLE_MODE.value: [
                    MessageHandler(Filters.text, logic.handle_mode_toggling)
                ]
            },
            fallbacks=[]
        )
        self.add_handler(
            CommandHandler('help', logic.handle_help)
        )
        self.add_handler(
            CommandHandler('examples', logic.handle_examples)
        )
        self.add_handler(
            CommandHandler('simple_mode', logic.handle_simple_mode)
        )
        self.add_handler(
            CommandHandler('detailed_mode', logic.handle_detailed_mode)
        )
        self.add_handler(conversation_handler)
        self.add_error_handler(logic.handle_errors)

    def _start_thread(self):
        dispatcher_thread = Thread(
            target=self.start,
            name='dispatcher',
            daemon=True
        )
        dispatcher_thread.start()
