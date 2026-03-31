"""
Version "buena" del codigo segun lo explicado en el capitulo.
"""

from typing import List


class Texto:
    def __init__(self, contenido: str):
        self.contenido = contenido
        self.editado = False

    def editar(self):
        self.editado = True


class ETL:
    def __init__(self, datos: List[str]):
        self.datos = datos

    def cargar(self) -> List[Texto]:
        for dato in self.datos:
            if not isinstance(dato, str):
                raise ValueError("Todos los elementos deben ser cadenas")
        return [Texto(dato) for dato in self.datos]

    def transformar(self, texto: Texto) -> Texto:
        texto.editar()
        return texto

    def mostrar(self, texto: Texto) -> None:
        print(texto.contenido)

    def main(self):
        # Enfoque correcto, dejamos que el programa explote ya que
        # "Dead programs tell no lies"
        textos = self.cargar()
        textos = [self.transformar(texto) for texto in textos]
        for texto in textos:
            self.mostrar(texto)


if __name__ == "__main__":
    # No lanza error ya que es el flujo esperado
    datos_crudos_buenos = ["Hola", "Mundo", "Python"]
    etl = ETL(datos_crudos_buenos)
    etl.main()

    # Lanza error, lo impensado ocurrio
    datos_crudos_malos = ["Hola", "Mundo", 123]
    etl = ETL(datos_crudos_malos)
    etl.main()
