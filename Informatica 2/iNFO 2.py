#POO(programación orientada a objetos) = paradigma de programación, hace referencia a la forma o metodos para realizar algo adecuadamente
#La abstracción = 1er pilar de este paradigma, consiste en extraer la información más importante del objeto
#Clase = plantilla - parte generica, objeto = se crea a partir de la plantilla - base, Atributos = características del objeto
#Método __init__, constructor
#Self es unicamente una palabra que ayuda a identificar el propio objeto
#Polimorfismo = versiones diferentes de un mismo objeto
#Notación UML = para representar gráficamente los componentes y relaciones entre objetos y clases

#CREAR UNA CLASE CON SUS ATRIBUTOS:
    #class Carro:
        #def __init__(self):
            #self.modelo = 2000
            #self.color = "Amarillo"

#CREAR OBJETOS:
    #x = Carro()
    #y = Carro()

###EJEMPLO:
#class Carro:
#    def __init__(self):
#        self.mod = 2000
#        self.color = "Amarillo"

#DEFINIR COMO SE MUESTRA EL OBJETO A CREAR CON LA CLASE:

#    def __str__(self):
#        return f"Este es un carro modelo {self.mod} y color {self.color}"

#CREACIÓN DE OBJETOS:
#x = Carro()
#y = Carro()
#y.mod = 1999
#z = Carro()
#print(x)
#print(y)
#print(z)

##EJEMPLO 2##:

class Animal:
   def __init__(self, esp):
       self.especie = esp
       self.dieta = "Carnivoro"
   def __str__(self):
       return f"Este es un animal {self.dieta}"
   def correr(self):
       if self.dieta != "Carnivoro":
           print("El animal corre a 50km/h")

########################################################

class Humano:
    def __init__(self):
        self.nombre = "Pepe"
    def __str__(self):
        return f"Este es un Humano llamado {self.nombre}"
    def correr(self):
        print("El humano Corre a 20km/h")

x = Humano()
z = Animal("Mamífero")
print(z)
print(x)
z.correr()
x.correr()

#HERENCIA:
class Ave:
    def __init__(self, tipo, vuela):
        self.ave = tipo #referente si es carnivoro, insectivora..... etc
        self.vuelo = vuela
        self.oviparos = True
        self.pico = True
    #Acciones basicas
    def comer(self, comida):
        print("Este tipo de ave come normalmente: ", comida)
    def volar(self):
        print("Este tipo de ave puede volar: ", self.vuelo)

class ganso(Ave):
    def __init__(self, tipo, vuela):
        pass

class pato(ganso):
    def __init__(self, tipo, vuela, accion, pata, col):
        ganso__init__(self,tipo,vuela,accion,pata):
        self.color = col
    def atacar(self, hambre):
        if hambre == "Sí":
            print("Ataca")

#ENCAPSULAMIENTO
#Volver privado un atributo o acción de la clase: se utiliza self.__Variable y restringe el acceso al atributo
#para extraer esta información restringida se puede hacer una funcion que retorne el dato: return self.__Variable

#EJERCICIO
class persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

class Paciente(persona):
    pass
class Enfermera(Paciente):
    pass
class Medico:
    pass