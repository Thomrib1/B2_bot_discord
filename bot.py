import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from conversation.arbre_binaire import ConversationManager
from conversation.qi import calculate_qi, get_qi_message
from historique.list import CommandLinkedList 
from storage.data_manager import save_data, load_data

load_dotenv()

print("Lancement du bot...")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
conversation_manager = ConversationManager()

print("Chargement de la sauvegarde...")
user_histories = load_data()

def add_to_history(user_id, command_name):
    if user_id not in user_histories:
        user_histories[user_id] = CommandLinkedList() 
    user_histories[user_id].add(command_name)
    save_data(user_histories)

@bot.event
async def on_ready():
    print("apagnan ça commence")
    await bot.tree.sync()
    print("Slash commands synchronisées")

@bot.tree.command(name="last_cmd", description="Affiche ta dernière commande")
async def cmd_last(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id in user_histories:
        last = user_histories[user_id].get_last()
        await interaction.response.send_message(f"Dernière commande : {last}")
    else:
        await interaction.response.send_message("Aucun historique.")

@bot.tree.command(name="history", description="Affiche tout ton historique")
async def cmd_history(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id in user_histories:
        history = user_histories[user_id].get_all()
        await interaction.response.send_message(f"Ton historique :\n{history}")
    else:
        await interaction.response.send_message("Historique vide.")

@bot.tree.command(name="clear_history", description="Vide ton historique")
async def cmd_clear(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id in user_histories:
        user_histories[user_id].clear()
        await interaction.response.send_message("Historique vidé !")
    else:
        await interaction.response.send_message("Rien à vider.")

@bot.tree.command(name="test", description="Lance le test de personnalité")
async def cmd_test(interaction: discord.Interaction):
    add_to_history(interaction.user.id, "/test")
    user_id = interaction.user.id
    question = conversation_manager.start_conversation(user_id)
    await interaction.response.send_message(f"Test de personnalité lancé !\n\n{question}")

@bot.tree.command(name="help", description="Affiche l'aide des commandes")
async def cmd_help(interaction: discord.Interaction):
    add_to_history(interaction.user.id, "/help")
    await interaction.response.send_message(
        "Voici les commandes disponibles :\n"
        "- /test : Lance le test de personnalité\n"
        "- /qi : Calcule ton QI aléatoirement\n"
        "- /abandonner : Abandonne le test en cours\n"
        "- /reset : Recommence le test\n"
        "- /history : Voir tout l'historique\n"
        "- /last_cmd : Voir la dernière commande\n"
        "- /clear_history : Vider l'historique\n"
        "- bonjour : Pour saluer la voyante"
    )

@bot.tree.command(name="qi", description="Calcule ton QI")
async def cmd_qi(interaction: discord.Interaction):
    add_to_history(interaction.user.id, "/qi")
    qi_score = calculate_qi()
    message = get_qi_message(qi_score)
    await interaction.response.send_message(message)

@bot.tree.command(name="abandonner", description="Abandonne le test en cours")
async def cmd_abandonner(interaction: discord.Interaction):
    add_to_history(interaction.user.id, "/abandonner")
    user_id = interaction.user.id
    conversation_manager.abandon(user_id)
    await interaction.response.send_message("Test abandonné sale faible d'esprit")

@bot.tree.command(name="reset", description="Recommence le test depuis le début")
async def cmd_reset(interaction: discord.Interaction):
    add_to_history(interaction.user.id, "/reset")
    user_id = interaction.user.id
    question = conversation_manager.reset(user_id)
    await interaction.response.send_message(f"Test recommencé !\n{question}")

@bot.tree.command(name="speak_about", description="Vérifie si le bot connait un sujet")
async def cmd_speak(interaction: discord.Interaction, sujet: str):
    add_to_history(interaction.user.id, f"/speak_about {sujet}")
    exists = conversation_manager.speak_about(sujet)
    
    if exists:
        await interaction.response.send_message(f"Oui, je parle de **{sujet}** dans mon test")
    else:
        await interaction.response.send_message("Non, je ne parle pas de ce sujet.")

@bot.command()
async def sync(ctx):
    try:
        synced = await bot.tree.sync()
        print(f"Commandes synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur de synchro : {e}")

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
    user_id = message.author.id
    content = message.content.lower()
    
    if content == 'bonjour':
        add_to_history(user_id, "bonjour")
        await message.channel.send("Bonjour :)")
        return
    
    if conversation_manager.is_in_conversation(user_id):
        if content in ['oui', 'non']:
            response = conversation_manager.answer(user_id, content)
            await message.channel.send(response)
        else:
            await message.channel.send("Tu es en plein test ! Réponds par 'oui', 'non', ou tape /reset ou /abandonner.")
        return

bot.run(os.getenv('DISCORD_TOKEN'))