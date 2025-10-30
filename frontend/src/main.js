import { createApp } from 'vue'
import App from './App.vue'
import router from './components/router'
import { loadSiteConfig } from './config/siteConfig'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// Cargar configuración del sitio al iniciar
loadSiteConfig()

const app = createApp(App)
app.use(router)
app.mount('#app')
