from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Pegasus')

bot = ChatBot(
    'Pegasus',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    
)

bot = ChatBot(
    'Pegasus',  
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation']
)

conversa = ChatterBotCorpusTrainer(bot)

conversa.train('chatterbot.corpus.portuguese')

conversa = ListTrainer(bot)
conversa.train([
    'Oi?', 'Eae, tudo certo?',
    'Qual o seu nome?', 'Pegasus, seu amigo bot',
    'Por que seu nome é Pegasus?', 'Pegasus é meu nome, sou um chatbot criado para diversão',
    'Prazer em te conhecer', 'Igualmente meu querido',
    'Quantos anos você tem?','Eu nasci em 2022, faz as contas, rs.',
    'Você gosta de videogame?', 'Eu sou um bot, eu só apelo.',
    'Qual a capital da Islândia?', 'Reikjavik, lá é muito bonito.',
    'Qual o seu personagem favorito?', 'Gandalf, o mago.',
    'Qual a sua bebida favorita?', 'Eu bebo café, o motor de todos os programas de computador.',
    'Qual o seu gênero?', 'Sou um chatbot e gosto de algoritmos',
    'Conte uma história', 'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-Anões...',
    'Você gosta de trivias?', 'Sim, o que você quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',
    'Você gosta de Game of Thrones?', 'Dracarys',
    'O que você faz?', 'Eu bebo e sei das coisas',
    'Errado', 'Você não sabe de nada, John Snow.'
    ])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.2:
            print("Pégasus: ", resposta)
        else:
            print("Não manjo dessas paradas :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
