import discord
import os
import random
from discord import Colour
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default() # or .all() if you ticked all, that is easier
intents.message_content = True 
intents.members = True

#bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
bot = commands.Bot(command_prefix='$', intents=intents)

load_dotenv()
token = os.getenv('TOKEN')
#client = discord.Client(intents=intents)

#@client.event
@bot.event
async def on_ready():
     print("logged in as a bot {0.user}".format(bot))

    #elif "$message" in message.content:
    #    randomNum = random.randint(0,4)
    #    if randomNum == 1:
    #        await message.channel.send("message 1")
    #    elif randomNum == 2:
    #        await message.channel.send("message 2")
    #    elif randomNum == 3:
    #        await message.channel.send("message 3")

@bot.command()
async def menu(ctx):
    myColour = random.randint(0,0xFFFFFF)
    msg = discord.Embed(
        title="List of Commands: \n $commandList \n $hello \n $coinFlip \n $reactionRoles",
        colour=myColour)

    await ctx.send(embed = msg)

@bot.command()
async def reactionRoles(ctx):
    myColour = random.randint(0,0xFFFFFF)
    embed = discord.Embed(
        title="WELCOME!: \n", 
        colour=myColour,
        description="click the heart for a random colour role!")

    msg = await ctx.send(embed = embed)

    await msg.add_reaction('💕')

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(731319107097722883)
    if payload.guild_id != guild.id:
        return
    if payload.emoji.name == "💕":
        role = discord.utils.get(payload.member.guild.roles, name = "BIG BOOTY")
        await payload.member.add_roles(role)



@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(731319107097722883)
    if payload.guild_id != guild.id:
        return
    if payload.emoji.name == "💕":
        guild = await bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = "BIG BOOTY")
        await member.remove_roles(role)


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!!')

@bot.command()
async def coinFlip(ctx):
    listOne = ["heads","tails"]
    coinNum = random.choice(listOne)

    await ctx.send("heads or tails?")
    def check(ctx):
        return (ctx.content == "heads" or ctx.content == "tails") and ctx.channel
    
    msg = await bot.wait_for('message',check=check)
    if msg.content == coinNum:
        await ctx.send("congrats you WON!")
    elif msg.content != coinNum:
        await ctx.send("sorry you LOST! \n your guess: " + msg.content + "\n the flip was: " + coinNum)

        
bot.run(token)

#client.run(token)







