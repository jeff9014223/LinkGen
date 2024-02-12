# Imports

try:
    import json, os, platform, time, discord, subprocess
except ModuleNotFoundError as e:
    module_name = str(e).split("'")[1]
    print(f"ModuleNotFound: {e} has not been found")
    if module_name == "discord":
        match input("Do you want to install it? (y/n)"):
            case 'y':
                os.system("pip install py-cord==2.0.0b4");subprocess.run(["python", __file__])
            case 'n':
                print("Ok, closing now")
                time.sleep(0.4);exit()
            case _:
                print("Invalid input! Closing..")
                time.sleep(0.4);exit()
    match input("Do you want to install it? (y/n)"):
        case 'y':
            os.system(f'pip install {module_name}');subprocess.run(["python", __file__])
        case 'n':
            print("Ok, closing now")
            time.sleep(0.4)
        case _:
            print("Invalid input! Closing..")
            time.sleep(0.4)

try:
    client = discord.Bot()
except Exception as e:
    os.system('cls' if os.name == "nt" else 'clear')
    print(f"An error occured: {e} \nLinkGen uses Pycord, Try to remove discord.py when installed")
    time.sleep(1.5);os.system('cls' if os.name == "nt" else 'clear')
    match input("Do you want to install pycord? (y/n)"):
        case 'y':
            os.system("pip uninstall discord");os.system("pip uninstall discord.py");os.system("pip uninstall discord.py-self")
            os.system("pip install py-cord==2.0.0b4");subprocess.run(["python", __file__])
        case 'n':
            print("ok, goodbye");time.sleep(0.3)
        case _:
            input("Invalid Input! Press enter to close")
# Check if correctly setup

if os.path.exists("accounts"): pass
else: os.mkdir("accounts")
if platform.system() == "Windows": os.system("cls")
else: os.system("clear")
try: json.loads(open("config.json", "r").read())
except Exception: print("[ERROR] Config File missing")
try:json.loads(open("config.json", "r").read())["token"]
except Exception: print("[ERROR] Discord Token not set")
try:json.loads(open("config.json", "r").read())["guild_id"]
except Exception: print("[ERROR] Guild ID not set")
try:json.loads(open("config.json", "r").read())["log_channel"]
except Exception: print("[ERROR] Log Channel not set")

# When bot is logged in

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    print(f"Using guild: {client.guilds[0].name}")
    print("LinkGen Ready", "\n")
    await client.change_presence(activity=discord.Game(name="LinkGen V2.0"))
    try: client.guilds[0].get_role(int(json.loads(open("config.json", "r").read())["gen_role"]))
    except Exception: print("[ERROR] Gen Role not set")
    try: client.guilds[0].get_channel(int(json.loads(open("config.json", "r").read())["gen_channel"]))
    except Exception: print("[ERROR] Gen Channel not set")
    services = ["nordvpn", "hulu", "expressvpn", "nitro", "creditcard", "spotify", "netflix", "disney", "minecraft"]
    for service in services:
        if os.path.exists(f"accounts/{service}.txt"): pass
        else:
            open(f"accounts/{service}.txt", "a").write(f"Paste {service} accounts here")
            print(f"[WARNING] No Accounts found for {service} - Creating file...")

# Generate Command

@client.slash_command(name="generate", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def generate(ctx, service_name):
    if str(ctx.channel.id) != json.loads(open("config.json", "r").read())["gen_channel"]:
        await ctx.respond(f"You can only gen in: <#{json.loads(open('config.json', 'r').read())['gen_channel']}>", ephemeral=True)
    else:
        services = ["NordVPN", "Hulu", "ExpressVPN", "Nitro", "CreditCard", "Spotify", "Netflix", "Disney", "Minecraft"]
        for service in services:
            if service_name.lower() == service.lower():
                if str(json.loads(open("config.json", "r").read())["gen_role"]) in str(ctx.author.roles):
                    if os.path.exists(f"accounts/{service.lower()}.txt"):
                        with open(f"accounts/{service.lower()}.txt", "r+") as accounts:
                            data = accounts.readlines()
                            accounts.seek(0)
                            accounts.truncate()
                            accounts.writelines(data[1:])
                            try:
                                embed = discord.Embed(title=f"{service} Account Generated", description="LinkGen Account Generator", color=0x46a9f0)
                                embed.add_field(name="Login Credentials", value=f"```{data[0]}```", inline=True)
                                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773133136929226763/797204521997828106/777514274829893683.gif")
                                user = await client.fetch_user(int(ctx.author.id))
                                await user.send(embed=embed)
                                log = client.guilds[0].get_channel(int(json.loads(open("config.json", "r").read())["log_channel"]))
                                embed = discord.Embed(title=f"{ctx.author.name} has genned 1 {service}", description=f"**Account**\n```{data[0]}```", color=0x46a9f0)
                                await log.send(embed=embed)
                                await ctx.respond("Account Generated, check your DM")
                            except Exception:
                                await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                    else:
                        await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                else:
                    await ctx.respond(f"You cannot gen {service}!", ephemeral=True)

# Help Command

@client.slash_command(name="help", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def help(ctx):
    embed = discord.Embed(title="LinkGen help command", description="Usage: /generate <service name>, /stock", color=0x46a9f0)
    embed.add_field(name="All Services", value="``nordvpn``, ``hulu``, ``expressvpn``, ``nitro``, ``creditcard``, ``spotify``, ``netflix``, ``disney``, ``minecraft``")
    embed.set_footer(text="Made by Snikker#1337")
    await ctx.respond(embed=embed)

# Stock Command

@client.slash_command(name="stock", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def stock(ctx):
    services = ["NordVPN", "Hulu", "ExpressVPN", "Nitro", "CreditCard", "Spotify", "Netflix", "Disney", "Minecraft"]
    stocklist = []
    for service in services:
        if os.path.exists(f"accounts/{service.lower()}.txt"):
            stocklist.append(f"{service} stock: {len(open(f'accounts/{service}.txt', 'r').readlines())} accounts")
    embed = discord.Embed(title="LinkGen Stock", description="Display's stock of all services", color=0x46a9f0)
    embed.add_field(name="Stock", value="\n".join(stocklist))
    embed.set_footer(text="Made by Snikker#1337")
    await ctx.respond(embed=embed)

client.run(json.loads(open("config.json", "r").read())["token"])

