#__init__ ... ctor
#self. ... this.

class Dog:
    species = "Canis blabla"        #Klassenvariable

    def __init__ (self, name, age):
        self.name = name            #Instanzvariablen - Kann nach Instanz Variieren
        self.age = age

#Klasse ist wie eine Vorlage - man macht mit dieser Vorlage mehrere Objekte
#Dieses Objekt hat Attribute - die Attribute sind die Instanzvariablen

#neue Klasse - a ist eine Referenz auf die Klasse
# a = Dog(Bello, 4)

#zugreifen
# a.name

#Bei instanzmethoden steht immer ein self am Anfang

#Vererbung
#class Child(Parent):
