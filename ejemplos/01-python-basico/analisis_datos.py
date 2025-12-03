"""
Ejemplo: Análisis básico de datos con Python y Pandas
Demuestra conceptos fundamentales de manipulación de datos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def crear_datos_ejemplo():
    """Crea un dataset de ejemplo para demostración"""
    np.random.seed(42)
    
    datos = {
        'estudiante': [f'Estudiante_{i}' for i in range(1, 51)],
        'python_score': np.random.randint(60, 100, 50),
        'ia_score': np.random.randint(55, 100, 50),
        'proyecto_completado': np.random.choice([True, False], 50, p=[0.7, 0.3])
    }
    
    return pd.DataFrame(datos)

def analizar_datos(df):
    """Realiza análisis básico de los datos"""
    print("=" * 50)
    print("ANÁLISIS DE DATOS DEL CURSO")
    print("=" * 50)
    
    # Estadísticas descriptivas
    print("\n📊 Estadísticas Descriptivas:")
    print(df.describe())
    
    # Promedio por materia
    print(f"\n📈 Promedio Python: {df['python_score'].mean():.2f}")
    print(f"📈 Promedio IA: {df['ia_score'].mean():.2f}")
    
    # Tasa de completitud de proyectos
    tasa_completitud = df['proyecto_completado'].sum() / len(df) * 100
    print(f"\n✅ Proyectos completados: {tasa_completitud:.1f}%")
    
    # Estudiantes destacados
    print("\n🌟 Estudiantes destacados (promedio > 85):")
    df['promedio'] = (df['python_score'] + df['ia_score']) / 2
    destacados = df[df['promedio'] > 85]
    print(destacados[['estudiante', 'promedio']].to_string(index=False))
    
    return df

def visualizar_datos(df):
    """Crea visualizaciones de los datos"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histograma de puntuaciones
    axes[0].hist(df['python_score'], bins=10, alpha=0.7, label='Python', color='blue')
    axes[0].hist(df['ia_score'], bins=10, alpha=0.7, label='IA', color='green')
    axes[0].set_xlabel('Puntuación')
    axes[0].set_ylabel('Frecuencia')
    axes[0].set_title('Distribución de Puntuaciones')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Gráfico de dispersión
    axes[1].scatter(df['python_score'], df['ia_score'], 
                   c=df['proyecto_completado'], cmap='coolwarm', alpha=0.6)
    axes[1].set_xlabel('Puntuación Python')
    axes[1].set_ylabel('Puntuación IA')
    axes[1].set_title('Relación entre Puntuaciones')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/analisis_curso.png')
    print("\n📊 Visualización guardada en /tmp/analisis_curso.png")

if __name__ == "__main__":
    print("🐍 Ejemplo de Análisis de Datos con Python\n")
    
    # Crear datos de ejemplo
    df = crear_datos_ejemplo()
    
    # Analizar
    df = analizar_datos(df)
    
    # Visualizar
    visualizar_datos(df)
    
    print("\n✨ Análisis completado!")
