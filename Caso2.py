from abc import ABC, abstractmethod

class ReglaCobro(ABC):
    @abstractmethod
    def aplicar(self, monto: float):
        pass

class RecargoExtemporanea(ReglaCobro):
    def aplicar(self, monto: float):
        return monto + 15

class RecargoDesaprobado(ReglaCobro):
    def aplicar(self, monto: float):
        return monto + 15

class DescuentoBeca(ReglaCobro):
    def aplicar(self, monto: float):
        return monto / 2

class Matricula:
    def __init__(self, estudiante: str):
        self.__estudiante = estudiante
        self.__monto_base = 60
        self.__reglas = []

    @property
    def estudiante(self):
        return self.__estudiante

    def agregar_regla(self, regla: ReglaCobro):
        self.__reglas.append(regla)

    def calcular_total(self):
        total = self.__monto_base
        for regla in self.__reglas:
            total = regla.aplicar(total)
        return total

if __name__ == "__main__":
    matricula_luis = Matricula("Luis Huamaní Cárdenas")
    matricula_luis.agregar_regla(RecargoExtemporanea())
    matricula_luis.agregar_regla(RecargoDesaprobado())
    matricula_luis.agregar_regla(DescuentoBeca())
    
    matricula_rosa = Matricula("Rosa Ccahuana Prado")
    matricula_rosa.agregar_regla(RecargoExtemporanea())
    matricula_rosa.agregar_regla(RecargoDesaprobado())
    matricula_rosa.agregar_regla(DescuentoBeca())
    
    print(f"Total a pagar por {matricula_luis.estudiante}: S/ {matricula_luis.calcular_total()}")
    print(f"Total a pagar por {matricula_rosa.estudiante}: S/ {matricula_rosa.calcular_total()}")