# CONTEXTO DEL PROYECTO — Plataforma de Evaluaciones CEG
> Actualizar este archivo al final de cada sesión de desarrollo.

---

## Datos del Programa

| Campo | Valor |
|---|---|
| Nombre | Programa de Formación en Competencia Económica e Inteligencia Artificial |
| Organizadores | Superintendencia de Competencia Económica (SCE) + Colegio de Economistas del Guayas (CEG) |
| Convenio | SCE-CEG-CM-NAC-2024-10 |
| Horario | Martes 14:00–17:00 |
| Duración | 26 may – 23 jun 2026 (5 semanas) |
| Mínimo participantes | 30 personas |

---

## Estructura del Curso

| Semana | Fecha | Módulo | Test |
|---|---|---|---|
| 1 | 26 may 2026 | Módulo 1 — Fundamentos de Competencia Económica | E1 |
| 2 | 02 jun 2026 | Módulo 2 — Inteligencia Artificial Básica para Economistas | E2 |
| 3 | 09 jun 2026 | Módulo 3 — Marco Jurídico de la Competencia en Ecuador | E3 |
| 4 | 16 jun 2026 | Módulo 4 — Herramientas de IA Aplicadas al Análisis | E4 |
| 5 | 23 jun 2026 | Proyecto Final + Clausura | Sin test |

**Nota:** Los temas de cada módulo pueden variar. Las fechas son fijas.

---

## Reglas del Sistema

- **Tests:** 10 preguntas de opción múltiple (A/B/C/D), tiempo límite 60 minutos
- **Nota mínima aprobatoria:** 7.0 / 10.0 por test
- **Acceso participante:** solo con número de cédula (10 dígitos)
- **Certificación requiere:** aprobar los 4 tests + asistencia ≥80% + entregar Proyecto Final
- **Certificado emitido por:** SCE + CEG conjuntamente
- **Solo 1 test activo a la vez** (activar E2 cierra E1 automáticamente)

---

## Perfil Administrador

- **Cédula admin:** `0924209984`
- **Acceso:** solo cédula, sin contraseña
- **Entrada:** botón "Administrador" en el footer del portal
- **Puede:** activar/cerrar tests, cargar participantes.xlsx, cargar preguntas, ver estadísticas, descargar reportes

---

## Estructura de Archivos

```
CEG/
├── data/
│   ├── participantes.xlsx          ← admin sube este archivo (cédula + nombre)
│   ├── test_01_preguntas.xlsx      ← 15 preguntas E1 con respuestas
│   ├── test_02_preguntas.xlsx      ← 15 preguntas E2 con respuestas
│   ├── test_03_preguntas.xlsx      ← 15 preguntas E3 con respuestas
│   ├── test_04_preguntas.xlsx      ← 15 preguntas E4 con respuestas
│   └── resultados.xlsx             ← generado automáticamente
├── prototype/
│   └── index.html                  ← FASE 1: prototipo local completo
├── assets/
│   ├── logo_sce.png
│   └── logo_ceg.png
├── .claude/
│   └── commands/
│       └── inicio.md               ← skill de carga de contexto
├── CONTEXTO_CEG.md                 ← este archivo
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Fases de Desarrollo

| Fase | Descripción | Estado |
|---|---|---|
| 1 | Prototipo HTML local (`prototype/index.html`) — HTML+CSS+JS vanilla, sin servidor | Pendiente |
| 2 | Migración a Streamlit (lee Excel reales de /data/, guarda resultados.xlsx) | Pendiente |
| 3 | Despliegue en GitHub + Streamlit Cloud | Pendiente |

---

## Pantallas del Sistema

### Portal Participante
1. **Inicio / Portal** — tarjetas E1-E4 con estado (PRÓXIMAMENTE / DISPONIBLE / COMPLETADO / CERRADO)
2. **Acceso al test** — ingreso de cédula + instrucciones
3. **Evaluación** — temporizador, 15 preguntas, navegación, progreso
4. **Resultados** — puntaje, APROBADO/REPROBADO, revisión de respuestas

### Panel Administrador
1. **Login** — campo de cédula, validación contra `0924209984`
2. **Dashboard** — tarjetas resumen (inscritos, tests tomados, promedio, elegibles)
3. **Estadísticas por test** — tabla E1-E4 + gráfico distribución de notas
4. **Tabla consolidada** — todos los participantes, notas E1-E4, asistencia (editable), proyecto (editable), estado certificado
5. **Lista elegibles** — solo quienes cumplen los 3 requisitos
6. **Gestión de tests** — activar / cerrar cada test
7. **Gestión de participantes** — cargar/ver participantes.xlsx
8. **Gestión de preguntas** — cargar test_0X_preguntas.xlsx, vista previa antes de activar

### Botones de exportación (siempre visibles en panel admin)
- `resultados_completos.xlsx` — todos los que completaron al menos 1 test
- `elegibles_certificado.xlsx` — solo quienes cumplen los 3 requisitos

---

## Diseño Visual

- **Colores:** azul oscuro `#003366` + dorado `#C8A84B`
- **Fuente mínima:** 16px (texto), 18px (preguntas) — audiencia adulta mayor
- **Botones:** mínimo 44px de alto
- **Idioma:** español (Ecuador), tono formal y profesional
- **Responsive:** funciona en tablets y laptops

