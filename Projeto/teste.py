import speech_recognition as sr
from random import choice
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess
from threading import Thread
import datetime
import os
from time import sleep, strftime
import serial


class Virtual_assit(Thread):

    def _init_(self):
        Thread._init_(self, target=Virtual_assit)
        self.start()

    def record_audio(self):

        while True:
            self.microfone = sr.Recognizer()
            with sr.Microphone() as source:

                self.microfone.adjust_for_ambient_noise(source)
                audio = self.microfone.listen(source)

            try:
                self.voice_data = self.microfone.recognize_google(
                    audio, language='pt-BR')
                print(self.voice_data)
                return self.voice_data.lower()

            except sr.UnknownValueError:
                return self.record_audio()

    def exist(self, terms):

        for term in terms:
            if term in voice_data_novo:
                return term

    def conexaoarduino(self):

        mic.falar2('ok , verificando conexões')
        sleep(1)

        for contador in range(1, 16):
            try:
                print(contador)
                self.arduino = serial.Serial(f'COM{contador}', 9600)
                sleep(1)
                mic.falar2('dispositivo conectado ')
                return

            except:

                if contador > 14:
                    mic.falar2('nenhum dispositivo foi encontrado')
                    return

    def respostacomandos(self, voice_data):

        if self.exist(['conectar ao arduino', 'conectar o arduíno', 'arduino']):
            self.conexaoarduino()

        if self.exist(['pesquisar', 'quero fazer uma pesquisa', 'pesquisa']):

            mic.falar2('oque deseja pesquisar?')
            voice_data = self.record_audio()

            if 'cancela' in voice_data:
                mic.falar2('tudo bem')

                return
            search_term = voice_data.split('pesquisar')[-1]
            url = "http://google.com/search?q=" + search_term
            mic.falar2("ok")
            webbrowser.get().open(url)

        elif self.exist(['versão do sistema']):
            fala = choice(('ok , vou verificar', 'certo vou da uma olhada'))
            mic.falar2(fala)
            sleep(0.6)
            os.system('winver')

        elif self.exist(['abrir o youtube', 'abra o youtube', 'abre o youtube']) and 'google' not in voice_data:
            search_term = voice_data.split("youtube")[-1]
            url = "http://www.youtube.com/" + search_term
            webbrowser.get().open(url)
            mic.falar2("ok")
            return

        elif self.exist(['abrir vs code']):

            subprocess.call(
                f"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif self.exist(['youtube']):

            search_term = voice_data.split("youtube")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            mic.falar2("ok")

        elif self.exist(['abre o facebook', 'abrir meu facebook', 'abrir facebook', 'facebook']):

            mic.falar2("ok")
            webbrowser.open("https://www.facebook.com/")

        elif self.exist(['bloquear pc', 'bloqueia o pc', 'bloquear computador']):
            mic.falar2('certo')
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif self.exist(['desligar pc']):
            mic.falar2('ok , desligando')
            os.system('shutdown -s -t 0')

        elif self.exist(['word', 'abrir word']):
            mic.falar2('ok')
            sleep(1)
            os.startfile('Winword.exe')

        elif self.exist(['whatsapp']):
            os.startfile(r'C:\Users\Thiago\appWindows\WhatsApp.lnk')

        elif self.exist(['dota']):

            try:
                mic.falar2('certo')
                webbrowser.open('steam://rungameid/570')
                sleep(3)
                mic.falar2('bom jogo senhor')
            except:
                mic.falar2('dota nao está instalado senhor')

        try:

            if self.exist(['liga o ventilador', 'ligar ventilador', 'desligar ventilador']):

                fala = choice(('ok , tudo bem', ' ligando'))
                mic.falar2(fala)
                self.arduino.write('a'.encode())
                voice_data
        except:
            mic.falar2('não detectei o dispositivo ')
            mic.falar2('vou verificar as conexões ')
            self.conexaoarduino()


class Micro(Thread):

    def _init_(self,):
        Thread._init_(self, target=Micro)
        self.start()
        self.microfone = sr.Recognizer()

    def run(self):

        while True:
            with sr.Microphone() as source:

                self.microfone.adjust_for_ambient_noise(source)
                audio = self.microfone.listen(source)

            try:
                frase = self.microfone.recognize_google(
                    audio, language='pt-BR')

                print(frase.lower())
                yield frase.lower()

            except sr.UnknownValueError:
                pass

    def falar2(self, audio):
        engine = pyttsx3.init('sapi3')
        engine.say(audio)
        engine.runAndWait()


mic = Micro()
assis = Virtual_assit()
hour = int(datetime.datetime.now().hour)


while True:

    if hour >= 0 and hour < 12:

        mic.falar2("bom dia, senhor ")

    elif hour >= 12 and hour < 18:
        mic.falar2("boa tarde, senhor")

    else:
        mic.falar2("Boa noite, senhor")

    for voice_data_novo in mic.run():

        if 'sofia' in voice_data_novo:

            voz = choice(('olá ', ' pode falar', 'pois não , pode falar'))
            mic.falar2(voz)

        assis.respostacomandos(voice_data_novo)

        if 'obrigado' in voice_data_novo:
            datavoz = choice(('de nada', 'disponha'))
            mic.falar2(datavoz)

        elif 'horas' in voice_data_novo:
            str_ime = strftime("%H:%M")
            mic.falar2(f"são {str_ime}")

        elif 'fechar assistente' in voice_data_novo:

            quit()

        if 'piada' in voice_data_novo:
            datavoz = choice((f'Fiquei confuso depois da aula de inglês, Se , car , significa carro ,e ,“men” significa “homens”, então minha tia Carmen é um Transformer?',
                              'Qual é o animal que não vale mais nada?  ,    O javali!'))

            mic.falar2(datavoz)

        try:
            app = voice_data_novo
            resp = eval(app.replace('x', '*'))
            mic.falar2(resp)
        except:
            True
