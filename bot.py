import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "-")
channelGeneral = client.get_channel(782072089662193677)

@client.event
async def on_ready():
    print("I smell a gay")

@client.event
async def on_member_join(member):
    GayInt = random.randint(0, 9)
    if GayInt <= 3:
        await channelGeneral.send(f'{member} is gay')
    
    else:
        await channelGeneral.send(f'welcome, {member}')

@client.command()
@commands.cooldown(1, 60*5, commands.BucketType.member)
async def gaydar(ctx, member: discord.Member):
    gayRole = discord.utils.get(ctx.guild.roles, name="gay")
    if gayRole:
        print('role already exists')
    else:
        await ctx.guild.create_role(name="gay", colour=discord.Colour(0xf500ff)) 

    role = discord.utils.get(ctx.guild.roles, name='gay')
    GayCheckInt = random.randint(0, 99)
    if GayCheckInt <= 100:
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
