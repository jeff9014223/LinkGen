# Imports

try:
    import json, os, platform, time, discord
except Exception:
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")
    print("LinkGen uses Pycord, Try to remove discord.py when installed")
    time.sleep(3)
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")
    print("Pycord not found - Installing...\n")
    os.system("pip install py-cord==2.0.0b4")
    os._exit(0)

client = discord.Bot()

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
    services = ["discord", "epicgames", "steam", "nitro", "spotify", "roblox", "tiktok",]
    for service in services:
        if os.path.exists(f"accounts/{service}.txt"): pass
        else:
            open(f"accounts/{service}.txt", "a").write(f"Paste {service} accounts here")
            print(f"[WARNING] No Accounts found for {service} - Creating file...")

# Generate Command

@client.dot_command(name="gen", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def generate(ctx, service_name):
    if str(ctx.channel.id) != json.loads(open("config.json", "r").read())["gen_channel"]:
        await ctx.respond(f"You can only gen in: <#{json.loads(open('config.json', 'r').read())['gen_channel']}>", ephemeral=True)
    else:
        services = ["discord", "epicgames", "steam", "nitro", "spotify", "roblox", "tiktok"]
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
                                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1288705140240678925/1322774408720420954/standard.gif?ex=67a77dea&is=67a62c6a&hm=56924172e7380dd6f5391e2137e1650734e1e5db59b58582c458124184403a82&")
                                user = await client.fetch_user(int(ctx.author.id))
                                await user.send(embed=embed)
                                log = client.guilds[0].get_channel(int(json.loads(open("config.json", "r").read())["log_channel"]))
                                embed = discord.Embed(title=f"{ctx.author.name} has genned 1 {service}", description=f"**Account**\n```{data[0]}```", color=00FFFF)
                                await log.send(embed=embed)
                                await ctx.respond("Account Generated!! check your DM please")
                            except Exception:
                                await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                    else:
                        await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                else:
                    await ctx.respond(f"You cannot gen {service}!", ephemeral=True)

# Help Command

@client.dot_command(name="help", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def help(ctx):
    embed = discord.Embed(title="Cronaus help command", description="Usage: /generate <service name>, /stock", color=00FFFF)
    embed.add_field(name="All Services", value="``discord``, ``epicgames``, ``steam,``, ``nitro``, ``spotify``, ``roblox``, ``tiktok``,")
    embed.set_footer(text="Made by Cronaus")
    await ctx.respond(embed=embed)

# Stock Command

@client.dot_command(name="stock", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def stock(ctx):
    services = ["discord", "epicgames", "steam", "nitro", "spotify", "roblox", "tiktok"]
    stocklist = []
    for service in services:
        if os.path.exists(f"accounts/{service.lower()}.txt"):
            stocklist.append(f"{service} stock: {len(open(f'accounts/{service}.txt', 'r').readlines())} accounts")
    embed = discord.Embed(title="LinkGen Stock", description="Display's stock of all services", color=00FFFF)
    embed.add_field(name="Stock", value="\n".join(stocklist))
    embed.set_footer(text="Made by Snikker#1337")
    await ctx.respond(embed=embed)

client.run(json.loads(open("config.json", "r").read())["token"])

