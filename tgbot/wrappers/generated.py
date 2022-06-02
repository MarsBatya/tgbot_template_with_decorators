"a generated file for copying aiogram.Dispatcher wrappers"

from collections import defaultdict


class BaseGatherer:
    "a base wrapper for the dispatcher"

    def __init__(self) -> None:
        self.handlers: dict[str, list[tuple[callable, list, dict]]] = defaultdict(list)

    def callback_query_handler(
        self, *custom_filters, state=None, run_task=None, **kwargs
    ):
        """
        Decorator for callback query handler

        Example:

        .. code-block:: python3

            @dp.callback_query_handler(lambda callback_query: True)
            async def some_callback_handler(callback_query: types.CallbackQuery)

        :param state:
        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["callback_query_handler"].append(
                callback, custom_filters, dict(state=state, run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def channel_post_handler(
        self,
        *custom_filters,
        commands=None,
        regexp=None,
        content_types=None,
        state=None,
        run_task=None,
        **kwargs
    ):
        """
        Decorator for channel post handler

        :param commands: list of commands
        :param regexp: REGEXP
        :param content_types: List of content types.
        :param state:
        :param custom_filters: list of custom filters
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        :return: decorated function
        """

        def decorator(callback):
            self.handlers["channel_post_handler"].append(
                callback,
                custom_filters,
                dict(
                    commands=commands,
                    regexp=regexp,
                    content_types=content_types,
                    state=state,
                    run_task=run_task,
                    **kwargs
                ),
            )
            return callback

        return decorator

    def chat_join_request_handler(self, *custom_filters, run_task=None, **kwargs):
        """
        Decorator for chat_join_request handler

        Example:

        .. code-block:: python3

            @dp.chat_join_request()
            async def some_handler(chat_member: types.ChatJoinRequest)

        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["chat_join_request_handler"].append(
                callback, custom_filters, dict(run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def chat_member_handler(self, *custom_filters, run_task=None, **kwargs):
        """
        Decorator for chat_member handler

        Example:

        .. code-block:: python3

            @dp.chat_member_handler()
            async def some_handler(chat_member: types.ChatMemberUpdated)

        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["chat_member_handler"].append(
                callback, custom_filters, dict(run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def chosen_inline_handler(
        self, *custom_filters, state=None, run_task=None, **kwargs
    ):
        """
        Decorator for chosen inline query handler

        Example:

        .. code-block:: python3

            @dp.chosen_inline_handler(lambda chosen_inline_result: True)
            async def some_chosen_inline_handler(chosen_inline_result: types.ChosenInlineResult)

        :param state:
        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        :return:
        """

        def decorator(callback):
            self.handlers["chosen_inline_handler"].append(
                callback, custom_filters, dict(state=state, run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def edited_channel_post_handler(
        self,
        *custom_filters,
        commands=None,
        regexp=None,
        content_types=None,
        state=None,
        run_task=None,
        **kwargs
    ):
        """
        Decorator for edited channel post handler

        :param commands: list of commands
        :param regexp: REGEXP
        :param content_types: List of content types.
        :param custom_filters: list of custom filters
        :param state:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        :return: decorated function
        """

        def decorator(callback):
            self.handlers["edited_channel_post_handler"].append(
                callback,
                custom_filters,
                dict(
                    commands=commands,
                    regexp=regexp,
                    content_types=content_types,
                    state=state,
                    run_task=run_task,
                    **kwargs
                ),
            )
            return callback

        return decorator

    def edited_message_handler(
        self,
        *custom_filters,
        commands=None,
        regexp=None,
        content_types=None,
        state=None,
        run_task=None,
        **kwargs
    ):
        """
        Decorator for edited message handler

        You can use combination of different handlers

        .. code-block:: python3

            @dp.message_handler()
            @dp.edited_message_handler()
            async def msg_handler(message: types.Message):

        :param commands: list of commands
        :param regexp: REGEXP
        :param content_types: List of content types.
        :param state:
        :param custom_filters: list of custom filters
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        :return: decorated function
        """

        def decorator(callback):
            self.handlers["edited_message_handler"].append(
                callback,
                custom_filters,
                dict(
                    commands=commands,
                    regexp=regexp,
                    content_types=content_types,
                    state=state,
                    run_task=run_task,
                    **kwargs
                ),
            )
            return callback

        return decorator

    def errors_handler(self, *custom_filters, exception=None, run_task=None, **kwargs):
        """
        Decorator for errors handler

        :param exception: you can make handler for specific errors type
        :param run_task: run callback in task (no wait results)
        :return:
        """

        def decorator(callback):
            self.handlers["errors_handler"].append(
                callback,
                custom_filters,
                dict(exception=exception, run_task=run_task, **kwargs),
            )
            return callback

        return decorator

    def inline_handler(self, *custom_filters, state=None, run_task=None, **kwargs):
        """
        Decorator for inline query handler

        Example:

        .. code-block:: python3

            @dp.inline_handler(lambda inline_query: True)
            async def some_inline_handler(inline_query: types.InlineQuery)

        :param state:
        :param custom_filters: list of custom filters
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        :return: decorated function
        """

        def decorator(callback):
            self.handlers["inline_handler"].append(
                callback, custom_filters, dict(state=state, run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def message_handler(
        self,
        *custom_filters,
        commands=None,
        regexp=None,
        content_types=None,
        state=None,
        run_task=None,
        **kwargs
    ):
        """
        Decorator for message handler

        Examples:

        Simple commands handler:

        .. code-block:: python3

            @dp.message_handler(commands=['start', 'welcome', 'about'])
            async def cmd_handler(message: types.Message):

        Filter messages by regular expression:

        .. code-block:: python3

            @dp.message_handler(regexp='^[a-z]+-[0-9]+')
            async def msg_handler(message: types.Message):

        Filter messages by command regular expression:

        .. code-block:: python3

            @dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['item_([0-9]*)']))
            async def send_welcome(message: types.Message):

        Filter by content type:

        .. code-block:: python3

            @dp.message_handler(content_types=ContentType.PHOTO | ContentType.DOCUMENT)
            async def audio_handler(message: types.Message):

        Filter by custom function:

        .. code-block:: python3

            @dp.message_handler(lambda message: message.text and 'hello' in message.text.lower())
            async def text_handler(message: types.Message):

        Use multiple filters:

        .. code-block:: python3

            @dp.message_handler(commands=['command'], content_types=ContentType.TEXT)
            async def text_handler(message: types.Message):

        Register multiple filters set for one handler:

        .. code-block:: python3

            @dp.message_handler(commands=['command'])
            @dp.message_handler(lambda message: demojize(message.text) == ':new_moon_with_face:')
            async def text_handler(message: types.Message):

        This handler will be called if the message starts with '/command' OR is some emoji

        By default content_type is :class:`ContentType.TEXT`

        :param commands: list of commands
        :param regexp: REGEXP
        :param content_types: List of content types.
        :param custom_filters: list of custom filters
        :param kwargs:
        :param state:
        :param run_task: run callback in task (no wait results)
        :return: decorated function
        """

        def decorator(callback):
            self.handlers["message_handler"].append(
                callback,
                custom_filters,
                dict(
                    commands=commands,
                    regexp=regexp,
                    content_types=content_types,
                    state=state,
                    run_task=run_task,
                    **kwargs
                ),
            )
            return callback

        return decorator

    def my_chat_member_handler(self, *custom_filters, run_task=None, **kwargs):
        """
        Decorator for my_chat_member handler

        Example:

        .. code-block:: python3

            @dp.my_chat_member_handler()
            async def some_handler(my_chat_member: types.ChatMemberUpdated)

        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["my_chat_member_handler"].append(
                callback, custom_filters, dict(run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def poll_answer_handler(self, *custom_filters, run_task=None, **kwargs):
        """
        Decorator for poll_answer handler

        Example:

        .. code-block:: python3

            @dp.poll_answer_handler()
            async def some_poll_answer_handler(poll_answer: types.PollAnswer)

        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["poll_answer_handler"].append(
                callback, custom_filters, dict(run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def poll_handler(self, *custom_filters, run_task=None, **kwargs):
        """
        Decorator for poll handler

        Example:

        .. code-block:: python3

            @dp.poll_handler()
            async def some_poll_handler(poll: types.Poll)

        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["poll_handler"].append(
                callback, custom_filters, dict(run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def pre_checkout_query_handler(
        self, *custom_filters, state=None, run_task=None, **kwargs
    ):
        """
        Decorator for pre-checkout query handler

        Example:

        .. code-block:: python3

            @dp.pre_checkout_query_handler(lambda shipping_query: True)
            async def some_pre_checkout_query_handler(shipping_query: types.ShippingQuery)

        :param state:
        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["pre_checkout_query_handler"].append(
                callback, custom_filters, dict(state=state, run_task=run_task, **kwargs)
            )
            return callback

        return decorator

    def shipping_query_handler(
        self, *custom_filters, state=None, run_task=None, **kwargs
    ):
        """
        Decorator for shipping query handler

        Example:

        .. code-block:: python3

            @dp.shipping_query_handler(lambda shipping_query: True)
            async def some_shipping_query_handler(shipping_query: types.ShippingQuery)

        :param state:
        :param custom_filters:
        :param run_task: run callback in task (no wait results)
        :param kwargs:
        """

        def decorator(callback):
            self.handlers["shipping_query_handler"].append(
                callback, custom_filters, dict(state=state, run_task=run_task, **kwargs)
            )
            return callback

        return decorator
