import discord, asyncio, random, os, json
from discord.ext import commands

cooldownTime = "60"
vibeFailTime = "5"

def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[str(message.guild.id)]
    except:
        return '--'

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

client = commands.Bot(command_prefix = get_prefix, help_command = help_command)



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

    gayRole = discord.utils.get(guild.roles, name="gay")
    if not gayRole:
       await guild.create_role(name="gay", colour=discord.Colour(0xf500ff)) 
       print('\'gay\' role created')

    failureRole = discord.utils.get(guild.roles, name="failure")
    if not failureRole:
       await guild.create_role(name="failure", colour=discord.Colour(0xe60505)) 
       print('\'failure\' role created')

    

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)



@client.command(brief = 'Change GayBot\'s command prefix', description = 'Change GayBot\'s command prefix; currently doesn\'t work :(')
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

@client.command(brief="Gay check a friend", description=f"The bot checks if the specified member is gay, can only be used once every {cooldownTime} seconds")
@commands.cooldown(1, cooldownTime, commands.BucketType.member)
async def gaydar(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='gay')
    GayCheckInt = random.randint(0, 99)
    if GayCheckInt <= 40:
        async for m in ctx.guild.fetch_members():    
            try:
                await m.remove_roles(role)
            except:
                print(f"Couldn't remove roles from {m}")

        await ctx.send(f'{member.mention} is gay, unfortunately')
        await member.add_roles(role)
    else:
        await ctx.send(f'{member.mention} is not gay')

@client.command(brief = 'Vibe checks the specified user', desription = f'Vibe checks the specified user, if they fail they get server muted for {vibeFailTime} seconds')
async def vibecheck(ctx, member: discord.Member):
    vibecheckrand = random.randint(0, 2)
    
    if vibecheckrand <= 1:
        await ctx.send(f'{member.mention} passed the vibe check. Congratulations.')
    else:
        role = discord.utils.get(ctx.guild.roles, name="failure")
        try:
            await member.add_roles(role)
            await member.edit(mute = True)
            await ctx.send(f'{member.mention} failed the vibe check, they have been muted for {vibeFailTime} seconds')

            await asyncio.sleep(int(vibeFailTime))
            await member.edit(mute = False)
            await member.remove_roles(role)
        except:
            await member.add_roles(role)
            await ctx.send(f'{member.mention} failed the vibe check, what a failure')

            await asyncio.sleep(int(vibeFailTime))
            await member.remove_roles(role)


@gaydar.error
async def gaydar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, wait {error.retry_after:,.2f} seconds.')



access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
