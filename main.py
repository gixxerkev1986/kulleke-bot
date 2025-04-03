
import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import openai

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Gebruik nieuwe OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Kulleke is live! Ingelogd als {bot.user} en klaar voor AI-voorspellingen.")

@bot.tree.command(name="voorspel", description="Laat Kulleke een AI-voorspelling doen van een wedstrijd.")
@app_commands.describe(wedstrijd="De match die je wil voorspellen (bv. België vs Frankrijk)")
async def voorspel(interaction: discord.Interaction, wedstrijd: str):
    await interaction.response.defer()
    prompt = (
        f"Je bent een voetbalanalist. Analyseer de match {wedstrijd}. "
        f"Geef een voorspelling van de winnaar, verwachte score en waarom, inclusief een vertrouwenspercentage."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{ "role": "user", "content": prompt }],
            max_tokens=200
        )
        antwoord = response.choices[0].message.content
    except Exception as e:
        antwoord = f"Er ging iets mis met de AI-voorspelling: {e}"

    await interaction.followup.send(f"**Voorspelling voor:** {wedstrijd}\n\n{antwoord}")

bot.run(TOKEN)
