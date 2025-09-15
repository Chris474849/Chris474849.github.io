# DY Prods - Estudio Fotográfico

Una aplicación web moderna para estudio fotográfico construida con Vue 3 y Vite.

## 🌐 Ver la Página Web

### Sitio en Vivo
**URL:** https://chris474849.github.io/

### Desarrollo Local
Para ver la página en tu computadora durante el desarrollo:

1. Instala las dependencias:
   ```sh
   npm install
   ```

2. Ejecuta el servidor de desarrollo:
   ```sh
   npm run dev
   ```

3. Abre tu navegador y ve a: **http://localhost:5173/**

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run End-to-End Tests with [Playwright](https://playwright.dev)

```sh
# Install browsers for the first run
npx playwright install

# When testing on CI, must build the project first
npm run build

# Runs the end-to-end tests
npm run test:e2e
# Runs the tests only on Chromium
npm run test:e2e -- --project=chromium
# Runs the tests of a specific file
npm run test:e2e -- tests/example.spec.ts
# Runs the tests in debug mode
npm run test:e2e -- --debug
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## 🚀 Deployment

Este proyecto se despliega automáticamente en GitHub Pages usando GitHub Actions.

### Cómo funciona:
- Cada `push` a la rama `main` activa automáticamente el deployment
- GitHub Actions ejecuta `npm run build` para generar los archivos estáticos
- Los archivos se despliegan automáticamente en GitHub Pages
- El sitio se actualiza en: https://chris474849.github.io/

### Manual Build para Producción

```sh
npm run build
```

Esto genera los archivos optimizados en la carpeta `dist/`.

## 🛠️ Tecnologías Utilizadas

- **Vue 3** - Framework JavaScript progresivo
- **Vite** - Build tool y servidor de desarrollo
- **Bootstrap 5** - Framework CSS
- **Font Awesome** - Iconos
- **GitHub Pages** - Hosting estático
- **GitHub Actions** - CI/CD automático
