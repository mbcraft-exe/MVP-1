import tkinter
from tkinter import PhotoImage
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.ttk import *
from tkinter import filedialog
global entree


#clé MB INC 1225


bad = 0
mne = 0

import io

fnt = tkinter.Tk()
mne += 1
fnt.title("MVP")
p1 = tkinter.PhotoImage(file='mvp logo simple red.png')
# Icon set for program window
fnt.iconphoto(False, p1)

img = tkinter.PhotoImage(file='mvp logo simple blue.png')
lb = tkinter.Label(image=img).pack()
label = tkinter.Label(text="Bienvenue sur MVP Scannner !")
label.pack()



def launch():
    import io
    global ana, img, label, menubar, menu1, filename
    if bad != 1:
        menubar = tkinter.Menu(fnt)
        menu1 = tkinter.Menu(menubar, tearoff=0)

        filename = askopenfilename(title="Ouvrir votre document",
                                   filetypes=[('Fichiers Python', '.py'), ('Fichiers JavaScript', '.js')])
        with io.open(filename, "r", encoding="utf-8") as fichier:
            content = fichier.read()
            print(content)
            if "#clé MB INC 1225" not in content:
                if "os.mkdir" in content and "import os" in content:
                    img.config(file="mvp logo simple red.png")

                    def verifplus():
                        showinfo('Info', 'Le scan va commencer !')
                        track = 0
                        print("ok")
                        fichier = open(filename, "r")
                        for line in fichier:
                            if "bot.login(" in line or 'const Discord = require("discord.js");' in line or "var mkdirp = require('mkdirp');" in line or "from pynput import keyboard" in line or "def on_press(key):" in line:
                                track += 1
                        showwarning('Détection:', f'Il a été détecté {int(track)} problème(s) de sécurité dans votre fichier !')

                    def read():
                        lne = 1
                        rd = tkinter.Tk()
                        rd.title(f"Lecture de {filename}")

                        liste = Listbox(rd, width=170, height=20)
                        with io.open(filename, "r", encoding="utf-8") as fichier:
                            for line in fichier:
                                liste.insert(lne, line)
                                lne += 1
                        liste.pack()
                        rd.mainloop()


                    def callback():
                        showinfo('Explication:',
                                 'Il semble que ce fichier contient un argument de type:\nos.mkdir()\n\nCe qui signifie que ce fichier peut créer des dossiers !')

                    label.config(text="Oh, il semble que ce fichier contient quelque chose de mauvais...")

                    with io.open("Historique.txt", "a", encoding="utf-8") as f:
                        f.write(f"\n{filename} - Mauvais")

                    def historique():
                        var = 1
                        with io.open("Historique.txt", "r", encoding="utf-8") as f:
                            hist = tkinter.Tk()
                            hist.title("Historique")
                            liste = Listbox(hist, width=90, height=20)
                            for line in f:
                                if line != "\n":
                                    liste.insert(var, line)
                                    var += 1

                            liste.pack()

                            def clear():
                                with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                    f.write("")

                            bt = tkinter.Button(hist, text="Vider", command=clear)
                            bt.pack(side=tkinter.RIGHT)

                            hist.mainloop()

                    def search():


                        searchwindow = tkinter.Tk()

                        entree = tkinter.Entry(searchwindow, width=30)
                        entree.pack()

                        def verif():
                            if entree.get() in content:
                                showwarning("Vérification", "Ce fichier semblerait contenir ")
                            else:
                                showinfo("Info", "Ce fichier ne contient pas l'argument que vous avez saisit")

                        bouton = Button(searchwindow, text="Chercher", command=verif)
                        bouton.pack(side=tkinter.LEFT)
                        searchwindow.mainloop()

                    def mscan():
                        sc = tkinter.Tk()
                        sc.title("Scan")
                        label = tkinter.Label(sc,
                                              text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                        label.pack()
                        import time
                        time.sleep(5)
                        import os
                        counter = 0
                        thisdir = os.getcwd()
                        liste = Listbox(hist, width=90, height=20)
                        for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                            for file in f:
                                filepath = os.path.join(r, file)
                                if ".py" in file or ".js" in file:
                                    counter += 1
                                    liste.insert(counter, os.path.join(r, file))
                                    liste.pack()

                        sc.mainloop()

                    menubar = tkinter.Menu(fnt)
                    menuII = tkinter.Menu(menubar, tearoff=0)
                    menuII.add_command(label="Analyse total du PC", command=mscan)
                    menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                    fnt.config(menu=menubar)
                    menu1.add_command(label="Chercher un élément", command=search)
                    menu1.add_command(label="Historique des fichiers", command=historique)
                    menu1.add_command(label="Lire un fichier", command=read)
                    menu1.add_command(label="Analyse approfondie", command=verifplus)
                    menu1.add_command(label="Afficher les détails", command=callback)
                else:
                    if "bot.token" in content or "client.token" in content and "import discord" in content:
                        img.config(file='mvp logo simple red.png')

                        def verifplus():
                            showinfo('Info', 'Le scan va commencer !')
                            track = 0
                            print("ok")
                            fichier = open(filename, "r")
                            for line in fichier:
                                if "bot.login(" in line or 'const Discord = require("discord.js");' in line or "var mkdirp = require('mkdirp');" in line or "from pynput import keyboard" in line or "def on_press(key):" in line:
                                    track += 1
                            showwarning('Détection:',
                                        f'Il a été détecté {int(track)} problème(s) de sécurité dans votre fichier !')

                        def callback():
                            showinfo('Explication:',
                                     'Il semble que ce fichier contient un argument de type:\nclient(bot).token\n\nCe qui signifie que ce fichier contient bot discord !')

                        label.config(text="Oh, il semble que ce fichier contient quelque chose de mauvais...")
                        label.pack()

                        def read():
                            lne = 1
                            rd = tkinter.Tk()
                            rd.title(f"Lecture de {filename}")

                            liste = Listbox(rd, width=170, height=20)
                            with io.open(filename, "r", encoding="utf-8") as fichier:
                                for line in fichier:
                                    liste.insert(lne, line)
                                    lne += 1
                            liste.pack()
                            rd.mainloop()

                        with io.open("Historique.txt", "a", encoding="utf-8") as f:
                            f.write(f"\n{filename} - Mauvais")

                        def historique():
                            var = 1
                            with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                hist = tkinter.Tk()
                                hist.title("Historique")
                                liste = Listbox(hist, width=90, height=20)
                                for line in f:
                                    if line != "\n":
                                        liste.insert(var, line)
                                        var += 1

                                liste.pack()

                                def clear():
                                    with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                        f.write("")

                                bt = tkinter.Button(hist, text="Vider", command=clear)
                                bt.pack(side=tkinter.RIGHT)

                                hist.mainloop()

                        def search():

                            searchwindow = tkinter.Tk()

                            entree = tkinter.Entry(searchwindow, width=30)
                            entree.pack()

                            def verif():
                                if entree.get() in content:
                                    showwarning("Vérification", "Ce fichier semblerait contenir ")
                                else:
                                    showinfo("Info", "Ce fichier ne contient pas l'argument que vous avez saisit")

                            bouton = Button(fenetre, text="Chercher", command=verif)
                            bouton.pack(side=tkinter.LEFT)
                            searchwindow.mainloop()

                        sc = tkinter.Tk()
                        sc.title("Scan")
                        label = tkinter.Label(sc,
                                              text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                        label.pack()
                        import time
                        time.sleep(5)
                        import os
                        counter = 0
                        thisdir = os.getcwd()
                        liste = Listbox(hist, width=90, height=20)
                        for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                            for file in f:
                                filepath = os.path.join(r, file)
                                if ".py" in file or ".js" in file:
                                    counter += 1
                                    liste.insert(counter, os.path.join(r, file))
                                    liste.pack()

                        sc.mainloop()

                        menubar = tkinter.Menu(fnt)
                        menuII = tkinter.Menu(menubar, tearoff=0)
                        menuII.add_command(label="Analyse total du PC", command=mscan)
                        menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                        fnt.config(menu=menubar)
                        menu1.add_command(label="Chercher un élément", command=search)
                        menu1.add_command(label="Historique des fichiers", command=historique)
                        menu1.add_command(label="Lire un fichier", command=read)
                        menu1.add_command(label="Analyse approfondie", command=verifplus)
                        menu1.add_command(label="Afficher les détails", command=callback)
                    else:
                        if "'Discord': roaming + " in content:
                            img.config(file='mvp logo simple orange.png')

                            def verifplus():
                                showinfo('Info', 'Le scan va commencer !')
                                track = 0
                                print("ok")
                                fichier = open(filename, "r")
                                for line in fichier:
                                    if "bot.login(" in line or 'const Discord = require("discord.js");' in line or "var mkdirp = require('mkdirp');" in line or "from pynput import keyboard" in line or "def on_press(key):" in line:
                                        track += 1
                                showwarning('Détection:',
                                            f'Il a été détecté {int(track)} problème(s) de sécurité dans votre fichier !')

                            def callback():
                                showinfo('Explication:',
                                         "Il semble que ce fichier contient un argument de type:\n'Discord': roaming + '\\Discord'\n\nCe qui signifie que ce fichier contient PROBABLEMENT un Discord Token Grabber (Pouvant 'pirater' votre compte Discord), cela n'est cependant pas sûr, cependant, nous vous recommandons de ne pas l'éxécuter !")

                            label.config(text="Oh, nous PENSONS que ce fichier contient quelque chose de mauvais...")
                            label.pack()

                            def read():
                                lne = 1
                                rd = tkinter.Tk()
                                rd.title(f"Lecture de {filename}")

                                liste = Listbox(rd, width=170, height=20)
                                with io.open(filename, "r", encoding="utf-8") as fichier:
                                    for line in fichier:
                                        liste.insert(lne, line)
                                        lne += 1
                                liste.pack()
                                rd.mainloop()

                            with io.open("Historique.txt", "a", encoding="utf-8") as f:
                                f.write(f"\n{filename} - Mauvais")

                            def historique():
                                var = 1
                                with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                    hist = tkinter.Tk()
                                    hist.title("Historique")
                                    liste = Listbox(hist, width=90, height=20)
                                    for line in f:
                                        if line != "\n":
                                            liste.insert(var, line)
                                            var += 1

                                    liste.pack()

                                    def clear():
                                        with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                            f.write("")

                                    bt = tkinter.Button(hist, text="Vider", command=clear)
                                    bt.pack(side=tkinter.RIGHT)

                                    hist.mainloop()

                            def search():

                                searchwindow = tkinter.Tk()

                                entree = tkinter.Entry(searchwindow, width=30)
                                entree.pack()

                                def verif():
                                    if entree.get() in content:
                                        showwarning("Vérification", "Ce fichier semblerait contenir ")
                                    else:
                                        showinfo("Info", "Ce fichier ne contient pas l'argument que vous avez saisit")

                                bouton = Button(fenetre, text="Chercher", command=verif)
                                bouton.pack(side=tkinter.LEFT)
                                searchwindow.mainloop()
                            def mscan():
                                sc = tkinter.Tk()
                                sc.title("Scan")
                                label = tkinter.Label(sc,
                                                      text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                                label.pack()
                                import time
                                time.sleep(5)
                                import os
                                counter = 0
                                thisdir = os.getcwd()
                                liste = Listbox(hist, width=90, height=20)
                                for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                                    for file in f:
                                        filepath = os.path.join(r, file)
                                        if ".py" in file or ".js" in file:
                                            counter += 1
                                            liste.insert(counter, os.path.join(r, file))
                                            liste.pack()

                                sc.mainloop()

                            menubar = tkinter.Menu(fnt)
                            menuII = tkinter.Menu(menubar, tearoff=0)
                            menuII.add_command(label="Analyse total du PC", command=mscan)
                            menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                            fnt.config(menu=menubar)
                            menu1.add_command(label="Chercher un élément", command=search)
                            menu1.add_command(label="Historique des fichiers", command=historique)
                            menu1.add_command(label="Lire un fichier", command=read)
                            menu1.add_command(label="Analyse approfondie", command=verifplus)
                            menu1.add_command(label="Afficher les détails", command=callback)
                        else:
                            if 'bot.login(' in content and 'const Discord = require("discord.js");' in content:
                                img.config(file='mvp logo simple red.png')

                                def verifplus():
                                    showinfo('Info', 'Le scan va commencer !')
                                    track = 0
                                    print("ok")
                                    fichier = open(filename, "r")
                                    for line in fichier:
                                        if "bot.login(" in line or 'const Discord = require("discord.js");' in line or "var mkdirp = require('mkdirp');" in line or "from pynput import keyboard" in line or "def on_press(key):" in line:
                                            track += 1
                                    showwarning('Détection:',
                                                f'Il a été détecté {int(track)} problème(s) de sécurité dans votre fichier !')

                                def callback():
                                    showinfo('Explication:',
                                             'Il semble que ce fichier contient un argument de type:\nclient(bot).token\n\nCe qui signifie que ce fichier contient bot discord !')

                                label.config(text="Oh, il semble que ce fichier contient quelque chose de mauvais...")
                                label.pack()

                                def read():
                                    lne = 1
                                    rd = tkinter.Tk()
                                    rd.title(f"Lecture de {filename}")

                                    liste = Listbox(rd, width=170, height=20)
                                    with io.open(filename, "r", encoding="utf-8") as fichier:
                                        for line in fichier:
                                            liste.insert(lne, line)
                                            lne += 1
                                    liste.pack()
                                    rd.mainloop()

                                with io.open("Historique.txt", "a", encoding="utf-8") as f:
                                    f.write(f"\n{filename} - Mauvais")

                                def historique():
                                    var = 1
                                    with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                        hist = tkinter.Tk()
                                        hist.title("Historique")
                                        liste = Listbox(hist, width=90, height=20)
                                        for line in f:
                                            if line != "\n":
                                                liste.insert(var, line)
                                                var += 1

                                        liste.pack()

                                        def clear():
                                            with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                                f.write("")

                                        bt = tkinter.Button(hist, text="Vider", command=clear)
                                        bt.pack(side=tkinter.RIGHT)

                                        hist.mainloop()

                                def search():

                                    searchwindow = tkinter.Tk()

                                    entree = tkinter.Entry(searchwindow, width=30)
                                    entree.pack()

                                    def verif():
                                        if entree.get() in content:
                                            showwarning("Vérification", "Ce fichier semblerait contenir ")
                                        else:
                                            showinfo("Info", "Ce fichier ne contient pas l'argument que vous avez saisit")

                                    bouton = Button(fenetre, text="Chercher", command=verif)
                                    bouton.pack(side=tkinter.LEFT)
                                    searchwindow.mainloop()

                                def mscan():
                                    sc = tkinter.Tk()
                                    sc.title("Scan")
                                    label = tkinter.Label(sc,
                                                          text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                                    label.pack()
                                    import time
                                    time.sleep(5)
                                    import os
                                    counter = 0
                                    thisdir = os.getcwd()
                                    liste = Listbox(hist, width=90, height=20)
                                    for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                                        for file in f:
                                            filepath = os.path.join(r, file)
                                            if ".py" in file or ".js" in file:
                                                counter += 1
                                                liste.insert(counter, os.path.join(r, file))
                                                liste.pack()

                                    sc.mainloop()

                                menubar = tkinter.Menu(fnt)
                                menuII = tkinter.Menu(menubar, tearoff=0)
                                menuII.add_command(label="Analyse total du PC", command=mscan)
                                menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                                fnt.config(menu=menubar)
                                menu1.add_command(label="Chercher un élément", command=search)
                                menu1.add_command(label="Historique des fichiers", command=historique)
                                menu1.add_command(label="Lire un fichier", command=read)
                                menu1.add_command(label="Analyse approfondie", command=verifplus)
                                menu1.add_command(label="Afficher les détails", command=callback)
                            else:
                                if "var mkdirp = require('mkdirp');" in content:
                                    img.config(file='mvp logo simple red.png')

                                    def verifplus():
                                        showinfo('Info', 'Le scan va commencer !')
                                        track = 0
                                        print("ok")
                                        fichier = open(filename, "r")
                                        for line in fichier:
                                            if "bot.login(" in line or 'const Discord = require("discord.js");' in line or "var mkdirp = require('mkdirp');" in line or "from pynput import keyboard" in line or "def on_press(key):" in line:
                                                track += 1
                                        showwarning('Détection:',
                                                    f'Il a été détecté {int(track)} problème(s) de sécurité dans votre fichier !')

                                    def callback():
                                        showinfo('Explication:',
                                                 'Il semble que ce fichier contient un argument de type:\nos.mkdir()\n\nCe qui signifie que ce fichier peut créer des dossiers !')

                                    label.config(
                                        text="Oh, il semble que ce fichier contient quelque chose de mauvais...")
                                    label.pack()

                                    def read():
                                        lne = 1
                                        rd = tkinter.Tk()
                                        rd.title(f"Lecture de {filename}")

                                        liste = Listbox(rd, width=170, height=20)
                                        with io.open(filename, "r", encoding="utf-8") as fichier:
                                            for line in fichier:
                                                liste.insert(lne, line)
                                                lne += 1
                                        liste.pack()
                                        rd.mainloop()

                                    with io.open("Historique.txt", "a", encoding="utf-8") as f:
                                        f.write(f"\n{filename} - Mauvais")

                                    def historique():
                                        var = 1
                                        with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                            hist = tkinter.Tk()
                                            hist.title("Historique")
                                            liste = Listbox(hist, width=90, height=20)
                                            for line in f:
                                                if line != "\n":
                                                    liste.insert(var, line)
                                                    var += 1

                                            liste.pack()

                                            def clear():
                                                with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                                    f.write("")

                                            bt = tkinter.Button(hist, text="Vider", command=clear)
                                            bt.pack(side=tkinter.RIGHT)

                                            hist.mainloop()

                                    def historique():
                                        var = 1
                                        with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                            hist = tkinter.Tk()
                                            hist.title("Historique")
                                            liste = Listbox(hist, width=90, height=20)
                                            for line in f:
                                                if line != "\n":
                                                    liste.insert(var, line)
                                                    var += 1

                                            liste.pack()

                                            def clear():
                                                with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                                    f.write("")

                                            bt = tkinter.Button(hist, text="Vider", command=clear)
                                            bt.pack(side=tkinter.RIGHT)

                                            hist.mainloop()

                                    def search():

                                        searchwindow = tkinter.Tk()

                                        entree = tkinter.Entry(searchwindow, width=30)
                                        entree.pack()

                                        def verif():
                                            if entree.get() in content:
                                                showwarning("Vérification", "Ce fichier semblerait contenir ")
                                            else:
                                                showinfo("Info", "Ce fichier ne contient pas l'argument que vous avez saisit")

                                        bouton = Button(fenetre, text="Chercher", command=verif)
                                        bouton.pack(side=tkinter.LEFT)
                                        searchwindow.mainloop()

                                    def mscan():
                                       sc = tkinter.Tk()
                                       sc.title("Scan")
                                       label = tkinter.Label(sc,
                                                             text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                                       label.pack()
                                       import time
                                       time.sleep(5)
                                       import os
                                       counter = 0
                                       thisdir = os.getcwd()
                                       liste = Listbox(hist, width=90, height=20)
                                       for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                                           for file in f:
                                               filepath = os.path.join(r, file)
                                               if ".py" in file or ".js" in file:
                                                   counter += 1
                                                   liste.insert(counter, os.path.join(r, file))
                                                   liste.pack()

                                       sc.mainloop()

                                    menubar = tkinter.Menu(fnt)
                                    menuII = tkinter.Menu(menubar, tearoff=0)
                                    menuII.add_command(label="Analyse total du PC", command=mscan)
                                    menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                                    fnt.config(menu=menubar)
                                    menu1.add_command(label="Chercher un élément", command=search)
                                    menu1.add_command(label="Historique des fichiers", command=historique)
                                    menu1.add_command(label="Lire un fichier", command=read)
                                    menu1.add_command(label="Analyse approfondie", command=verifplus)
                                    menu1.add_command(label="Afficher les détails", command=callback)

                                else:
                                    if "from pynput import keyboard" in content or "def on_press(key):" in content:
                                        img.config(file='mvp logo simple red.png')

                                        def verifplus():
                                            showinfo('Info', 'Le scan va commencer !')
                                            track = 0
                                            print("ok")
                                            fichier = open(filename, "r")
                                            for line in fichier:
                                                if "bot.login(" in line or 'const Discord = require("discord.js");' in line or "var mkdirp = require('mkdirp');" in line or "from pynput import keyboard" in line or "def on_press(key):" in line:
                                                    track += 1
                                            showwarning('Détection:',
                                                        f'Il a été détecté {int(track)} problème(s) de sécurité dans votre fichier !')

                                        def callback():
                                            showinfo('Explication:',
                                                     'Il semble que ce fichier contient un argument de type:\ndef get_key(key\:n\nCe qui signifie que ce fichier peut potentiellement être un KeyLogger !')

                                        label.config(
                                            text="Oh, il semble que ce fichier contient quelque chose de mauvais...")
                                        label.pack()

                                        def read():
                                            lne = 1
                                            rd = tkinter.Tk()
                                            rd.title(f"Lecture de {filename}")

                                            liste = Listbox(rd, width=170, height=20)
                                            with io.open(filename, "r", encoding="utf-8") as fichier:
                                                for line in fichier:
                                                    liste.insert(lne, line)
                                                    lne += 1
                                            liste.pack()
                                            rd.mainloop()

                                        with io.open("Historique.txt", "a", encoding="utf-8") as f:
                                            f.write(f"\n{filename} - Mauvais")

                                        def historique():
                                            var = 1
                                            with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                                hist = tkinter.Tk()
                                                hist.title("Historique")
                                                liste = Listbox(hist, width=90, height=20)
                                                for line in f:
                                                    if line != "\n":
                                                        liste.insert(var, line)
                                                        var += 1

                                                liste.pack()

                                                def clear():
                                                    with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                                        f.write("")

                                                bt = tkinter.Button(hist, text="Vider", command=clear)
                                                bt.pack(side=tkinter.RIGHT)

                                                hist.mainloop()

                                        def search():

                                            searchwindow = tkinter.Tk()

                                            entree = tkinter.Entry(searchwindow, width=30)
                                            entree.pack()

                                            def verif():
                                                if entree.get() in content:
                                                    showwarning("Vérification", "Ce fichier semblerait contenir ")
                                                else:
                                                    showinfo("Info",
                                                             "Ce fichier ne contient pas l'argument que vous avez saisit")

                                            bouton = Button(fenetre, text="Chercher", command=verif)
                                            bouton.pack(side=tkinter.LEFT)
                                            searchwindow.mainloop()

                                        def mscan():
                                            sc = tkinter.Tk()
                                            sc.title("Scan")
                                            label = tkinter.Label(sc,
                                                                  text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                                            label.pack()
                                            import time
                                            time.sleep(5)
                                            import os
                                            counter = 0
                                            thisdir = os.getcwd()
                                            liste = Listbox(sc, width=100, height=100)
                                            for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                                                for file in f:
                                                    filepath = os.path.join(r, file)
                                                    if ".py" in file or ".js" in file:
                                                        counter += 1
                                                        liste.insert(counter, os.path.join(r, file))
                                                        liste.pack()

                                            sc.mainloop()

                                        menubar = tkinter.Menu(fnt)
                                        menuII = tkinter.Menu(menubar, tearoff=0)
                                        menuII.add_command(label="Analyse total du PC", command=mscan)
                                        menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                                        fnt.config(menu=menubar)
                                        menu1.add_command(label="Chercher un élément", command=search)
                                        menu1.add_command(label="Historique des fichiers", command=historique)
                                        menu1.add_command(label="Lire un fichier", command=read)
                                        menu1.add_command(label="Analyse approfondie", command=verifplus)
                                        menu1.add_command(label="Afficher les détails", command=callback)

                                    else:
                                        img.config(file='mvp logo simple green.png')
                                        label.config(text="Bonne nouvelle ! Ce fichier semble sécurisé !")

                                        def read():
                                            lne = 1
                                            rd = tkinter.Tk()
                                            rd.title(f"Lecture de {filename}")

                                            liste = Listbox(rd, width=170, height=20)
                                            with io.open(filename, "r", encoding="utf-8") as fichier:
                                                for line in fichier:
                                                    liste.insert(lne, line)
                                                    lne += 1
                                            liste.pack()
                                            rd.mainloop()

                                        def callback():
                                            showinfo('Explication:',
                                                     'Il semble que ce type de fichier est incorrect ou est pas encore utilisable...')


                                        with io.open("Historique.txt", "a", encoding="utf-8") as f:
                                            f.write(f"\n{filename} - Mauvais")

                                        def historique():
                                            var = 1
                                            with io.open("Historique.txt", "r", encoding="utf-8") as f:
                                                hist = tkinter.Tk()
                                                hist.title("Historique")
                                                liste = Listbox(hist, width=90, height=20)
                                                for line in f:
                                                    if line != "\n":
                                                        liste.insert(var, line)
                                                        var += 1

                                                liste.pack()

                                                def clear():
                                                    with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                                        f.write("")

                                                bt = tkinter.Button(hist, text="Vider", command=clear)
                                                bt.pack(side=tkinter.RIGHT)

                                                hist.mainloop()

                                        def mscan():
                                            sc = tkinter.Tk()
                                            sc.title("Scan")
                                            label = tkinter.Label(sc,
                                                                  text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...\n(MVP va peut être planter pendant l'opération, c'est normal !)")
                                            label.pack()
                                            import time
                                            time.sleep(5)
                                            import os
                                            counter = 0
                                            ct = 0
                                            thisdir = os.getcwd()
                                            liste = Listbox(sc, width=100, height=100)
                                            for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                                                for file in f:
                                                    filepath = os.path.join(r, file)
                                                    if ".py" in file or ".js" in file:
                                                        counter += 1
                                                        liste.insert(counter, os.path.join(r, file))
                                                        import io
                                                        with io.open("bad words.txt", "r", encoding="utf-8") as f:
                                                            if (counter, os.path.join(r, file)) in f.read():
                                                                ct += 1
                                            liste.pack()

                                            sc.mainloop()

                                        menubar = tkinter.Menu(fnt)
                                        menuII = tkinter.Menu(menubar, tearoff=0)
                                        menuII.add_command(label="Analyse total du PC", command=mscan)
                                        menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                                        fnt.config(menu=menubar)
                                        menu1.add_command(label="Historique des fichiers", command=historique)
                                        menu1.add_command(label="Lire un fichier", command=read)
                                        menu1.add_command(label="Afficher les détails", command=callback)

                                        label.pack()
            else:
                img.config(file='mvp logo simple gris.png')

                def read():
                    lne = 1
                    rd = tkinter.Tk()
                    rd.title(f"Lecture de {filename}")

                    liste = Listbox(rd, width=170, height=20)
                    with io.open(filename, "r", encoding="utf-8") as fichier:
                        for line in fichier:
                            liste.insert(lne, line)
                            lne += 1
                    liste.pack()
                    rd.mainloop()

                def callback():
                    showinfo('Explication:',
                             'Ce fichier appartient à MB INC et est donc sécurisé.')

                label.config(text="Ce fichier est certifié de MB INC et est donc sécurisé !")
                label.pack()

                with io.open("Historique.txt", "a", encoding="utf-8") as f:
                    f.write(f"\n{filename} - Cetifié de MB INC")

                def historique():
                    var = 1
                    with io.open("Historique.txt", "r", encoding="utf-8") as f:
                        hist = tkinter.Tk()
                        hist.title("Historique")
                        liste = Listbox(hist, width=90, height=20)
                        for line in f:
                            if line != "\n":
                                liste.insert(var, line)
                                var += 1

                        liste.pack()

                        def clear():
                            with io.open("Historique.txt", "w", encoding="utf-8") as f:
                                f.write("")

                        bt = tkinter.Button(hist, text="Vider", command=clear)
                        bt.pack(side=tkinter.RIGHT)

                        hist.mainloop()

                def mscan():
                    sc = tkinter.Tk()
                    label = tkinter.Label(sc,
                                          text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
                    label.pack()
                    import time
                    time.sleep(5)
                    import os
                    counter = 0
                    thisdir = os.getcwd()
                    for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                        for file in f:
                            filepath = os.path.join(r, file)
                            if ".py" in file or ".js" in file:
                                counter += 1
                                label.config(text=os.path.join(r, file))

                    sc.mainloop()

                menubar = tkinter.Menu(fnt)
                menuII = tkinter.Menu(menubar, tearoff=0)
                menuII.add_command(label="Analyse total du PC", command=mscan)
                menubar.add_cascade(label="Mode arrière plan", menu=menuII)
                fnt.config(menu=menubar)
                menu1.add_command(label="Historique des fichiers", command=historique)
                menu1.add_command(label="Lire un fichier", command=read)
                menu1.add_command(label="Afficher les détails", command=callback)

    else:
        img.config(file='mvp logo simple blue.png')

        def read():
            lne = 1
            rd = tkinter.Tk()
            rd.title(f"Lecture de {filename}")

            liste = Listbox(rd, width=170, height=20)
            with io.open(filename, "r", encoding="utf-8") as fichier:
                for line in fichier:
                    liste.insert(lne, line)
                    lne += 1
            liste.pack()
            rd.mainloop()

        def callback():
            showinfo('Explication:',
                     'Il semble que ce type de fichier est incorrect ou est pas encore utilisable...')

        label.config(text="Oh... Ce fichier est inconnu est est invalide...")
        label.pack()

        with io.open("Historique.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{filename} - Mauvais")

        def historique():
            var = 1
            with io.open("Historique.txt", "r", encoding="utf-8") as f:
                hist = tkinter.Tk()
                hist.title("Historique")
                liste = Listbox(hist, width=90, height=20)
                for line in f:
                    if line != "\n":
                        liste.insert(var, line)
                        var += 1

                liste.pack()

                def clear():
                    with io.open("Historique.txt", "w", encoding="utf-8") as f:
                        f.write("")

                bt = tkinter.Button(hist, text="Vider", command=clear)
                bt.pack(side=tkinter.RIGHT)

                hist.mainloop()

        def mscan():
            sc = tkinter.Tk()
            label = tkinter.Label(sc,
                                  text="Le scan va commencer dans 5 secondes, cette opération va prendre un moment...")
            label.pack()
            import time
            time.sleep(5)
            import os
            counter = 0
            thisdir = os.getcwd()
            for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                for file in f:
                    filepath = os.path.join(r, file)
                    if ".py" in file or ".js" in file:
                        counter += 1
                        label.config(text=os.path.join(r, file))

            sc.mainloop()

        menubar = tkinter.Menu(fnt)
        menuII = tkinter.Menu(menubar, tearoff=0)
        menuII.add_command(label="Analyse total du PC", command=mscan)
        menubar.add_cascade(label="Mode arrière plan", menu=menuII)
        fnt.config(menu=menubar)
        menu1.add_command(label="Historique des fichiers", command=historique)
        menu1.add_command(label="Lire un fichier", command=read)
        menu1.add_command(label="Afficher les détails", command=callback)


    menu1.add_command(label="BlackList", command=menu1)
    menubar.add_cascade(label="Fonctions personnels", menu=menu1)
    fnt.config(menu=menubar)

def scan_file():
    track = 0
    excepts = 0
    import io
    folder_selected = filedialog.askdirectory()
    import os
    entries = os.listdir(folder_selected)
    for entry in entries:
        try:
            fichier = io.open(f"{folder_selected}\\{entry}", "r", encoding="utf-8")
            for line in fichier:
                if "os.mkdir" in line or "import discord" in line or "'Discord': roaming + " in line:
                    track += 1
                    print("tracked")
            fichier.close()
        except:
            print("Pass")
    if track < 1:
        print("track = 8")
        img.config(file='mvp logo simple green.png')
        label.config(text="Bonne nouvelle ! Ce fichier semble sécurisé !")
        label.pack()
        showinfo("Info", "Le fichier est sécurisé !")
        import time
        time.sleep(1)
        img.config(file='mvp logo simple blue.png')
        label.config(text="Autre chose ?")
    else:
        print("track = 1")
        img.config(file="mvp logo simple red.png")
        label.config(text="Oh, il semble que ce fichier contient quelque chose de mauvais...")
        showwarning('Détection:', f'Il a été détecté {int(track)} problème(s) de sécurité dans votre dossier !')
        import time
        time.sleep(1)
        img.config(file='mvp logo simple blue.png')
        label.config(text="Autre chose ?")


va = tkinter.Button(fnt, text='Vérifier un fichier', command=launch).pack(side=tkinter.LEFT, padx=5, pady=5)
var = tkinter.Button(fnt, text='Vérifier un dossier', command=scan_file).pack(side=tkinter.RIGHT, padx=5, pady=5)
fnt.mainloop()