# import
import discord
from discord.ext import commands
from discord_slash import SlashCommand
import json
import asyncio

# config
file = open("config.json","r")
json = json.loads(file.read())

token = json["token"]
servers = json["servers"]
directory = json["directory"]
cmd_description = json["cmd_description"]

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("\nready!\n")
    
    with open(f"{directory}Snip.txt", encoding="utf8") as file:
        song = file.readline()
        temp = song
    
    while True:
        try:
            # read current song
            
            with open(f"{directory}Snip.txt", encoding="utf8") as file:
                song = file.readline()
                # check if the file still reads the same song (pass if so)
                if song != temp:
                    # check song is not blank (nothing playing)
                    if song != "":
                        activity = discord.Activity(type=discord.ActivityType.listening, name=song)
                    else:
                        activity = discord.Activity(type=discord.ActivityType.listening, name="nothing")
                    await bot.change_presence(activity=activity)
                    print (f"new song! {song}")
                # update temp
                temp = song
        except FileNotFoundError:
            # pass (ignore) if error but log to console
            print (f"[ERROR] 'Snip.txt' not found in {directory}, check your Snip installation and try again")
            pass
        
        # await sleep
        await asyncio.sleep(1.5)
        # could technically be faster per api limits but snip is slow anyway

# send song info
@slash.slash(name="song",description=cmd_description,guild_ids=servers)
async def song(ctx):
    
    # update
    with open(f"{directory}Snip_Track.txt", encoding="utf8") as file:
        track = file.readline()
    with open(f"{directory}Snip_Artist.txt", encoding="utf8") as file:
        artist = file.readline()
    with open(f"{directory}Snip_Album.txt", encoding="utf8") as file:
        album = file.readline()
    
    # local file check (if album field is not marked)
    if album != "":
        albumtext = f"on **{album}**"
    else:
        albumtext = "`(local)`"
    
    # attach file
    file = discord.File(f"{directory}Snip_Artwork.jpg")
    # send off message
    await ctx.send(f"**{track}**\nby **{artist}**\n{albumtext}", file = file, hidden=True)
    
    # ^ was previously using embeds but couldn't get the local image to attach as the embed's thumbnail

bot.run(token)