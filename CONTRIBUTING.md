# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a Python-AI! Este documento te guiará sobre cómo compartir tu proyecto personal o mejorar el material del curso.

## Cómo Contribuir

### 1. Compartir tu Proyecto Personal

Si has desarrollado un proyecto personal y quieres compartirlo con la comunidad:

1. **Fork este repositorio**
   ```bash
   # Haz clic en el botón "Fork" en GitHub
   ```

2. **Clona tu fork**
   ```bash
   git clone https://github.com/TU_USUARIO/Python-AI.git
   cd Python-AI
   ```

3. **Crea una rama para tu proyecto**
   ```bash
   git checkout -b proyecto/nombre-de-tu-proyecto
   ```

4. **Agrega tu proyecto**
   - Crea una carpeta en `proyectos/` con un nombre descriptivo
   - Incluye un README.md completo
   - Asegúrate de que tu código esté bien documentado
   - Incluye un `requirements.txt` si tu proyecto tiene dependencias específicas

5. **Estructura mínima de tu proyecto**
   ```
   proyectos/tu-proyecto/
   ├── README.md              # Descripción completa del proyecto
   ├── src/                   # Código fuente
   │   └── main.py
   ├── requirements.txt       # Dependencias (si aplica)
   └── results/               # Resultados o ejemplos de salida
   ```

6. **Commit tus cambios**
   ```bash
   git add proyectos/tu-proyecto/
   git commit -m "Agrego proyecto: [Nombre del Proyecto]"
   ```

7. **Push a tu fork**
   ```bash
   git push origin proyecto/nombre-de-tu-proyecto
   ```

8. **Crea un Pull Request**
   - Ve a tu fork en GitHub
   - Haz clic en "New Pull Request"
   - Describe tu proyecto y qué aprendiste desarrollándolo

### 2. Mejorar Material del Curso

Si quieres contribuir con lecciones, ejercicios o ejemplos:

1. Sigue los mismos pasos 1-3 de arriba
2. Agrega o modifica el contenido en la carpeta correspondiente
3. Asegúrate de seguir el formato existente
4. Commit y crea un Pull Request

### 3. Reportar Errores o Sugerir Mejoras

Si encuentras un error o tienes una sugerencia:

1. Abre un Issue en GitHub
2. Describe el problema o sugerencia claramente
3. Incluye ejemplos si es posible

## Estándares de Calidad

Para mantener la calidad del repositorio, asegúrate de:

### Código
- ✅ El código debe ser legible y estar bien comentado
- ✅ Sigue las convenciones de Python (PEP 8)
- ✅ Incluye manejo de errores básico
- ✅ Evita dependencias innecesarias

### Documentación
- ✅ README completo con descripción, instalación y uso
- ✅ Comentarios en el código donde sea necesario
- ✅ Ejemplo de uso o resultado
- ✅ Texto en español (salvo nombres técnicos)

### Proyecto Personal
- ✅ Debe estar funcional y probado
- ✅ Incluye una descripción de qué aprendiste
- ✅ Explica los desafíos que enfrentaste
- ✅ Comparte insights y lecciones aprendidas

## Plantilla para README de Proyecto

```markdown
# Nombre del Proyecto

## 📝 Descripción
[Descripción breve de qué hace tu proyecto]

## 🎯 Motivación
[Por qué decidiste crear este proyecto]

## 🛠️ Tecnologías Utilizadas
- Python 3.x
- [Biblioteca 1]
- [Biblioteca 2]

## 📦 Instalación

\```bash
pip install -r requirements.txt
\```

## 🚀 Uso

\```python
# Ejemplo de cómo usar tu proyecto
python src/main.py
\```

## 📊 Resultados
[Describe los resultados obtenidos, incluye imágenes si aplica]

## 🧠 Aprendizajes
[Qué aprendiste desarrollando este proyecto]

## 🔮 Próximos Pasos
[Mejoras futuras que planeas implementar]

## 👤 Autor
[Tu nombre o usuario de GitHub]

## 📄 Licencia
[Tipo de licencia, si aplica]
```

## Proceso de Revisión

1. Revisaremos tu Pull Request
2. Podríamos sugerir cambios o mejoras
3. Una vez aprobado, tu contribución será integrada
4. ¡Tu proyecto será parte de la comunidad!

## Código de Conducta

- Sé respetuoso con todos los miembros de la comunidad
- Acepta críticas constructivas
- Ayuda a otros cuando puedas
- Comparte conocimiento generosamente
- Celebra los logros de otros

## ¿Preguntas?

Si tienes preguntas sobre cómo contribuir:
- Abre un Issue en GitHub
- Etiquétalo como "pregunta"
- La comunidad estará encantada de ayudarte

---

¡Gracias por contribuir al curso de Python-AI! 🎉
