import logging
from telegram import Update
from telegram.ext import Application, ChatMemberHandler, CallbackContext

# Activer les logs pour voir ce qui se passe
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Votre token du BotFather
TOKEN = '7356602517:AAHHzr4B6Z7WAvjduuJttXcrohpNRvPdhFQ'

async def welcome_message(update: Update, context: CallbackContext):
    logging.info(f"New members joined: {update.chat_member.new_chat_members}")
    
    # Extraire l'utilisateur qui vient de rejoindre
    for member in update.chat_member.new_chat_members:
        user_id = member.id
        first_name = member.first_name

        # Debug: Imprimer dans le terminal pour vérifier
        logging.info(f"Bienvenue à {first_name} (ID: {user_id})")

        # Envoyer un message privé à l'utilisateur
        await context.bot.send_message(
            chat_id=user_id,
            text=f"Bienvenue {first_name} ! 🎉 Merci d'avoir rejoint notre canal. Si tu as des questions, n'hésite pas à demander."
        )

def main():
    # Initialiser l'application (nouvelle approche dans la version 20.x)
    application = Application.builder().token(TOKEN).build()

    # Détecter l'arrivée de nouveaux membres dans le groupe
    chat_member_handler = ChatMemberHandler(welcome_message)

    # Ajouter les handlers
    application.add_handler(chat_member_handler)

    # Démarrer le bot avec polling
    application.run_polling()

if __name__ == '__main__':
    main()
