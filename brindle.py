import discord
from discord.ext import commands
import ast
import random

intents = discord.Intents.all()

bot = commands.Bot(intents=intents,command_prefix="!")
f = open("spundle.txt",'r')
s = f.read()
f.close()
lump = ast.literal_eval(s)
words = [a[0] for a in lump]

@bot.event
async def on_ready():
    print('EGGBOT ONLINE')

@bot.command()
async def talk(ctx):
        s = ''
        j = random.randint(0,len(lump)-1)
        for i in range(69):
                s += " " + lump[j][0]
                r = random.uniform(0,1)
                for k in range(len(lump[j][1])):
                        if r <= lump[j][1][k]:
                                if lump[j][2][k] in words:
                                        j = words.index(lump[j][2][k])
                                else:
                                        j = random.randint(0,1005)
                                break
        await ctx.send(s)


@bot.command()
@commands.has_role('Math Youkai')
async def foo(ctx):
    await ctx.send("egglike gameplay")

    
@bot.command()
@commands.has_role('Math Youkai')
async def scrape(ctx):

    await ctx.send("startinggg")
##    james = discord.utils.get(bot.get_all_members(),name = "WhatLizard")
    async for message in ctx.channel.history(limit = 1000000):
        if not message.author == bot.user:
            with open("Posts/"+str(message.author.id)+".txt",'a',encoding="utf-8") as f:
                f.write(message.content+"\n")
    await ctx.send("done!!")
    
@bot.command()
@commands.has_role('Math Youkai')
async def graph(ctx):
    for a in os.list("Posts"):
        with f as open(a,'r'):
            s = f.read()
            s = re.sub("\<.*\>",'',s)
            s = re.sub("http.*",'',s)
            

##    await ctx.send("startinggg")
####    james = discord.utils.get(bot.get_all_members(),name = "WhatLizard")
##    print(james.name," ",james.id)
##    posts = open("posts.txt",'w',encoding="utf-8")
##    async for message in ctx.channel.history(limit = 1000000):
##        if message.author.name == "WhatLizard":
##            posts.write(message.content+"\n")
##    await ctx.send("done!!")
##    posts.close()


##@bot.event
##async def on_message(message):
##    if message.author == bot.user:
##        return
##
##    if 'egg' in message.content:
##        print("test")
##        await message.channel.send('EGG')        

            
    

bot.run('i am a lazy hack and im keeping the key in this file atm 8>')
