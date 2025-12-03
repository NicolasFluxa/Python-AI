"""
Juego PIG (El Cerdo) - Juego de Dados
Jugador Humano vs Máquina
"""

import random
import time


# Representación ASCII de los dados
def dibujar_dado(numero):
    """Dibuja un dado con ASCII art"""
    dados = {
        1: [
            " ┌─────────┐",
            " │         │",
            " │    ●    │",
            " │         │",
            " └─────────┘"
        ],
        2: [
            " ┌─────────┐",
            " │  ●      │",
            " │         │",
            " │      ●  │",
            " └─────────┘"
        ],
        3: [
            " ┌─────────┐",
            " │  ●      │",
            " │    ●    │",
            " │      ●  │",
            " └─────────┘"
        ],
        4: [
            " ┌─────────┐",
            " │  ●   ●  │",
            " │         │",
            " │  ●   ●  │",
            " └─────────┘"
        ],
        5: [
            " ┌─────────┐",
            " │  ●   ●  │",
            " │    ●    │",
            " │  ●   ●  │",
            " └─────────┘"
        ],
        6: [
            " ┌─────────┐",
            " │  ●   ●  │",
            " │  ●   ●  │",
            " │  ●   ●  │",
            " └─────────┘"
        ]
    }

    for linea in dados[numero]:
        print(linea)


def lanzar_dado():
    """Simula el lanzamiento de un dado"""
    return random.randint(1, 6)


def turno_humano(puntos_totales):
    """Gestiona el turno del jugador humano"""
    puntos_turno = 0
    print("\n" + "=" * 50)
    print("🎮 TU TURNO")
    print("=" * 50)

    while True:
        print(f"\n📊 Puntos totales: {puntos_totales}")
        print(f"💰 Puntos en este turno: {puntos_turno}")

        respuesta = input("\n¿Quieres lanzar el dado? (s/n): ").lower()

        if respuesta != 's':
            print(f"\n✅ Te plantas con {puntos_turno} puntos este turno")
            return puntos_turno

        print("\n🎲 Lanzando dado...")
        time.sleep(0.5)

        dado = lanzar_dado()
        dibujar_dado(dado)

        if dado == 1:
            print("\n💥 ¡OH NO! Sacaste un 1")
            print("❌ Pierdes todos los puntos de este turno")
            time.sleep(1.5)
            return 0
        else:
            puntos_turno += dado
            print(f"\n✨ Sumaste {dado} puntos")


def turno_maquina(puntos_totales):
    """Gestiona el turno de la máquina"""
    puntos_turno = 0
    print("\n" + "=" * 50)
    print("🤖 TURNO DE LA MÁQUINA")
    print("=" * 50)
    time.sleep(1)

    # Estrategia simple: la máquina se planta al llegar a 20 puntos en el turno
    # o si está cerca de ganar
    limite = 20
    if puntos_totales >= 80:
        limite = 10  # Más conservadora cerca de la victoria

    while puntos_turno < limite:
        print(f"\n📊 Puntos totales máquina: {puntos_totales}")
        print(f"💰 Puntos en este turno: {puntos_turno}")
        print("\n🎲 La máquina lanza el dado...")
        time.sleep(1)

        dado = lanzar_dado()
        dibujar_dado(dado)

        if dado == 1:
            print("\n💥 ¡La máquina sacó un 1!")
            print("❌ Pierde todos los puntos de este turno")
            time.sleep(1.5)
            return 0
        else:
            puntos_turno += dado
            print(f"\n✨ La máquina sumó {dado} puntos")
            time.sleep(1)

    print(f"\n✅ La máquina se planta con {puntos_turno} puntos")
    time.sleep(1.5)
    return puntos_turno


def jugar_pig():
    """Función principal del juego"""
    print("=" * 60)
    print("🐷 BIENVENIDO AL JUEGO PIG (EL CERDO) 🐷")
    print("=" * 60)
    print("\n📜 REGLAS:")
    print("1. Cada jugador lanza el dado en su turno")
    print("2. Puedes seguir lanzando y acumular puntos")
    print("3. Si sacas un 1, pierdes TODOS los puntos del turno")
    print("4. Puedes plantarte y guardar los puntos del turno")
    print("5. El primero en llegar a 100 puntos GANA")
    print("\n" + "=" * 60)

    input("\nPresiona ENTER para comenzar...")

    puntos_humano = 0
    puntos_maquina = 0
    meta = 100

    while puntos_humano < meta and puntos_maquina < meta:
        # Turno del humano
        ganancia = turno_humano(puntos_humano)
        puntos_humano += ganancia

        if puntos_humano >= meta:
            break

        # Turno de la máquina
        ganancia = turno_maquina(puntos_maquina)
        puntos_maquina += ganancia

    # Mostrar resultado final
    print("\n" + "=" * 60)
    print("🏁 ¡JUEGO TERMINADO!")
    print("=" * 60)
    print(f"\n👤 Puntos Humano: {puntos_humano}")
    print(f"🤖 Puntos Máquina: {puntos_maquina}")

    if puntos_humano >= meta:
        print("\n🎉🎊 ¡FELICIDADES! ¡HAS GANADO! 🎊🎉")
    else:
        print("\n😔 La máquina ha ganado. ¡Mejor suerte la próxima vez!")

    print("\n" + "=" * 60)


# Iniciar el juego
if __name__ == "__main__":
    jugar_pig()

    # Preguntar si quiere jugar otra vez
    while input("\n¿Quieres jugar otra vez? (s/n): ").lower() == 's':
        jugar_pig()

    print("\n👋 ¡Gracias por jugar! ¡Hasta pronto!")
