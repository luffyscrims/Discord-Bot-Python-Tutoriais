![Imgur](https://i.imgur.com/Ppj8XVL.png)
 Types:<p>
 1 = Jogando<p>
 2 = ouvindo<p>
 3 = assistindo<p>

Type 1
```await client.change_presence(game=discord.Game(name="Vagner Tutorial", type=1))```

![Imgur](https://i.imgur.com/5KJZMdb.jpg)

Type 2
```await client.change_presence(game=discord.Game(name="Vagner Tutorial", type=2))```

![Imgur](https://i.imgur.com/735pB21.jpg)

Type 3
```await client.change_presence(game=discord.Game(name="Vagner Tutorial", type=3))```

![Imgur](https://i.imgur.com/0PIRMWf.jpg)

Modo Stream
```await client.change_presence(game=discord.Game(name='Sesshomru TV', type=1, url='https://www.twitch.tv/vagner8k'),status='streaming')```

![Imgur](https://i.imgur.com/6uTj8vD.jpg)

Modo Dnd
```await client.change_presence(game=discord.Game(name='Vagner Tutorial'), status=discord.Status.dnd)```

![Imgur](https://i.imgur.com/ztJ1qmg.jpg)

Modo Idle
```await client.change_presence(game=discord.Game(name='Vagner Tutorial'), status=discord.Status.idle)```

![Imgur](https://i.imgur.com/bcJQVIc.jpg)



