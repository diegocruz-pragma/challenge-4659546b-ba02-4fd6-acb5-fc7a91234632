# Optimización de Procesamiento de Pagos en Fintech

Una empresa fintech necesita optimizar su sistema de procesamiento de pagos. El sistema actual tiene una alta tasa de transacciones fallidas debido a errores de validación y latencia en la comunicación con servicios externos. El objetivo es mejorar la eficiencia y confiabilidad del procesamiento de pagos.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Desarrollo |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-6 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Análisis del Sistema Actual

**Objetivo:** Identificar las causas de las transacciones fallidas y proponer mejoras.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Investiga el flujo actual de procesamiento de pagos.
- Identifica las etapas donde ocurren más fallos y las posibles causas.

**Entregable:** Informe de análisis con propuestas de mejora.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la validación de datos en múltiples etapas.
- Evalúa la latencia en las llamadas a servicios externos.

</details>

### Fase 2: Implementación de Mejoras

**Objetivo:** Implementar las mejoras propuestas para reducir las transacciones fallidas.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Aplica las mejoras identificadas en la fase anterior.
- Realiza pruebas para asegurar que las mejoras son efectivas.

**Entregable:** Sistema de procesamiento de pagos optimizado.

<details>
<summary>Pistas de conocimiento</summary>

- Usa estrategias de validación en cascada.
- Implementa reintentos inteligentes para llamadas a servicios externos.

</details>

### Fase 3: Evaluación y Documentación

**Objetivo:** Evaluar el impacto de las mejoras y documentar el proceso.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Evalúa el impacto de las mejoras en la tasa de transacciones exitosas.
- Documenta el proceso de implementación y las decisiones tomadas.

**Entregable:** Informe de evaluación y documentación del proceso.

<details>
<summary>Pistas de conocimiento</summary>

- Usa métricas para evaluar el impacto de las mejoras.
- Documenta las decisiones y trade-offs considerados.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es el procesamiento de pagos y por qué es importante en una fintech?
- **paraQueSirve**: ¿Para qué sirve la validación en cascada en el procesamiento de pagos?
- **comoSeUsa**: ¿Cómo se pueden implementar reintentos inteligentes para reducir la latencia en llamadas a servicios externos?
- **erroresComunes**: ¿Cuáles son los errores comunes en el procesamiento de pagos y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica la optimización del procesamiento de pagos y cuáles son los trade-offs considerados?

## Criterios de Evaluacion

- Identificar causas de transacciones fallidas.
- Proponer y aplicar mejoras en el procesamiento de pagos.
- Evaluar el impacto de las mejoras y documentar el proceso.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
