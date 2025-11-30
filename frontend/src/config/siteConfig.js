import { reactive } from 'vue'
import { fetchCurrentConfig } from '@/api/config'

export const siteConfig = reactive({})

export const loadSiteConfigFromBackend = async () => {
  try {
    const response = await fetchCurrentConfig()
    const data = response.data

    for (const key in data) delete siteConfig[key]
    Object.assign(siteConfig, data)

    syncContactServices()
  } catch (error) {
    console.error("Error cargando config del backend:", error)
  }
}

export const syncContactServices = () => {
  if (!siteConfig.services || !siteConfig.services.items) return
  const serviceOptions = siteConfig.services.items.map(service => ({
    value: service.title.toLowerCase().replace(/\s+/g, '-').replace(/[áéíóúñü]/g, match => {
      const accents = { 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n', 'ü': 'u' }
      return accents[match] || match
    }),
    label: service.title
  }))
  siteConfig.contact.services = serviceOptions
}

export const saveSiteConfig = () => {
  syncContactServices() 
  localStorage.setItem('siteConfig', JSON.stringify(siteConfig))
}

export const loadSiteConfig = () => {
  const saved = localStorage.getItem('siteConfig')
  if (saved) {
    const parsedConfig = JSON.parse(saved)
    Object.assign(siteConfig, parsedConfig)
  }
  syncContactServices()
}

export const resetSiteConfig = () => {
  localStorage.removeItem('siteConfig')
  location.reload()
}