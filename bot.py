import os
import discord
from discord.ext import commands
from xvideos import choose_random_porn_comment, choose_random_video

BOT_TOKEN = os.getenv('BOT_TOKEN')

client = commands.Bot(command_prefix='!')

def format_comment(author, content, title, url):
    mask = '**O {0}  comentou o seguinte:**\n`{1}`\n\n**vi isso no video:**\n`{2}`'
    return mask.format(author, content, title)

@client.event
async def on_ready():
    print("Bot online!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='digite !meajuda para mais informações'))

@client.command(description='Apresenta a lista de ajuda ao usuário.')
async def meajuda(ctx):
    await client.send_message(ctx.message.author, '*Olá. Aqui estão os comandos:*\n - `!mensagem` - Procura um comentario aleatório no Xvideos em Portugês\n - `!telemensagem` - Procura um comentario aleatório no Xvideos em Portugês e o envia com TTS (Text to Speech)\n - `!busca *termo*` - Procura um video pelo termo passado, se não passado nenhum, é retornado um video aleatório\n - `!meajuda` - Mostra esta mensagem.\n\n Encontrou algum problema ou tem alguma sugestão para o bot? Sinta-se livre para nos enviar uma mensagem por este link https://github.com/marquesgabriel/bot-discord-comentarios-xvideos/issues\n')
    await client.delete_message(ctx.message)


@client.command(description='Procura um comentário no xvideos.')
async def mensagem(ctx):
    await ctx.say('**Buscando...\n**')
    try:
        comment, url = choose_random_porn_comment()
        await ctx.say(format_comment(*comment))
        await ctx.say('https://xvideos.com'+url)
    except Exception :
        await ctx.say('Houve uma falha na busca. Tente novamente.')

    await client.delete_message(ctx.message)

@client.command(description='Procura um comentário no xvideos. COM TTS.')
async def telemensagem(ctx):
    await ctx.say('Buscando...')
    try:
        author, comment, title, url = choose_random_porn_comment()
        author = '**O '+author+'  comentou o seguinte:**\n'
        title = '**vi isso no video:**\n`'+title+'`'
        await ctx.say(author)
        await ctx.say(comment, tts=True)
        await ctx.say(title)
        await ctx.say('https://xvideos.com'+url)
    except Exception :
        await ctx.say('Houve uma falha na busca. Tente novamente.')

    await client.delete_message(ctx.message)


@client.command(description='Procura um video baseado na tag passada.')
async def busca(ctx, tag=None):
    try:
        link = choose_random_video(tag)
        await client.send_message(ctx.message.author, 'Segura esse link aí meu parceiro: ' + link)
    except Exception:
        await ctx.say('Houve uma falha na busca. Tente novamente.')

    await client.delete_message(ctx.message)


client.run(BOT_TOKEN)
