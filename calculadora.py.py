import math 
 
class aritmetica: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def suma(self): 
        return self.x + self.y 

    def resta(self): 
        return self.x - self.y 

    def multi(self): 
        return self.x * self.y 

    def division(self): 
        if self.y == 0:
            return "Error division por 0"
        else:
            return self.x / self.y 
     
    def modulo(self): 
        if self.y == 0:
            return "Error modulo por 0"
        else:
            return self.x % self.y 
 
 
class trigonometria: 
    def __init__(self, x): 
        self.x = x 

    def seno(self): 
        return math.sin(self.x) 

    def coseno(self): 
        return math.cos(self.x) 
 
 
class potencia: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def potencia(self): 
        return pow(self.x, self.y) 

    def lognat(self): 
        return math.log(self.x) 

    def log10(self): 
        return math.log10(self.x) 
 
 
x = float(input("Ingrese el valor x: ")) 
y = float(input("Ingrese el valor y: ")) 
 
print("1 suma") 
print("2 resta") 
print("3 multi") 
print("4 división") 
print("5 modulo") 
print("6 potencia") 
print("7 seno") 
print("8 coseno") 
print("9 lognat") 
print("10 log10") 
 
opcion = int(input("Elija una operación: ")) 
 
arit = aritmetica(x, y) 
trigo = trigonometria(x) 
pot = potencia(x, y) 
 
if opcion == 1: 
    print(arit.suma()) 

if opcion == 2: 
    print(arit.resta()) 

if opcion == 3: 
    print(arit.multi()) 

if opcion == 4: 
    print(arit.division()) 

if opcion == 5: 
    print(arit.modulo()) 

if opcion == 6: 
    print(pot.potencia()) 

if opcion == 7: 
    print(trigo.seno()) 

if opcion == 8: 
    print(trigo.coseno()) 

if opcion == 9: 
    print(pot.lognat()) 

if opcion == 10: 
    print(pot.log10())