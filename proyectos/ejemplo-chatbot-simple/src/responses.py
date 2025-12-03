"""
Base de conocimiento del chatbot
Contiene patrones de preguntas y respuestas
"""

# Palabras clave para saludos
SALUDOS = [
    'hola', 'buenas', 'hey', 'hi', 'hello', 'saludos', 
    'buenos días', 'buenas tardes', 'buenas noches'
]

# Palabras clave para despedidas
DESPEDIDAS = [
    'adiós', 'adios', 'chao', 'hasta luego', 'nos vemos', 
    'bye', 'goodbye', 'hasta pronto', 'me voy'
]

# Base de conocimiento de respuestas
RESPUESTAS = [
    {
        'patrones': [
            '¿qué es python?',
            'qué es python',
            'python',
            'lenguaje python',
            'sobre python'
        ],
        'respuestas': [
            'Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su sintaxis clara y legible.',
            'Python es un lenguaje versátil usado en desarrollo web, ciencia de datos, IA, automatización y más.',
            'Python fue creado por Guido van Rossum y es uno de los lenguajes más populares del mundo.'
        ]
    },
    {
        'patrones': [
            '¿qué es ia?',
            '¿qué es inteligencia artificial?',
            'inteligencia artificial',
            'ia',
            'sobre ia'
        ],
        'respuestas': [
            'La Inteligencia Artificial (IA) es la capacidad de las máquinas para realizar tareas que normalmente requieren inteligencia humana.',
            'La IA incluye áreas como machine learning, procesamiento de lenguaje natural, visión por computadora y más.',
            'La IA permite a las computadoras aprender de datos, reconocer patrones y tomar decisiones inteligentes.'
        ]
    },
    {
        'patrones': [
            '¿qué es machine learning?',
            'machine learning',
            'aprendizaje automático',
            'ml'
        ],
        'respuestas': [
            'Machine Learning es una rama de la IA que permite a las computadoras aprender de datos sin ser programadas explícitamente.',
            'En Machine Learning, los algoritmos aprenden patrones de datos y pueden hacer predicciones o tomar decisiones.',
            'Existen tres tipos principales de ML: supervisado, no supervisado y por refuerzo.'
        ]
    },
    {
        'patrones': [
            '¿cómo empezar?',
            'cómo comenzar',
            'por dónde empiezo',
            'iniciar',
            'comenzar'
        ],
        'respuestas': [
            '¡Excelente pregunta! Empieza con los fundamentos de Python en la carpeta "lecciones", luego practica con los ejercicios.',
            'Te recomiendo empezar aprendiendo Python básico, luego explorar las bibliotecas de IA como scikit-learn y TensorFlow.',
            'Comienza con pequeños proyectos y ve aumentando la complejidad. ¡La práctica es clave!'
        ]
    },
    {
        'patrones': [
            'proyecto',
            'proyectos personales',
            'ideas de proyectos',
            'qué proyecto hacer'
        ],
        'respuestas': [
            'Puedes crear un chatbot, un clasificador de imágenes, un analizador de sentimientos, o cualquier idea que te apasione.',
            'Los mejores proyectos son aquellos que resuelven problemas reales o que te interesan personalmente.',
            'Revisa la carpeta "proyectos" para ver ejemplos y la carpeta "ideas" para inspirarte.'
        ]
    },
    {
        'patrones': [
            'ayuda',
            'help',
            'necesito ayuda',
            '¿qué puedes hacer?',
            'qué puedes hacer'
        ],
        'respuestas': [
            'Puedo ayudarte con preguntas sobre Python, IA, Machine Learning y orientarte sobre proyectos.',
            'Pregúntame sobre Python, Inteligencia Artificial, cómo empezar, o ideas para proyectos.',
            'Estoy aquí para responder tus dudas sobre el curso. ¡Pregunta lo que necesites!'
        ]
    },
    {
        'patrones': [
            'gracias',
            'thank you',
            'muchas gracias',
            'te lo agradezco'
        ],
        'respuestas': [
            '¡De nada! Estoy aquí para ayudarte. 😊',
            '¡Un placer ayudarte! Sigue aprendiendo. 🚀',
            '¡Para eso estoy! ¿Necesitas algo más?'
        ]
    },
    {
        'patrones': [
            'nombre',
            '¿cómo te llamas?',
            'tu nombre',
            'quién eres'
        ],
        'respuestas': [
            'Me llamo PyBot, tu asistente para el curso de Python-AI.',
            'Soy PyBot, un chatbot creado como ejemplo para este curso.',
            '¡Soy PyBot! Estoy aquí para ayudarte con Python e IA.'
        ]
    }
]
