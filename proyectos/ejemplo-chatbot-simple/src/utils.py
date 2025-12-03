"""
Funciones auxiliares para el chatbot
"""

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocesar_texto(texto):
    """
    Preprocesa el texto para análisis
    
    Args:
        texto (str): Texto a procesar
        
    Returns:
        str: Texto procesado
    """
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Remover caracteres especiales pero mantener espacios
    texto = re.sub(r'[^\w\s]', '', texto)
    
    # Remover espacios múltiples
    texto = ' '.join(texto.split())
    
    return texto

def calcular_similitud(texto1, texto2):
    """
    Calcula la similitud entre dos textos usando TF-IDF y similitud de coseno
    
    Args:
        texto1 (str): Primer texto
        texto2 (str): Segundo texto
        
    Returns:
        float: Valor de similitud entre 0 y 1
    """
    try:
        # Crear vectorizador TF-IDF
        vectorizer = TfidfVectorizer()
        
        # Transformar textos a vectores
        textos = [texto1, texto2]
        tfidf_matrix = vectorizer.fit_transform(textos)
        
        # Calcular similitud de coseno
        similitud = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        
        return similitud
    except:
        # Si hay algún error, retornar 0
        return 0.0

def limpiar_respuesta(respuesta):
    """
    Limpia y formatea una respuesta
    
    Args:
        respuesta (str): Respuesta a limpiar
        
    Returns:
        str: Respuesta formateada
    """
    # Capitalizar primera letra
    respuesta = respuesta.strip()
    if respuesta:
        respuesta = respuesta[0].upper() + respuesta[1:]
    
    # Asegurar que termina con punto
    if respuesta and respuesta[-1] not in ['.', '!', '?']:
        respuesta += '.'
    
    return respuesta
