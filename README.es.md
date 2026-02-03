<div align="center">

# 🎓 Descargador de Currículum Lattes CNPq

**Herramienta automatizada para descargar currículums Lattes de CNPq con bypass de reCAPTCHA**

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green?logo=flask)](https://flask.palletsprojects.com/)
[![2Captcha](https://img.shields.io/badge/2Captcha-API-orange)](https://2captcha.com/)
[![Licencia](https://img.shields.io/badge/Licencia-Propietaria-red)](LICENSE)

[Características](#-características-principales) • [Inicio Rápido](#-inicio-rápido) • [Instalación](#-instalación) • [Configuración](#%EF%B8%8F-configuración) • [Uso](#-uso) • [Licencia](#-licencia)

**Idiomas:** [🇺🇸 English](README.md) • [🇧🇷 Português](README.pt-BR.md)

</div>

---

## 📋 Índice

- [Descripción General](#-descripción-general)
- [Sobre el Desarrollador](#-sobre-el-desarrollador)
- [Características Principales](#-características-principales)
- [Stack Tecnológico](#%EF%B8%8F-stack-tecnológico)
- [Inicio Rápido](#-inicio-rápido)
- [Instalación](#-instalación)
- [Configuración](#%EF%B8%8F-configuración)
- [Uso](#-uso)
- [Despliegue como Servicio](#-despliegue-como-servicio)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Licencia](#-licencia)
- [Aviso Legal](#%EF%B8%8F-aviso-legal)

---

## 🎯 Descripción General

El **Descargador de Currículum Lattes CNPq** es una herramienta automatizada diseñada para descargar currículums vitae de la Plataforma Lattes de CNPq. El sistema evita automáticamente la protección reCAPTCHA utilizando el servicio 2Captcha, permitiendo una extracción de currículums eficiente y sin interrupciones.

**Capacidades principales:**
- Resolución automática de reCAPTCHA con integración 2Captcha
- Interfaz web Flask para descargas fáciles de currículums
- Gestión de cookies para control de sesiones
- Extracción automática de currículums en XML
- Sistema de almacenamiento local para archivos descargados
- Script de línea de comandos para procesamiento por lotes
- Soporte de servicio systemd para despliegue en producción

**Perfecto para:**
- Investigadores académicos
- Departamentos de RRHH
- Proyectos de recopilación de datos
- Análisis académico
- Instituciones de investigación

---

## 👨‍💻 Sobre el Desarrollador

<div align="center">

**Desarrollado por Rafael Vieira (TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

**Desarrollador Full-Stack & Especialista en Automatización**

Especializado en **web scraping**, **sistemas de automatización**, **desarrollo de bots** y **soluciones de bypass de reCAPTCHA**.

### 💼 Experiencia Principal

- 🔍 Web Scraping & Extracción de Datos
- 🤖 Desarrollo de Bots & Automatización
- 🛡️ Soluciones de Bypass de CAPTCHA
- 💻 Desarrollo Full-Stack (Python, Flask, Next.js, React)
- ⚡ Automatización de Procesos & Flujos de Trabajo
- 📊 Procesamiento & Análisis de Datos

### 🌍 Idiomas

🇺🇸 **English** • 🇧🇷 **Português** • 🇪🇸 **Español**

### 📬 Contacto

**Email**: [contact@techbe.me](mailto:contact@techbe.me)

</div>

---

## ✨ Características Principales

### 🔐 Bypass de reCAPTCHA
- Resolución automática de reCAPTCHA usando API 2Captcha
- Alta tasa de éxito con generación confiable de tokens
- Manejo de errores y mecanismos de reintento

### 🌐 Interfaz Web
- Interfaz web limpia e intuitiva basada en Flask
- Estado de descarga en tiempo real
- Entrada de ID de currículum mediante formulario
- Servir archivos automáticamente

### 💾 Gestión de Almacenamiento
- Almacenamiento automático de archivos locales en la carpeta `resumes/`
- Caché de archivos para evitar descargas duplicadas
- Extracción de currículums XML de archivos ZIP
- Nomenclatura organizada de archivos con ID Lattes

### 🔄 Uso Flexible
- Interfaz web con Flask (`run.py`)
- Script de línea de comandos (`cnpq.py`)
- Interfaz web alternativa (`render.py`)
- Servicio systemd para despliegue en producción

### 📝 Registro de Actividad
- Sistema de registro integral
- Seguimiento de información de depuración
- Informes de errores y monitoreo

---

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Propósito |
|------------|---------|----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.7+ | Lenguaje de programación principal |
| **Flask** | 3.0+ | Framework web para interfaz |
| **2Captcha** | Más reciente | Servicio de resolución de reCAPTCHA |
| **Requests** | Más reciente | Cliente HTTP para peticiones web |
| **Gunicorn** | Más reciente | Servidor HTTP WSGI para producción |

---

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.7 o superior
- Clave API de 2Captcha ([Obtén una aquí](https://2captcha.com/))
- ID Lattes de CNPq (número de 16 dígitos)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/TechBeme/cnpq.git
cd cnpq
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar

Copiar `config.ini.example` a `config.ini` y agregar tus credenciales:

```ini
[DEFAULT]
recaptcha_key = 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

[TWOCAPTCHA]
API_KEY = tu_clave_api_2captcha_aqui
```

### 4. Ejecutar la Interfaz Web

```bash
python run.py
```

Accede a la aplicación en `http://localhost:5000`

---

## 📦 Instalación

### Opción 1: Instalación Estándar

```bash
# Clonar repositorio
git clone https://github.com/TechBeme/cnpq.git
cd cnpq

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar
cp config.ini.example config.ini
# Editar config.ini con tus credenciales

# Ejecutar
python run.py
```

### Opción 2: Despliegue en Producción

```bash
# Instalar y configurar como arriba
# Luego configurar servicio systemd

sudo cp cnpq.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cnpq
sudo systemctl start cnpq
sudo systemctl status cnpq
```

---

## ⚙️ Configuración

### config.ini

Crear un archivo `config.ini` basado en `config.ini.example`:

```ini
[DEFAULT]
# Clave del sitio reCAPTCHA de CNPq (generalmente esta)
recaptcha_key = 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

[TWOCAPTCHA]
# Tu clave API de 2Captcha
API_KEY = tu_clave_api_2captcha_aqui
```

### Obtener tu Clave API de 2Captcha

1. Regístrate en [2Captcha](https://2captcha.com/)
2. Navega a tu panel de control
3. Copia tu clave API
4. Pégala en el archivo `config.ini`

### Encontrar IDs Lattes

Los IDs Lattes son números de 16 dígitos que se encuentran en las URLs de currículums Lattes de CNPq:

```
http://lattes.cnpq.br/1234567890123456
                      ^^^^^^^^^^^^^^^^
                         ID Lattes
```

---

## 🎮 Uso

### Interfaz Web (Recomendado)

1. Iniciar el servidor Flask:
   ```bash
   python run.py
   ```

2. Abre tu navegador y ve a `http://localhost:5000`

3. Ingresa el ID Lattes (16 dígitos)

4. Haz clic en "Download"

5. El archivo XML se descargará automáticamente

**Nota:** Los archivos descargados se almacenan en la carpeta `resumes/` con el formato `{id_lattes}.xml`

### Script de Línea de Comandos

Para descargas individuales sin la interfaz web:

```bash
python cnpq.py
```

**Nota:** Edita el script para establecer el ID Lattes deseado antes de ejecutar.

### Interfaz Web Alternativa

Una versión simplificada sin registro o caché:

```bash
python render.py
```

---

## 🚀 Despliegue como Servicio

### Servicio Systemd (Linux)

El archivo `cnpq.service` incluido permite ejecutar la aplicación como un servicio systemd.

**Instalación:**

```bash
# Copiar archivo de servicio
sudo cp cnpq.service /etc/systemd/system/

# Actualizar rutas en el archivo de servicio si es necesario
sudo nano /etc/systemd/system/cnpq.service

# Recargar systemd
sudo systemctl daemon-reload

# Habilitar servicio (iniciar al arrancar)
sudo systemctl enable cnpq

# Iniciar servicio
sudo systemctl start cnpq

# Verificar estado
sudo systemctl status cnpq
```

**Comandos de Gestión:**

```bash
# Iniciar
sudo systemctl start cnpq

# Detener
sudo systemctl stop cnpq

# Reiniciar
sudo systemctl restart cnpq

# Ver registros
sudo journalctl -u cnpq -f
```

---

## 📁 Estructura del Proyecto

```
cnpq/
├── cnpq.py               # Script de línea de comandos
├── run.py                # Aplicación Flask principal con registro
├── render.py             # Aplicación Flask alternativa
├── config.ini.example    # Plantilla de configuración
├── config.ini            # Tu configuración (ignorada por git)
├── cnpq.service          # Archivo de servicio systemd
├── requirements.txt      # Dependencias de Python
├── templates/
│   └── index.html        # Plantilla de interfaz web
├── resumes/              # Archivos de currículum descargados
└── cnpq.log              # Registros de aplicación
```

---

## 📝 Licencia

**Licencia Propietaria - Todos los Derechos Reservados**

Copyright © 2026 Rafael Vieira (TechBeme)

### ❌ Restricciones

- **Sin uso comercial** sin permiso explícito
- **Sin modificaciones** o trabajos derivados
- **Sin distribución** o sublicencia
- **Sin ingeniería inversa**
- **Sin alojamiento público** sin autorización

### ✅ Uso Permitido

- Ver código fuente con fines educativos
- Ejecutar para uso personal y de investigación no comercial
- Fork para estudio personal únicamente (no para distribución)

### 📧 Licenciamiento Comercial

Para uso comercial, soluciones white-label o desarrollo personalizado:

**Contacto:** [contact@techbe.me](mailto:contact@techbe.me)

---

## ⚠️ Aviso Legal

Esta herramienta se proporciona **únicamente con fines educativos y de investigación**.

- Este proyecto es **independiente** y **NO está afiliado** con CNPq o el gobierno brasileño
- Los usuarios son responsables del cumplimiento de los Términos de Servicio de CNPq
- Recopila solo datos disponibles públicamente
- Limitación de tasa integrada para respetar los recursos del servidor
- Los usuarios deben cumplir con las leyes de protección de datos aplicables (LGPD, GDPR, etc.)
- El desarrollador no es responsable del mal uso de esta herramienta

**Use con responsabilidad y ética.**

---

## 🙏 Agradecimientos

Construido con:
- [Flask](https://flask.palletsprojects.com/) - Framework web
- [2Captcha](https://2captcha.com/) - Servicio de resolución de reCAPTCHA
- [Requests](https://requests.readthedocs.io/) - Biblioteca HTTP
- [Gunicorn](https://gunicorn.org/) - Servidor HTTP WSGI

---

<div align="center">

**Desarrollado por [Rafael Vieira](https://github.com/TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

</div>
