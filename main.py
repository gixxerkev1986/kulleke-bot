
import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

class KullekeBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands gesynchroniseerd.")

bot = KullekeBot()

@bot.event
async def on_ready():
    print(f"Kulleke is live! Ingelogd als {bot.user}.")

@bot.tree.command(name="voorspel", description="Laat Kulleke een voorspelling doen.")
@app_commands.describe(wedstrijd="De match die je wil voorspellen (bv. België vs Nederland)")
async def voorspel(interaction: discord.Interaction, wedstrijd: str):
    antwoord = f"⚽ Kulleke gokt op een winst voor {wedstrijd.split('vs')[0].strip()}! (gesimuleerd)"
    await interaction.response.send_message(antwoord)

bot.run(TOKEN)
