"""
a way to let dispatcher stay non global
"""
import functools
import logging

from typing import Union
from dataclasses import dataclass, field

from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineQuery, CallbackQuery, Message

from .generated import BaseGatherer

@dataclass
class GatheredHandler:
    "a simple representation of a wrapped handler"
    callback: callable
    logger: logging.Logger = field(default=None)

    def __post_init__(self):
        if not self.logger:
            self.logger = logging.getLogger(self.callback.__module__)

    def wrap_log(self) -> callable:
        "call it if u want the function to log all the actions"

        def wrapper(callback: callable):
            self.logger.info("initiating %s", self.callback.__name__)

            @functools.wraps(callback)
            async def _wrapped(update: Union[Message, CallbackQuery, InlineQuery], *args, **kwargs):

                if isinstance(update, (Message, CallbackQuery, InlineQuery)):
                    self.logger.info(
                        "%s by %s (%s)",
                        callback.__name__,
                        update.from_user.id,
                        update.from_user.first_name,
                    )

                return await callback(update, *args, **kwargs)

            return _wrapped

        return wrapper(self.callback)


class Gatherer(BaseGatherer):
    "a wrapper for the aiogram.Dispatcher"

    def __call__(self, dispatcher: Dispatcher, verbose: bool = True) -> None:
        """
        call it in the main file to release handlers into the provided `dispatcher`

        set `verbose=False` if u don't want logs about each handler initiated or triggered
        """

        for method_name, handlers in self.handlers.items():
            method = getattr(dispatcher, method_name)
            for callback, args, kwargs in handlers:
                handler = GatheredHandler(callback=callback)
                method(*args, **kwargs)(handler.wrap_log() if verbose else callback)
