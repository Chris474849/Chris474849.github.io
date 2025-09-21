# DY Prods - Sitio Web

Sitio web moderno de DY Prods desarrollado con Vue.js 3, Vite y Bootstrap 5.

## 🚀 Características

- **Framework**: Vue.js 3 con Composition API
- **Build Tool**: Vite para desarrollo rápido
- **UI Framework**: Bootstrap 5 para diseño responsivo
- **Componentes Modulares**: Arquitectura escalable
- **Validación en Tiempo Real**: Formularios con validación avanzada
- **Modales Interactivos**: Información detallada de servicios
- **Design Responsivo**: Optimizado para todos los dispositivos

## 📁 Estructura del Proyecto

```
├── frontend/              # Proyecto Vue.js
│   ├── src/
│   │   ├── components/    # Componentes Vue
│   │   ├── assets/       # Assets estáticos
│   │   └── App.vue       # Componente principal
│   ├── public/           # Archivos públicos
│   └── dist/            # Build de producción (generado)
├── .github/
│   └── workflows/        # GitHub Actions
└── css/                 # CSS original (legacy)
```

## 🛠️ Desarrollo Local

### Prerrequisitos
- Node.js 18.0.0+ 
- npm

### Instalación Rápida

```bash
cd frontend
npm install
npm run dev
```

El proyecto estará disponible en `http://localhost:5173/`

### ❗ ¿Problemas con la instalación?

**¡IMPORTANTE!** Si tienes errores con npm o Node.js, consulta nuestra **[Guía de Setup Local Completa](SETUP_LOCAL.md)** que incluye:

- Soluciones a todos los errores comunes
- Guía paso a paso detallada
- Alternativas con Docker
- Troubleshooting específico por sistema operativo

### Build de Producción

```bash
npm run build
```

## 🚀 Deployment

El sitio se despliega automáticamente en GitHub Pages usando GitHub Actions:

- **Rama de desarrollo**: `develop` (contiene el código Vue.js)
- **Rama de producción**: GitHub Pages se configura desde Actions
- **URL del sitio**: https://chris474849.github.io/Chris474849.github.io/

### Proceso Automático

1. Cualquier push a la rama `develop` trigger el workflow
2. GitHub Actions ejecuta el build del proyecto Vue.js
3. Los archivos compilados se despliegan automáticamente a GitHub Pages

### Deployment Manual

También puedes ejecutar el deployment manualmente desde la pestaña "Actions" en GitHub.

## 📱 Funcionalidades Principales

### Secciones
- **Hero**: Presentación principal con call-to-action
- **Servicios**: Cards interactivos con modales detallados
- **Portfolio**: Galería de proyectos realizados
- **Acerca de**: Información sobre la empresa
- **Contacto**: Formulario con validación en tiempo real

### Características Técnicas
- ✅ Diseño responsivo y mobile-first
- ✅ Validación de formularios en tiempo real
- ✅ Modales informativos para servicios
- ✅ Pre-llenado de formularios desde servicios
- ✅ Manejo de errores visual
- ✅ Campos opcionales y obligatorios claramente marcados
- ✅ Optimización para SEO y performance

## 🌐 Enlaces

- **Sitio en vivo**: https://chris474849.github.io/Chris474849.github.io/
- **Desarrollo local**: http://localhost:5173/
- **Repositorio**: https://github.com/Chris474849/Chris474849.github.io

## 📄 Licencia

Este proyecto es propietario de DY Prods.

---

Desarrollado con ❤️ por DY Prods