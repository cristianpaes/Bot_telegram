import telebot

chave_api = "5895823774:AAFXVFSoqLnc8yPnf85es15GAz02kht6kVo"

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=["CNPJ"])
def cnpj(mensagem):
    bot.send_message(mensagem.chat.id,"verificando CNPJ")

@bot.message_handler(commands=["Empresa"])
def empresa(mensagem):
    bot.send_message(mensagem.chat.id,"verificando por empresa")

@bot.message_handler(commands=["Pedido"])
def pedido(mensagem):
    bot.send_message(mensagem.chat.id,"verificando número do pedido")

@bot.message_handler(commands=["Status"])
def status(mensagem):
    texto = """
    Deseja realizar a busca por?
    /CNPJ - Número do CNPJ
    /Empresa - Nome da Empresa
    /Pedido - Número do pedido
    /Menu
    """
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands=["Reclamar"])
def reclamar(mensagem):
    bot.send_message(mensagem.chat.id, "Favor enviar um email para sac@artlatex.com.br")

@bot.message_handler(commands=["Sair"])
def sair(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado por entrar em contato.")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def menu(mensagem):
    texto = """
    Olá squi é Artlatex
    Em que eu posso lhe ajudar?
    (Clique nas opções)
    /Status - Status do Pedido
    /Reclamar - Reclamação do Pedido 
    /Sair
Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
    """
    bot.reply_to(mensagem, texto)

bot.polling()