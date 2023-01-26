from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import discord
from discord import Interaction, app_commands, ui
from discord.ext import commands

if TYPE_CHECKING:
    from bot import ValorantBot


class Admin(commands.Cog):
    """Error handler"""

    def __init__(self, bot: ValorantBot) -> None:
        self.bot: ValorantBot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, sync_type: Literal['guild', 'global']) -> None:
        """Sync the application commands"""

        async with ctx.typing():
            if sync_type == 'guild':
                self.bot.tree.copy_global_to(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced guild !")
                return

            await self.bot.tree.sync()
            await ctx.reply(f"Synced global !")

    @commands.command()
    @commands.is_owner()
    async def unsync(self, ctx: commands.Context, unsync_type: Literal['guild', 'global']) -> None:
        """Unsync the application commands"""

        async with ctx.typing():
            if unsync_type == 'guild':
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Un-Synced guild !")
                return

            self.bot.tree.clear_commands()
            await self.bot.tree.sync()
            await ctx.reply(f"Un-Synced global !")

    @app_commands.command(description='Shows basic information about the bot.')
    async def about(self, interaction: Interaction) -> None:
        """Shows basic information about the bot."""

        owner_url = f'https://www.khanacademy.org/'
        github_project = 'https://www.khanacademy.org/'
        support_url = 'https://www.khanacademy.org/'

        embed = discord.Embed(color=0xFFFFFF)
        embed.set_author(name='VALORANT BOT PROJECT', url=github_project)
        embed.set_thumbnail(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F1%2F18%2FISO_C%252B%252B_Logo.svg%2F800px-ISO_C%252B%252B_Logo.svg.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FC%252B%252B&tbnid=08WFFr4vmxBy7M&vet=12ahUKEwj87uXWwuH8AhVO1MkDHZJsBYMQMygAegUIARDrAQ..i&docid=bnoQF5njVnaw-M&w=800&h=899&q=c%2B%2B&ved=2ahUKEwj87uXWwuH8AhVO1MkDHZJsBYMQMygAegUIARDrAQ')
        embed.add_field(name='DEV:', value=f"[Master]({owner_url})", inline=False)
        embed.add_field(
            name='ᴄᴏɴᴛʀɪʙᴜᴛᴏʀꜱ:',
            value=f"[master](https://www.khanacademy.org/)\n"
            "[evernever](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n"
            "[master](https://www.khanacademy.org/)\n",
            inline=False,
        )
        view = ui.View()
        view.add_item(ui.Button(label='GITHUB', url=github_project, row=0))
        view.add_item(ui.Button(label='NICE', url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F1%2F18%2FISO_C%252B%252B_Logo.svg%2F800px-ISO_C%252B%252B_Logo.svg.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FC%252B%252B&tbnid=08WFFr4vmxBy7M&vet=12ahUKEwj87uXWwuH8AhVO1MkDHZJsBYMQMygAegUIARDrAQ..i&docid=bnoQF5njVnaw-M&w=800&h=899&q=c%2B%2B&ved=2ahUKEwj87uXWwuH8AhVO1MkDHZJsBYMQMygAegUIARDrAQ', row=0))
        view.add_item(ui.Button(label='SUPPORT SERVER', url=support_url, row=0))

        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: ValorantBot) -> None:
    await bot.add_cog(Admin(bot))
