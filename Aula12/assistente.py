## é nessa biblioteca que está rede de deep learning rodando a IA
import speech_recognition as sr

## faz a comunicação com o Sistema Operacional
import os

## Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #chama algoritmo de redução de ruídos
        microfone.adjust_for_ambient_noise(source)

        #frase para solicitar que o usuário diga algo
        print("Diga alguma coisa: ")

        #leitura e armazenamento do que foi dito
        audio = microfone.listen(source)

    try:
        #passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "anotações" in frase:
            os.system("open /Users/viniciussouza/Documents/Anotações.txt")
            #os.open("open /Users/viniciussouza/Documents/Anotações.txt")
            print("abrindo anotações")
        
        if "navegador" in frase: 
            #os.system("start Chrome.exe")
            os.system("open /Applications/Google\ Chrome.app")
            print("abrindo chrome")

        if "WhatsApp" in frase: 
            os.system("open /Applications/WhatsApp.app")
            print("abrindo whatsapp")
            
        #Comando para o Windows
        #if "Excel" in frase:
            #os.system("start Excel.exe")
            #print("abrindo excel")
        
        #retorna a frase pronunciada
        print("Você disse: " + frase)

    except sr.UnknownValueError:
        print('Não entendi')

        return frase
    ## FIM - Função para ouvir e reconhecer a fala

## INÍCIO DO PROGRAMA
print("Início do Programa Assistente Pessoal")

ouvir_microfone()