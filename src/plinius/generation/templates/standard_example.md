# {{projectTitle}}

**Fecha de Creación o Última Actualización:** {{creationDate}}

**Autor(es):** {{authors}}

## Tabla de Contenidos

- [Introducción](#introduction)
- [Arquitectura del Sistema](#systemArchitecture)
- [API y Documentación del Código](#apiDocumentation)
- [Configuración Avanzada](#advancedConfiguration)
- [Glosario](#glossary) (Opcional)
- [Referencias](#references)
- [Licencia](#license)

## Introducción

{{projectIntroduction}}

## Arquitectura del Sistema

{{systemArchitectureDescription}}

## API y Documentación del Código

{{apiDocumentationDetails}}

### Resumen de Endpoints

- **Envío de CFE:** {{sendCFEDescription}}
- **Consulta de CFE:** {{queryCFEDescription}}

### Autenticación

{{authenticationDetails}}

### Errores Comunes

{{commonErrors}}

### Clases Principales

#### Core

- **PFacturasUY:** La clase `PFacturasUY` es el núcleo del sistema de facturación electrónica `pFacturasUY`. Se encarga de la generación, envío y gestión de los Comprobantes Fiscales Electrónicos (CFE) conforme a las regulaciones y estándares establecidos. Esta clase integra diversas funcionalidades, incluyendo la preparación de la información del documento fiscal, la validación de la configuración del sistema, la comunicación con la API de PFacturasUY para el envío de CFEs, y el procesamiento de las respuestas recibidas. Utiliza una serie de servicios y utilidades internas para llevar a cabo estas tareas, asegurando que los documentos fiscales se generen, envíen y gestionen de manera eficiente y conforme a los requisitos legales y de negocio.
**PFacturasUYProcessing:** La clase `PFacturasUYProcessing` se encarga del procesamiento posterior de los Comprobantes Fiscales Electrónicos (CFE) dentro del sistema `pFacturasUY`. Su principal responsabilidad es manejar la consulta de estados de los CFEs enviados, asegurando que se realice un seguimiento adecuado de cada documento fiscal emitido. Esta clase interactúa con servicios como `ConfigurationService`, `InvoiceService`, `DocumentService`, y `NotificationService` para recuperar configuraciones específicas del cliente, obtener detalles de facturas almacenadas, gestionar documentos relacionados y enviar notificaciones correspondientes. Además, implementa métodos para procesar mensajes de una cola de mensajes, validando la integridad de las facturas y configuraciones antes de realizar consultas de estado en el servicio de facturación electrónica. Su funcionalidad es crítica para garantizar la fiabilidad y la trazabilidad de las transacciones fiscales electrónicas dentro del sistema.

#### Entidades

- **Adenda:** La Adenda es un elemento opcional en los documentos de facturación electrónica que permite incluir información adicional relevante para el emisor o el receptor del documento. Puede contener notas, términos y condiciones, o cualquier otro texto informativo que se considere importante adjuntar al CFE. La estructura de `Adenda` incluye uno o más `AdendaItem`, cada uno identificado por un `Id` único y conteniendo el texto (`Texto`) de la adenda.
- **CAE:** La Autorización de Comprobantes Electrónicos (CAE) es un código esencial en el sistema de facturación electrónica, emitido por la autoridad fiscal para autorizar la emisión de un Comprobante Fiscal Electrónico (CFE). Incluye detalles como la autorización, la serie, y las fechas de validez, asegurando la conformidad de los documentos con los requisitos legales.
- **CFE:** {{CFEDescription}}
- **Cobranza:** {{CobranzaDescription}}
- **Emisor:** {{EmisorDescription}}
- **Receptor:** {{ReceptorDescription}}
- **Documento:** {{DocumentoDescription}}
- **Detalle y DetalleItem:** {{DetalleDescription}}

#### Enums

- **InvoiceType:** {{InvoiceTypeDescription}}

#### Errores

- **PFacturasError:** {{PFacturasErrorDescription}}

#### Tipos

- **EnviarCFEOut:** {{EnviarCFEOutDescription}}

#### Utils

- **getCFEType:** {{getCFETypeDescription}}
- **parseStringXml:** {{parseStringXmlDescription}}
- **validateConfiguration:** {{validateConfigurationDescription}}
- **validateIncrementData:** {{validateIncrementDataDescription}}

### Ejemplos de Código

#### Envío de CFE

```javascript
{{sendCFEExample}}
```

### Consulta de Estado de CFE

```javascript
{{queryCFEExample}}
```
### Pruebas y Validación

{{testingAndValidationDetails}}

## Configuración Avanzada (si es aplicable)

{{advancedConfigurationDetails}}

## Glosario (Opcional)

{{glossaryDefinitions}}

## Referencias

{{referencesLinks}}

## Licencia

{{licenseInfo}}
