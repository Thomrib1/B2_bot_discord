import discord
import os
from dotenv import load_dotenv
from conversation.arbre_binaire import ConversationManager
load_dotenv()

print("Lancement du bot...")
bot = discord.Client(intents=discord.Intents.all())
conversation_manager = ConversationManager()

async def cmd_test(message):
    user_id = message.author.id
    question = conversation_manager.start_conversation(user_id)
    await message.channel.send(f" Questionnaire de personnalité lancé !\n\n{question}")

async def cmd_help(message):

    await message.channel.send(
        " Voici les commandes disponibles :\n"
        "- !test : Lance le questionnaire de personnalité\n"
        "- bonjour : Salue le bot\n"
        "- !help : Affiche cette aide"
    )

async def cmd_bonjour(message):
    await message.channel.send("bien le sang")

async def cmd_abandonner(message):

    user_id = message.author.id
    conversation_manager.abandon(user_id)
    await message.channel.send(" Questionnaire abandonné. Sale faible d'esprit")

async def cmd_reset(message):

    user_id = message.author.id
    question = conversation_manager.reset(user_id)
    await message.channel.send(f"Questionnaire recommencé !\n{question}")

async def handle_conversation(message):

    user_id = message.author.id
    content = message.content.lower()
    
    if content in ['oui', 'non']:
        response = conversation_manager.answer(user_id, content)
        await message.channel.send(response)
    else:
        await message.channel.send("Tu es en plein questionnaire ! Réponds par 'oui', 'non', tape '!reset' ou '!abandonner'.")

COMMANDS = {
    '!test': cmd_test,
    '!help': cmd_help,
    '!bonjour': cmd_bonjour,
    '!abandonner': cmd_abandonner,
    '!reset': cmd_reset
}

@bot.event
async def on_ready():
    print("apagnan ça commence")

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
    user_id = message.author.id
    content = message.content.lower()
    
    if conversation_manager.is_in_conversation(user_id):
        if content in ['!abandonner', '!reset']:
            await COMMANDS[content](message)
        else:
            await handle_conversation(message)
        return

    if not content.startswith('!'):
        return

    if content in COMMANDS:
        await COMMANDS[content](message)
    else:
        await message.channel.send("Commande inconnue. Tape !help pour voir les commandes disponibles !")

bot.run(os.getenv('DISCORD_TOKEN'))