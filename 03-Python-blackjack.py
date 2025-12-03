"""
Juego de Blackjack (21)
Jugador Humano vs Máquina (Dealer)
Sin usar POO, solo funciones
"""

import random
import time

# Configuración del juego
PALOS = ['♠', '♥', '♦', '♣']
VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALORES_CARTA = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}


def crear_baraja():
    """Crea una baraja completa de 52 cartas"""
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            carta = {'valor': valor, 'palo': palo}
            baraja.append(carta)
    return baraja


def mezclar_baraja(baraja):
    """Mezcla la baraja"""
    random.shuffle(baraja)
    return baraja


def repartir_carta(baraja):
    """Reparte una carta de la baraja"""
    if len(baraja) > 0:
        return baraja.pop()
    return None


def dibujar_carta(carta, oculta=False):
    """Dibuja una carta con ASCII art"""
    if oculta:
        return [
            "┌─────────┐",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "└─────────┘"
        ]

    valor = carta['valor']
    palo = carta['palo']

    # Ajustar el espaciado según el valor
    if len(valor) == 1:
        valor_str = f" {valor} "
    else:
        valor_str = f"{valor} "

    return [
        "┌─────────┐",
        f"│{valor_str}      │",
        f"│         │",
        f"│    {palo}    │",
        f"│      {valor_str}│",
        "└─────────┘"
    ]


def mostrar_cartas(cartas, ocultar_primera=False):
    """Muestra múltiples cartas horizontalmente"""
    if not cartas:
        return

    # Preparar las líneas de todas las cartas
    todas_lineas = []
    for i, carta in enumerate(cartas):
        oculta = (i == 0 and ocultar_primera)
        lineas_carta = dibujar_carta(carta, oculta)
        todas_lineas.append(lineas_carta)

    # Imprimir las cartas lado a lado
    for linea_idx in range(6):
        linea_completa = "  ".join([lineas[linea_idx] for lineas in todas_lineas])
        print(linea_completa)


def calcular_valor_mano(mano):
    """Calcula el valor total de una mano"""
    valor = 0
    ases = 0

    for carta in mano:
        valor_carta = VALORES_CARTA[carta['valor']]
        valor += valor_carta
        if carta['valor'] == 'A':
            ases += 1

    # Ajustar el valor de los ases si es necesario
    while valor > 21 and ases > 0:
        valor -= 10
        ases -= 1

    return valor


def mostrar_mano(nombre, mano, ocultar_primera=False):
    """Muestra la mano de un jugador"""
    print(f"\n{nombre}:")
    mostrar_cartas(mano, ocultar_primera)

    if not ocultar_primera:
        valor = calcular_valor_mano(mano)
        print(f"Valor total: {valor}")


def tiene_blackjack(mano):
    """Verifica si una mano es Blackjack (21 con 2 cartas)"""
    return len(mano) == 2 and calcular_valor_mano(mano) == 21


def turno_jugador(baraja, mano_jugador):
    """Gestiona el turno del jugador"""
    while True:
        valor = calcular_valor_mano(mano_jugador)

        if valor > 21:
            return False  # Se pasó

        if valor == 21:
            return True  # Plantarse automáticamente en 21

        print("\n" + "="*50)
        respuesta = input("¿Quieres otra carta? (s/n): ").lower()

        if respuesta == 's':
            print("\n🎴 Repartiendo carta...")
            time.sleep(0.5)
            carta = repartir_carta(baraja)
            mano_jugador.append(carta)
            mostrar_mano("🎮 TU MANO", mano_jugador)
        else:
            return True  # Se plantó


def turno_dealer(baraja, mano_dealer):
    """Gestiona el turno del dealer (máquina)"""
    print("\n" + "="*50)
    print("🤖 TURNO DEL DEALER")
    print("="*50)
    time.sleep(1)

    print("\n🎴 El dealer revela su carta oculta...")
    time.sleep(1)
    mostrar_mano("🤖 MANO DEL DEALER", mano_dealer)

    # El dealer debe pedir carta hasta tener 17 o más
    while calcular_valor_mano(mano_dealer) < 17:
        time.sleep(1.5)
        print("\n🎴 El dealer pide otra carta...")
        time.sleep(0.5)
        carta = repartir_carta(baraja)
        mano_dealer.append(carta)
        mostrar_mano("🤖 MANO DEL DEALER", mano_dealer)

    valor_dealer = calcular_valor_mano(mano_dealer)

    if valor_dealer > 21:
        print("\n💥 ¡El dealer se pasó de 21!")
        return False
    else:
        print(f"\n✅ El dealer se planta con {valor_dealer}")
        return True


