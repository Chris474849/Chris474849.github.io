import { reactive } from 'vue'

// Configuración reactiva del sitio
export const siteConfig = reactive({
  // Configuración general
  siteName: 'DY Prods',
  tagline: 'Capturando momentos, creando recuerdos',
  
  // Hero Section
  hero: {
    title: 'DY Prods',
    subtitle: 'Capturando momentos, creando recuerdos',
    ctaText: 'Reserva ahora',
    backgroundImage: 'https://via.placeholder.com/1920x1080/2c3e50/ffffff?text=DY+Prods'
  },

  // Sección Servicios
  services: {
    title: 'Nuestros Servicios',
    items: [
      {
        id: 1,
        icon: 'fas fa-camera',
        title: 'Sesiones Fotográficas',
        description: 'Capturamos tu esencia con retratos profesionales para individuos, parejas y familias.',
        fullDescription: 'Nuestras sesiones fotográficas están diseñadas para capturar la verdadera esencia de cada persona. Trabajamos en ambientes relajados y naturales, ya sea en nuestro estudio profesional o en locaciones exteriores de tu elección.',
        detailImage: 'https://via.placeholder.com/600x400/e67e22/ffffff?text=Sesion+Fotografica',
        duration: '1-3 horas',
        price: '$150 USD',
        idealFor: 'Individuos, parejas, familias',
        includes: [
          'Sesión fotográfica completa',
          'Edición profesional de imágenes',
          '20-30 fotos en alta resolución',
          'Galería online privada',
          'Consulta previa de styling'
        ]
      },
      {
        id: 2,
        icon: 'fas fa-film',
        title: 'Videografía',
        description: 'Inmortalizamos tus eventos importantes con videos de alta calidad y edición profesional.',
        fullDescription: 'Creamos videos cinematográficos que cuentan tu historia de manera única. Desde eventos corporativos hasta celebraciones familiares, capturamos cada momento importante con equipo profesional 4K.',
        detailImage: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Videografia',
        duration: '2-8 horas',
        price: '$300 USD',
        idealFor: 'Eventos, bodas, corporativos',
        includes: [
          'Grabación en 4K',
          'Audio profesional',
          'Edición cinematográfica',
          'Video final de 3-10 minutos',
          'Material en bruto incluido',
          'Música libre de derechos'
        ]
      },
      {
        id: 3,
        icon: 'fas fa-building',
        title: 'Fotografía Comercial',
        description: 'Elevamos tu marca con fotografía profesional para productos, servicios y espacios.',
        fullDescription: 'Especializados en fotografía comercial que hace que tu negocio destaque. Desde productos e-commerce hasta retratos corporativos, creamos imágenes que impulsan tu marca.',
        detailImage: 'https://via.placeholder.com/600x400/e67e22/ffffff?text=Comercial',
        duration: '2-4 horas',
        price: '$250 USD',
        idealFor: 'Empresas, productos, marcas',
        includes: [
          'Fotografía de productos',
          'Retratos corporativos',
          'Fotografía de espacios',
          'Edición profesional',
          'Formatos optimizados para web',
          'Derechos comerciales incluidos'
        ]
      }
    ]
  },

  // Sección Portfolio
  portfolio: {
    title: 'Nuestro Portafolio',
    images: [
      {
        id: 1,
        url: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Retrato',
        alt: 'Fotografía de retrato'
      },
      {
        id: 2,
        url: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Evento',
        alt: 'Fotografía de evento'
      },
      {
        id: 3,
        url: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Comercial',
        alt: 'Fotografía comercial'
      },
      {
        id: 4,
        url: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Producto',
        alt: 'Fotografía de producto'
      },
      {
        id: 5,
        url: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Boda',
        alt: 'Fotografía de boda'
      },
      {
        id: 6,
        url: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Artística',
        alt: 'Fotografía artística'
      }
    ]
  },

  // Sección About
  about: {
    title: 'Sobre DY Prods',
    image: 'https://via.placeholder.com/800x600/2c3e50/ffffff?text=Nuestro+Equipo',
    subtitle: 'Somos un equipo apasionado de fotógrafos y videógrafos comprometidos con la excelencia.',
    description: [
      'Fundado en 2015, DY Prods se ha convertido en uno de los estudios fotográficos más reconocidos de la región. Nuestro enfoque se centra en capturar la belleza auténtica en cada toma, ya sea para eventos personales, corporativos o proyectos creativos.',
      'Trabajamos con equipos de última generación y técnicas innovadoras para garantizar resultados excepcionales en cada proyecto.'
    ]
  },

  // Sección Contacto
  contact: {
    title: 'Reserva tu Sesión',
    services: [
      { value: 'retrato', label: 'Fotografía de Retrato' },
      { value: 'evento', label: 'Fotografía de Evento' },
      { value: 'comercial', label: 'Fotografía Comercial' },
      { value: 'video', label: 'Videografía' }
    ],
    staff: [
      { 
        id: 1,
        value: 'daineris', 
        name: 'Daineris',
        specialty: 'Fotografía de Retratos y Eventos',
        image: 'https://via.placeholder.com/150x150/e67e22/ffffff?text=D'
      },
      { 
        id: 2,
        value: 'yoi', 
        name: 'Yoi',
        specialty: 'Videografía y Fotografía Comercial',
        image: 'https://via.placeholder.com/150x150/2c3e50/ffffff?text=Y'
      }
    ]
  },

  // Lista de solicitudes de usuarios
  requests: [],

  // Footer
  footer: {
    description: 'Tu estudio fotográfico de confianza para capturar los momentos más importantes de tu vida.',
    contact: {
      phones: ['+53 56601651', '+53 55494545'],
      email: 'dyprods0581@gmail.com'
    },
    schedule: {
      weekdays: 'Lunes a Viernes: 9:00 AM - 6:00 PM',
      saturday: 'Sábados: 10:00 AM - 3:00 PM',
      sunday: 'Domingos: Cerrado'
    },
    social: {
      facebook: '#',
      instagram: 'https://www.instagram.com/DY_Prods/',
      twitter: '#',
      linkedin: '#'
    }
  },

  // Configuración de colores y tema
  theme: {
    primaryColor: '#007bff',
    secondaryColor: '#e67e22',
    backgroundColor: '#ffffff',
    textColor: '#333333'
  }
})

// Función para guardar configuración en localStorage
export const saveSiteConfig = () => {
  localStorage.setItem('siteConfig', JSON.stringify(siteConfig))
}

// Función para cargar configuración desde localStorage
export const loadSiteConfig = () => {
  const saved = localStorage.getItem('siteConfig')
  if (saved) {
    const parsedConfig = JSON.parse(saved)
    Object.assign(siteConfig, parsedConfig)
  }
}

// Función para resetear a configuración por defecto
export const resetSiteConfig = () => {
  localStorage.removeItem('siteConfig')
  location.reload()
}