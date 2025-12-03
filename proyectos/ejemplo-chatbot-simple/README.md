# Chatbot Simple con IA 🤖

## 📝 Descripción

Este es un proyecto de ejemplo que demuestra cómo crear un chatbot simple utilizando procesamiento de lenguaje natural. El chatbot puede responder preguntas básicas y mantener conversaciones simples.

## 🎯 Motivación

Crear este proyecto como ejemplo para demostrar cómo estructurar un proyecto personal en el curso Python-AI. El objetivo es mostrar las mejores prácticas de documentación y organización de código.

## 🛠️ Tecnologías Utilizadas

- Python 3.8+
- NLTK (Natural Language Toolkit)
- NumPy
- scikit-learn (para similitud de texto)

## 📦 Instalación

```bash
# Navega a la carpeta del proyecto
cd proyectos/ejemplo-chatbot-simple

# Instala las dependencias
pip install -r requirements.txt
```

## 🚀 Uso

```bash
# Ejecuta el chatbot
python src/chatbot.py
```

Ejemplo de conversación:
```
Usuario: Hola
Bot: ¡Hola! ¿Cómo puedo ayudarte hoy?

Usuario: ¿Qué es Python?
Bot: Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.

Usuario: Adiós
Bot: ¡Hasta luego! Que tengas un excelente día.
```

## 📊 Características

- ✅ Reconocimiento de saludos
- ✅ Respuestas a preguntas frecuentes sobre Python e IA
- ✅ Similitud de texto para encontrar respuestas relevantes
- ✅ Interfaz de línea de comandos simple
- ✅ Fácilmente extensible con nuevas respuestas

## 🧠 Aprendizajes

Durante el desarrollo de este proyecto aprendí:

1. **Procesamiento de texto**: Cómo tokenizar y procesar texto natural
2. **Similitud semántica**: Uso de TF-IDF para encontrar respuestas similares
3. **Arquitectura de chatbots**: Estructura básica de un sistema conversacional
4. **Manejo de intenciones**: Cómo clasificar la intención del usuario

## 🔮 Próximos Pasos

Mejoras futuras planificadas:
- [ ] Integrar un modelo de lenguaje pre-entrenado (GPT)
- [ ] Agregar memoria de conversación
- [ ] Crear interfaz gráfica
- [ ] Añadir reconocimiento de emociones
- [ ] Implementar aprendizaje continuo

## 🤝 Estructura del Proyecto

```
ejemplo-chatbot-simple/
├── README.md              # Este archivo
├── requirements.txt       # Dependencias
├── src/
│   ├── __init__.py       # Inicializador del paquete
│   ├── chatbot.py        # Código principal del chatbot
│   ├── responses.py      # Base de conocimiento
│   └── utils.py          # Funciones auxiliares
└── data/                  # Carpeta para datos futuros
```

## 👤 Autor

Este es un proyecto de ejemplo creado para el curso Python-AI.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

**Nota**: Este es un ejemplo demostrativo. ¡Crea tu propio proyecto único! 🚀
