#!/usr/bin/env python3

import asyncio
from flask import Flask
from kasa import SmartPlug
import logging
import os

# --- To be passed in to container ---
# Mandatory vars
PLUG = os.getenv('PLUG')
TZ = os.getenv('TZ', 'America/New_York')
ON_HOOK = os.getenv('ON_HOOK', 'onhook')
OFF_HOOK = os.getenv('OFF_HOOK', 'offhook')

# Optional Vars
DEBUG = int(os.getenv('DEBUG', 0))

# Version Info
VER = "0.3.5"
APP_VERSION = f"plughook/{VER}"

# Setup logger
LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
logging.basicConfig(level=LOG_LEVEL,
                    format='[%(levelname)s] %(asctime)s %(message)s',
                    datefmt='[%d %b %Y %H:%M:%S %Z]')
logger = logging.getLogger()

logger.info(f'Startup: {APP_VERSION}')


class Hooks:
    ON = ON_HOOK
    OFF = OFF_HOOK


async def plug_off(ip: str) -> None:
    p = SmartPlug(ip)
    await p.update()
    await p.turn_off()
    logger.info('Plug turned off.')
    return "Plug turned off."


async def plug_on(ip: str) -> None:
    p = SmartPlug(ip)
    await p.update()
    await p.turn_on()
    logger.info('Plug turned on.')
    return "Plug turned on."


app = Flask(__name__)


@app.route("/")
def index():
    return "Get Lost!"


@app.route("/hook/<command>")
def parse_hook(command):
    match command:
        case Hooks.ON:
            return asyncio.run(plug_on(PLUG))
        case Hooks.OFF:
            return asyncio.run(plug_off(PLUG))
        case _:
            return "Hook Not Found!"


if __name__ == "__main__":
    from waitress import serve
    serve(app, port=8080)
