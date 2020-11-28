import discord
import random
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
async def gaydar(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='gay')
    GayCheckInt = random.randint(0, 99)

    if GayCheckInt <= 25:
        await ctx.send(f'{member.mention} is gay, unfortunately')
        await member.add_roles(role)
    else:
        await ctx.send(f'{member.mention} is not gay')



client.run('token')