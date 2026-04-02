"""
Version "buena" del codigo segun lo explicado en el capitulo.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Recurso:
    nombre: str
    contenido: List[str]


class Manejador:
    def leer(self, recurso: Recurso):
        print(f"Recurso {recurso.nombre} leido.")

    def escribir(self, recurso: Recurso) -> List[str]:
        return recurso.contenido

    def actualizar(self, recurso: Recurso, contenido_agregar: str) -> List[str]:
        # Acá dentro de la misma función leemos y cerramos el recurso, pasandolo
        # como parámetro en vez de ser un recurso compartido
        recurso_manejado = recurso
        self.leer(recurso_manejado)
        recurso_manejado.contenido += [contenido_agregar]
        recurso_mostrar = self.escribir(recurso_manejado)
        recurso_manejado = None
        return recurso_mostrar


if __name__ == "__main__":
    manejador = Manejador()
    recurso = Recurso(nombre="ejemplo.txt", contenido=[])
    resultado = manejador.actualizar(recurso, "hola")
    print(resultado)
