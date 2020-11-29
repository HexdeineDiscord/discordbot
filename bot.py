import discord
import random
import os
import json
from discord.ext import commands

cooldownTime = "60"

def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[str(message.guild.id)]
    except:
        return '--'

client = commands.Bot(command_prefix = get_prefix)



@client.event
async def on_ready():
    print("I smell a gay")

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '_'
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)



@client.command()
async def gaydarprefix(ctx, prefix):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent = 4)

        await ctx.send(f'Prefix set to `{prefix}` successfully!')
    except:
        await ctx.send('There has been an error setting the prefix, please try again later <3')

@client.command()
@commands.cooldown(1, cooldownTime, commands.BucketType.member)
async def gaydar(ctx, member: discord.Member):
    gayRole = discord.utils.get(ctx.guild.roles, name="gay")
    if gayRole:
        print('role already exists')
    else:
        await ctx.guild.create_role(name="gay", colour=discord.Colour(0xf500ff)) 

    role = discord.utils.get(ctx.guild.roles, name='gay')
    GayCheckInt = random.randint(0, 99)
    if GayCheckInt <= 40:
        gayRole 
        async for m in ctx.guild.fetch_members():    
            try:
                await m.remove_roles(gayRole)
                print(m)
            except:
                print(f"Couldn't remove roles from {m}")

        await ctx.send(f'{member.mention} is gay, unfortunately')
        await member.add_roles(role)
    else:
        await ctx.send(f'{member.mention} is not gay')



@gaydar.error
async def gaydar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, wait {error.retry_after:,.2f} seconds.')



access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
