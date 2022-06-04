import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Status
import os
#import pynacl
#import dnspython
import server

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='?', intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    activity = discord.Game(name="/arcticsmp in status for Warrior Role", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    checkstatus.start()

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a robot")

@tasks.loop(seconds=5)
async def checkstatus():

    #await bot.wait_until_ready() # waits for the bot to be ready until it starts


    guild = bot.get_guild(970480476747857940)

    channel = guild.get_channel(982098484171767838)

    role = guild.get_role(982076623132192848) 


    for member in guild.members: # for every member in the server

                
        for status in member.activities: # for every status that member has.
        
            if isinstance(status, discord.CustomActivity):

                if('arcticsmp' in str(status)): #if test is in the members status
                    if(role in member.roles): #check if members have the role 
                        print()

                    else:
                        await member.add_roles(role) #gives the pic perms roles to the members with the status

                        embed=discord.Embed(title="Role Given", description="Warrior Status", color=0x00ff00)
                        embed.add_field(name=member, value="Thank you for supporting us by putting our vanity in your status! ✔️", inline=False)
                        
                        await channel.send(embed=embed)
                
                else:

                    if(role in member.roles): #check if members have the role 
                        await member.remove_roles(role) #removes the role if the member doesnt have the status
                        
                    
                    else:
                        print()
                    
                
                    
                        
 #starts the loop
server.server()
client.run(TOKEN)
