# Análisis del sistema de pagos

Aunque el servicio externo actual es un mock, el flujo presenta los siguientes problemas que podrían afectar la eficiencia, confiabilidad y trazabilidad del procesamiento de pagos al integrarlo con servicios reales.

## Problemas encontrados

1. **Instanciación en cada solicitud:** se crea una nueva instancia de `PaymentService` por cada request.
2. **Ausencia de validaciones de negocio:** no se verifica que `amount` sea mayor que cero ni que `currency` pertenezca a una lista de monedas válidas.
3. **Ausencia de manejo de errores:** si `ExternalService.call()` lanza una excepción, esta se propaga y la solicitud falla sin una respuesta controlada.
4. **Ausencia de reintentos:** una llamada fallida al servicio externo no se vuelve a intentar, incluso cuando el error podría ser transitorio.
5. **Ausencia de logging:** no se registran las etapas del procesamiento ni los errores, por lo que no existe trazabilidad sobre lo ocurrido durante una transacción.

## Mejoras propuestas

1. **Inyectar `PaymentService`:** administrar su creación mediante una instancia compartida o una factory, en lugar de instanciarlo directamente en cada request.
2. **Fortalecer las validaciones:** exigir que `amount` sea mayor que cero y validar `currency` contra una lista de monedas permitidas.
3. **Agregar manejo de excepciones:** capturar los errores del servicio externo y devolver respuestas controladas según el tipo de fallo.
4. **Implementar reintentos:** reintentar errores transitorios mediante backoff exponencial y un límite de intentos.
5. **Agregar logging:** registrar cada etapa relevante del flujo y sus errores para facilitar el monitoreo y diagnóstico de las transacciones.
