import lichess.api
import random
import discord
from discord.ext import commands
import time
import asyncio
from covid import Covid

# id = 559392094351917076
messages = 0
joined = 0
bot = commands.Bot(command_prefix="-")
murdered = {}
covid = Covid()
covid.get_data()
countries = covid.list_countries()
confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()
covid = Covid(source="worldometers")

#Country list
italy_cases = covid.get_status_by_country_name("Italy")
USA_cases = covid.get_status_by_country_name("USA")
spain_cases = covid.get_status_by_country_name("Spain")
france_cases = covid.get_status_by_country_name("France")
germany_cases = covid.get_status_by_country_name("Germany")
china_cases = covid.get_status_by_country_name("China")
iran_cases = covid.get_status_by_country_name("Iran")
uk_cases = covid.get_status_by_country_name("Uk")
turkey_cases = covid.get_status_by_country_name("Turkey")
belgium_cases = covid.get_status_by_country_name("Belgium")
switzerland_cases = covid.get_status_by_country_name("Switzerland")
netherlands_cases = covid.get_status_by_country_name("Netherlands")
canada_cases = covid.get_status_by_country_name("Canada")
brazil_cases = covid.get_status_by_country_name("Brazil")
portugal_cases = covid.get_status_by_country_name("Portugal")
austria_cases = covid.get_status_by_country_name("Austria")
korea_cases = covid.get_status_by_country_name("S. Korea")
russia_cases = covid.get_status_by_country_name("Russia")
sweden_cases = covid.get_status_by_country_name("Sweden")
norway_cases = covid.get_status_by_country_name("Norway")
ireland_cases = covid.get_status_by_country_name("Ireland")
australia_cases = covid.get_status_by_country_name("Australia")
india_cases = covid.get_status_by_country_name("India")
chile_cases = covid.get_status_by_country_name("Chile")
denmark_cases = covid.get_status_by_country_name("Denmark")
czechia_cases = covid.get_status_by_country_name("Czechia")
poland_cases = covid.get_status_by_country_name("Poland")
romania_cases = covid.get_status_by_country_name("Romania")
japan_cases = covid.get_status_by_country_name("Japan")
finland_cases = covid.get_status_by_country_name("Finland")
greece_cases = covid.get_status_by_country_name("Greece")
ukraine_cases = covid.get_status_by_country_name("Ukraine")
syria_cases = covid.get_status_by_country_name("Syria")




