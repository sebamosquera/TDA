class Pila:

    def __init__(self):
        self.items=[]

    def apilar(self,x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")

    def es_vacia(self):
        return self.items == []

    def imprimir(self):
        for i in self.items:
            print(i)
        print('\n')
