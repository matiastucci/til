"""Estudio de patrones en la ruleta americana.

La ruleta americana tiene 38 casilleros: 0, 00 y 1..36.
Rojos: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
Negros: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
Verdes (cero): 0, 00
"""

import random
from collections import Counter

ROJOS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
NEGROS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
CEROS = {"0", "00"}

CASILLEROS = ["0", "00"] + [str(n) for n in range(1, 37)]


def color_de(numero: str) -> str:
    if numero in CEROS:
        return "cero"
    n = int(numero)
    if n in ROJOS:
        return "rojo"
    if n in NEGROS:
        return "negro"
    raise ValueError(f"Número inválido: {numero}")


def tirar(cantidad: int) -> list[str]:
    return [random.choice(CASILLEROS) for _ in range(cantidad)]


def max_seguidos_por_color(tiradas: list[str], color_objetivo: str) -> int:
    actual = 0
    maximo = 0
    for numero in tiradas:
        if color_de(numero) == color_objetivo:
            actual += 1
            if actual > maximo:
                maximo = actual
        else:
            actual = 0
    return maximo


def numero_mas_seguido(tiradas: list[str]) -> tuple[str, int]:
    if not tiradas:
        return ("", 0)
    mejor_numero = tiradas[0]
    mejor_racha = 1
    actual_numero = tiradas[0]
    actual_racha = 1
    for numero in tiradas[1:]:
        if numero == actual_numero:
            actual_racha += 1
        else:
            actual_numero = numero
            actual_racha = 1
        if actual_racha > mejor_racha:
            mejor_racha = actual_racha
            mejor_numero = actual_numero
    return (mejor_numero, mejor_racha)


def analizar(tiradas: list[str]) -> None:
    print(f"\n=== Análisis de {len(tiradas)} tiradas ===\n")

    max_negros = max_seguidos_por_color(tiradas, "negro")
    max_rojos = max_seguidos_por_color(tiradas, "rojo")
    max_ceros = max_seguidos_por_color(tiradas, "cero")
    numero, racha = numero_mas_seguido(tiradas)

    print(f"1) Máxima racha de NEGROS seguidos: {max_negros}")
    print(f"2) Máxima racha de ROJOS seguidos:  {max_rojos}")
    print(f"3) Máxima racha de CEROS (0/00):    {max_ceros}")
    print(f"4) Número que salió más veces seguidas: {numero} ({racha} veces seguidas)")

    conteo = Counter(tiradas)
    numero_top, veces_top = conteo.most_common(1)[0]
    print(f"5) Número más frecuente en total: {numero_top} ({veces_top} apariciones)")


def menu() -> None:
    opciones = {
        "1": 1000,
        "2": 2000,
        "3": 3000,
        "4": 4000,
        "5": 5000,
    }
    while True:
        print("\n========== ESTUDIO DE RULETA AMERICANA ==========")
        print("Elegí un módulo de tiradas aleatorias:")
        for clave, cantidad in opciones.items():
            print(f"  {clave}) {cantidad} tiradas")
        print("  0) Salir")
        eleccion = input("\nOpción: ").strip()

        if eleccion == "0":
            print("Chau.")
            return
        if eleccion not in opciones:
            print("Opción inválida.")
            continue

        cantidad = opciones[eleccion]
        tiradas = tirar(cantidad)
        analizar(tiradas)


if __name__ == "__main__":
    menu()
