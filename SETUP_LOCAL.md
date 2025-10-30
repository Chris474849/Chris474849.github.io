# 🔧 Guía de Setup Local - DY Prods Vue.js

Esta guía te ayudará a configurar el proyecto localmente paso a paso, incluyendo soluciones a problemas comunes.

## 📋 Prerrequisitos

### Node.js
- **Versión mínima**: Node.js 18.0.0 o superior
- **Versión recomendada**: Node.js 18.x LTS o 20.x LTS
- **Descargar**: https://nodejs.org/

#### Verificar versión instalada
```bash
node --version
npm --version
```

Si tienes una versión anterior a 18.0.0, actualiza Node.js antes de continuar.

## 🚀 Instalación Paso a Paso

### 1. Clonar el repositorio
```bash
git clone https://github.com/Chris474849/Chris474849.github.io.git
cd Chris474849.github.io
```

### 2. Cambiar a la rama de desarrollo
```bash
git checkout develop
```

### 3. Navegar a la carpeta del frontend
```bash
cd frontend
```

### 4. Limpiar caché de npm (recomendado)
```bash
npm cache clean --force
```

### 5. Instalar dependencias
```bash
npm install
```

### 6. Ejecutar el proyecto
```bash
npm run dev
```

El sitio estará disponible en: `http://localhost:5173/`

## ❌ Problemas Comunes y Soluciones

### Error: "node: not found" o "npm: not found"
**Problema**: Node.js no está instalado o no está en el PATH
**Solución**:
1. Descargar e instalar Node.js desde https://nodejs.org/
2. Reiniciar la terminal/command prompt
3. Verificar instalación: `node --version`

### Error: "Unsupported engine"
**Problema**: Tu versión de Node.js es muy antigua
**Solución**:
1. Actualizar Node.js a la versión 18.0.0 o superior
2. O usar nvm para gestionar versiones de Node:
   ```bash
   # Windows (con nvm-windows)
   nvm install 18.17.0
   nvm use 18.17.0
   
   # macOS/Linux
   nvm install 18.17.0
   nvm use 18.17.0
   ```

### Error: "permission denied" o "EACCES"
**Problema**: Permisos insuficientes para instalar paquetes
**Solución**:

#### Windows:
```bash
# Ejecutar terminal como administrador
npm install
```

#### macOS/Linux:
```bash
# Cambiar permisos de npm
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}

# O usar npm con --unsafe-perm
npm install --unsafe-perm
```

### Error: "network timeout" o "registry error"
**Problema**: Problemas de conectividad con npm registry
**Solución**:
```bash
# Cambiar a registry oficial
npm config set registry https://registry.npmjs.org/

# Limpiar caché y reinstalar
npm cache clean --force
npm install
```

### Error: "peer dependency warnings"
**Problema**: Advertencias sobre dependencias peer (generalmente no crítico)
**Solución**:
```bash
# Instalar con --legacy-peer-deps si hay conflictos
npm install --legacy-peer-deps

# O ignorar warnings (si no afectan funcionalidad)
npm install --no-fund --no-audit
```

### Error: "Port 5173 is already in use"
**Problema**: El puerto ya está ocupado por otra aplicación
**Solución**:
```bash
# Vite automáticamente intentará el siguiente puerto disponible
# O especificar un puerto diferente
npm run dev -- --port 3000
```

### Error: "cannot resolve dependency"
**Problema**: Conflictos o dependencias faltantes
**Solución**:
```bash
# Eliminar node_modules y package-lock.json
rm -rf node_modules package-lock.json  # Linux/macOS
# o en Windows:
rmdir /s node_modules
del package-lock.json

# Reinstalar todo
npm install
```

## 🐳 Alternativa con Docker (si tienes problemas de Node)

Si continúas teniendo problemas con Node.js, puedes usar Docker:

### 1. Crear Dockerfile
```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]
```

### 2. Ejecutar con Docker
```bash
# En la carpeta frontend/
docker build -t dy-prods-vue .
docker run -p 5173:5173 dy-prods-vue
```

## 📝 Scripts Disponibles

```bash
npm run dev        # Servidor de desarrollo
npm run build      # Build de producción
npm run preview    # Vista previa del build
npm run lint       # Linter de código
npm run format     # Formatear código
```

## 🔍 Verificar que Todo Funciona

Una vez que `npm run dev` se ejecute sin errores, deberías ver:

```
  VITE v7.x.x ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

Abre tu navegador en `http://localhost:5173/` y deberías ver el sitio de DY Prods funcionando.

## 🆘 Si Nada Funciona

Si después de seguir todos estos pasos aún tienes problemas:

1. **Comparte la salida completa del error**:
   ```bash
   npm run dev > error.log 2>&1
   ```

2. **Información del sistema**:
   ```bash
   node --version
   npm --version
   npx envinfo --system --npmPackages --binaries
   ```

3. **Contacta al equipo** con esta información para obtener ayuda específica.

## 🌐 Enlaces Útiles

- [Node.js Download](https://nodejs.org/)
- [NVM for Windows](https://github.com/coreybutler/nvm-windows)
- [NVM for macOS/Linux](https://github.com/nvm-sh/nvm)
- [Vite Troubleshooting](https://vitejs.dev/guide/troubleshooting.html)

---

**Desarrollado por DY Prods** 🚀