#Root & Sword 0.1v beta

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame
import random
import json
import sys
import os

class ftesons:
    def __init__(self):
        pygame.mixer.init()
        self.pasta = os.path.dirname(os.path.abspath(__file__))
        self.arquivo = os.path.join(self.pasta, 'save.json')
        self.arquivo2 = os.path.join(self.pasta, 'estoques.json')

        self.save = []
        self.estoques = []

        self.tarazerado = PhotoImage(file=self.carregarimagem('tarazerado'))

        self.normal = PhotoImage(file=self.carregarimagem('normal'))
        self.atacando = PhotoImage(file=self.carregarimagem('atacando'))
        self.defendendo = PhotoImage(file=self.carregarimagem('defendendo'))
        self.morto = PhotoImage(file=self.carregarimagem('morto'))
        
        self.tarav2normal = PhotoImage(file=self.carregarimagem('tarav2normal'))
        self.tarav2atacando = PhotoImage(file=self.carregarimagem('tarav2atacando'))
        self.tarav2defendendo = PhotoImage(file=self.carregarimagem('tarav2defendendo'))
        self.tarav2morto = PhotoImage(file=self.carregarimagem('tarav2morto'))

        self.goblinnormal = PhotoImage(file=self.carregarimagem('goblinnormal'))
        self.goblinatacando = PhotoImage(file=self.carregarimagem('goblinatacando'))
        self.goblindefendendo = PhotoImage(file=self.carregarimagem('goblindefendendo'))
        self.goblinmorto = PhotoImage(file=self.carregarimagem('goblinmorto'))

        self.orcnormal = PhotoImage(file=self.carregarimagem('orcnormal'))
        self.orcatacando = PhotoImage(file=self.carregarimagem('orcatacando'))
        self.orcdefendendo = PhotoImage(file=self.carregarimagem('orcdefendendo'))
        self.orcmorto = PhotoImage(file=self.carregarimagem('orcmorto')) 

        self.golemnormal = PhotoImage(file=self.carregarimagem('golemnormal'))
        self.golematacando = PhotoImage(file=self.carregarimagem('golematacando'))
        self.golemdefendendo = PhotoImage(file=self.carregarimagem('golemdefendendo'))
        self.golemmorto = PhotoImage(file=self.carregarimagem('golemmorto'))

        self.bruxonormal = PhotoImage(file=self.carregarimagem('bruxonormal'))
        self.bruxoatacando = PhotoImage(file=self.carregarimagem('bruxoatacando'))
        self.bruxodefendendo = PhotoImage(file=self.carregarimagem('bruxodefendendo'))
        self.bruxomorto = PhotoImage(file=self.carregarimagem('bruxomorto'))

        self.dragaonormal = PhotoImage(file=self.carregarimagem('dragaonormal'))
        self.dragaoatacando = PhotoImage(file=self.carregarimagem('dragaoatacando'))
        self.dragaodefendendo = PhotoImage(file=self.carregarimagem('dragaodefendendo'))
        self.dragaomorto = PhotoImage(file=self.carregarimagem('dragaomorto'))          

    def efeito(self, nome):
        arquivo = os.path.join(self.pasta, 'sons', 'efeitos', f'{nome}.mp3')

        efeito = pygame.mixer.Sound(arquivo)
        efeito.play()

    def musica(self, nome):
        arquivo = os.path.join(self.pasta, 'sons', f'{nome}.mp3')

        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()

    def carregarimagem(self, nome):
        arquivo = os.path.join(self.pasta, 'fotos', f'{nome}.png')
        return arquivo
    
    def carregarJson(self):  
        if not os.path.exists(self.arquivo):
            return [], 'n'

        with open(self.arquivo, 'r', encoding='utf-8') as f:
            self.save = json.load(f)
            return 'p'

    def salvarJson(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.save, f, indent=4, ensure_ascii=False)

    def carregarJsonestoques(self):  
        with open(self.arquivo2, 'r', encoding='utf-8') as f:
            self.estoques = json.load(f)

    def salvarJsonestoques(self):
        with open(self.arquivo2, 'w', encoding='utf-8') as f:
            json.dump(self.estoques, f, indent=4, ensure_ascii=False)

