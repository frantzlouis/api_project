# Contact Management API

Este proyecto implementa una solución completa de ingesta de datos desde un servidor CentOS a una base de datos PostgreSQL, y una API REST para exponer esos datos.

## Componentes

- **PostgreSQL**: Base de datos relacional.
- **FastAPI**: Framework para construir la API REST.
- **CentOS**: Nodo para procesamiento/ingesta de datos.
- **Docker**: Entorno contenerizado y reproducible.
- **CI/CD**: GitHub Actions para testing y despliegue.

Endpoints

- `GET /contacts/`: Lista de contactos con información de su empresa asociada.

Visita [http://localhost:8000/docs](http://localhost:8000/docs) para probar la API.


Cómo ejecutar este proyecto
1. Clonar el repositorio

```bash
git clone https://github.com/frantzlouis/api_project.git
cd <api_project>
```

---

2. Ejecutar el proyecto con Docker

```bash
chmod +x run.sh
./run.sh
```

Este script:
- Detiene contenedores anteriores
- Limpia imágenes viejas (si existen)
- Construye todos los servicios desde cero:
  - `db`: PostgreSQL
  - `centos`: Ingesta de datos
  - `api`: API REST con FastAPI

---

3. Verificar que la API esté corriendo

Abre en tu navegador:

[http://localhost:8000/docs](http://localhost:8000/docs)

---

4. Ejecutar los tests localmente (opcional)

```bash
pip install pytest requests
pytest tests/
```

O dentro del contenedor Docker:

```bash
docker exec $(docker ps -qf "name=api") pytest /app/tests/
```

---

5. CI/CD con GitHub Actions

Este proyecto incluye un pipeline de CI en:

```
.github/workflows/python-app.yml
```

Se ejecutan tests automáticamente en cada push o pull request a `main`.

---

Requisitos

- Docker + Docker Compose
- Python 3.10+ (solo si usas pytest local)
- Puertos 8000 y 5432 libres
