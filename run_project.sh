#!/bin/bash

echo "🛠️  Paso 1: Construyendo contenedores con Docker Compose..."
docker compose up -d --build

echo "⏳ Esperando que la API esté disponible en http://localhost:8000 ..."
for i in {1..30}; do
    if curl -s http://localhost:8000/docs > /dev/null; then
        echo "✅ API disponible"
        break
    fi
    sleep 2
done

echo "🌐 Abriendo documentación Swagger en el navegador..."
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open http://localhost:8000/docs
elif command -v open >/dev/null 2>&1; then
  open http://localhost:8000/docs
elif command -v start >/dev/null 2>&1; then
  start http://localhost:8000/docs
else
  echo "⚠️ No se pudo abrir el navegador automáticamente. Abre manualmente: http://localhost:8000/docs"
fi

echo "✅ Contenedores corriendo. Ejecutando pruebas..."
docker compose exec api pytest tests/

echo "🎉 Todo listo."
