<template>
  <section id="services" class="py-5">
    <div class="container">
      <h2 class="text-center section-title">Nuestros Servicios</h2>
      <div class="row">
        <div class="col-md-4" v-for="service in services" :key="service.id">
          <div class="card text-center p-4 service-card" @click="openServiceModal(service)">
            <div class="service-icon">
              <i :class="service.icon"></i>
            </div>
            <h3 class="h4">{{ service.title }}</h3>
            <p>{{ service.description }}</p>
            <div class="service-overlay">
              <i class="fas fa-info-circle"></i>
              <span>Ver detalles</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para mostrar detalles del servicio -->
    <div 
      class="modal fade" 
      id="serviceModal" 
      tabindex="-1" 
      aria-labelledby="serviceModalLabel" 
      aria-hidden="true"
      ref="serviceModal"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="serviceModalLabel">
              <i :class="selectedService?.icon" class="me-2"></i>
              {{ selectedService?.title }}
            </h5>
            <button 
              type="button" 
              class="btn-close" 
              data-bs-dismiss="modal" 
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body" v-if="selectedService">
            <div class="row">
              <div class="col-md-6">
                <img 
                  :src="selectedService.detailImage" 
                  :alt="selectedService.title" 
                  class="img-fluid rounded mb-3"
                >
              </div>
              <div class="col-md-6">
                <h6 class="text-primary mb-3">Descripción detallada</h6>
                <p>{{ selectedService.fullDescription }}</p>
                
                <h6 class="text-primary mb-2">¿Qué incluye?</h6>
                <ul class="list-unstyled">
                  <li v-for="item in selectedService.includes" :key="item" class="mb-1">
                    <i class="fas fa-check text-success me-2"></i>{{ item }}
                  </li>
                </ul>
              </div>
            </div>
            
            <div class="row mt-4">
              <div class="col-md-4">
                <div class="service-detail-card">
                  <i class="fas fa-clock text-primary"></i>
                  <h6>Duración</h6>
                  <p>{{ selectedService.duration }}</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="service-detail-card">
                  <i class="fas fa-dollar-sign text-primary"></i>
                  <h6>Desde</h6>
                  <p>{{ selectedService.price }}</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="service-detail-card">
                  <i class="fas fa-users text-primary"></i>
                  <h6>Ideal para</h6>
                  <p>{{ selectedService.idealFor }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              Cerrar
            </button>
            <button 
              type="button" 
              class="btn btn-primary" 
              @click="contactService"
              data-bs-dismiss="modal"
            >
              <i class="fas fa-envelope me-2"></i>Solicitar cotización
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { Modal } from 'bootstrap'

const selectedService = ref(null)
const serviceModal = ref(null)

const services = ref([
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
])

const openServiceModal = (service) => {
  selectedService.value = service
  const modal = new Modal(serviceModal.value)
  modal.show()
}

const contactService = () => {
  if (selectedService.value) {
    // Mapear el servicio al valor del select
    const serviceMap = {
      'Sesiones Fotográficas': 'retrato',
      'Videografía': 'video',
      'Fotografía Comercial': 'comercial'
    }
    
    // Crear mensaje personalizado con información del servicio
    const message = `Hola! Estoy interesado/a en el servicio de ${selectedService.value.title}. Me gustaría conocer más detalles sobre los precios y disponibilidad. Gracias!`
    
    // Enviar evento personalizado para pre-rellenar el formulario
    window.dispatchEvent(new CustomEvent('preselect-service', {
      detail: {
        service: serviceMap[selectedService.value.title] || '',
        message: message
      }
    }))
    
    // Navegar al formulario de contacto
    const contactSection = document.querySelector('#contact')
    if (contactSection) {
      contactSection.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      })
    }
  }
}
</script>

<style scoped>
section {
  scroll-margin-top: 80px;
}

.section-title {
  position: relative;
  padding-bottom: 15px;
  margin-bottom: 30px;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 50px;
  height: 3px;
  background-color: var(--secondary-color, #e67e22);
}

.card {
  transition: all 0.3s ease;
  margin-bottom: 20px;
  border: none;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
}

.service-card {
  cursor: pointer;
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.service-card:hover .service-overlay {
  opacity: 1;
  visibility: visible;
}

.service-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(44, 62, 80, 0.9), rgba(230, 126, 34, 0.9));
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  color: white;
}

.service-overlay i {
  font-size: 2rem;
  margin-bottom: 10px;
}

.service-overlay span {
  font-weight: 600;
  font-size: 1.1rem;
}

.service-icon {
  font-size: 3rem;
  color: var(--secondary-color, #e67e22);
  margin-bottom: 15px;
  transition: transform 0.3s ease;
}

.service-card:hover .service-icon {
  transform: scale(1.1);
}

.service-detail-card {
  text-align: center;
  padding: 20px;
  border-radius: 10px;
  background: #f8f9fa;
  margin-bottom: 15px;
}

.service-detail-card i {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.service-detail-card h6 {
  font-weight: 600;
  margin-bottom: 5px;
  color: var(--primary-color, #2c3e50);
}

.service-detail-card p {
  margin-bottom: 0;
  font-weight: 500;
}

.modal-header {
  background: linear-gradient(135deg, var(--primary-color, #2c3e50), var(--secondary-color, #e67e22));
  color: white;
}

.modal-header .btn-close {
  filter: brightness(0) invert(1);
}

.btn-primary {
  background-color: var(--secondary-color, #e67e22);
  border-color: var(--secondary-color, #e67e22);
}

.btn-primary:hover {
  background-color: #d35400;
  border-color: #d35400;
}
</style>