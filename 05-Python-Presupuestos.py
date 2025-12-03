import pandas as pd


def formatear_precio(precio):
    """Función auxiliar para dar formato de peso chileno"""
    return f"${precio:,.0f}".replace(",", ".")


def cotizador_pc():
    archivo_csv = 'componentes_pc.csv'

    try:
        df = pd.read_csv(archivo_csv)
    except FileNotFoundError:
        print(f"❌ Error: No se encuentra {archivo_csv}")
        return

    # Definimos el orden lógico para preguntar al usuario
    orden_categorias = [
        'Procesador',
        'Placa Madre',
        'Memoria RAM',
        'Almacenamiento',
        'Tarjeta de Video',
        'Fuente de Poder',
        'Gabinete'
    ]

    carrito_compras = []
    total_presupuesto = 0

    print("\n🖥️  BIENVENIDO AL CONFIGURADOR DE PC GAMER 🖥️")
    print("Vamos a armar tu equipo paso a paso.\n")

    # Bucle principal: Vamos categoría por categoría
    for categoria in orden_categorias:
        print(f"\n🔵 SELECCIONA: {categoria.upper()}")
        print("-" * 80)
        # Encabezado de la tabla
        print(f"{'ID':<4} | {'Nombre':<30} | {'Precio':<12} | {'Gama':<10} | {'Uso'}")
        print("-" * 80)

        # Filtramos el DataFrame solo por la categoría actual
        opciones = df[df['categoria'] == categoria]

        # Mostramos las opciones disponibles
        for index, row in opciones.iterrows():
            precio_fmt = formatear_precio(row['precio'])
            print(
                f"{row['id']:<4} | {row['nombre']:<30} | {precio_fmt:<12} | {row['gama']:<10} | {row['uso_recomendado']}")

        print("-" * 80)

        # Validación del input del usuario
        seleccion_valida = False
        while not seleccion_valida:
            try:
                eleccion = input(f"👉 Ingresa el ID de tu {categoria} (o 0 para saltar): ")
                id_elegido = int(eleccion)

                if id_elegido == 0:
                    print(f"⏩ Saltaste la categoría {categoria}.")
                    seleccion_valida = True
                    continue

                # Buscamos si el ID existe Y si pertenece a la categoría actual
                # (Para evitar que elijan una RAM cuando se les pide CPU)
                item = opciones[opciones['id'] == id_elegido]

                if not item.empty:
                    nombre_componente = item.iloc[0]['nombre']
                    precio_componente = item.iloc[0]['precio']

                    print(f"✅ Agregado: {nombre_componente}")

                    # Guardamos en el carrito y sumamos
                    carrito_compras.append({
                        'categoria': categoria,
                        'nombre': nombre_componente,
                        'precio': precio_componente,
                        'specs': item.iloc[0]['specs']
                    })
                    total_presupuesto += precio_componente
                    seleccion_valida = True
                else:
                    print("⚠️ ID no válido para esta categoría. Intenta de nuevo.")

            except ValueError:
                print("⚠️ Por favor ingresa un número.")

    # === RESUMEN FINAL ===
    print("\n\n")
    print("=" * 50)
    print("📄 RESUMEN DE TU COTIZACIÓN")
    print("=" * 50)

    if not carrito_compras:
        print("No seleccionaste ningún componente 😢")
    else:
        for item in carrito_compras:
            # Formato bonito: Categoria: Nombre ....... Precio
            print(f"• {item['categoria']}: {item['nombre']}")
            print(f"  └─ Specs: {item['specs']}")
            print(f"  └─ Valor: {formatear_precio(item['precio'])}")
            print("-" * 50)

        print(f"\n💰 PRECIO TOTAL ESTIMADO: {formatear_precio(total_presupuesto)}")
        print("=" * 50)


if __name__ == "__main__":
    cotizador_pc()