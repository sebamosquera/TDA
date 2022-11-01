class Socio:
    def __init__(self, numero_socio, conocidos, nombre):
        self.numero_socio = numero_socio
        self.conocidos = conocidos # lista de socios
        self.invitable  = True
        self.nombre = nombre

    def get_numero(self):
        return self.numero_socio

    def get_conocidos(self):
        return self.conocidos

    def es_invitable(self):
        return self.invitable

    def get_nombre(self):
        return self.nombre

    def desinvitar(self):
        self.invitable = False

    def __str__(self):
        return  str(self.numero_socio) + ": " + self.nombre
