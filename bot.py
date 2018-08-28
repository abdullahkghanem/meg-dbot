#bot made by abdullahkghanem
import discord
from discord.ext import commands
import webbrowser
import asyncio

prefix = "?"
bot = commands.Bot(command_prefix=prefix)


# ---------------------------------------------

#------------------EVENTS---------------------

#----------------------------------------------


# On Ready and Online Event
@bot.event
async def on_ready():
    print("Bot is up and Running..")
    game = discord.Game("?help")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    mention = message.author.mention
    if "fuck" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{mention} No Swearing Allowed in This Server!")
    elif "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{mention} No Swearing Allowed in This Server!")
    elif "ass" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{mention} No Swearing Allowed in This Server!")
    elif "dick" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{mention} No Swearing Allowed in This Server!")
        
    await bot.process_commands(message)

# ---------------------------------------------

#-------------------COMMANDS-------------------

#----------------------------------------------

@bot.command()
async def remove_role(ctx, Member: discord.Member, Role: discord.Role):
    '''Removes Roles from a Member (Requires Admin Permissions)'''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator:
        await Member.remove_roles(Role, reason=None, atomic=True)
        await ctx.send(f"Removed Role: {Role} from {Member}")
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")


#adds roles
@bot.command()
async def add_role(ctx, Member: discord.Member, Role: discord.Role):
    '''Adds Roles to a Member (Requires Admin Permissions)'''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator:
        await Member.add_roles(Role, reason=None, atomic=True)
        await ctx.send(f"Added Role: {Role} to {Member}")
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")

#bulk delete messages
@bot.command()
async def purge(ctx, num: int):
    '''Bulk Deletes Messages (Requires Admin Permissions)'''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=num + 1)
        await ctx.send(f"Deleted Messages Successfully! {mention}")
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")

#ping command
@bot.command()
async def ping(ctx):
    '''Replies with Pong!'''
    word = "pong!"
    await ctx.send(word)



#intro command
@bot.command()
async def whoareyou(ctx):
    '''Replies with an intro to the bot'''
    text = "I am Devi and I will help you manage the server!"
    await ctx.send(text)


#test command
@bot.command()
async def test(ctx):
    '''
    Checks if the bot is working
    '''
    text = "Everything's alright!"
    mention = ctx.author.mention
    await ctx.send(mention + " " + text)



#ban command
@bot.command()
async def ban(ctx, Member: discord.Member):
    '''
    Bans a member permanently (Requires Admin Permissions)
    '''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator:
        await Member.ban()
        await ctx.send("Successfuly Banned {} by {}".format(Member, ctx.author.mention))
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")


#kick command
@bot.command()
async def kick(ctx, Member: discord.Member):
    '''
    Kicks a Member (Requires Admin Permissions)
    '''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator:
        await Member.kick()
        await ctx.send("Successfuly Kicked {} by {}".format(Member, ctx.author.mention))
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")

#running bot
file = open("important.txt", "r")
important = file.read()
bot.run(important)

