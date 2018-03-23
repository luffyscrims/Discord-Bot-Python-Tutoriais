#METODO 1 
#pegand o id do usuario

 if  message.content.lower().startswith('/teste'):
        if not message.author.id == 'INSIRA O ID AQUI':
         return await client.send_message(message.channel, "Sem permissão.Voçe nao possui o Id para usar esse comando")
        await client.send_message(message.channel, "Olá Mundo,estou vivo.")
        
#METODO 2 
#pelo maior cargo do usuario 
#ou seja ele vai ter que possuir esse cargo como seu maior cargo

if message.content.lower().startswith('/teste'):
         if not  message.author.top_role.name == "INSIRA O NOME DO CARGO AQUI":
             return await client.send_message(message.channel, "Sem permissão.Voçe nao possiu permissão do cargo")
         await client.send_message(message.channel, "Olá Mundo,estou vivo."
                                 
#METODO 3 
#pelo nome do cargo
#so vai pode usar o comando que possui o cargo especificado                                   
                                   
    if message.content.lower().startswith('/teste'):
        role = discord.utils.get(message.server.roles, name='INSIRA O NOME DO CARGO AQUI')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Sem permissão.Voçe nao possuir o cargo")
        await client.send_message(message.channel, "Olá Mundo,estou vivo.")   

#METODO 4 
#por id em uma lista
#antes do client event coloque
nomedasulista= ['id1','id2','id3']  
#dentro do evento on_message coloque o comando 
#se o id nao estive na lista nao irá poder executar o comando                                   
if  message.content.lower().startswith('/teste'):
        if not message.author.id in nomedasulista:
         return await client.send_message(message.channel, "Sem permissão.voçe nao possui o id")
        await client.send_message(message.channel, "Olá Mundo,estou vivo.")                                
                                   
