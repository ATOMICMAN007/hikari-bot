import lightbulb
from lightbulb.context import Context


class Master(lightbulb.Plugin):
    @lightbulb.command()
    async def ping(self, ctx: Context):
        await ctx.respond(f"Pong! `{ctx.bot.heartbeat_latency * 1_000:.0f}ms`")


def load(bot: lightbulb.Bot):
    bot.add_plugin(Master())


def unload(bot: lightbulb.Bot):
    bot.remove_plugin("Master")
