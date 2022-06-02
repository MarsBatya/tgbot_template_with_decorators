"the file for regenerating the BaseGatherer code"

import inspect
import logging

from aiogram import Dispatcher

from .codegenerator import CodeGenerator

def extract_args_n_kwargs(sig: inspect.Signature) -> tuple[str, str]:
    "how args and kwargs should be passed based on what is given"
    args: list[str] = []
    kwargs: list[str] = []
    for name, param in sig.parameters.items():
        if name == "self":
            continue
        elif param.kind in (
            param.POSITIONAL_ONLY,
            param.POSITIONAL_OR_KEYWORD,
            param.VAR_POSITIONAL,
        ):
            args.append(str(param))
        elif param.kind == param.KEYWORD_ONLY:
            kwargs.append(f"{name}={name}")
        elif param.kind == param.VAR_KEYWORD:
            kwargs.append(str(param))

    if len(args) == 1 and args[0].startswith("*"):
        formatted_args = args[0].strip("*")
    else:
        formatted_args = f"list({', '.join(args)})"
    if len(kwargs) == 1 and kwargs[0].startswith("**"):
        formatted_kwargs = args[0].strip("**")
    else:
        formatted_kwargs = f"dict({', '.join(kwargs)})"

    return formatted_args, formatted_kwargs


def main():
    c = CodeGenerator()

    c.write('"a generated file for copying aiogram.Dispatcher handler wrappers"')
    c.write()
    c.write("from collections import defaultdict")
    c.write()

    with c.new_block("class BaseGatherer:"):
        c.write('"a base wrapper for the dispatcher"')
        c.write()
        with c.new_block("def __init__(self) -> None:", ""):
            c.write(
                "self.handlers: dict[str, list[tuple[callable, list, dict]]] = defaultdict(list)"
            )

        for attr, method in inspect.getmembers(Dispatcher):
            if attr.startswith("register") or not attr.endswith("handler"):
                continue
            logging.info("%s is generated", attr)
            sig = inspect.signature(method)
            args, kwargs = extract_args_n_kwargs(sig)
            documentation = inspect.getdoc(method)
            with c.new_block(f"def {attr}{sig}:", ""):
                if documentation:
                    for line in ['"""'] + documentation.split("\n") + ['"""']:
                        c.write(line)

                with c.new_block("def decorator(callback):"):
                    with c.new_block(f'self.handlers["{attr}"].append((', "))"):
                        c.write(f"callback, {args}, {kwargs}")
                    c.write("return callback")
                c.write("return decorator")

    c.dump()


if __name__ == "__main__":
    main()