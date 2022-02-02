# import
import discord
from discord.ext import commands
from discord_slash import SlashCommand
import json
import asyncio
import datetime
# custom colours in terminal
from colorama import init
from colorama import Fore, Back, Style
init()

# config
try:
    file = open("config.json","r")
    json = json.loads(file.read())
except FileNotFoundError:
    print (f"{Back.RED}{Style.BRIGHT}[ERROR]{Style.RESET_ALL} No configuration file found (config.json), ensure it is located in the same directory.")
    exit()

token = json["token"]
servers = json["servers"]
directory = json["directory"]
cmd_description = json["cmd_description"]
expose_listening = json["expose_listening"]

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command("help")

time_listening = 0

restart = datetime.datetime.now()
restart_time = restart.strftime("%H:%M:%S")

@bot.event
async def on_ready():
    global time_listening
    print (f"{Back.GREEN}{Style.BRIGHT}[READY]{Style.RESET_ALL} Signed in as {bot.user}")
    
    try:
        with open(f"{directory}Snip.txt", encoding="utf8") as file:
            song = file.readline()
            temp = song
    except FileNotFoundError:
        print (f"{Back.RED}{Style.BRIGHT}[ERROR]{Style.RESET_ALL} Unable to retrieve music information (Snip.txt), ensure it is located in {directory}Snip.txt")
    
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
                    print (f"{Back.GREEN}{Style.BRIGHT}[SONG]{Style.RESET_ALL}  {song}")
                
                if song != "":
                    time_listening += 1
                # update temp
                temp = song
        except FileNotFoundError:
            # pass (ignore) if error but log to console
            print (f"{Back.RED}{Style.BRIGHT}[ERROR]{Style.RESET_ALL} Unable to retrieve music information (Snip.txt), ensure it is located in {directory}Snip.txt")
            pass
        
        # await sleep
        await asyncio.sleep(1)
        # could technically be faster per api limits but snip is slow anyway

# send song info
@slash.slash(name="song",description=cmd_description,guild_ids=servers)
async def song(ctx):
    global time_listening
    
    print (f"{Back.GREEN}{Style.BRIGHT}[CMD]{Style.RESET_ALL}   Sent /song output via user request.")
    
    # update
    with open(f"{directory}Snip_Track.txt", encoding="utf8") as file:
        track = file.readline()
    with open(f"{directory}Snip_Artist.txt", encoding="utf8") as file:
        artist = file.readline()
    with open(f"{directory}Snip_Album.txt", encoding="utf8") as file:
        album = file.readline()
    # link
    with open(f"{directory}Snip_TrackId.txt", encoding="utf8") as file:
        trackid = file.readline()
    
    # local file check (if album field is not marked)
    if album != "":
        albumtext = f"on **{album}**"
    else:
        albumtext = "`(local)`"
    
    if expose_listening == "true":
        full_time_listening = str(datetime.timedelta(seconds=time_listening))
        listeningtext = f"\n\nListening for **{full_time_listening}** since **{restart_time}**"
    else:
        listeningtext = ""
    
    # attach file
    file = discord.File(f"{directory}Snip_Artwork.jpg")
    # send off message
    await ctx.send(f"**{track}**\nby **{artist}**\n{albumtext}\n<https://open.spotify.com/track/{trackid}>{listeningtext}", file = file, hidden=True)
    
    # ^ was previously using embeds but couldn't get the local image to attach as the embed's thumbnail

bot.run(token)
