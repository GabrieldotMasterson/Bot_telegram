
'''
TITULO DO PROJETO: Moai bot
DATA DO INICIO: 02/01/24
OBJETIVO DO PROJETO: ser um bot com algumas funções aleatorias para teste
FEATURES: 
  1- responder oi
  2- enviar conselho recebido de uma api
  3- enviar imagens de gatinhos recebido de uma api

'''

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import json
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= "en", target= "pt")

async def oi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.first_name == "Masterson":
        await update.message.reply_text(f'sai daqui vc carrega nezucos {update.effective_user.first_name}')
    elif update.effective_user.first_name == "Lecteo":
        await update.message.reply_text(f'tu ajuda o masterso a carrega nezuku {update.effective_user.first_name}')
    elif update.effective_user.first_name == "João Daniel":
        await update.message.reply_text(f'n me misturo com pato como vc {update.effective_user.first_name}')
    else:
        await update.message.reply_text(f'oi {update.effective_user.first_name} vc n esta com nenhuma nezuco ne?')

async def conselho(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get("https://api.adviceslip.com/advice")
    obj = response.json()
    text = obj['slip']['advice']
    traduc = tradutor.translate(text)
    
    await update.message.reply_text(traduc)

async def gato(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get("https://api.thecatapi.com/v1/images/search?limit=1")
    json = response.json()
    print(json)
    
    #await update.message.reply_photo(requests.get(json['url']))
    if update.effective_user.first_name == "Masterson":
        sl = json['url']
        await update.message.reply_text(sl)
    else:
        await update.message.reply_text(f'vc n merece gagos {update.effective_user.first_name} ')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("oi", oi))
app.add_handler(CommandHandler("conselho", conselho))
app.add_handler(CommandHandler("gago", gato))

app.run_polling()
