class Estacionamiento(object):
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if self.horas <= 2:
            tarifa = 15 
        elif self.horas <= 5:
            tarifa = 12
        else:
            tarifa = 10
        return self.horas * tarifa

    def mostrarRecibo(self):
        total = self.calcularPago()
        print(f"Horas estacionadas: {self.horas}")
        print("RECIBO DE ESTACIONAMIENTO")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total:.2f}")
tarifa1 = Estacionamiento(4)
tarifa1.mostrarRecibo()
tarifa2 = Estacionamiento(2)
tarifa2.mostrarRecibo()  
tarifa3 = Estacionamiento(6)
tarifa3.mostrarRecibo()