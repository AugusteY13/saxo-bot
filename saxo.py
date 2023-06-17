
import asyncio
import youtube_dl

import discord
from discord import app_commands
from discord.ext import commands

import random
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
    # print("Nom d'utilisateur :", bot.user.name)
    # print("ID :", bot.user.id)
    
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
        
        
        
        embed_c = discord.Embed(title = f"Confession Anonyme (#{id})", description = confession, color = 0xb8cd40)
        
        await interaction.response.send_message("Votre confession sera envoyé de façon anonyme dans quelques instants.", ephemeral = True)
        await interaction.channel.send(embed = embed_c)

    else:
        await interaction.response.send_message("Cette commande n'est pas autorisée dans ce salon.", ephemeral = True)



















voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}




# This event happens when a message gets sent
@bot.event
async def on_message(msg):
    if msg.content.startswith("?play"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable = "C:\\Users\\yamad\\Desktop\\ffmpeg\\ffmpeg.exe")

            voice_clients[msg.guild.id].play(player)

        except Exception as err:
            print(err)


    if msg.content.startswith("?pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)

    # This resumes the current song playing if it's been paused
    if msg.content.startswith("?resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)

    # This stops the current playing song
    if msg.content.startswith("?stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)



bot.run("MTExNjQ0NDM0NjExNjQ3Njk0OA.GoGyuZ.T02QCCWzHvAOme8E1dVzMWVENjS1O021VNWvIU")

