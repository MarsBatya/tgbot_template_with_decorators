# tgbot_template_with_decorators
A template based on Tishka17' repo, expanded for easy use of decorators via a generated wrapper around dispatcher

Minimal telegram bot example
==============================

This is trivial bot example.
Each part can be replaced keeping the overall structure the same

### How to start

1. Edit code in a correspoing way

2. Update `pip` and `setuptools` packages

```shell
pip install -U setuptools pip 
```

3. Install bot

```shell
pip install .
```

For development install it via command

```shell
pip install -e .[test,lint]
```

4. Create and fill `bot.ini` file ([example](bot.ini.example))

5. Start bot to check

```shell
tgbot
```

6. Edit systemd service file and copy it to a proper location

if you wanna play with the code generation tool, u can run it w/ `python3 -m tgbot.wrappers.main`

