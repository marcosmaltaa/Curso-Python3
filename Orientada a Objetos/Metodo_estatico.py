class MinhaClasse:

    def __init__(self,estado) -> None:
        self.estado = estado

    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")

obj = MinhaClasse(True)
obj.metodo_estatico()
MinhaClasse.metodo_estatico()