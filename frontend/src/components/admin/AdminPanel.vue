<template>
  <div class="container-fluid mt-4">
    <div class="row">
      <!-- Sidebar de navegación -->
      <div class="col-md-3">
        <div class="card">
          <div class="card-header">
            <h5 class="mb-0">Secciones del Sitio</h5>
          </div>
          <div class="list-group list-group-flush">
            <button 
              v-for="section in sections" 
              :key="section.id"
              @click="activeSection = section.id"
              :class="['list-group-item', 'list-group-item-action', 
                      activeSection === section.id ? 'active' : '']"
            >
              <i :class="section.icon + ' me-2'"></i>
              {{ section.name }}
            </button>
          </div>
        </div>
        
        <div class="card mt-3">
          <div class="card-body text-center">
            <button @click="saveAllChanges" class="btn btn-success btn-lg mb-2 w-100">
              <i class="fas fa-save me-2"></i>
              Guardar Cambios
            </button>
            <button @click="resetToDefaults" class="btn btn-warning w-100">
              <i class="fas fa-undo me-2"></i>
              Restaurar Por Defecto
            </button>
          </div>
        </div>
      </div>

      <!-- Contenido principal -->
      <div class="col-md-9">
        <!-- Sección General -->
        <div v-if="activeSection === 'general'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Configuración General</h5>
          </div>
          <div class="card-body">
            <div class="mb-3">
              <label class="form-label">Nombre del Sitio</label>
              <input v-model="siteConfig.siteName" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">Eslogan</label>
              <input v-model="siteConfig.tagline" class="form-control" type="text">
            </div>
          </div>
        </div>

        <!-- Sección Hero -->
        <div v-if="activeSection === 'hero'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Sección Principal (Hero)</h5>
          </div>
          <div class="card-body">
            <div class="mb-3">
              <label class="form-label">Título Principal</label>
              <input v-model="siteConfig.hero.title" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">Subtítulo</label>
              <input v-model="siteConfig.hero.subtitle" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">Texto del Botón</label>
              <input v-model="siteConfig.hero.ctaText" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">URL de Imagen de Fondo</label>
              <input v-model="siteConfig.hero.backgroundImage" class="form-control" type="url">
            </div>
          </div>
        </div>

        <!-- Sección Servicios -->
        <div v-if="activeSection === 'services'" class="card">
          <div class="card-header d-flex justify-content-between align-items-center">
            <h5 class="mb-0">Sección de Servicios</h5>
            <button @click="addNewService" class="btn btn-success btn-sm">
              <i class="fas fa-plus me-2"></i>Agregar Servicio
            </button>
          </div>
          <div class="card-body">
            <div class="mb-4">
              <label class="form-label">Título de la Sección</label>
              <input v-model="siteConfig.services.title" class="form-control" type="text">
            </div>
            
            <div v-for="(service, index) in siteConfig.services.items" :key="service.id" class="border p-3 mb-3 rounded position-relative">
              <button @click="removeService(index)" class="btn btn-danger btn-sm position-absolute" style="top: 10px; right: 10px;">
                <i class="fas fa-trash"></i>
              </button>
              
              <h6>Servicio {{ index + 1 }}</h6>
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="form-label">Ícono (clase FontAwesome)</label>
                  <input v-model="service.icon" class="form-control" type="text" placeholder="fas fa-camera">
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label">Título del Servicio</label>
                  <input v-model="service.title" class="form-control" type="text">
                </div>
                <div class="col-12 mb-3">
                  <label class="form-label">Descripción Corta</label>
                  <textarea v-model="service.description" class="form-control" rows="2"></textarea>
                </div>
                <div class="col-12 mb-3">
                  <label class="form-label">Descripción Completa</label>
                  <textarea v-model="service.fullDescription" class="form-control" rows="3"></textarea>
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label">Duración</label>
                  <input v-model="service.duration" class="form-control" type="text" placeholder="1-3 horas">
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label">Precio</label>
                  <input v-model="service.price" class="form-control" type="text" placeholder="$150 USD">
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label">Ideal Para</label>
                  <input v-model="service.idealFor" class="form-control" type="text" placeholder="Individuos, parejas, familias">
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label">Imagen de Detalle (URL)</label>
                  <input v-model="service.detailImage" class="form-control" type="url">
                </div>
                <div class="col-12 mb-3">
                  <label class="form-label">Qué Incluye (un item por línea)</label>
                  <textarea 
                    :value="service.includes.join('\n')"
                    @input="updateServiceIncludes(index, $event.target.value)"
                    class="form-control" 
                    rows="4"
                    placeholder="Sesión fotográfica completa&#10;Edición profesional de imágenes&#10;20-30 fotos en alta resolución"
                  ></textarea>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sección Portfolio -->
        <div v-if="activeSection === 'portfolio'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Sección de Portafolio</h5>
          </div>
          <div class="card-body">
            <div class="mb-4">
              <label class="form-label">Título de la Sección</label>
              <input v-model="siteConfig.portfolio.title" class="form-control" type="text">
            </div>
            
            <div class="row">
              <div v-for="(image, index) in siteConfig.portfolio.images" :key="image.id" class="col-md-6 mb-3">
                <div class="border p-3 rounded">
                  <h6>Imagen {{ index + 1 }}</h6>
                  <div class="mb-2">
                    <label class="form-label">URL de la imagen</label>
                    <input v-model="image.url" class="form-control" type="url">
                  </div>
                  <div class="mb-2">
                    <label class="form-label">Texto alternativo</label>
                    <input v-model="image.alt" class="form-control" type="text">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sección About -->
        <div v-if="activeSection === 'about'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Sección Acerca De</h5>
          </div>
          <div class="card-body">
            <div class="mb-3">
              <label class="form-label">Título de la Sección</label>
              <input v-model="siteConfig.about.title" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">URL de Imagen</label>
              <input v-model="siteConfig.about.image" class="form-control" type="url">
            </div>
            <div class="mb-3">
              <label class="form-label">Subtítulo</label>
              <textarea v-model="siteConfig.about.subtitle" class="form-control" rows="2"></textarea>
            </div>
            <div v-for="(paragraph, index) in siteConfig.about.description" :key="index" class="mb-3">
              <label class="form-label">Párrafo {{ index + 1 }}</label>
              <textarea v-model="siteConfig.about.description[index]" class="form-control" rows="4"></textarea>
            </div>
          </div>
        </div>

        <!-- Sección Contacto -->
        <div v-if="activeSection === 'contact'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Sección de Contacto</h5>
          </div>
          <div class="card-body">
            <div class="mb-4">
              <label class="form-label">Título de la Sección</label>
              <input v-model="siteConfig.contact.title" class="form-control" type="text">
            </div>
            
            <div class="row">
              <div class="col-md-6">
                <div class="d-flex justify-content-between align-items-center mb-3">
                  <h6>Servicios en el Formulario</h6>
                  <button @click="addNewContactService" class="btn btn-success btn-sm">
                    <i class="fas fa-plus me-1"></i>Agregar
                  </button>
                </div>
                <div v-for="(service, index) in siteConfig.contact.services" :key="index" class="border p-3 mb-3 rounded position-relative">
                  <button @click="removeContactService(index)" class="btn btn-danger btn-sm position-absolute" style="top: 10px; right: 10px;">
                    <i class="fas fa-trash"></i>
                  </button>
                  <div class="row">
                    <div class="col-12 mb-2">
                      <label class="form-label">Valor</label>
                      <input v-model="service.value" class="form-control" type="text">
                    </div>
                    <div class="col-12 mb-2">
                      <label class="form-label">Etiqueta</label>
                      <input v-model="service.label" class="form-control" type="text">
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="col-md-6">
                <div class="d-flex justify-content-between align-items-center mb-3">
                  <h6>Personal Disponible</h6>
                  <button @click="addNewStaffMember" class="btn btn-success btn-sm">
                    <i class="fas fa-plus me-1"></i>Agregar
                  </button>
                </div>
                <div v-for="(staff, index) in siteConfig.contact.staff" :key="staff.id" class="border p-3 mb-3 rounded position-relative">
                  <button @click="removeStaffMember(index)" class="btn btn-danger btn-sm position-absolute" style="top: 10px; right: 10px;">
                    <i class="fas fa-trash"></i>
                  </button>
                  <div class="row">
                    <div class="col-12 mb-2">
                      <label class="form-label">Nombre</label>
                      <input v-model="staff.name" class="form-control" type="text">
                    </div>
                    <div class="col-12 mb-2">
                      <label class="form-label">Valor (ID interno)</label>
                      <input v-model="staff.value" class="form-control" type="text">
                    </div>
                    <div class="col-12 mb-2">
                      <label class="form-label">Especialidad</label>
                      <input v-model="staff.specialty" class="form-control" type="text">
                    </div>
                    <div class="col-12 mb-2">
                      <label class="form-label">Imagen (URL)</label>
                      <input v-model="staff.image" class="form-control" type="url">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sección Footer -->
        <div v-if="activeSection === 'footer'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Pie de Página</h5>
          </div>
          <div class="card-body">
            <div class="mb-3">
              <label class="form-label">Descripción</label>
              <textarea v-model="siteConfig.footer.description" class="form-control" rows="3"></textarea>
            </div>
            
            <h6>Información de Contacto</h6>
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input v-model="siteConfig.footer.contact.email" class="form-control" type="email">
            </div>
            <div class="mb-3">
              <label class="form-label">Teléfonos (separados por coma)</label>
              <input 
                :value="siteConfig.footer.contact.phones.join(', ')"
                @input="updatePhones($event.target.value)"
                class="form-control" 
                type="text"
              >
            </div>
            
            <h6>Horarios</h6>
            <div class="mb-3">
              <label class="form-label">Entre Semana</label>
              <input v-model="siteConfig.footer.schedule.weekdays" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">Sábados</label>
              <input v-model="siteConfig.footer.schedule.saturday" class="form-control" type="text">
            </div>
            <div class="mb-3">
              <label class="form-label">Domingos</label>
              <input v-model="siteConfig.footer.schedule.sunday" class="form-control" type="text">
            </div>
            
            <h6>Redes Sociales</h6>
            <div class="row">
              <div class="col-md-6 mb-3">
                <label class="form-label">Facebook</label>
                <input v-model="siteConfig.footer.social.facebook" class="form-control" type="url">
              </div>
              <div class="col-md-6 mb-3">
                <label class="form-label">Instagram</label>
                <input v-model="siteConfig.footer.social.instagram" class="form-control" type="url">
              </div>
              <div class="col-md-6 mb-3">
                <label class="form-label">Twitter</label>
                <input v-model="siteConfig.footer.social.twitter" class="form-control" type="url">
              </div>
              <div class="col-md-6 mb-3">
                <label class="form-label">LinkedIn</label>
                <input v-model="siteConfig.footer.social.linkedin" class="form-control" type="url">
              </div>
            </div>
          </div>
        </div>

        <!-- Sección Tema -->
        <div v-if="activeSection === 'theme'" class="card">
          <div class="card-header">
            <h5 class="mb-0">Configuración de Tema</h5>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-md-6 mb-3">
                <label class="form-label">Color Primario</label>
                <div class="input-group">
                  <input v-model="siteConfig.theme.primaryColor" class="form-control" type="color">
                  <input v-model="siteConfig.theme.primaryColor" class="form-control" type="text">
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <label class="form-label">Color Secundario</label>
                <div class="input-group">
                  <input v-model="siteConfig.theme.secondaryColor" class="form-control" type="color">
                  <input v-model="siteConfig.theme.secondaryColor" class="form-control" type="text">
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <label class="form-label">Color de Fondo</label>
                <div class="input-group">
                  <input v-model="siteConfig.theme.backgroundColor" class="form-control" type="color">
                  <input v-model="siteConfig.theme.backgroundColor" class="form-control" type="text">
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <label class="form-label">Color de Texto</label>
                <div class="input-group">
                  <input v-model="siteConfig.theme.textColor" class="form-control" type="color">
                  <input v-model="siteConfig.theme.textColor" class="form-control" type="text">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Modal de confirmación -->
    <div v-if="showConfirmModal" class="modal d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirmar Acción</h5>
          </div>
          <div class="modal-body">
            <p>¿Estás seguro de que deseas restaurar la configuración por defecto?</p>
          </div>
          <div class="modal-footer">
            <button @click="showConfirmModal = false" class="btn btn-secondary">Cancelar</button>
            <button @click="confirmReset" class="btn btn-warning">Restaurar</button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showConfirmModal" class="modal-backdrop show"></div>
    
    <!-- Toast de notificaciones -->
    <div v-if="showToast" class="toast-container position-fixed bottom-0 end-0 p-3">
      <div class="toast show" role="alert">
        <div class="toast-header">
          <i :class="toastIcon + ' me-2'"></i>
          <strong class="me-auto">{{ toastTitle }}</strong>
          <button @click="showToast = false" type="button" class="btn-close"></button>
        </div>
        <div class="toast-body">
          {{ toastMessage }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { siteConfig, saveSiteConfig, resetSiteConfig } from '@/config/siteConfig'

const activeSection = ref('general')
const showConfirmModal = ref(false)
const showToast = ref(false)
const toastTitle = ref('')
const toastMessage = ref('')
const toastIcon = ref('')

const sections = [
  { id: 'general', name: 'General', icon: 'fas fa-cog' },
  { id: 'hero', name: 'Sección Principal', icon: 'fas fa-home' },
  { id: 'services', name: 'Servicios', icon: 'fas fa-briefcase' },
  { id: 'portfolio', name: 'Portafolio', icon: 'fas fa-images' },
  { id: 'about', name: 'Acerca De', icon: 'fas fa-users' },
  { id: 'contact', name: 'Contacto', icon: 'fas fa-envelope' },
  { id: 'footer', name: 'Pie de Página', icon: 'fas fa-align-center' },
  { id: 'theme', name: 'Tema', icon: 'fas fa-palette' }
]

onMounted(() => {
  // Cargar configuración guardada si existe
  const saved = localStorage.getItem('siteConfig')
  if (saved) {
    const parsedConfig = JSON.parse(saved)
    Object.assign(siteConfig, parsedConfig)
  }
})

const saveAllChanges = () => {
  saveSiteConfig()
  showToastMessage('Éxito', 'Cambios guardados correctamente', 'fas fa-check-circle text-success')
}

const resetToDefaults = () => {
  showConfirmModal.value = true
}

const confirmReset = () => {
  resetSiteConfig()
  showConfirmModal.value = false
  showToastMessage('Información', 'Configuración restaurada por defecto', 'fas fa-info-circle text-info')
}

const updatePhones = (value) => {
  siteConfig.footer.contact.phones = value.split(',').map(phone => phone.trim())
}

const showToastMessage = (title, message, icon) => {
  toastTitle.value = title
  toastMessage.value = message
  toastIcon.value = icon
  showToast.value = true
  
  setTimeout(() => {
    showToast.value = false
  }, 3000)
}

// Funciones para servicios
const addNewService = () => {
  const newId = Math.max(...siteConfig.services.items.map(s => s.id)) + 1
  siteConfig.services.items.push({
    id: newId,
    icon: 'fas fa-star',
    title: 'Nuevo Servicio',
    description: 'Descripción del servicio',
    fullDescription: 'Descripción completa del servicio con todos los detalles.',
    detailImage: 'https://via.placeholder.com/600x400/e67e22/ffffff?text=Nuevo+Servicio',
    duration: '1-2 horas',
    price: '$100 USD',
    idealFor: 'Todo tipo de clientes',
    includes: [
      'Servicio profesional',
      'Atención personalizada',
      'Resultados de calidad'
    ]
  })
}

const removeService = (index) => {
  if (confirm('¿Estás seguro de que deseas eliminar este servicio?')) {
    siteConfig.services.items.splice(index, 1)
  }
}

const updateServiceIncludes = (serviceIndex, value) => {
  const includes = value.split('\n').filter(item => item.trim() !== '')
  siteConfig.services.items[serviceIndex].includes = includes
}

// Funciones para servicios de contacto
const addNewContactService = () => {
  siteConfig.contact.services.push({
    value: 'nuevo-servicio',
    label: 'Nuevo Servicio'
  })
}

const removeContactService = (index) => {
  if (confirm('¿Estás seguro de que deseas eliminar este servicio del formulario?')) {
    siteConfig.contact.services.splice(index, 1)
  }
}

// Funciones para personal
const addNewStaffMember = () => {
  const newId = Math.max(...siteConfig.contact.staff.map(s => s.id)) + 1
  siteConfig.contact.staff.push({
    id: newId,
    value: 'nuevo-personal',
    name: 'Nuevo Miembro',
    specialty: 'Especialidad del miembro del equipo',
    image: 'https://via.placeholder.com/150x150/2c3e50/ffffff?text=N'
  })
}

const removeStaffMember = (index) => {
  if (confirm('¿Estás seguro de que deseas eliminar este miembro del personal?')) {
    siteConfig.contact.staff.splice(index, 1)
  }
}
</script>

<style scoped>
.card {
  border: 1px solid #dee2e6;
  margin-bottom: 1rem;
}

.list-group-item.active {
  background-color: #007bff;
  border-color: #007bff;
}

.toast-container {
  z-index: 1055;
}

.modal {
  z-index: 1050;
}

.modal-backdrop {
  z-index: 1040;
}

.form-control:focus {
  border-color: #007bff;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
}

.btn-warning {
  background-color: #ffc107;
  border-color: #ffc107;
  color: #212529;
}

.input-group .form-control:first-child {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.input-group .form-control:last-child {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
</style>