def determinar_ganador(mano_jugador, mano_dealer):
    """Determina el ganador de la partida"""
    valor_jugador = calcular_valor_mano(mano_jugador)
    valor_dealer = calcular_valor_mano(mano_dealer)

    print("\n" + "="*60)
    print("🏁 RESULTADO FINAL")
    print("="*60)

    # Verificar Blackjack
    blackjack_jugador = tiene_blackjack(mano_jugador)
    blackjack_dealer = tiene_blackjack(mano_dealer)

    if blackjack_jugador and not blackjack_dealer:
        print("\n🎉🎊 ¡BLACKJACK! ¡HAS GANADO! 🎊🎉")
        return "jugador"
    elif blackjack_dealer and not blackjack_jugador:
        print("\n😔 El dealer tiene Blackjack. Has perdido.")
        return "dealer"
    elif blackjack_jugador and blackjack_dealer:
        print("\n🤝 Ambos tienen Blackjack. ¡EMPATE!")
        return "empate"

    # Verificar si alguien se pasó
    if valor_jugador > 21:
        print("\n😔 Te pasaste de 21. Has perdido.")
        return "dealer"

    if valor_dealer > 21:
        print("\n🎉 ¡El dealer se pasó! ¡HAS GANADO!")
        return "jugador"

    # Comparar valores
    print(f"\n👤 Tu puntuación: {valor_jugador}")
    print(f"🤖 Puntuación del dealer: {valor_dealer}")

    if valor_jugador > valor_dealer:
        print("\n🎉🎊 ¡HAS GANADO! 🎊🎉")
        return "jugador"
    elif valor_dealer > valor_jugador:
        print("\n😔 El dealer gana. Has perdido.")
        return "dealer"
    else:
        print("\n🤝 ¡EMPATE!")
        return "empate"


def jugar_blackjack():
    """Función principal del juego"""
    print("="*60)
    print("🎰 BIENVENIDO AL BLACKJACK 🎰")
    print("="*60)
    print("\n📜 REGLAS:")
    print("1. El objetivo es llegar a 21 o acercarse sin pasarse")
    print("2. Las cartas numéricas valen su número")
    print("3. J, Q, K valen 10 puntos")
    print("4. El As vale 11 u 1 (se ajusta automáticamente)")
    print("5. Blackjack = 21 con 2 cartas (¡Ganas automáticamente!)")
    print("6. El dealer pide carta hasta tener 17 o más")
    print("\n" + "="*60)

    input("\nPresiona ENTER para comenzar...")

    # Crear y mezclar baraja
    print("\n🎴 Mezclando baraja...")
    time.sleep(1)
    baraja = crear_baraja()
    baraja = mezclar_baraja(baraja)

    # Repartir cartas iniciales
    print("\n🎴 Repartiendo cartas...")
    time.sleep(1)

    mano_jugador = []
    mano_dealer = []

    # Repartir 2 cartas a cada uno
    mano_jugador.append(repartir_carta(baraja))
    mano_dealer.append(repartir_carta(baraja))
    mano_jugador.append(repartir_carta(baraja))
    mano_dealer.append(repartir_carta(baraja))

    # Mostrar manos iniciales
    print("\n" + "="*50)
    mostrar_mano("🎮 TU MANO", mano_jugador)
    mostrar_mano("🤖 MANO DEL DEALER", mano_dealer, ocultar_primera=True)

    # Verificar Blackjack inmediato
    if tiene_blackjack(mano_jugador):
        print("\n🎉 ¡BLACKJACK! ¡Tienes 21!")
        # Revelar carta del dealer
        mostrar_mano("🤖 MANO DEL DEALER", mano_dealer)
        resultado = determinar_ganador(mano_jugador, mano_dealer)
        return resultado

    # Turno del jugador
    jugador_ok = turno_jugador(baraja, mano_jugador)

    if not jugador_ok:
        valor_jugador = calcular_valor_mano(mano_jugador)
        print(f"\n💥 ¡Te pasaste! Valor final: {valor_jugador}")
        mostrar_mano("🤖 MANO DEL DEALER", mano_dealer)
        resultado = determinar_ganador(mano_jugador, mano_dealer)
        return resultado

    # Turno del dealer
    turno_dealer(baraja, mano_dealer)

    # Determinar ganador
    resultado = determinar_ganador(mano_jugador, mano_dealer)

    print("\n" + "="*60)
    return resultado


# Iniciar el juego
if __name__ == "__main__":
    # Estadísticas del jugador
    victorias = 0
    derrotas = 0
    empates = 0

    while True:
        resultado = jugar_blackjack()

        # Actualizar estadísticas según el resultado
        if resultado == "jugador":
            victorias += 1
        elif resultado == "dealer":
            derrotas += 1
        elif resultado == "empate":
            empates += 1

        # Preguntar si quiere jugar otra vez
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if respuesta != 's':
            break

    print("\n👋 ¡Gracias por jugar! ¡Hasta pronto!")
    print(f"\n📊 Estadísticas finales:")
    print(f"   🏆 Victorias: {victorias}")
    print(f"   😔 Derrotas: {derrotas}")
    print(f"   🤝 Empates: {empates}")
    print(f"   🎮 Total de partidas: {victorias + derrotas + empates}")

