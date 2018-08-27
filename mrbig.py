#bot made by abdullahkghanem
import discord
from discord.ext import commands
import webbrowser

prefix = "$"
bot = commands.Bot(command_prefix=prefix)


# ---------------------------------------------

#------------------EVENTS---------------------

#----------------------------------------------


# On Ready and Online Event
@bot.event
async def on_ready():
    print("Everything's ready Boss ;)")
    game = discord.Game("with the API :P")
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

# ---------------------------------------------

#-------------------COMMANDS-------------------

#----------------------------------------------

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
    text = "I am your AI friend! that will help you manage the server! and my name is Mr.Moustache!"
    await ctx.send(text)



#latency command
@bot.command()
async def latency(ctx):
    '''
    Shows the latency to the bot
    '''
    latency = bot.latency
    await ctx.send(latency)



#test command
@bot.command()
async def test(ctx):
    '''
    Checks if the bot is working
    '''
    text = "I am working good!"
    mention = ctx.author.mention
    await ctx.send(mention + " " + text)



#ban command
@bot.command()
async def ban(ctx, Member: discord.Member):
    '''
    Bans a member permanently
    '''
    await Member.ban()
    await ctx.send("Successfuly Banned {} by {}".format(Member, ctx.author.mention))



#kick command
@bot.command()
async def kick(ctx, Member: discord.Member):
    '''
    Kicks a Member
    '''
    await Member.kick()
    await ctx.send("Successfuly Kicked {} by {}".format(Member, ctx.author.mention))



#openlink command
@bot.command()
async def openlink(ctx, *, link: str):
    '''
    Opens a website link in your default web browser
    '''
    await webbrowser.open(link)




#running bot
file = open("important.txt", "r")
important = file.read()
bot.run(important)


