# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced

### Brecha de conocimiento
Ha trabajado con algún asistente AI en desarrollo (Amazon Q Dev, Kiro, Github Copilot) y lo utiliza en su día a día como desarrollador. Candidato con experiencia avanzada en backend, familiarizado con herramientas de desarrollo asistidas por IA.

### Reto
- Tema: Desarrollo
- Seniority: advanced-l2
- Tipo: practical
- Título: Optimización de Procesamiento de Pagos en Fintech
- Tiempo estimado: 4-6 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Análisis del Sistema Actual — objetivo: Identificar las causas de las transacciones fallidas y proponer mejoras. — entregable (NO resolver): Informe de análisis con propuestas de mejora.
- Fase 2: Implementación de Mejoras — objetivo: Implementar las mejoras propuestas para reducir las transacciones fallidas. — entregable (NO resolver): Sistema de procesamiento de pagos optimizado.
- Fase 3: Evaluación y Documentación — objetivo: Evaluar el impacto de las mejoras y documentar el proceso. — entregable (NO resolver): Informe de evaluación y documentación del proceso.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

import httpx
from fastapi import FastAPI
from pydantic import BaseModel
from src.application.services import PaymentService

app = FastAPI()

class PaymentRequest(BaseModel):
    amount: float
    currency: str

@app.post('/process-payment')
async def process_payment(payment: PaymentRequest):
    service = PaymentService()
    return await service.process(payment)

// === ARCHIVO: src/domain/entities.py ===
from pydantic import BaseModel

class Payment(BaseModel):
    amount: float
    currency: str

// === ARCHIVO: src/application/services.py ===
from src.domain.entities import Payment
from src.infrastructure.repositories import PaymentRepository
from src.infrastructure.external_services import ExternalService

class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()
        self.external_service = ExternalService()

    async def process(self, payment: Payment):
        # Simulate validation and external service call
        validated_payment = await self.validate(payment)
        result = await self.external_service.call(validated_payment)
        return result

    async def validate(self, payment: Payment):
        # Simulate validation logic
        return payment

// === ARCHIVO: src/infrastructure/repositories.py ===
class PaymentRepository:
    async def save(self, payment: Payment):
        # Simulate saving to database
        return payment

// === ARCHIVO: src/infrastructure/external_services.py ===
class ExternalService:
    async def call(self, payment: Payment):
        # Simulate external service call
        return {"status": "success", "payment": payment.dict()}

// === ARCHIVO: tests/test_services.py ===
from src.application.services import PaymentService
from src.domain.entities import Payment

def test_process_payment():
    service = PaymentService()
    payment = Payment(amount=100.0, currency='USD')
    result = service.process(payment)
    assert result['status'] == 'success'

// === ARCHIVO: docs/analysis_report.md ===
# Informe de Análisis

## Propuestas de Mejora
- Mejorar la validación de datos en múltiples etapas.
- Implementar reintentos inteligentes para llamadas a servicios externos.

// === ARCHIVO: docs/evaluation_report.md ===
# Informe de Evaluación

## Documentación del Proceso
- Se aplicaron mejoras en la validación y reintentos.
- Se evaluó el impacto en la tasa de transacciones exitosas.

// === ARCHIVO: pyproject.toml ===
[tool.poetry]
name = "fintech-payment-system"
version = "0.1.0"
description = "A fintech payment processing system."
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "0.115.0"
pydanticv2 = "2.0.0"
httpx = "0.26.0"
pytest = "7.4.0"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

```
