import re
import black
from typing import Optional
from contextlib import contextmanager


class CodeGenerator:
    "a simple tool to keep track of all the indentation"

    def __init__(self, step: str = "    "):
        self.level = 0
        self.code = []
        self.step = step

    def write(self, string: bool = "", new_line: bool = True):
        text = self.step * self.level + string
        if new_line:
            text += "\n"
        self.code.append(text)

    def indent(self):
        self.level += 1

    def dedent(self):
        if self.level > 0:
            self.level -= 1

    def end(self):
        return "".join(self.code)

    @contextmanager
    def new_block(self, begin: str = None, end: str = None):
        "start a new indentation w/ `begin` and `end` around it if provided"
        try:
            if begin is not None:
                self.write(begin)
            self.indent()
            yield self
        finally:
            self.dedent()
            if end is not None:
                self.write(end)

    def dump(self, file_path: Optional[str] = None, format: bool = True):
        code = self.end()
        if format:
            code = black.format_file_contents(code, fast=False, mode=black.Mode())
        if file_path is None:
            file_path = re.sub(r"\w+.py$", "generated.py", __file__)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)


if __name__ == "__main__":
    c = CodeGenerator()
    c.write('"hello"')
    c.write()
    with c.new_block("def kek():", ""):
        c.write("return 1")
    with c.new_block('if __name__ == "__main__":', ""):
        c.write("kek()")
    c.dump()
