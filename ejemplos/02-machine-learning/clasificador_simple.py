"""
Ejemplo: Clasificador Simple con Scikit-learn
Demuestra un flujo básico de Machine Learning
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np

def cargar_y_preparar_datos():
    """Carga y prepara el dataset Iris"""
    print("📦 Cargando dataset Iris...")
    
    # Cargar datos
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    print(f"   - Muestras: {X.shape[0]}")
    print(f"   - Features: {X.shape[1]}")
    print(f"   - Clases: {len(np.unique(y))}")
    
    return X, y, iris.target_names

def entrenar_modelo(X_train, y_train):
    """Entrena un clasificador Random Forest"""
    print("\n🎯 Entrenando modelo Random Forest...")
    
    # Crear y entrenar modelo
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    
    print("   ✅ Modelo entrenado exitosamente!")
    return modelo

def evaluar_modelo(modelo, X_test, y_test, nombres_clases):
    """Evalúa el rendimiento del modelo"""
    print("\n📊 Evaluando modelo...")
    
    # Predicciones
    y_pred = modelo.predict(X_test)
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n   Accuracy: {accuracy * 100:.2f}%")
    
    # Reporte de clasificación
    print("\n📈 Reporte de Clasificación:")
    print(classification_report(y_test, y_pred, target_names=nombres_clases))
    
    # Matriz de confusión
    print("🔢 Matriz de Confusión:")
    print(confusion_matrix(y_test, y_pred))
    
    # Importancia de features
    print("\n🌟 Importancia de Features:")
    feature_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
    importancias = modelo.feature_importances_
    for nombre, importancia in zip(feature_names, importancias):
        print(f"   {nombre:15s}: {importancia:.4f}")

def predecir_nueva_muestra(modelo, nombres_clases):
    """Realiza una predicción en una muestra nueva"""
    print("\n🔮 Predicción en nueva muestra:")
    
    # Nueva muestra (inventada)
    nueva_muestra = np.array([[5.1, 3.5, 1.4, 0.2]])
    
    prediccion = modelo.predict(nueva_muestra)
    probabilidades = modelo.predict_proba(nueva_muestra)
    
    print(f"   Muestra: {nueva_muestra[0]}")
    print(f"   Clase predicha: {nombres_clases[prediccion[0]]}")
    print(f"   Probabilidades:")
    for nombre, prob in zip(nombres_clases, probabilidades[0]):
        print(f"      {nombre:10s}: {prob * 100:.2f}%")

def main():
    """Función principal que ejecuta el flujo completo"""
    print("🤖 Ejemplo de Clasificación con Machine Learning")
    print("=" * 50)
    
    # 1. Cargar datos
    X, y, nombres_clases = cargar_y_preparar_datos()
    
    # 2. Dividir datos
    print("\n✂️  Dividiendo datos (80% entrenamiento, 20% prueba)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 3. Normalizar datos (opcional pero recomendado)
    print("🔧 Normalizando datos...")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # 4. Entrenar modelo
    modelo = entrenar_modelo(X_train, y_train)
    
    # 5. Evaluar modelo
    evaluar_modelo(modelo, X_test, y_test, nombres_clases)
    
    # 6. Predicción en nueva muestra
    predecir_nueva_muestra(modelo, nombres_clases)
    
    print("\n" + "=" * 50)
    print("✨ Ejemplo completado exitosamente!")
    print("\n💡 Próximos pasos:")
    print("   - Experimenta con otros algoritmos")
    print("   - Prueba con tus propios datos")
    print("   - Ajusta los hiperparámetros")
    print("   - Crea tu propio proyecto de clasificación")

if __name__ == "__main__":
    main()