client = discord.Client()


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("statts.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

                messages = 0
                joined = 0

                await asyncio.sleep(300)
        except Exception as e:
            print(e)
            await asyncio.sleep(300)


channel_id = 0
print(repr(token))

@client.event
async def on_ready():
    print('Logged in...')
    print('Username: ' + str(client.user.name))
    print('Client ID: ' + str(client.user.id))

@client.event
async def on_message(message):
    args = message.content.split(' ')
    if args[0] == '-antichess':
        name = ' '.join(args[1:])
        try:
            user = lichess.api.user(name)
        except:
            return await message.channel.send("user not found")
        await message.channel.send((user['perfs']['antichess']['rating']))
    elif args[0] == '-atomic':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['atomic']['rating']))
    elif args[0] == '-bullet':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['bullet']['rating']))
    elif args[0] == '-blitz':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['blitz']['rating']))
    elif args[0] == '-rapid':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['rapid']['rating']))
    elif args[0] == '-classical':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['classical']['rating']))
    elif args[0] == '-crazyhouse':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['crazyhouse']['rating']))
    elif args[0] == '-chess960':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['chess960']['rating']))
    elif args[0] == '-kingOfTheHill':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['kingofthehill']['rating']))
    elif args[0] == '-threeCheck':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['threeCheck']['rating']))
    elif args[0] == '-horde':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['horde']['rating']))
    elif args[0] == '-racingKings':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['racingkings']['rating']))
    elif args[0] == '-ultrabullet':
        name = ' '.join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user['perfs']['ultrabullet']['rating']))
    if message.content == "-github":
        await message.channel.send("https://github.com/Maj0rites/Maj0rs-lichess-bot")
    elif message.content == "-help":
        await message.channel.send("My prefix is - for more info type -info")
    elif message.content == "-info":
        await message.channel.send(
            "```-github ~ Shows the github link of bot \n -author ~ shows who made that bot \n -bullet [nickname] ~ Shows the [nickname]'s bullet rating \n -blitz [nickname] ~ Shows the [nickname]'s blitz rating \n -rapid [nickname] ~ Shows the [nickname]'s rapid rating \n -classical [nickname] ~ Shows the [nickname]'s classical rating \n -crazyhouse [nickname] ~ Shows the [nickname]'s crazyhouse rating \n  -chess960 [nickname] ~ Shows the [nickname]'s chess960 rating \n -kingOfTheHill [nickname] ~ Shows the [nickname]'s king of the hill rating \n -threeCheck [nickname] ~ Shows the [nickname]'s threeCheck rating \n -antichess [nickname] ~ Shows the [nickname]'s antichess rating \n -atomic [nickname] ~ Shows the [nickname]'s atomic rating \n -horde [nickname] ~ Shows the [nickname]'s horde rating \n -racingKings [nickname] ~ Shows the [nickname]'s racingKings rating \n -ultrabullet [nickname] ~ Shows the [nickname]'s ultrabullet rating \n Usage : -antichess AskMeWhoAmI \n -[variant]Tv sends [variant's] lichess Tv link!```")
    elif message.content == "-author":
        await message.channel.send(f"""Major#3173""")
    elif message.content.startswith("-random "):
        args = message.content.split(" ")[1:]
        await message.channel.send(random.choice(args))
    elif message.content == ("-antichessTv"):
        await message.channel.send("https://lichess.org/tv/antichess")
    elif message.content == ("-bulletTv"):
        await message.channel.send("https://lichess.org/tv/bullet")
    elif message.content == ("-blitzTv"):
        await message.channel.send("https://lichess.org/tv/blitz")
    elif message.content == ("-rapidTv"):
        await message.channel.send("https://lichess.org/tv/rapid")
    elif message.content == ("-classicalTv"):
        await message.channel.send("https://lichess.org/tv/classical")
    elif message.content == ("-crazyhouseTv"):
        await message.channel.send("https://lichess.org/tv/crazyhouse")
    elif message.content == ("-chess960Tv"):
        await message.channel.send("https://lichess.org/tv/chess960")
    elif message.content == ("-kingOfTheHillTv"):
        await message.channel.send("https://lichess.org/tv/kingOfTheHill")
    elif message.content == ("-threeCheckTv"):
        await message.channel.send("https://lichess.org/tv/threeCheck")
    elif message.content == ("-antichessTv"):
        await message.channel.send("https://lichess.org/tv/antichess")
    elif message.content == ("-atomicTv"):
        await message.channel.send("https://lichess.org/tv/atomic")
    elif message.content == ("-hordeTv"):
        await message.channel.send("https://lichess.org/tv/horde")
    elif message.content == ("-racingKingsTv"):
        await message.channel.send("https://lichess.org/tv/racingKings")
    elif message.content == ("-ultraBulletTv"):
        await message.channel.send("https://lichess.org/tv/ultraBullet")
    elif message.content == ("-computerTv"):
        await message.channel.send("https://lichess.org/tv/computer")
    elif message.content == ("-botTv"):
        await message.channel.send("https://lichess.org/tv/bot")
    elif message.content.startswith("-murder"):
        global murdered
        if message.mentions[0].id in murdered:
            if murdered[message.mentions[0].id]['time'] + 90 > time.time():
                return await message.channel.send("```You have already murdered him wait for 90 seconds```")
        murdered[message.mentions[0].id] = {}
        murdered[message.mentions[0].id]['time'] = time.time()
        embed = discord.Embed()
        embed.add_field(name="I will murder you!", value="Job done!", inline=False)
        await message.channel.send(embed=embed)
    elif message.content == ("-covid total deaths"):
        await message.channel.send(deaths)
    elif message.content == ("-covid total cases"):
        await message.channel.send(confirmed)
    elif message.content == ("-covid Italy"):
        await message.channel.send(f"```Confirmed cases: {italy_cases['confirmed']} Deaths: {italy_cases['deaths']} Recovered: {italy_cases['recovered']}```")
    elif message.content == ("-covid USA"):
        await message.channel.send(f"```Confirmed cases: {USA_cases['confirmed']} Deaths: {USA_cases['deaths']} Recovered: {USA_cases['recovered']}```")
    elif message.content == ("-covid Spain"):
        await message.channel.send(f"```Confirmed cases: {spain_cases['confirmed']} Deaths: {spain_cases['deaths']} Recovered: {spain_cases['recovered']}```")
    elif message.content == ("-covid Turkey"):
        await message.channel.send(f"```Confirmed cases: {turkey_cases['confirmed']} Deaths: {turkey_cases['deaths']} Recovered: {turkey_cases['recovered']}```")
    elif message.content == ("-covid India"):
        await message.channel.send(f"```Confirmed cases: {india_cases['confirmed']} Deaths: {india_cases['deaths']} Recovered: {india_cases['recovered']}```")
    elif message.content == ("-covid France"):
        await message.channel.send(f"```Confirmed cases: {france_cases['confirmed']} Deaths: {france_cases['deaths']} Recovered: {france_cases['recovered']}```")
    elif message.content == ("-covid Germany"):
        await message.channel.send(f"```Confirmed cases: {germany_cases['confirmed']} Deaths: {germany_cases['deaths']} Recovered: {germany_cases['recovered']}```")
    elif message.content == ("-covid Uk"):
        await message.channel.send(f"```Confirmed cases: {uk_cases['confirmed']} Deaths: {uk_cases['deaths']} Recovered: {uk_cases['recovered']}```")
    elif message.content == ("-covid China"):
        await message.channel.send(f"```Confirmed cases: {china_cases['confirmed']} Deaths: {china_cases['deaths']} Recovered: {china_cases['recovered']}```")
    elif message.content == ("-covid Belgium"):
        await message.channel.send(f"```Confirmed cases: {belgium_cases['confirmed']} Deaths: {belgium_cases['deaths']} Recovered: {belgium_cases['recovered']}```")
    elif message.content == ("-covid Switzerland"):
        await message.channel.send(f"```Confirmed cases: {switzerland_cases['confirmed']} Deaths: {switzerland_cases['deaths']} Recovered: {switzerland_cases['recovered']}```")
    elif message.content == ("-covid Canada"):
        await message.channel.send(f"```Confirmed cases: {canada_cases['confirmed']} Deaths: {canada_cases['deaths']} Recovered: {canada_cases['recovered']}```")
    elif message.content == ("-covid Brazil"):
        await message.channel.send(f"```Confirmed cases: {brazil_cases['confirmed']} Deaths: {brazil_cases['deaths']} Recovered: {brazil_cases['recovered']}```")
    elif message.content == ("-covid Portugal"):
        await message.channel.send(f"```Confirmed cases: {portugal_cases['confirmed']} Deaths: {portugal_cases['deaths']} Recovered: {portugal_cases['recovered']}```")
    elif message.content == ("-covid Austria"):
        await message.channel.send(f"```Confirmed cases: {austria_cases['confirmed']} Deaths: {austria_cases['deaths']} Recovered: {austria_cases['recovered']}```")
    elif message.content == ("-covid Korea"):
        await message.channel.send(f"```Confirmed cases: {korea_cases['confirmed']} Deaths: {korea_cases['deaths']} Recovered: {korea_cases['recovered']}```")
    elif message.content == ("-covid Russia"):
        await message.channel.send(f"```Confirmed cases: {russia_cases['confirmed']} Deaths: {russia_cases['deaths']} Recovered: {russia_cases['recovered']}```")
    elif message.content == ("-covid Sweden"):
        await message.channel.send(f"```Confirmed cases: {sweden_cases['confirmed']} Deaths: {sweden_cases['deaths']} Recovered: {sweden_cases['recovered']}```")
    elif message.content == ("-covid Norway"):
        await message.channel.send(f"```Confirmed cases: {norway_cases['confirmed']} Deaths: {norway_cases['deaths']} Recovered: {norway_cases['recovered']}```")
    elif message.content == ("-covid Ireland"):
        await message.channel.send(f"```Confirmed cases: {ireland_cases['confirmed']} Deaths: {ireland_cases['deaths']} Recovered: {ireland_cases['recovered']}```")
    elif message.content == ("-covid Australia"):
        await message.channel.send(f"```Confirmed cases: {australia_cases['confirmed']} Deaths: {australia_cases['deaths']} Recovered: {australia_cases['recovered']}```")
    elif message.content == ("-covid Chile"):
        await message.channel.send(f"```Confirmed cases: {chile_cases['confirmed']} Deaths: {chile_cases['deaths']} Recovered: {chile_cases['recovered']}```")
    elif message.content == ("-covid Denmark"):
        await message.channel.send(f"```Confirmed cases: {denmark_cases['confirmed']} Deaths: {denmark_cases['deaths']} Recovered: {denmark_cases['recovered']}```")
    elif message.content == ("-covid Czechia"):
        await message.channel.send(f"```Confirmed cases: {czechia_cases['confirmed']} Deaths: {czechia_cases['deaths']} Recovered: {czechia_cases['recovered']}```")
    elif message.content == ("-covid Poland"):
        await message.channel.send(f"```Confirmed cases: {poland_cases['confirmed']} Deaths: {poland_cases['deaths']} Recovered: {poland_cases['recovered']}```")
    elif message.content == ("-covid Romania"):
        await message.channel.send(f"```Confirmed cases: {romania_cases['confirmed']} Deaths: {romania_cases['deaths']} Recovered: {romania_cases['recovered']}```")
    elif message.content == ("-covid Japan"):
        await message.channel.send(f"```Confirmed cases: {japan_cases['confirmed']} Deaths: {japan_cases['deaths']} Recovered: {japan_cases['recovered']}```")


client.loop.create_task(update_stats())
client.run(token)
