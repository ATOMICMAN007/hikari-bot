import os
import pathlib

import hikari
import lightbulb
from dotenv import load_dotenv

load_dotenv()
prefix = [".."]
owner_ids = (515586764472320010,)
bot_guilds = (771293539928637470,)


class Bot(lightbulb.Bot):
    def __init__(self):
        super().__init__(
            token=os.getenv("DISCORD_TOKEN"),
            prefix=lightbulb.when_mentioned_or(prefix),
            insensitive_commands=True,
            owner_ids=owner_ids,
            default_enabled_guilds=bot_guilds,
            intents=hikari.Intents.ALL,
        )

    def run(self):
        super().load_extensions_from(path=pathlib.Path("theBot/plugs/"))
        super().run(
            activity=hikari.Activity(name="with mud.", type=hikari.ActivityType.PLAYING)
        )

    # TODO extensions are not loading, CommandNotFound error is raised on
    # command, `..ping`
