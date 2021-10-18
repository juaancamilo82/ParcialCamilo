import pygame
import pygame as py
import random
import tkinter
import time
import os
from tkinter import messagebox
start_ticks=pygame.time.get_ticks()

from pygame import time as pytime

from Persistencia.persistencia import Persistencia


class Boton(py.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor,Texto,x,y,valor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
        pantalla.blit(Texto,(x,y))
class Cursor(py.Rect):
    def __init__(self):
        py.Rect.__init__(self,1,1,1,1)
    def update(self):
        self.left,self.top=py.mouse.get_pos()

guardar = Persistencia()

def cargarPreguntas():
    for file in os.listdir("files") :
        if '.json' in file:
           return Persistencia.cargar_json(file)


def ganancia():
    lista=[100,200,500,1000,2000,3000,5000,10000,20000,30000,50000,75000,100000,200000,300000,500000, 750000, 1000000]
    return lista

def temporizador():
   numero =5
   for i in range(numero):
     print(numero)
     time.sleep(1)
     os.system("cls")
     numero-=1
     if(numero ==0):
         print(numero)

def Vista_jugar(pantalla, cursor1):

    reloj1= py.time.Clock()
    puntaje=0
    contadorPuntos=0


    gan= ganancia()
    fondo = py.image.load("archivosJuego/imagenes/FondoPreguntaQuienQuiereSerMillonario.jpg")

    pantalla.blit(fondo,(0,0))
    fuente2=py.font.SysFont("Comic Sans MS", 20, False, False)
    blanco=(255,255,255)
    valor1=py.image.load("archivosJuego/imagenes/remarcado2.gif")
    valor2=py.image.load("archivosJuego/imagenes/remarcado2.gif")
    lista=cargarPreguntas()
    temp=20
    fuente1=py.font.SysFont("Comic Sans MS", 34, False, False)
    jboton1=Boton(valor1,valor2,37,421)
    jboton2=Boton(valor1,valor2,426,421)
    jboton3=Boton(valor1,valor2,37,496)
    jboton4=Boton(valor1,valor2,426,496)
    reloj1.tick(20)
    salir=False
    

    while salir!=True:
        
        for event in py.event.get():
            if event.type == py.QUIT:
                salir=True
        if temp==1:
            salir=True
                        
        aleatorio = random.choice(range(temp))
        temp=temp-1
        preg=lista.pop(aleatorio)
        cursor1.update()
        pantalla.blit(fondo,(0,0))

        textoPregunta =  fuente2.render(preg[0],1, blanco)
        opcionA = fuente2.render(preg[1],1, blanco)
        opcionB = fuente2.render(preg[2],1, blanco)
        opcionC = fuente2.render(preg[3],1, blanco)
        opcionD = fuente2.render(preg[4],1, blanco)
        precio= "Dinero: $ "+str(puntaje)
        dinero= fuente1.render(precio,1,blanco)
        pantalla.blit(dinero,(40,400))
        pantalla.blit(textoPregunta,(300,700))
        jboton1.update(pantalla,cursor1,opcionA,65,430,"1")
        jboton2.update(pantalla,cursor1,opcionB,450,430,"1")
        jboton3.update(pantalla,cursor1,opcionC,65,508,"1")
        jboton4.update(pantalla,cursor1,opcionD,450,508,"1")
        py.display.update()


        salirJuego=False
        resp=False
        py.time.set_timer(1,0)

        while salirJuego!=True:
            
            for event2 in py.event.get():

                if event2.type == py.QUIT:
                    salirJuego=True
                    py.mixer.stop()
                if event2.type == py.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(jboton1.rect):
                        salirJuego=True
                        py.mixer.stop()
                        if preg[5]==1:
                            resp= True
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoAcierto.ogg")
                            sound.play()
                            pytime.wait(10)
                        else:
                            resp= False
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoError.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton2.rect):
                        salirJuego=True
                        py.mixer.stop()
                        if preg[5]==2:
                            resp= True
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoAcierto.ogg")
                            sound.play()
                            pytime.wait(10)
                        else:
                            resp= False
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoError.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton3.rect):
                        salirJuego=True
                        py.mixer.stop()
                        if preg[5]==3:
                            resp= True
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoAcierto.ogg")
                            sound.play()
                            pytime.wait(10)
                        else:
                            resp= False
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoError.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton4.rect):
                        salirJuego=True
                        py.mixer.stop()
                        if preg[5]==4:
                            resp= True
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoAcierto.ogg")
                            sound.play()
                            pytime.wait(10)
                        else:
                            resp= False
                            sound = py.mixer.Sound("archivosJuego/Sonidos/SonidoError.ogg")
                            sound.play()
            cursor1.update()
            pantalla.blit(fondo,(0,0))

            pantalla.blit(dinero,(530,40))
            pantalla.blit(textoPregunta,(90,345))
            jboton1.update(pantalla,cursor1,opcionA,65,430,"1")
            jboton2.update(pantalla,cursor1,opcionB,450,430,"1")
            jboton3.update(pantalla,cursor1,opcionC,65,508,"1")
            jboton4.update(pantalla,cursor1,opcionD,450,508,"1")

            reloj = (py.time.get_ticks() / 1000)
            reloj= str(reloj)
            contador= fuente1.render("Tiempo: " + reloj,1,blanco)
            pantalla.blit(contador,(40,40))
            py.display.update()
        if resp == True:
            contadorPuntos = contadorPuntos+1
            puntaje = gan[contadorPuntos]
        else:
            salir=True
def main():
    
    py.init()
    pytime.wait(500)

    pantalla=py.display.set_mode((833,559))

    sound = py.mixer.Sound("archivosJuego/Sonidos/sonidoPrincipal.ogg")
    sound.play()



    py.display.set_caption("Quien quiere ser millonario")
    icon = py.image.load("archivosJuego/imagenes/IconoMillonario.jpg")  #fondoPrincipal
    fondo = py.image.load("archivosJuego/imagenes/MenuMillonario1.jpg")
    valor1=py.image.load("archivosJuego/imagenes/remarcado2.gif")
    valor2=py.image.load("archivosJuego/imagenes/remarcado2.gif")
    boton1=Boton(valor1,valor2,28,443)
    boton2=Boton(valor1,valor2,444,443)

    cursor1=Cursor()
    fuente1=py.font.SysFont("Comic Sans MS", 37, True, False)
    fuenteAutor = py.font.SysFont("Comic Sans MS", 16, True, False)

    py.display.set_icon(icon)
    blanco=(255,255,255)
    autor = "autor: Camilo Peña Marín "
    autor_pantalla = fuenteAutor.render(autor, 1, blanco)
    pantalla.blit(autor_pantalla, (20, 400))

    texto1 = fuente1.render("         Jugar", 1, blanco)
    texto2 = fuente1.render("         Salir", 1, blanco)

    salir=False
    
    #Pantalla Principal
    while salir!=True:

        pantalla.blit(fondo,(0,0))
        cursor1.update()
        boton1.update(pantalla,cursor1,texto1,28,443,"1")
        boton2.update(pantalla,cursor1,texto2,444,443,"2")

        autor = "Autor: Camilo Peña Marín "
        autor_pantalla = fuenteAutor.render(autor, 1, blanco)
        pantalla.blit(autor_pantalla, (40, 10))

        py.display.update()
            
        for event in py.event.get():
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    py.mixer.stop()
                    Vista_jugar(pantalla,cursor1)


            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton2.rect):
                     salir=True

    py.quit()
    
main() 