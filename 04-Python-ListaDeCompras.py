import pandas as pd
import sys


def main():
    nombre_archivo = 'menu_recetas.csv'

    try:
        # 1. Cargamos el archivo CSV
        # El encoding='utf-8' es importante para que se vean bien las tildes y ñ
        df = pd.read_csv(nombre_archivo)
    except FileNotFoundError:
        print(f"❌ Error: No encontré el archivo '{nombre_archivo}'.")
        print("Por favor, asegúrate de crear el CSV en la misma carpeta que este script.")
        return

    # 2. Saludamos y mostramos el menú
    print("\n==========================================")
    print(" 👩‍🍳 BIENVENIDO AL ASISTENTE DE COCINA 👨‍🍳    ")
    print("==========================================\n")
    print("Aquí tienes los platos disponibles:")
    print("-" * 40)

    # Iteramos para mostrar id y nombre de forma ordenada
    for index, row in df.iterrows():
        print(f" {row['id']}. {row['nombre_plato']} ({row['categoria']})")

    print("-" * 40)

    # 3. Solicitamos la elección del usuario
    while True:
        try:
            seleccion = int(input("\n👉 Por favor, escribe el NÚMERO del plato que quieres cocinar: "))

            # Verificamos si el ID existe en nuestro DataFrame
            plato_elegido = df[df['id'] == seleccion]

            if not plato_elegido.empty:
                # Salimos del bucle si la elección es correcta
                break
            else:
                print("⚠️  Ese número no está en la lista. Intenta de nuevo.")
        except ValueError:
            print("⚠️  Por favor, ingresa solo números.")

    # 4. Procesamos la información del plato elegido
    nombre = plato_elegido.iloc[0]['nombre_plato']
    ingredientes_raw = plato_elegido.iloc[0]['ingredientes']
    tiempo = plato_elegido.iloc[0]['tiempo_estimado']

    # Convertimos el texto de ingredientes en una lista separada
    lista_ingredientes = [ingrediente.strip() for ingrediente in ingredientes_raw.split(',')]

    # 5. Generamos la "Lista de Compras" final
    print("\n" + "=" * 50)
    print(f"✅ ¡EXCELENTE ELECCIÓN! VAMOS A COCINAR: {nombre.upper()}")
    print(f"⏱️  Tiempo estimado: {tiempo}")
    print("=" * 50)

    print("\n🛒 TU LISTA DE COMPRAS:")
    print("-----------------------")
    for item in lista_ingredientes:
        # Ponemos una casilla de verificación vacía [ ] para dar estilo
        print(f"[ ] {item.capitalize()}")

    print("\n" + "=" * 50)
    print("¡Guarda esta lista (puedes tomarle una foto) y corre al mercado!")
    print("¡Buen provecho! 😋")


if __name__ == "__main__":
    main()