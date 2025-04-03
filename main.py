
import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Laad omgeving variabelen
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Zet intents
intents = discord.Intents.default()
intents.message_content = True

# Maak bot aan
bot = commands.Bot(command_prefix="!", intents=intents)

# Sync slash commands
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Kulleke is live! Ingelogd als {bot.user}. Slash commands gesynchroniseerd.")

# Slash command: /voorspel
@bot.tree.command(name="voorspel", description="Laat Kulleke een voorspelling doen.")
@app_commands.describe(wedstrijd="De match die je wil voorspellen (bv. België vs Nederland)")
async def voorspel(interaction: discord.Interaction, wedstrijd: str):
    thuisploeg = wedstrijd.split('vs')[0].strip()
    antwoord = f"⚽ Kulleke voorspelt een overwinning voor **{thuisploeg}**! (gesimuleerd)"
    await interaction.response.send_message(antwoord)

bot.run(TOKEN)
