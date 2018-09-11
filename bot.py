#bot made by abdullahkghanem
'''
════════════════════════════
©️ COPYRIGHT INFRINGEMENT! ©️
════════════════════════════
According to Law of the United States of America, You Can't use, distribute or pretend to own
any of my files duo to copyright and any way of doing that or taking snippets of my code
will lead you to serious legal trouble which will invite you to USA courts which may harm you in any of these legal ways:
1. Sueing Money and House.
2. Get in Jail
So please do not claim to use the code under or you may get in trouble.
'''
import discord
from discord.ext import commands
import webbrowser
import asyncio
import random



prefix = "+"
bot = commands.Bot(command_prefix=prefix)


# ---------------------------------------------

#------------------EVENTS---------------------

#----------------------------------------------


# On Ready and Online Event
@bot.event
async def on_ready():
    print("----------------------------")
    print("Logged In as {}".format(bot.user))
    print("----------------------------")
    game = discord.Game("with Jason Statham!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):

    if "fuck" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} No Swearing Allowed in This Server!")
    elif "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} No Swearing Allowed in This Server!")
    elif "nigg" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} No Swearing Allowed in This Server!")
    elif "dick" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} No Swearing Allowed in This Server!")
    elif "asshole" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} No Swearing Allowed in This Server!")

    await bot.process_commands(message)

# ---------------------------------------------

#-------------------COMMANDS-------------------

#----------------------------------------------

@bot.command()
async def eat(ctx, Member: discord.Member):
    '''The Meg will eat you baby!'''
    await ctx.send(
        f":meat_on_bone: You are tasty {Member.mention} :meat_on_bone: Yum! https://www.tenor.co/Y2aU.gif")



@bot.command()
async def truth(ctx, *, question):
    '''Ask the bot some questions and he will answer without lying!'''
    answers = ["Without a doubt!", "Ofcourse No!!", "I will tell you next time..", "I am too lazy to tell you now!", "Can you please ask your question again?", "Kill them.", "Yes", "BEEB BOOP ERROR 2876 (I won't answer u lolololol)"]
    reply = random.choice(answers)
    await ctx.channel.send(f"{ctx.author.mention} {reply}")


@bot.command()
async def shut(ctx, Member: discord.Member):
    '''Mutes a Member from a voice channel (Requires Admin Permissions)'''
    if ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
        await Member.edit(mute=True, deafen=True)
        await ctx.send(f"{Member} was muted by {ctx.author.mention}")
    else:
        ctx.send(f"You do not have permission to run this command. {ctx.author.mention}")



#removes roles
@bot.command()
async def remove_role(ctx, Member: discord.Member, Role: discord.Role):
    '''Removes Roles from a Member (Requires Admin Permissions)'''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
        await Member.remove_roles(Role, reason=None, atomic=True)
        await ctx.send(f"Removed Role: {Role} from {Member}")
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")


#adds roles
@bot.command()
async def add_role(ctx, Member: discord.Member, Role: discord.Role):
    '''Adds Roles to a Member (Requires Admin Permissions)'''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
        await Member.add_roles(Role, reason=None, atomic=True)
        await ctx.send(f"Added Role: {Role} to {Member}")
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")

#bulk delete messages
@bot.command()
async def purge(ctx, num: int):
    '''Bulk Deletes Messages (Requires Admin Permissions)'''
    mention = ctx.author.mention

    if ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
        await ctx.channel.purge(limit=num + 1)
        await ctx.send(f"Deleted Messages Successfully! {mention}")
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")

#ping command
@bot.command()
async def ping(ctx):
    '''Replies with Pong! and the latency!'''
    latency = bot.latency
    await ctx.send(f"{ctx.author.mention} :ping_pong: PONG! Latency = {latency} ms")



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

    if ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
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

    if ctx.author.guild_permissions.administrator or ctx.author.id == 302409090959671297:
        await Member.kick()
        await ctx.send("Successfuly Kicked {} by {}".format(Member, ctx.author.mention))
    else:
        await ctx.send(f"You do not have permission to run this command. {mention}")

#running bot
file = open("important.txt")
token = file.read()
bot.run(str(token))

