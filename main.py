import discord
from discord.ext import commands
import os

os.system("clear||cls")

care = commands.Bot(command_prefix="69", intents=discord.Intents.all())

roleidtogive = 1256529540084400237 #your role id
vanity = ".gg/noctaine-gen"#your vanity 
tk = ""# token
logging_channel_id = 1256529541418057761 # channel id

@care.event
async def on_ready():
  print("Ready!")



@care.event
async def on_member_update(before, after):
  if str(before.raw_status) == "offline":
    return
  else:
    try:
     bst = after.activities[0].name
     ast = before.activities[0].name
     if vanity in bst:
       if not vanity in ast:
         channel = care.get_channel(logging_channel_id)
         role = after.guild.get_role(roleidtogive)
         await after.add_roles(role, reason="Added Vanity In Status")
         await channel.send(f"Added")
     elif vanity in ast:
       if not vanity in bst:
         channel = care.get_channel(logging_channel_id)
         role = after.guild.get_role(roleidtogive)
         if role in after.roles:
           await after.remove_roles(role, reason="Removed Vanity From Status")
         await channel.send(f"Removed")
    except:
      pass

         

care.run(tk)
