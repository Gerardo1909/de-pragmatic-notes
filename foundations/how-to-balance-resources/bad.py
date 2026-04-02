"""
Version "mala" del codigo segun lo explicado en el capitulo.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Recurso:
    nombre: str
    contenido: List[str]


class Manejador:
    def __init__(self):
        self.recurso = ...

    def leer(self, recurso: Recurso):
        self.recurso = recurso
        print(f"Recurso {self.recurso.nombre} leido.")

    def escribir(self) -> List[str]:
        recurso_return = self.recurso.contenido
        # Simulamos liberación del recurso
        self.recurso = None
        return recurso_return

    def actualizar(self, recurso: Recurso, contenido_agregar: str) -> List[str]:
        # Notar que esta función nunca se encarga ni de traer al recurso ni de escribirlo de vuelta
        self.leer(recurso)
        self.recurso.contenido += [contenido_agregar]
        return self.escribir()


if __name__ == "__main__":
    manejador = Manejador()
    recurso = Recurso(nombre="ejemplo.txt", contenido=[])
    resultado = manejador.actualizar(recurso, "hola")
    print(resultado)
