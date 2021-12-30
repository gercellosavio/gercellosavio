#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram import *
from telegram.ext import *

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

listar = "listar"
apuestas = "apuestas"
# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""

    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('0,001')],[KeyboardButton('/jugar'),KeyboardButton(listar),KeyboardButton(apuestas)],
     [KeyboardButton('estadistica'),KeyboardButton('saldo ganador'),KeyboardButton('resultado')]
     ]
    
  
    context.bot.send_message(chat_id=update.effective_chat.id, text="comencemos 🥳", reply_markup=ReplyKeyboardMarkup(buttons))

def jugar(update: Update, context: CallbackContext):
      buttons2 = [[KeyboardButton('🐋Ballena'),KeyboardButton('🐶Perro'),KeyboardButton('🐱Gato'),KeyboardButton('🦒Jirafa')],
      [KeyboardButton('🐐Chivo'),KeyboardButton('🐀Raton'),KeyboardButton('🐏Carnero'),KeyboardButton('🐷Cochino')]
      ,[KeyboardButton('🦉Buho'),KeyboardButton('🐔Gallo'),KeyboardButton('🐍Culebra'),KeyboardButton('🦃Pavo')],
      [KeyboardButton('🦌Venado'),KeyboardButton('🐮Toro'),KeyboardButton('🦎iguana'),KeyboardButton('🐵Mono')],
      [KeyboardButton('🦂alacran'),KeyboardButton('🐊Caiman'),KeyboardButton('🦅Aguila'),KeyboardButton('🐯Tigre')],
      [KeyboardButton('🐛100pies'),KeyboardButton('🦁leon'),KeyboardButton('🐸rana'),KeyboardButton('🦜perico')],
      [KeyboardButton('🐴Caballo'),KeyboardButton('🦊Zorro'),KeyboardButton('🐻Oso'),KeyboardButton('🐎Burro')],
      [KeyboardButton('🐬Delfin'),KeyboardButton('🐫Camello'),KeyboardButton('🦓Cebra'),KeyboardButton('🐄Vaca')],
      [KeyboardButton('🐘Elefante'),KeyboardButton('🦔Lapa'),KeyboardButton('🐟Pescado'),KeyboardButton('🐿Ardilla')],
      [KeyboardButton('🐓Gallina'),KeyboardButton('🐧Zamuro'),KeyboardButton('/Regresar🔙')]
      ]
      context.bot.send_message(chat_id=update.effective_chat.id, text="comencemos 🥳",reply_markup=ReplyKeyboardMarkup(buttons2))


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    print(update.message.text)
    chat_id = update.message.chat_id 
    print(chat_id)
    print(update.effective_chat.id)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5039897959:AAEBlceAfn4flNvX_IUN29wFR5LXJz1NvpA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", startCommand))
    dispatcher.add_handler(CommandHandler("Regresar", startCommand))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("jugar", jugar))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()