import discord
from discord import app_commands
from discord.ext import commands

import random
import asyncio
import youtube_dl
from dotenv import load_dotenv
from datetime import datetime

print("""
      _____                 _   ____        _   
     / ____|               ( ) |  _ \      | |  
    | (___   __ ___  _____ |/  | |_) | ___ | |_ 
     \___ \ / _` \ \/ / _ \    |  _ < / _ \| __|
     ____) | (_| |>  < (_) |   | |_) | (_) | |_ 
    |_____/ \__,_/_/\_\___/    |____/ \___/ \__|
     """)

# PARAMÉTRER LE BOT

intents = discord.Intents().all()

intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix = "§", intents = intents, description = "Saxo' Bot")

tree = app_commands.CommandTree(discord.Client(intents = intents))

# MONTRER QUE LE BOT EST CONNECTÉ

@bot.event
async def on_ready():
    
    await bot.change_presence(activity = discord.Game(name = "Saxo"))
    # activity = discord.Activity(type = discord.ActivityType.listening, name = "a song")
    # activity = discord.Activity(type = discord.ActivityType.watching, name= "a movie")
    
    print("\n---------------------- Le bot est en ligne ----------------------")
    
    try:
        synced = await bot.tree.sync()
        print(f"\n-------------- {len(synced)} commandes ont été synchronisées ! --------------\n")
        
    except Exception as e:
        print(e)

# CRÉER DES COMMANDES DE TESTS

@bot.tree.command(name = "test", description = "Tester les commandes.")
async def test(interaction : discord.Interaction):
    
    await interaction.response.send_message(f"Salut ! Tu viens d'utiliser une slash commande.", ephemeral = True)

def identifier():
    
    id = ''
    
    for i in range(8):
        id += str(random.randint(0, 10))
            
    return id
 
# SE CONFESSER

@bot.tree.command(name = "confess", description = "Soumettre une confession.")
@app_commands.describe(confession = "Texte de la confession.")

async def confess(interaction : discord.Interaction, confession : str):
    
    if interaction.channel_id == 1110596206800932864:
            
        id = identifier()
           
        embed_c = discord.Embed(title = f"Confession Anonyme (#{id})", description = confession, color = 0xb8cd40)
        
        await interaction.response.send_message("Votre confession sera envoyé de façon anonyme dans quelques instants.", ephemeral = True)
        await interaction.channel.send(embed = embed_c)

    else:
      
        await interaction.response.send_message("Cette commande n'est pas autorisée dans ce salon.", ephemeral = True)

bot.run("token")
