#Actividad 1. Identificar elementos de POO 

class Producto(object): 
    def __init__(self, nombre, precio): 
        self.nombre = nombre 
        self.precio = precio 
        self.total = 0 
    def calcularTotal(self, cantidad): 
        self.total = self.precio * cantidad 
    def mostrarTotal(self): 
        print(f"Producto: {self.nombre}") 
        print(f"Total: ${self.total:.2f}") 
producto1 = Producto("Cuaderno", 35) 
producto1.calcularTotal(3) 
producto1.mostrarTotal() 

#Responder las siguetntes preguntas:
#1. ¿Cuál es el nombre de la clase? 
# Producto

#2. ¿Cuáles son sus propiedades? 
# nombre, precio, total

#3. ¿Cuáles son sus métodos? 
# __init__, calcularTotal, mostrarTotal

#4. ¿Qué función cumple __init__? 
# Es el constructor de la clase, se utiliza para inicializar los atributos del objeto cuando se crea una instancia de la clase.

#5. ¿Para qué se utiliza self? 
# Se utiliza para referirse a la instancia actual de la clase y acceder a sus atributos y métodos.

#6. ¿En qué instrucción se crea un objeto? 
# En la instrucción producto1 = Producto("Cuaderno", 35) se crea un objeto de la clase Producto.

#7. ¿Cuál es el nombre del objeto? 
# El nombre del objeto es producto1

#8. ¿Cómo se llama a calcularTotal()? 
# Se llama a calcularTotal() mediante la instrucción producto1.calcularTotal(3), donde se pasa el argumento 3 como cantidad.

#9. ¿Qué valores recibe el constructor cuando se crea el objeto? 
# El constructor recibe los valores "Cuaderno" y 35 cuando se crea el objeto producto1.

#10. ¿Qué resultado mostrará el programa?
# El programa mostrará: Producto: Cuaderno

#Actividad 2. Completar código 
class Rectangulo(object): 
    def __init__(self, base, altura): 
        self.base = base 
        self.altura = altura
    def calcularArea(self): 
        area = self.base * self.altura
        return area
    def mostrarArea(self): 
        area = self.calcularArea()
        print(f"El área del rectángulo es: {area}")
figura1 = Rectangulo(8, 5)
figura1.calcularArea()
figura1.mostrarArea()

#Actividad 3. Interpretar herencia (8 puntos) 
class Operacion(object): 
    def __init__(self, numero1, numero2): 
        self.numero1 = numero1 
        self.numero2 = numero2 
  
    def calcular(self): 
        return self.numero1 + self.numero2 
  
class Multiplicacion(Operacion): 
    def calcular(self): 
        return self.numero1 * self.numero2
operacion1 = Operacion(8, 4) 
operacion2 = Multiplicacion(8, 4) 
print(operacion1.calcular()) 
print(operacion2.calcular()) 

#Responder las siguientes preguntas:
#1. ¿Cuál es la clase padre? 
# La clase padre es Operacion

#2. ¿Cuál es la clase hija? 
# La clase hija es Multiplicacion

#3. ¿Cómo se indica la herencia? 
# Se indica la herencia colocando el nombre de la clase padre entre paréntesis después del nombre de la clase hija,
#  como en class Multiplicacion(Operacion).

#4. ¿Qué propiedades utiliza la clase hija? 
# La clase hija utiliza las propiedades numero1 y numero2 que hereda de la clase padre Operacion.

#5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
# Porque la clase hija Multiplicacion hereda el método __init__ de la clase padre Operacion,

#6. ¿Por qué los métodos calcular() tienen resultados distintos? 
# Porque la clase hija Multiplicacion sobrescribe el método calcular() de la clase padre Operacion,

#7. ¿Qué valores se imprimen? 
# Se imprimen los valores 12 y 32, que son los resultados de las operaciones de suma y multiplicación respectivamente.

#8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
# Si eliminamos calcular() de Multiplicacion, la clase hija utilizaría el método calcular() de la clase padre Operacion,
#  y ambos objetos operacion1 y operacion2 devolverían el mismo resultado de la suma, que sería 12 en este caso.
  

