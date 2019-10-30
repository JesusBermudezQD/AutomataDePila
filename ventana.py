# -*- coding: utf-8 -*-
from tkinter import *
from automatachambon import *
from pygame.locals import *
import pygame, sys
import pyttsx3
import random



class Ventana():

    def __init__(self):
        self.raiz=Tk()
        self.raiz.geometry("470x620")
        self.raiz.configure(background="#ddf796")
        self.raiz.resizable(0,0)
        self.canvaspalabra=None
        self.canvasPila=None
        self.palabra=""
        self.res=""
        self.var=StringVar()
        self.grafo=Grafo()
        self.palabra=StringVar()
        self.say = pyttsx3.init()
        self.listaCanciones=["plata.mp3","osama.mp3","rebelion.mp3","guarare.mp3"]
        self.ran=random.randint(0,3)
        self.aumento=0
        self.n=0


    def inicio(self):
        pygame.init()

        self.titulo=Label(self.raiz,text="AUTOMATA DE PILA",width=28,height=2,font=("Fixedsys",20), background="#ddf796")
        self.titulo.place(x=0,y=0)

        self.canvasGrafo=Canvas(self.raiz, width=600, height=200, background="#ddf796",highlightthickness=0)
        self.canvasGrafo.place(x=0, y=130)
        #--------------------primeras transiciones---------------------------
        
        self.canvasGrafo.create_line(22, 109, 30, 115, width=2, fill='black')
        self.canvasGrafo.create_line(10, 115, 30, 115, width=2, fill='black') 
        self.canvasGrafo.create_line(22, 120, 30, 115, width=2, fill='black')

        self.canvasGrafo.create_arc(30, 80, 78, 190, start=10,width=2 ,extent=150, fill="#ddf796")
        self.canvasGrafo.create_line(33, 90, 35, 100, width=2, fill='black')
        self.canvasGrafo.create_line(33, 90, 40, 100, width=2, fill='black')

        self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
        self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
        self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
        self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
        self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
        self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
    
        self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#42b883') 
        self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="black")

        #--------------------segundas transiciones---------------------------

        self.arco7=self.canvasGrafo.create_text(150, 67, anchor=N,width=60,text="c,#/#")
        self.arco8=self.canvasGrafo.create_text(150, 80, anchor=N,width=60,text="c,b/b")
        self.arco9=self.canvasGrafo.create_text(150, 93, anchor=N,width=60,text="c,a/a")

        self.canvasGrafo.create_line(200, 109, 210, 115, width=2, fill='black')
        self.canvasGrafo.create_line(80, 115, 210, 115, width=2, fill='black')
        self.canvasGrafo.create_line(200, 120, 210, 115, width=2, fill='black')



        #--------------------terceras transiciones---------------------------

        self.canvasGrafo.create_arc(210, 80, 260, 163, start=10, extent=150,width=2 ,fill="#ddf796")
        self.canvasGrafo.create_line(213, 90, 215, 110, width=2, fill='black')
        self.canvasGrafo.create_line(213, 90, 218, 100, width=2, fill='black')

        self.arco10=self.canvasGrafo.create_text(235, 40, anchor=N,width=60,text="b,b/λ")
        self.arco11=self.canvasGrafo.create_text(235, 53, anchor=N,width=60,text="a,a/λ")

        self.nodoq=self.canvasGrafo.create_oval(210, 90, 260, 140, width=2, fill='#42b883')
        self.textoq=self.canvasGrafo.create_text(235, 105, anchor=N,width=60,text="Q",fill="black")

        #--------------------terceras transiciones---------------------------

        self.arco12=self.canvasGrafo.create_text(350, 93, anchor=N,width=60,text="λ,#/#")

        self.canvasGrafo.create_line(390, 109, 400, 115, width=2, fill='black')
        self.canvasGrafo.create_line(260, 115, 400, 115, width=2, fill='black') 
        self.canvasGrafo.create_line(390, 120, 400, 115, width=2, fill='black')

      
        self.nodor1=self.canvasGrafo.create_oval(400, 90, 450, 140, width=2, fill='#94aa2a') 
        self.nodor2=self.canvasGrafo.create_oval(410, 100, 440, 130, width=2, fill='#94aa2a') 
        self.textor=self.canvasGrafo.create_text(425, 107, anchor=N,width=60,text="R",fill="white")

        Entry(self.raiz, textvariable=self.palabra).place(x=30,y=300)

        Button(self.raiz,text="INICIAR",background="#94aa2a" ,command=self.capturar).place(x=60,y=340)
        
        pygame.mixer.music.load("musica/"+self.listaCanciones[self.ran])
        #pygame.mixer.music.play()

        self.raiz.mainloop()

    
    def capturar(self):

        self.res=self.palabra.get()
        self.palabra.set("")
        p=0

        if(self.canvaspalabra!=None and self.canvasPila!=None and self.respuestaPalabra!=None): 
            self.canvaspalabra.destroy()
            self.canvasPila.destroy()
            self.respuestaPalabra.destroy()

        self.canvaspalabra=Canvas(self.raiz, width=300, height=30, background="#ddf796",highlightthickness=0)
        self.canvaspalabra.place(x=30, y=380)


        for i in range(0,len(self.res)):
            
            self.canvaspalabra.create_rectangle(5+p,5,25+p,25,fill="#42b883")
            self.canvaspalabra.create_text(14+p, 5, anchor=N,width=10,text=self.res[i])

            p=p+22

        self.rapido1=Button(self.raiz,text="Rapido",background="#94aa2a",command=self.rapido)
        self.rapido1.place(x=20,y=420)
        self.lento1=Button(self.raiz,text="Lento",background="#94aa2a",command=self.lento)
        self.lento1.place(x=130,y=420)
        self.aumento=0
        self.n=0


    def destruirBoton(self):
        self.rapido1.destroy()
        self.lento1.destroy()
        

    
    def lento(self): 
        self.grafo.iniciarGrafo(self.res)
        self.destruirBoton()
        self.grafo.verificar()
        self.animacionLenta()

        self.grafo.caminos=[]
        self.grafo.aceptada=False
        self.grafo.verticeActual="p"

    def rapido(self): 
        self.grafo.iniciarGrafo(self.res)
        self.destruirBoton()
        self.grafo.verificar()
        self.animacionRapida()
  
        self.grafo.caminos=[]
        self.grafo.aceptada=False
        self.grafo.verticeActual="p"
        self.rapido1.destroy()
        self.lento1.destroy()





    def animarPila(self,letra,p):
        
        self.cuadro=self.canvasPila.create_rectangle(5,198-p,25,218-p,fill="#42b883")
        self.texto=self.canvasPila.create_text(14, 201-p, anchor=N,width=10,text=letra)

    def animarPalabra(self):

        self.canvaspalabra.create_rectangle(5+self.n,5,25+self.n,25,fill="#35495e")
        self.canvaspalabra.create_text(14+self.n, 5, anchor=N,fill="white",width=10,text=self.res[self.aumento])
        self.aumento+=1
        self.n+=22
        

        
        
    
    def animarAutomata(self,arcoGuardado):
        
        if(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="bb"):
            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.nodop)
            self.canvasGrafo.delete(self.textop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb", fill="#35495e")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")

            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")
            

        elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="ba"):

            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba", fill="#35495e")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
        
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")

        elif(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="ab"):

            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab", fill="#35495e")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
        
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")

        elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="aa"):
            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa", fill="#35495e")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
        
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")

            


        elif(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#b"):

            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b", fill="#35495e")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
        
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")



        elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#a"):

            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a", fill="#35495e")
        
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")



        elif(arcoGuardado.palabra=="c" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#"):

            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.arco7)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
            self.arco7=self.canvasGrafo.create_text(150, 67, anchor=N,width=60,text="c,#/#", fill="#35495e")
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")


                
        elif(arcoGuardado.palabra=="c" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="b"):

            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.arco8)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
            self.arco8=self.canvasGrafo.create_text(150, 80, anchor=N,width=60,text="c,b/b", fill="#35495e")
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")


        elif(arcoGuardado.palabra=="c" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="a"):
        
            self.canvasGrafo.delete(self.arco1)
            self.canvasGrafo.delete(self.arco2)
            self.canvasGrafo.delete(self.arco3)
            self.canvasGrafo.delete(self.arco4)
            self.canvasGrafo.delete(self.arco5)
            self.canvasGrafo.delete(self.arco6)
            self.canvasGrafo.delete(self.arco9)
            self.canvasGrafo.delete(self.nodop)


            self.arco1=self.canvasGrafo.create_text(55, 11, anchor=N,width=60,text="a,b/ba")
            self.arco2=self.canvasGrafo.create_text(55, 0, anchor=N,width=60,text="b,b/bb")
            self.arco3=self.canvasGrafo.create_text(55, 24, anchor=N,width=60,text="b,a/ab")
            self.arco4=self.canvasGrafo.create_text(55, 37, anchor=N,width=60,text="a,a/aa")
            self.arco5=self.canvasGrafo.create_text(55, 50, anchor=N,width=60,text="b,#/#b")
            self.arco6=self.canvasGrafo.create_text(55, 63, anchor=N,width=60,text="a,#/#a")
            self.arco9=self.canvasGrafo.create_text(150, 93, anchor=N,width=60,text="c,a/a", fill="#35495e")
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#35495e') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="white")
            

        elif(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="λ"):
            self.canvasGrafo.delete(self.arco7)
            self.canvasGrafo.delete(self.arco8)
            self.canvasGrafo.delete(self.arco9)
            self.canvasGrafo.delete(self.arco10)
            self.canvasGrafo.delete(self.arco11)
            self.canvasGrafo.delete(self.nodop)
            self.canvasGrafo.delete(self.nodoq)
            self.canvasGrafo.delete(self.textop)
            self.canvasGrafo.delete(self.textoq)

            self.arco7=self.canvasGrafo.create_text(150, 67, anchor=N,width=60,text="c,#/#")
            self.arco8=self.canvasGrafo.create_text(150, 80, anchor=N,width=60,text="c,b/b")
            self.arco9=self.canvasGrafo.create_text(150, 93, anchor=N,width=60,text="c,a/a")
            self.arco10=self.canvasGrafo.create_text(235, 40, anchor=N,width=60,text="b,b/λ",fill="#35495e")
            self.arco11=self.canvasGrafo.create_text(235, 53, anchor=N,width=60,text="a,a/λ")
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#42b883') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="black")
            self.nodoq=self.canvasGrafo.create_oval(210, 90, 260, 140, width=2, fill='#35495e')
            self.textoq=self.canvasGrafo.create_text(235, 105, anchor=N,width=60,text="Q",fill="white")

                
        elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="λ"):
            self.canvasGrafo.delete(self.arco7)
            self.canvasGrafo.delete(self.arco8)
            self.canvasGrafo.delete(self.arco9)
            self.canvasGrafo.delete(self.arco10)
            self.canvasGrafo.delete(self.arco11)
            self.canvasGrafo.delete(self.nodop)
            self.canvasGrafo.delete(self.nodoq)
            self.canvasGrafo.delete(self.textop)
            self.canvasGrafo.delete(self.textoq)


            self.arco7=self.canvasGrafo.create_text(150, 67, anchor=N,width=60,text="c,#/#")
            self.arco8=self.canvasGrafo.create_text(150, 80, anchor=N,width=60,text="c,b/b")
            self.arco9=self.canvasGrafo.create_text(150, 93, anchor=N,width=60,text="c,a/a")
            self.arco10=self.canvasGrafo.create_text(235, 40, anchor=N,width=60,text="b,b/λ")
            self.arco11=self.canvasGrafo.create_text(235, 53, anchor=N,width=60,text="a,a/λ",fill="#35495e")
            self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#42b883') 
            self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="black")
            self.nodoq=self.canvasGrafo.create_oval(210, 90, 260, 140, width=2, fill='#35495e')
            self.textoq=self.canvasGrafo.create_text(235, 105, anchor=N,width=60,text="Q",fill="white")



        elif(arcoGuardado.palabra=="λ" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#"):
             
            self.canvasGrafo.delete(self.arco10)
            self.canvasGrafo.delete(self.arco11)
            self.canvasGrafo.delete(self.arco12)
            self.canvasGrafo.delete(self.nodoq)
            self.canvasGrafo.delete(self.nodor1)
            self.canvasGrafo.delete(self.nodor2)
            self.canvasGrafo.delete(self.textoq)
            self.canvasGrafo.delete(self.textor)

            self.arco10=self.canvasGrafo.create_text(235, 40, anchor=N,width=60,text="b,b/λ")
            self.arco11=self.canvasGrafo.create_text(235, 53, anchor=N,width=60,text="a,a/λ")
            self.arco12=self.canvasGrafo.create_text(350, 93, anchor=N,width=60,text="λ,#/#")
            self.nodor1=self.canvasGrafo.create_oval(400, 90, 450, 140, width=2, fill='#35495e') 
            self.nodor2=self.canvasGrafo.create_oval(410, 100, 440, 130, width=2, fill='#35495e') 
            self.textor=self.canvasGrafo.create_text(425, 107, anchor=N,width=60,text="R",fill="white")
            self.nodoq=self.canvasGrafo.create_oval(210, 90, 260, 140, width=2, fill='#42b883')
            self.textoq=self.canvasGrafo.create_text(235, 105, anchor=N,width=60,text="Q",fill="black")

    


    def respuesta(self,texto):
        self.respuestaPalabra = Label(self.raiz,text=texto,font=("Fixedsys",20), background="#ddf796")
        self.respuestaPalabra.place(x=30,y=500)

    def hablar(self,texto):

        volume = self.say.getProperty('volume')
        voces=self.say.getProperty("voices")
        rate = self.say.getProperty('rate')
        
        for voz in voces:
            if(voz.languages[0]==u"en_US"):
                self.say.setProperty("voice",voz.id )
                self.say.setProperty('volume', volume-0.75)
                self.say.setProperty('rate', rate+20)
                break
        self.say.say(texto)
        self.say.runAndWait()
    
    def animacionLenta(self):

        self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#42b883') 
        self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="black")

        self.nodoq=self.canvasGrafo.create_oval(210, 90, 260, 140, width=2, fill='#42b883')
        self.textoq=self.canvasGrafo.create_text(235, 105, anchor=N,width=60,text="Q",fill="black")

        self.nodor1=self.canvasGrafo.create_oval(400, 90, 450, 140, width=2, fill='#94aa2a') 
        self.nodor2=self.canvasGrafo.create_oval(410, 100, 440, 130, width=2, fill='#94aa2a') 
        self.textor=self.canvasGrafo.create_text(425, 107, anchor=N,width=60,text="R",fill="white")

        self.canvasPila=Canvas(self.raiz, width=40, height=250, background="#ddf796",highlightthickness=0)
        self.canvasPila.place(x=400, y=283) 

        self.canvasPila.create_rectangle(5,220,25,240,fill="#42b883")   
        self.canvasPila.create_text(14, 224, anchor=N,width=10,text="#")

        
        n=0
        aux=1
        aux1=0 
        con=0
        for p in self.grafo.caminos:  
            if(p.origen=="p"and p.destino=="p"):
                for s in p.apilar[-1]:
                    if(s!="λ" and s!="#"):
                        self.canvasPila.after(900*aux,self.animarPila,s,n)
                        self.canvasGrafo.after(900*aux,self.animarAutomata,p)
                        self.canvaspalabra.after(900*aux,self.animarPalabra)
                        n=n+22
                        aux+=1
            elif(p.origen=="q" and p.destino=="q"):
                n=n-22
                self.canvasPila.after(900*aux,self.animarPila,"",n)
                self.canvasGrafo.after(900*aux,self.animarAutomata,p)
                self.canvaspalabra.after(900*aux,self.animarPalabra)  
                aux+=1

            elif(p.origen=="p" and p.destino=="q"):
                self.canvasGrafo.after(900*aux,self.animarAutomata,p)
                self.canvaspalabra.after(900*aux,self.animarPalabra)
                aux+=1

            elif(p.origen=="q" and p.destino=="r"):
                n-=22
                self.canvasGrafo.after(900*aux,self.animarAutomata,p)
                

                aux+=1

                if(self.grafo.aceptada==True):
                    self.canvasGrafo.after(950*aux,self.respuesta,"palabra aceptada")
                    self.canvasGrafo.after(980*aux,self.hablar,"palabra aceptada")
                else:
                    self.canvasGrafo.after(950*aux,self.respuesta,"palabra no aceptada")
                    self.canvasGrafo.after(980*aux,self.hablar,"palabra no aceptada")



    def animacionRapida(self):
    
        self.nodop=self.canvasGrafo.create_oval(30, 90, 80, 140, width=2, fill='#42b883') 
        self.textop=self.canvasGrafo.create_text(55, 105, anchor=N,width=60,text="P",fill="black")

        self.nodoq=self.canvasGrafo.create_oval(210, 90, 260, 140, width=2, fill='#42b883')
        self.textoq=self.canvasGrafo.create_text(235, 105, anchor=N,width=60,text="Q",fill="black")

        self.nodor1=self.canvasGrafo.create_oval(400, 90, 450, 140, width=2, fill='#94aa2a') 
        self.nodor2=self.canvasGrafo.create_oval(410, 100, 440, 130, width=2, fill='#94aa2a') 
        self.textor=self.canvasGrafo.create_text(425, 107, anchor=N,width=60,text="R",fill="white")

        self.canvasPila=Canvas(self.raiz, width=40, height=250, background="#ddf796",highlightthickness=0)
        self.canvasPila.place(x=400, y=283) 

        self.canvasPila.create_rectangle(5,220,25,240,fill="#42b883")   
        self.canvasPila.create_text(14, 224, anchor=N,width=10,text="#")

        
        n=0
        aux=1 
        con=0
        for p in self.grafo.caminos:  
            if(p.origen=="p"and p.destino=="p"):
                for s in p.apilar[-1]:
                    if(s!="λ" and s!="#"):
                        self.canvasPila.after(200*aux,self.animarPila,s,n)
                        self.canvasGrafo.after(200*aux,self.animarAutomata,p)
                        self.canvaspalabra.after(200*aux,self.animarPalabra)
                        n=n+22
                        aux+=1
            elif(p.origen=="q" and p.destino=="q"):
                n=n-22
                self.canvasPila.after(200*aux,self.animarPila,"",n)
                self.canvasGrafo.after(200*aux,self.animarAutomata,p)
                self.canvaspalabra.after(200*aux,self.animarPalabra)  
                aux+=1

            elif(p.origen=="p" and p.destino=="q"):
                
                self.canvasGrafo.after(200*aux,self.animarAutomata,p)
                self.canvaspalabra.after(200*aux,self.animarPalabra)
                aux+=1

            elif(p.origen=="q" and p.destino=="r"):
                n-=22
                self.canvasGrafo.after(200*aux,self.animarAutomata,p) 
                aux+=1

                if(self.grafo.aceptada==True):
                    self.canvasGrafo.after(250*aux,self.respuesta,"palabra aceptada")
                    self.canvasGrafo.after(280*aux,self.hablar,"palabra aceptada")
                else:
                    self.canvasGrafo.after(250*aux,self.respuesta,"palabra no aceptada")
                    self.canvasGrafo.after(280*aux,self.hablar,"palabra no aceptada")



p=Ventana()
p.inicio()