---

## Dependencias Técnicas

### Prototipo HTML (Fase 1)
- HTML5 + CSS3 + JavaScript vanilla (sin frameworks)
- **SheetJS (xlsx.js)** desde CDN — única dependencia externa (para exportar Excel)
- `localStorage` para persistencia de sesión y resultados
- Funciona offline, sin instalar nada

### Streamlit (Fase 2)
- Python + Streamlit
- pandas, openpyxl (lectura/escritura de Excel)
- Credenciales admin en `.env` / `secrets.toml`

---

## Registro de Sesiones de Desarrollo

### Sesión 1 — 2026-05-25
- Definición completa del proyecto y requisitos
- Lectura del PDF del programa (Convenio SCE-CEG-CM-NAC-2024-10)
- Creación del prompt definitivo de desarrollo
- Creación de la estructura de carpetas
- Creación de CONTEXTO_CEG.md y skill /inicio
- **Próximo paso:** crear `prototype/index.html` completo con panel admin

### Sesión 2 — 2026-05-25
- Creación de `prototype/index.html` — prototipo Fase 1 completo
- Incluye: portal con 4 tarjetas E1-E4, acceso por cédula, test con temporizador 60 min, pantalla de resultados con revisión de respuestas
- Panel admin completo: login, dashboard KPI, estadísticas con gráfico de barras, tabla consolidada (asistencia y proyecto editables), lista de elegibles, gestión de tests (activar/cerrar), carga de participantes.xlsx via SheetJS, carga de preguntas via Excel, exportación de resultados_completos.xlsx y elegibles_certificado.xlsx
- Funciones demo: botón "Cargar datos de demostración" (5 participantes + preguntas E1) y "Limpiar todos los datos"
- Todo en un solo archivo HTML+CSS+JS, sin servidor, con localStorage
- **Próximo paso:** probar el prototipo abriendo prototype/index.html en el navegador — cargar datos demo, activar E1, rendir test con cédula de prueba, verificar resultados y panel admin

### Sesión 3 — 2026-05-26
- Eliminados logos SCE/CEG del header (eran placeholders de texto)
- Cambiado N_PREGS de 15 a 10 preguntas por test (actualizado en toda la lógica y textos)
- Agregado formulario de registro manual en panel admin → Participantes → "Registrar individualmente" (campos: cédula 10 dígitos obligatorio, primer nombre, segundo nombre, primer apellido, segundo apellido)
- Validación de cédula en tiempo real: bloquea si no son exactamente 10 dígitos numéricos
- Agregada "Guía de archivos" desplegable en Dashboard admin con instrucciones de formato y nombres de archivo
- Actualizado CONTEXTO_CEG.md: tests cambiados a 10 preguntas
- Repositorio GitHub creado (público): joselmatias/plataforma-evaluaciones-ceg
- Creado app.py para despliegue en Streamlit Cloud
- Desplegado en Streamlit Cloud (plataforma-evaluaciones-ceg.streamlit.app)

### Sesión 4 — 2026-05-26
- E1 ahora arranca como 'activo' por defecto (sin necesidad de acción del admin)
- Estado inicial incluye 10 preguntas demo para E1 (visible en Streamlit Cloud en navegadores frescos)
- Pantalla de acceso al test rediseñada: cédula + primer nombre + segundo nombre + primer apellido + segundo apellido
- Botón "Iniciar evaluación" bloqueado hasta que la cédula tenga exactamente 10 dígitos
- Validación en tiempo real: "Faltan X dígito(s)" si cédula < 10; bloquea si no son dígitos
- Auto-registro: si el participante no está en el sistema, se registra automáticamente con los datos ingresados

### Sesión 5 — 2026-05-27
- Corregido: preguntas demo visibles en otros dispositivos — las 10 preguntas reales de E1 se leyeron de Banco_Preguntas_Modulo1.xlsx y se hardcodearon en `defaultPreguntas()`
- `migrateState()` detecta preguntas demo y las reemplaza automáticamente en cualquier dispositivo
- Agregado sistema de PPTs: admin puede cargar hasta 3 URLs por módulo desde el panel → Materiales
- `normalizarSlides()` y `defaultSlides()` gestionan hasta 3 URLs por módulo

### Sesión 6 — 2026-05-28
- Corregido: botones de presentaciones no aparecían en otros dispositivos (mismo root cause que preguntas — localStorage es por navegador)
- Agregada función `defaultSlides()` con las 3 URLs reales de E1 hardcodeadas en el HTML
- `cargar()` usa `defaultSlides()` como fallback cuando `ceg_slides` está vacío
- `migrateState()` detecta si un dispositivo no tiene URLs de E1 y las aplica automáticamente
- **Próximo paso:** cuando el admin tenga las URLs de presentaciones de E2, E3, E4, agregarlas en `defaultSlides()` con el mismo patrón

---
> **INSTRUCCIÓN PARA CLAUDE:** Al final de cada sesión de trabajo, añadir una entrada en "Registro de Sesiones de Desarrollo" con la fecha, lo que se hizo y el próximo paso pendiente.
