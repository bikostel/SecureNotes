🔐 SecureNotes – Plataforma de Notas Cifradas

Proyecto académico de desarrollo seguro, despliegue en contenedores y monitorización avanzada

SecureNotes es una aplicación web creada para demostrar la implementación real de buenas prácticas de Desarrollo Seguro (DevSecOps) dentro de un entorno moderno.
Incluye cifrado de notas, autenticación segura, despliegue con Docker, proxy inverso con NGINX, análisis estático/dinámico, monitorización y detección de incidentes.

Este proyecto nace como práctica académica del curso de Puesta y Producción Segura, extendido con mejoras profesionales para simular un entorno real de producción.

📌 Características Principales

📝 Notas cifradas con claves gestionadas de forma segura.

🔐 Autenticación segura con hashing robusto de contraseñas.

⚙️ API en FastAPI, ligera, rápida y validada.

🐳 Despliegue con Docker y Docker Compose.

🔁 NGINX como reverse proxy, con certificados propios en /certs.

📦 Gestión de secretos mediante variables de entorno.

🛡️ Hardening del sistema y contenedores.

🧪 Análisis de seguridad:

Bandit (SAST)

Flake8 (estilo y calidad)

Trivy (escaneo de imágenes Docker)

Safety (dependencias vulnerables)

Gitleaks (detección de secretos filtrados)

🚀 CI/CD con GitHub Actions automatizando tests, análisis y build.

📊 Monitorización con Prometheus + Grafana.

📜 Logging unificado con Loki.

🚨 Alertas de eventos anómalos (intentos de login fallidos, errores, etc.)

🔥 Simulación real de incidente por fuga de credenciales en Git.

📂 Arquitectura del Proyecto
SecureNotes/
 ├── backend/
 │    ├── app.py
 │    ├── routes/
 │    ├── models/
 │    ├── security/
 │    ├── crypto/
 │    └── requirements.txt
 ├── nginx/
 │    ├── nginx.conf
 │    └── certs/
 ├── prometheus/
 │    └── prometheus.yml
 ├── grafana/
 ├── docker-compose.yml
 ├── Dockerfile
 └── README.md

🔧 Tecnologías Utilizadas

Python 3 + FastAPI

Docker / Docker Compose

NGINX reverse proxy

SQLite (entorno académico)

Prometheus + Grafana

Loki

GitHub Actions

OpenSSL para gestionar certificados

🚀 Instalación y Puesta en Marcha
1️⃣ Clonar repositorio
git clone https://github.com/tuusuario/SecureNotes.git
cd SecureNotes

2️⃣ Construir y levantar contenedores
docker compose up --build


Servicios disponibles:

Backend → http://localhost:8000

NGINX (proxy) → https://localhost

Prometheus → http://localhost:9090

Grafana → http://localhost:3000

Loki → acceso interno

🔐 Seguridad y Cifrado

Notas cifradas antes de almacenarse.

Gestión de claves a través de variables de entorno (SECRET_KEY).

Contraseñas de usuarios protegidas con hashing robusto.

Validaciones y sanitización a nivel de API.

Hardening del backend y del reverse proxy.

Eliminación de secretos expuestos tras análisis con Gitleaks.

📊 Monitorización y Detección de Incidentes

SecureNotes expone métricas para Prometheus (ej: http_requests_total).
En Grafana se configuró un panel que incluye:

peticiones al backend

endpoints más usados

tiempos de respuesta

errores 4xx / 5xx

alertas en tiempo real

Además, se creó una alerta que detecta:

🚨 "FallosLoginRepetidos"

Se dispara cuando hay múltiples errores 401 en /auth/login en un intervalo corto.

🔥 Simulación de Incidente

Para el punto 5 del proyecto se simuló una fuga de credenciales detectada con Gitleaks:

2 SECRET_KEY antiguos filtrados

1 clave privada comprometida

Se documentó:

detección

contención

rotación de claves

lecciones aprendidas

🧪 CI/CD Automatizado (GitHub Actions)

Cada push ejecuta:

✔ flake8

✔ bandit

✔ pytest

✔ trivy (imágenes Docker)

✔ build de contenedor

✔ validación antes del despliegue

📜 Licencia

Licencia MIT.

👥 Autores

Sergio Izquierdo Planells

Compañero de equipo (nombre real si quieres ponerlo)

🔗 Repositorio

👉 (aquí pones tu link)