class prota:
    def __init__(self, nome, vida, ataque, defesa, agilidade, moedas):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.moedas = moedas

    def serializar(self):
        return {
            'nome': self.nome,
            'vida': self.vida,
            'ataque': self.ataque,
            'defesa': self.defesa,
            'agilidade': self.agilidade,
            'moedas': self.moedas
        }
    
    @classmethod
    def deserializar(cls, dados):
        return cls(dados['nome'], dados['vida'], dados['ataque'], dados['defesa'], dados['agilidade'], dados['moedas'])
        
class inimigo:
    def __init__(self, nome, vida, ataque, defesa, agilidade, moedas):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.moedas = moedas

class rootP:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Root & Sword 0.1v beta')
        self.root.resizable(False, False)
        self.root.geometry('1100x800')
        self.root.config(bg='white')

        self.frameM = tk.Frame(self.root, bg='white')
        self.frameM.pack()

        for x in self.frameM.winfo_children():
            x.destroy()

        self.SeF = ftesons()

        self.SeF.musica('menu')

        self.frameN = tk.Frame(bg='white')
        self.frameMJ = tk.Frame(bg='white')
        self.frameS = tk.Frame(bg='white')
        self.frameL = tk.Frame(bg='white')
        self.frameML = tk.Frame(bg='green')
        self.frameZ = tk.Frame(bg='yellow')

        self.Goblin = inimigo(nome="Goblin Saqueador", vida=60, ataque=12, defesa=3, moedas=35, agilidade=1000)
        self.Orc = inimigo(nome="Orc Guerreiro", vida=150, ataque=25, defesa=8, moedas=100, agilidade=950)
        self.Golem = inimigo(nome="Golem de Pedra", vida=350, ataque=40, defesa=25, moedas=250, agilidade=900)
        self.Bruxo = inimigo(nome="Bruxo das Sombras", vida=800, ataque=95, defesa=45, moedas=550, agilidade=850)
        self.Dragao = inimigo(nome="Dragão de Sangue", vida=2000, ataque=210, defesa=110, moedas=1100, agilidade=800)

        tk.Label(self.frameM, text='===Root & Sword===', font=('Arial', 50), bg='white').pack(pady=5)

        ftI = tk.Label(self.frameM, image=self.SeF.normal)
        ftI.image = self.SeF.normal
        ftI.pack(pady=5, expand=True)

        labelC = tk.Label(self.frameM, text='vc n tem save, ent n consegue continuar', font=('Arial', 15), bg='white')

        botaoC = tk.Button(self.frameM, text='Continuar', command=self.menujogo, width=20, height=3)

        self.salvo = self.SeF.carregarJson()

        if 'n' in self.salvo:
            labelC.pack(pady=5)
        
        else:
            botaoC.pack(pady=5)

        tk.Button(self.frameM, text='Começar novo jogo', width=20, height=3, command=self.NovoJogo).pack(pady=10)

        self.root.mainloop()

    def voltarM(self, desaparecer, aparecer, cor):
        desaparecer.pack_forget()

        self.root.config(bg=cor)

        aparecer.pack()

    def NovoJogo(self):
        self.frameM.pack_forget()

        for x in self.frameN.winfo_children():
            x.destroy()

        tk.Label(self.frameN, text='=Novo jogo=', font=('Arial', 100), bg='white').pack(pady=5)

        self.resultadoN = tk.Label(self.frameN, text='escreva o nome do seu personagem', font=('Arial', 30), bg='white')
        self.resultadoN.pack(pady=10)

        self.nome = tk.Entry(self.frameN, font=("Arial", 40))
        self.nome.pack(pady=15)

        tk.Button(self.frameN, text='Criar', width=20, height=3, command=self.criar).pack(pady=15)

        tk.Button(self.frameN, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameN, self.frameM, 'white')).pack(pady=15)

        self.frameN.pack()

    def voltarL(self):
        self.resultadoN.config(text='escreva o nome do seu personagem')

    def criar(self):
        nick = self.nome.get()

        if len(nick) < 3:
            self.resultadoN.config(text='o seu nick possui menos de 3 letras')

            self.root.after(1500, self.voltarL)

        else:

            self.jogador = prota(nome=nick, vida=50, ataque=10, defesa=5, agilidade=1000, moedas=0)

            self.SeF.save = self.jogador.serializar()
            self.SeF.salvarJson()

            self.SeF.carregarJsonestoques()

            for x in self.SeF.estoques:
                self.SeF.estoques[x] = 1

            self.SeF.salvarJsonestoques()

            messagebox.showinfo('Sucesso', 'o save foi criado com sucesso, o jogo vai ser reniciado!')

            argumentos = [f'"{arg}"' if " " in arg else arg for arg in sys.argv]
            os.execv(sys.executable, [sys.executable] + argumentos)

            self.root.destroy()      

    def menujogo(self):
        self.frameM.pack_forget()

        for x in self.frameMJ.winfo_children():
            x.destroy()

        self.saveU = prota.deserializar(self.SeF.save)

        tk.Label(self.frameMJ, text=f'=Olá {self.saveU.nome}=', font=('Arial', 100), bg='white').pack(pady=5)

        tk.Button(self.frameMJ, text='Lutar', command=self.ML, width=20, height=3).pack(pady=15)

        tk.Button(self.frameMJ, text='Loja', width=20, height=3, command=self.loja).pack(pady=15)

        tk.Button(self.frameMJ, text='Mostrar status', command=self.mostrarstatus, width=20, height=3).pack(pady=15)

        tk.Button(self.frameMJ, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameMJ, self.frameM, 'white')).pack(pady=15)

        self.frameMJ.pack()

    def ML(self):
        self.frameMJ.pack_forget()

        for x in self.frameML.winfo_children():
            x.destroy()

        self.root.config(bg='green')

        self.frameLl = tk.Frame(bg='green')

        tk.Label(self.frameML, text='=Campo de batalha=', font=('Arial', 80), bg='green').pack(pady=5)

        inimigos = ['Goblin', 'Orc', 'Golem', 'Bruxo', 'Dragao']

        for x, n in enumerate(inimigos):
            tk.Button(

                self.frameML, 
                text=f'{n}', 
                width=20,
                height=3,
                command=lambda ind=x: self.certeza(ind)

            ).pack(pady=5)

        tk.Button(self.frameML, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameML, self.frameMJ, 'white')).pack(pady=50)

        self.frameML.pack()

    def certeza(self, indice):
        inimigosM = [self.Goblin, self.Orc, self.Golem, self.Bruxo, self.Dragao]
        escolhidoM = inimigosM[indice]
        
        duvida = messagebox.askyesno('confirmar', f'tem certeza q deseja lutar com o {escolhidoM.nome}? vida: {escolhidoM.vida}, ataque: {escolhidoM.ataque}, defesa: {escolhidoM.defesa}, agilidade: {escolhidoM.agilidade} e recompensa: {escolhidoM.moedas}')

        if duvida:
            self.inimigoE(indice)

    def inimigoE(self, indice):
        self.frameML.pack_forget()

        for x in self.frameLl.winfo_children():
            x.destroy()

        self.tarafotos = [self.SeF.normal, self.SeF.atacando, self.SeF.defendendo, self.SeF.morto]
        self.tarav2fotos = [self.SeF.tarav2normal, self.SeF.tarav2atacando, self.SeF.tarav2defendendo, self.SeF.tarav2morto]

        self.goblinfotos = [self.SeF.goblinnormal, self.SeF.goblinatacando, self.SeF.goblindefendendo, self.SeF.goblinmorto]
        self.orcfotos = [self.SeF.orcnormal, self.SeF.orcatacando, self.SeF.orcdefendendo, self.SeF.orcmorto]
        self.golemfotos = [self.SeF.golemnormal, self.SeF.golematacando, self.SeF.golemdefendendo, self.SeF.golemmorto]
        self.bruxofotos = [self.SeF.bruxonormal, self.SeF.bruxoatacando, self.SeF.bruxodefendendo, self.SeF.bruxomorto]
        self.dragaofotos = [self.SeF.dragaonormal, self.SeF.dragaoatacando, self.SeF.dragaodefendendo, self.SeF.dragaomorto]

        self.goblinsons = ['ataque', 'defesa', 'goblinmorto']
        self.orcsons = ['ataque', 'defesa', 'orcmorto']
        self.golemsons = ['golemataque', 'defesa', 'golemmorto']
        self.bruxosons = ['bruxoataque', 'defesa', 'bruxomorto']
        self.dragaosons = ['dragaoataque', 'defesa', 'dragaomorto']

        self.sonsI = [self.goblinsons, self.orcsons, self.golemsons, self.bruxosons, self.dragaosons]

        self.CDF = [self.goblinfotos, self.orcfotos, self.golemfotos, self.bruxofotos, self.dragaofotos]

        self.inimigos = [self.Goblin, self.Orc, self.Golem, self.Bruxo, self.Dragao]

        if self.saveU.vida >= 430 and self.saveU.ataque >= 320 and self.saveU.defesa >= 350 and 755 >= self.saveU.agilidade:
            self.FDJ = self.tarav2fotos

        else:
            self.FDJ = self.tarafotos

        self.FDI = self.CDF[indice]

        self.escolhido = self.inimigos[indice]

        self.escolhidosom = self.sonsI[indice]

        self.vidas = [self.saveU.vida, self.escolhido.vida]
        self.ataques = [self.saveU.ataque, self.escolhido.ataque]
        self.defesas = [self.saveU.defesa, self.escolhido.defesa]

        self.ataqueJB = ''
        self.defesaJB = ''
        self.ataqueIB = ''
        self.defesaIB = ''

        self.trava = False
        self.trava2 = False

        tk.Label(self.frameLl, text='=em luta=', font=('Arial', 80), bg='green').pack(pady=5)

        framein = tk.Frame(self.frameLl, bg='green')
        framein.pack(side='left', padx=50, expand=True)

        self.ftI = tk.Label(framein, image=self.FDI[0])
        self.ftI.image = self.FDI[0]
        self.ftI.pack(pady=5)      

        self.botaoA = tk.Button(framein, text='Ataque', width=12, height=2, command=self.acaoA)
        self.botaoA.pack(pady=10)

        framejo = tk.Frame(self.frameLl, bg='green')
        framejo.pack(side='right', padx=50, expand=True)

        self.ftJ = tk.Label(framejo, image=self.FDJ[0])
        self.ftJ.image = self.FDJ[0]
        self.ftJ.pack(pady=5)

        self.botaoD = tk.Button(framejo, text='Defesa', width=12, height=2, command=self.acaoD)
        self.botaoD.pack(pady=10)

        self.vidastk = tk.Label(self.frameLl, text=f'vida do inimigo: {self.vidas[1]}, vida do jogador: {self.vidas[0]}')
        self.vidastk.pack(pady=5)

        self.info = tk.Label(self.frameLl, text='...')
        self.info.pack(pady=5)

        frameembaixo = tk.Frame(self.frameLl, bg='green')
        frameembaixo.pack(side='bottom', pady=20, fill='x')

        tk.Button(frameembaixo, text='Voltar', width=20, height=3, command=self.desistir).pack()

        self.botaoA.config(state='disabled')
        self.botaoD.config(state='disabled')

        self.SeF.efeito('fight')

        self.root.after(1000, self.iniciar)

        self.frameLl.pack(fill='both', expand=True)

    def iniciar(self):
        self.botaoA.config(state='normal')
        self.botaoD.config(state='normal')

        self.SeF.musica('fight2')

        self.inimigoA()
        self.verificar()

    def desistir(self):
        duvida = messagebox.askyesno('confirmar', 'se vc desistir da luta vc perdera suas moedas')

        if duvida:
            self.saveU.moedas -= self.escolhido.moedas

            self.SeF.save = self.saveU.serializar()
            self.SeF.salvarJson()

            self.trava = True

            self.voltarM(self.frameLl, self.frameML, 'green')

    def vitoriabox(self):
        messagebox.showinfo('Vitória', 'parabens vc ganhou a luta, vc ganhou as moedas do inimigo! O PROGRAMA VAI SER RENICIADO!')

        argumentos = [f'"{arg}"' if " " in arg else arg for arg in sys.argv]
        os.execv(sys.executable, [sys.executable] + argumentos)

        self.root.destroy()

    def derrotabox(self):
        messagebox.showinfo('Derrorta', 'vc perdeu a luta e morreu, ent vc perdeu o seu save! O PROGRAMA VAI SER RENICIADO!')

        os.remove(self.SeF.arquivo)

        argumentos = [f'"{arg}"' if " " in arg else arg for arg in sys.argv]
        os.execv(sys.executable, [sys.executable] + argumentos)
        
        self.root.destroy()

    def fugiubox(self):
        messagebox.showinfo('Fugiu da luta', 'vc fugiu da luta ent vc perdeu umas moedas para o inimigo. Covarde! O PROGRAMA VAI SER RENICIADO!')

        argumentos = [f'"{arg}"' if " " in arg else arg for arg in sys.argv]
        os.execv(sys.executable, [sys.executable] + argumentos)

        self.root.destroy()

    def acaoA(self):
        self.atacarJ()
        self.atacarJL('on')

    def acaoD(self):
        self.defesaJ()
        self.defesaJL('on')

    def desligarAc(self, acao):
        setattr(self, acao, 'off')

    def atacarJL(self, valor):
        self.ataqueJB = valor

        if self.ataqueJB == 'on':
            self.vidas[1] -= self.ataques[0]

            self.info.config(text='o jogador atacou')

        self.root.after(self.saveU.agilidade, lambda: self.desligarAc('ataqueJB'))

        self.vidastk.config(text=f'vida do inimigo: {self.vidas[1]}, vida do jogador: {self.vidas[0]}')

    def defesaJL(self, valor):
        self.defesaJB = valor

        self.root.after(self.saveU.agilidade, lambda: self.desligarAc('defesaJB'))

    def atacarIL(self, valor):
        self.ataqueIB = valor

        if self.ataqueIB == 'on':
            self.vidas[0] -= self.ataques[1]

            self.info.config(text='o inimigo atacou')

        self.root.after(self.escolhido.agilidade, lambda: self.desligarAc('ataqueIB'))

        self.vidastk.config(text=f'vida do inimigo: {self.vidas[1]}, vida do jogador: {self.vidas[0]}')

    def defesaIL(self, valor):
        self.defesaIB = valor

        self.root.after(self.escolhido.agilidade, lambda: self.desligarAc('defesaIB'))

    def verificar(self):
        if self.defesaJB == 'on':
            if self.defesaIB == 'on':
                self.info.config(text='nada acontece, pois os dois estavam defendendo')

                self.defesaJB = 'processado'
                self.defesaIB = 'processado'
                self.ataqueJB = 'processado'
                self.ataqueIB = 'processado'

            elif self.ataqueIB == 'on':
                conta = self.ataques[1] - self.defesas[0]

                if conta <= 0:
                    self.info.config(text='ataque anulado do inimigo')
                    self.vidas[0] -= 0

                else:
                    self.info.config(text='o jogador defendeu')
                    self.vidas[0] -= conta

                self.defesaJB = 'processado'
                self.defesaIB = 'processado'
                self.ataqueJB = 'processado'
                self.ataqueIB = 'processado'

            else:
                self.info.config(text='nada acontece pois o jogador defendeu e o inimigo n atacou')

                self.defesaJB = 'processado'
                self.defesaIB = 'processado'
                self.ataqueJB = 'processado'
                self.ataqueIB = 'processado'

        elif self.defesaIB == 'on':
            if self.defesaJB == 'on':
                self.info.config(text='nada acontece, pois os dois estavam defendendo')

                self.defesaJB = 'processado'
                self.defesaIB = 'processado'
                self.ataqueJB = 'processado'
                self.ataqueIB = 'processado'

            elif self.ataqueJB == 'on':
                conta = self.ataques[0] - self.defesas[1]

                if conta <= 0:
                    self.info.config(text='ataque anulado do jogador')
                    self.vidas[1] -= 0

                else:
                    self.info.config(text='o inimigo defendeu')
                    self.vidas[1] -= conta

                self.defesaJB = 'processado'
                self.defesaIB = 'processado'
                self.ataqueJB = 'processado'
                self.ataqueIB = 'processado'

            else:
                self.info.config(text='nada acontece, pois o inimigo defendeu e o jogador n atacou')

                self.defesaJB = 'processado'
                self.defesaIB = 'processado'
                self.ataqueJB = 'processado'
                self.ataqueIB = 'processado'

        self.vidastk.config(text=f'vida do inimigo: {self.vidas[1]}, vida do jogador: {self.vidas[0]}')
        self.loop()

    def loop(self):
        if self.trava2:
            print('loop parou')
            return

        elif self.vidas[0] <= 0 or self.vidas[1] <= 0:
            if self.vidas[0] > 0:
                if self.escolhido.nome == 'Dragão de Sangue':
                    self.trava2 = True

                    self.ftI.config(image=self.FDI[3])
                    self.ftI.image = self.FDI[3]

                    self.SeF.efeito(self.escolhidosom[2])

                    self.root.after(750, self.zerado)
                    return

                else:
                    self.trava2 = True

                    self.ftI.config(image=self.FDI[3])
                    self.ftI.image = self.FDI[3]

                    if not self.trava2:
                        self.SeF.efeito(self.escolhidosom[2])

                    self.root.after(750, self.derrotaINI)               
                    return

            elif self.vidas[1] > 0:
                self.trava2 = True

                self.ftJ.config(image=self.FDJ[3])
                self.ftJ.image = self.FDJ[3]

                self.SeF.efeito('taramorto')

                self.root.after(750, self.derrotaJO)
                return

        elif self.trava:
            self.trava2 = True

            self.fugiubox()
            return

        else:
            self.root.after(1, self.verificar)   

    def derrotaJO(self):
        self.voltarM(self.frameLl, self.frameML, 'green')

        self.derrotabox()

    def derrotaINI(self):
        self.saveU.moedas += self.escolhido.moedas

        self.SeF.save = self.saveU.serializar()
        self.SeF.salvarJson()

        self.voltarM(self.frameLl, self.frameML, 'green')

        self.vitoriabox()

    def atacarJ(self):
        self.ftJ.config(image=self.FDJ[1])
        self.ftJ.image = self.FDJ[1]

        self.SeF.efeito('ataque')

        self.botaoA.config(state='disabled')
        self.botaoD.config(state='disabled')

        self.root.after(self.saveU.agilidade, self.voltarJ)

    def defesaJ(self):
        self.ftJ.config(image=self.FDJ[2])
        self.ftJ.image = self.FDJ[2]

        self.SeF.efeito('defesa')

        self.botaoA.config(state='disabled')
        self.botaoD.config(state='disabled')

        self.root.after(self.saveU.agilidade, self.voltarJ)

    def voltarJ(self):
        self.ftJ.config(image=self.FDJ[0])
        self.ftJ.image = self.FDJ[0]

        self.botaoA.config(state='normal')
        self.botaoD.config(state='normal')

    def inimigoA(self):
        lista = ['atacar', 'defender']
        escolha = random.choice(lista)

        if escolha == 'atacar':
            self.atacarI()
            self.atacarIL('on')

        else:
            self.defesaI()
            self.defesaIL('on')

        self.root.after(self.escolhido.agilidade, self.voltarI)

    def atacarI(self):
        self.ftI.config(image=self.FDI[1])
        self.ftI.image = self.FDI[1]

        if not self.trava2:
            self.SeF.efeito(self.escolhidosom[0])

    def defesaI(self):
        self.ftI.config(image=self.FDI[2])
        self.ftI.image = self.FDI[2]

        if not self.trava2:
            self.SeF.efeito(self.escolhidosom[1])

    def voltarI(self):
        self.ftI.config(image=self.FDI[0])
        self.ftI.image = self.FDI[0]

        self.root.after(self.escolhido.agilidade, self.inimigoA)

    def zerado(self):
        self.frameLl.pack_forget()

        for x in self.frameZ.winfo_children():
            x.destroy()

        self.root.config(bg='yellow')

        self.SeF.musica('zerado')

        tk.Label(self.frameZ, text='🎊PARABENS, VC ZEROU O GAME🎉', font=('Arial', 35), bg='yellow').pack(pady=5)

        tk.Label(self.frameZ, text='vc matou o boss e agr vc é o mais forte do lugar!', font=('Arial', 20), bg='yellow').pack(pady=5)

        fotoZ = tk.Label(self.frameZ, image=self.SeF.tarazerado)
        fotoZ.image = self.SeF.tarazerado
        fotoZ.pack(pady=5, expand=True)

        tk.Button(self.frameZ, text='Voltar', width=20, height=3, command=self.voltarZ).pack(pady=15)

        self.frameZ.pack()

    def voltarZ(self):
        self.saveU.moedas += self.escolhido.moedas

        self.SeF.save = self.saveU.serializar()
        self.SeF.salvarJson()

        argumentos = [f'"{arg}"' if " " in arg else arg for arg in sys.argv]
        os.execv(sys.executable, [sys.executable] + argumentos)

        self.root.destroy()

    def loja(self):
        self.frameMJ.pack_forget()

        for x in self.frameL.winfo_children():
            x.destroy()

        self.valorVida = [5, 32, 92, 238, 480]
        self.valorAtaque = [15, 40, 100, 250, 500]
        self.valorDefesa = [10, 38, 97, 242, 492]
        self.valorAgilidade = [7, 35, 87, 233, 495]
        
        self.buffvida = [30, 100, 250, 750, 1400]
        self.buffdano = [30, 80, 200, 500, 1000]
        self.buffdefesa = [25, 90, 230, 650, 1300]
        self.buffAgilidade = [75, 80, 90, 100, 120]

        self.SeF.carregarJsonestoques()

        self.vidaC = [
            {'nome': f'vida{x + 1}', 'buff': b, 'preço': p, 'estoque': 1}
            for x, (b, p) in enumerate(zip(self.buffvida, self.valorVida))
        ]
        
        self.ataqueC = [
            {'nome': f'ataque{x + 1}', 'buff': b, 'preço': p, 'estoque': 1}
            for x, (b, p) in enumerate(zip(self.buffdano, self.valorAtaque))
        ]
        
        self.defesaC = [
            {'nome': f'defesa{x + 1}', 'buff': b, 'preço': p, 'estoque': 1}
            for x, (b, p) in enumerate(zip(self.buffdefesa, self.valorDefesa))
        ]

        self.agilidadeC = [
            {'nome': f'agilidade{x + 1}', 'buff': b, 'preço': p, 'estoque': 1}
            for x, (b, p) in enumerate(zip(self.buffAgilidade, self.valorAgilidade))
        ]

        self.frameVida = tk.Frame(bg='white')
        self.frameAtaque = tk.Frame(bg='white')
        self.frameDefesa = tk.Frame(bg='white')
        self.frameAgilidade= tk.Frame(bg='white')

        tk.Label(self.frameL, text='=Loja=', font=('Arial', 100), bg='white').pack(pady=5)

        nomes = ['Vida', 'Ataque', 'Defesa', 'Agilidade']

        chamar = [self.vida, self.ataque, self.defesa, self.agilidade]

        for x, (n, c) in enumerate(zip(nomes, chamar)):
            tk.Button(

                self.frameL, 
                text=f'{n}', 
                width=20,
                height=3,
                command=c

            ).pack(pady=5)

        tk.Button(self.frameL, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameL, self.frameMJ, 'white')).pack(pady=15)

        self.frameL.pack()

    def vida(self):
        self.frameL.pack_forget()

        for x in self.frameVida.winfo_children():
            x.destroy()

        tk.Label(self.frameVida, text='=Categoria vida=', font=('Arial', 50), bg='white').pack(pady=5)

        self.botoesV = [
            tk.Button(

                self.frameVida, 
                text=f'buff{x + 1}, buff: {b}, valor: {v}', 
                width=20,
                height=3,
                command= lambda nome='vida', ind=x: self.comprar(nome, ind)

            )

            for x, (v, b) in enumerate(zip(self.valorVida, self.buffvida)) 

        ]

        for x in self.botoesV:
            x.pack(pady=5)

        tk.Button(self.frameVida, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameVida, self.frameL, 'white')).pack(pady=15)

        self.frameVida.pack()

    def ataque(self):
        self.frameL.pack_forget()

        for x in self.frameAtaque.winfo_children():
            x.destroy()

        tk.Label(self.frameAtaque, text='=Categoria ataque=', font=('Arial', 50), bg='white').pack(pady=5)

        self.botoesAt = [
            tk.Button(

                self.frameAtaque, 
                text=f'buff{x + 1}, buff: {b}, valor: {v}', 
                width=20,
                height=3,
                command= lambda nome='ataque', ind=x: self.comprar(nome, ind)

            )

            for x, (v, b) in enumerate(zip(self.valorAtaque, self.buffdano))

        ]

        for x in self.botoesAt:
            x.pack(pady=5)

        tk.Button(self.frameAtaque, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameAtaque, self.frameL, 'white')).pack(pady=15)

        self.frameAtaque.pack()

    def defesa(self):
        self.frameL.pack_forget()

        for x in self.frameDefesa.winfo_children():
            x.destroy()

        tk.Label(self.frameDefesa, text='=Categoria defesa=', font=('Arial', 50), bg='white').pack(pady=5)

        self.botoesD = [
            tk.Button(

                self.frameDefesa,
                text=f'buff{x + 1}, buff: {b}, valor: {v}', 
                width=20,
                height=3,
                command= lambda nome='defesa', ind=x: self.comprar(nome, ind)

            )

            for x, (v, b) in enumerate(zip(self.valorDefesa, self.buffdefesa))
            
        ]

        for x in self.botoesD:
            x.pack(pady=5)

        tk.Button(self.frameDefesa, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameDefesa, self.frameL, 'white')).pack(pady=15)

        self.frameDefesa.pack()

    def agilidade(self):
        self.frameL.pack_forget()

        for x in self.frameAgilidade.winfo_children():
            x.destroy()

        tk.Label(self.frameAgilidade, text='=Categoria agilidade=', font=('Arial', 50), bg='white').pack(pady=5)

        self.botoesAg = [
            tk.Button(

                self.frameAgilidade,
                text=f'buff{x + 1}, buff: {b}, valor: {v}', 
                width=20,
                height=3,
                command= lambda nome='agilidade', ind=x: self.comprar(nome, ind)

            )

            for x, (v, b) in enumerate(zip(self.valorAgilidade, self.buffAgilidade))       

        ]

        for x in self.botoesAg:
            x.pack(pady=5)

        tk.Button(self.frameAgilidade, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameAgilidade, self.frameL, 'white')).pack(pady=15)

        self.frameAgilidade.pack()

    def comprar(self, produtoE, buffE):
        nomes = ['vida', 'ataque', 'defesa', 'agilidade']

        for x, n in enumerate(nomes):
            if produtoE == n:
                indice = x
                break

        categorias = [self.vidaC, self.ataqueC, self.defesaC, self.agilidadeC]

        categoriaI = categorias[indice]

        escolhido = categoriaI[buffE]

        itemN = escolhido['nome']

        if escolhido['preço'] > self.saveU.moedas:
            messagebox.showwarning('erro', 'vc n tem moedas suficiente para comprar esse buff')

        elif 0 >= self.SeF.estoques[itemN]:
            messagebox.showwarning('erro', 'vc ja comprou esse buff antes')

        else:
            duvida = messagebox.askyesno("Confirmar", "Tem certeza q deseja comprar esse buff?")

            if duvida:
                self.SeF.efeito('buying')

                valorT = getattr(self.saveU, produtoE)

                self.saveU.moedas -= escolhido['preço']
                
                if produtoE == 'agilidade':
                    valorN = valorT - escolhido['buff']

                else:
                    valorN = valorT + escolhido['buff']

                setattr(self.saveU, produtoE, valorN)

                self.SeF.save = self.saveU.serializar()
                self.SeF.salvarJson()

                self.SeF.estoques[itemN] -= 1

                self.SeF.salvarJsonestoques()

                messagebox.showinfo('sucesso', 'vc comprou esse item!')

    def mostrarstatus(self):
        self.frameMJ.pack_forget()

        for x in self.frameS.winfo_children():
            x.destroy()

        fotos = [self.SeF.tarav2normal, self.SeF.normal]

        if self.saveU.vida >= 430 and self.saveU.ataque >= 320 and self.saveU.defesa >= 350 and 755 >= self.saveU.agilidade:
            fotoU = fotos[0]

        else:
            fotoU = fotos[1]

        tk.Label(self.frameS, text='=Seus status=', font=('Arial', 20), bg='white').pack(pady=5)
        
        ftS = tk.Label(self.frameS, image=fotoU)
        ftS.image = fotoU
        ftS.pack(pady=5, expand=True)

        nomes = ['Vida', 'Ataque', 'Defesa', 'Agilidade', 'Moedas']

        nomesC = [self.saveU.vida, self.saveU.ataque, self.saveU.defesa, self.saveU.agilidade, self.saveU.moedas]

        for n, c in zip(nomes, nomesC):
            tk.Label(

                self.frameS, 
                text=f'{n}: {c}', 
                font=('Arial', 10), 
                bg='white'

            ).pack(pady=5)

        tk.Button(self.frameS, text='Voltar', width=20, height=3, command=lambda: self.voltarM(self.frameS, self.frameMJ, 'white')).pack(pady=15)

        self.frameS.pack()

jogo = rootP()

if '__init__' == '__main__':
    jogo = rootP()