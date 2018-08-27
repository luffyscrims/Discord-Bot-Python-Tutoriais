import discord
#Obs on_message é uma merda
#istancia do discord
# o shard_count é numero de fragmentação que o bot terá
client = discord.AutoShardedClient(shard_count=2)
prefixo = "t!"

@client.event
async def on_ready():
    print(client.user.name)
    print("logado")

@client.event
async def on_message(message):
    if message.content.lower().startswith(prefixo+'teste'):
        await message.channel.send("ok")

    if message.content.lower().startswith(prefixo+'shard'):
        tutorial = '\n'.join(f'ID {shard} -- **' + str(round(client.latencies[shard][1] * 1000)) + '**ms'for shard in client.shards)
        await message.channel.send("**Shards Rodando**\n"+tutorial)



client.run('token aqui')