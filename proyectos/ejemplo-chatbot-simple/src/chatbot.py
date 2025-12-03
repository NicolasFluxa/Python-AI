"""
Chatbot Simple con Procesamiento de Lenguaje Natural
Proyecto de ejemplo para el curso Python-AI
"""

import random
from responses import RESPUESTAS, SALUDOS, DESPEDIDAS
from utils import preprocesar_texto, calcular_similitud

class ChatbotSimple:
    """Clase principal del chatbot"""
    
    def __init__(self):
        """Inicializa el chatbot"""
        self.nombre = "PyBot"
        self.activo = True
        print(f"🤖 {self.nombre} inicializado correctamente")
    
    def saludar(self):
        """Muestra un saludo inicial"""
        saludo = random.choice([
            f"¡Hola! Soy {self.nombre}, tu asistente de Python e IA.",
            f"¡Bienvenido! Me llamo {self.nombre}. ¿En qué puedo ayudarte?",
            f"¡Hola! Soy {self.nombre}. Pregúntame sobre Python e IA."
        ])
        print(f"\n{saludo}")
        print("(Escribe 'salir' para terminar la conversación)\n")
    
    def es_saludo(self, texto):
        """Detecta si el mensaje es un saludo"""
        texto_lower = texto.lower()
        return any(saludo in texto_lower for saludo in SALUDOS)
    
    def es_despedida(self, texto):
        """Detecta si el mensaje es una despedida"""
        texto_lower = texto.lower()
        return any(despedida in texto_lower for despedida in DESPEDIDAS)
    
    def responder_saludo(self):
        """Responde a un saludo"""
        respuestas = [
            "¡Hola! ¿Cómo puedo ayudarte hoy?",
            "¡Hola! ¿Qué te gustaría saber?",
            "¡Hola! Estoy aquí para ayudarte con Python e IA."
        ]
        return random.choice(respuestas)
    
    def responder_despedida(self):
        """Responde a una despedida"""
        self.activo = False
        respuestas = [
            "¡Hasta luego! Que tengas un excelente día. 👋",
            "¡Adiós! Fue un placer ayudarte. 😊",
            "¡Nos vemos! Sigue aprendiendo. 🚀"
        ]
        return random.choice(respuestas)
    
    def buscar_respuesta(self, pregunta):
        """Busca la mejor respuesta para la pregunta"""
        pregunta_procesada = preprocesar_texto(pregunta)
        
        mejor_similitud = 0
        mejor_respuesta = "Lo siento, no tengo información sobre eso. ¿Podrías reformular tu pregunta?"
        
        # Buscar en la base de conocimiento
        for item in RESPUESTAS:
            for patron in item['patrones']:
                similitud = calcular_similitud(pregunta_procesada, patron)
                if similitud > mejor_similitud:
                    mejor_similitud = similitud
                    mejor_respuesta = random.choice(item['respuestas'])
        
        # Si la similitud es muy baja, usar respuesta por defecto
        if mejor_similitud < 0.3:
            mejor_respuesta = "No estoy seguro de entender tu pregunta. ¿Podrías ser más específico?"
        
        return mejor_respuesta
    
    def procesar_mensaje(self, mensaje):
        """Procesa el mensaje del usuario y genera una respuesta"""
        if not mensaje.strip():
            return "Por favor, escribe algo. 😊"
        
        # Verificar saludos
        if self.es_saludo(mensaje):
            return self.responder_saludo()
        
        # Verificar despedidas
        if self.es_despedida(mensaje):
            return self.responder_despedida()
        
        # Buscar respuesta en base de conocimiento
        return self.buscar_respuesta(mensaje)
    
    def ejecutar(self):
        """Ejecuta el loop principal del chatbot"""
        self.saludar()
        
        while self.activo:
            try:
                # Obtener input del usuario
                mensaje_usuario = input("Tú: ")
                
                # Verificar comando de salida
                if mensaje_usuario.lower() in ['salir', 'exit', 'quit']:
                    print(f"{self.nombre}: {self.responder_despedida()}")
                    break
                
                # Procesar y responder
                respuesta = self.procesar_mensaje(mensaje_usuario)
                print(f"{self.nombre}: {respuesta}\n")
                
            except KeyboardInterrupt:
                print(f"\n{self.nombre}: ¡Hasta luego! 👋")
                break
            except Exception as e:
                print(f"{self.nombre}: Ocurrió un error. Por favor, inténtalo de nuevo.")
                print(f"Error: {str(e)}")

def main():
    """Función principal"""
    print("=" * 60)
    print("   CHATBOT SIMPLE - PROYECTO DE EJEMPLO")
    print("   Curso: Python-AI")
    print("=" * 60)
    
    # Crear y ejecutar chatbot
    bot = ChatbotSimple()
    bot.ejecutar()
    
    print("\n" + "=" * 60)
    print("   ¡Gracias por usar el chatbot!")
    print("=" * 60)

if __name__ == "__main__":
    main()
