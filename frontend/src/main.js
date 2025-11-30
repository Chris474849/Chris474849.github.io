import { createApp } from 'vue'
import App from './App.vue'
import router from './components/router'
import { loadSiteConfigFromBackend } from './config/siteConfig'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import axios from "axios"

axios.interceptors.request.use((config) => {
  const token = sessionStorage.getItem("access")
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

axios.interceptors.response.use(
  res => res,
  async (error) => {
    const original = error.config
    if (error.response?.status === 401 && !original._retry) {
      original._retry = true

      const rt = sessionStorage.getItem("refresh")
      if (!rt) return Promise.reject(error)

      try {
        const { data } = await axios.post("http://127.0.0.1:9670/refresh", { rt })
        sessionStorage.setItem("access", data.access)
        sessionStorage.setItem("refresh", data.refresh)
        original.headers.Authorization = `Bearer ${data.access}`
        return axios(original)
      } catch (e) {
        sessionStorage.clear()
        window.location.href = "/login"
      }
    }
    return Promise.reject(error)
  }
)

loadSiteConfigFromBackend()

const app = createApp(App)
app.use(router)
app.mount('#app')
