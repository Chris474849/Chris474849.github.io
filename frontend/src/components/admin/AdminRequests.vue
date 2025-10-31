<template>
  <div class="card shadow p-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h4 class="mb-0">Gestión de Solicitudes</h4>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-primary" @click="refreshRequests">
          <i class="fas fa-sync-alt me-2"></i> Refrescar
        </button>
        <button class="btn btn-success" @click="openCreateModal">
          <i class="fas fa-plus me-2"></i> Crear Solicitud
        </button>
        <button class="btn btn-primary" :disabled="!hasChanges" @click="saveRequestsChanges">
          <i class="fas fa-save me-2"></i> Guardar
        </button>
      </div>
      <div v-if="showSaveModal" class="custom-modal-overlay" @click.self="showSaveModal = false">
          <div class="custom-modal">
            <h5 class="mb-3 text-primary">{{ saveModalTitle }}</h5>
            <p>{{ saveModalMessage }}</p>
            <div class="text-end mt-4">
              <button class="btn btn-secondary" @click="showSaveModal = false">Cerrar</button>
            </div>
          </div>
        </div>
    </div>


    <table class="table table-striped align-middle">
      <thead class="table-dark">
        <tr>
          <th>Tipo de solicitud</th>
          <th>Nombre</th>
          <th>Gmail</th>
          <th>Hora</th>
          <th>Responsable</th>
          <th>Acciones</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(req, i) in requests" :key="req.id">
          <td>{{ req.tipo }}</td>
          <td>{{ req.nombre }}</td>
          <td>{{ req.gmail }}</td>

          <td>
            <input
              type="datetime-local"
              v-model="req.hora"
              class="form-control form-control-sm"
              style="max-width: 220px;"
            />
          </td>

          <td>
            <select
              v-model="req.responsable"
              class="form-select form-select-sm"
              style="max-width: 200px;"
            >
              <option disabled value="">Seleccionar...</option>
              <option v-for="p in personal" :key="p">{{ p }}</option>
            </select>
          </td>

          <td class="text-center">
            <div class="d-flex gap-2 justify-content-center">
              <button class="btn btn-info btn-sm" @click="viewRequest(req)">
                Ver Todo
              </button>
              <button class="btn btn-danger btn-sm" @click="confirmDelete(i)">
                Eliminar
              </button>
            </div>
          </td>
        </tr>

        <tr v-if="!requests.length">
          <td colspan="6" class="text-center text-muted">
            No hay solicitudes registradas.
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal Ver Todo -->
    <div v-if="showModal" class="custom-modal-overlay" @click.self="closeModal">
      <div class="custom-modal">
        <h5 class="mb-3 text-primary">Detalles de la Solicitud</h5>
        <div class="modal-content-body">
          <p><strong>Tipo:</strong> {{ selectedRequest.tipo }}</p>
          <p><strong>Nombre:</strong> {{ selectedRequest.nombre }}</p>
          <p><strong>Correo:</strong> {{ selectedRequest.gmail }}</p>
          <p><strong>Teléfono:</strong> {{ selectedRequest.telefono || '—' }}</p>
          <p><strong>Fecha solicitada:</strong> {{ selectedRequest.fecha || '—' }}</p>
          <p><strong>Hora de registro:</strong> {{ formatDate(selectedRequest.hora) }}</p>
          <p><strong>Responsable:</strong> {{ selectedRequest.responsable || 'No asignado' }}</p>
          <p><strong>Mensaje:</strong></p>
          <div class="message-box">{{ selectedRequest.mensaje }}</div>
        </div>
        <div class="text-end mt-4">
          <button class="btn btn-secondary" @click="closeModal">Cerrar</button>
        </div>
      </div>
    </div>

    <!-- Modal Crear Solicitud -->
    <div v-if="showCreateModal" class="custom-modal-overlay" @click.self="closeCreateModal">
      <div class="custom-modal large">
        <div class="modal-content">
          <button class="close-btn" @click="closeCreateModal">✖</button>
          <h3>Crear nueva solicitud</h3>

          <ServiceRequestForm :onSubmit="handleRequestSubmit" />
        </div>
      </div>
    </div>

    <!-- Popup confirmación de eliminación -->
    <div v-if="showDeletePopup" class="custom-modal-overlay" @click.self="cancelDelete">
      <div class="custom-modal text-center">
        <h5 class="text-danger mb-3">Confirmar Eliminación</h5>
        <p>¿Estás seguro de que deseas eliminar esta solicitud?</p>
        <div class="mt-4 d-flex justify-content-center gap-3">
          <button class="btn btn-outline-secondary" @click="cancelDelete">Cancelar</button>
          <button class="btn btn-danger" @click="deleteRequest">Eliminar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import ServiceRequestForm from '../common/ServiceRequestForm.vue'
import { siteConfig, saveSiteConfig, loadSiteConfig } from '@/config/siteConfig'
import { computed, ref, onMounted, watch } from 'vue'

// Cargar configuración
onMounted(() => loadSiteConfig())

// Obtener datos del usuario desde sessionStorage
const data = sessionStorage.getItem('authUser')
let parsedData = null
try {
  parsedData = JSON.parse(data)
} catch (e) {
  parsedData = null
}
const currentRole = ref(parsedData?.role || 'worker')

const currentUserId = ref(parsedData?.id || '')
console.log(data)
console.log(currentUserId)
// Filtrar solicitudes según rol
const requests = computed(() => {
  if (!siteConfig.requests) return []
  
  if (currentRole.value === 'admin') {
    return siteConfig.requests
  } else {
    // Worker solo ve solicitudes donde responsable === id del usuario
    return siteConfig.requests.filter(req => req.responsable === currentUserId.value)
  }
})

// Lista de personal para select
const personal = computed(() => siteConfig.contact.staff.map(s => s.name))

// === Estados modales ===
const showModal = ref(false)
const showCreateModal = ref(false)
const selectedRequest = ref({})
const deleteIndex = ref(null)
const showDeletePopup = ref(false)
const showSaveModal = ref(false)
const saveModalTitle = ref('')
const saveModalMessage = ref('')

// Servicio seleccionado por defecto
const selectedService = ref({
  title: "Asesoría Legal",
  fullDescription: "Orientación profesional en materia judicial y administrativa.",
  includes: ["Consulta inicial", "Revisión de documentos", "Seguimiento de caso"],
  duration: "30-60 minutos",
  price: "Gratis",
  idealFor: "Ciudadanos en proceso judicial",
  detailImage: "/assets/img/service-legal.jpg"
})

// === Funciones modales ===
const viewRequest = (req) => {
  selectedRequest.value = { ...req }
  showModal.value = true
}
const closeModal = () => { showModal.value = false }
const openCreateModal = () => { showCreateModal.value = true }
const closeCreateModal = () => { showCreateModal.value = false }

// Crear nueva solicitud
const handleRequestSubmit = async (data) => {
  const newReq = {
    id: Date.now(),
    tipo: selectedService.value.title,
    nombre: data.name,
    gmail: data.email,
    hora: new Date().toISOString(),
    responsable: "", // se puede asignar después
    telefono: data.phone || "",
    fecha: data.date || "",
    mensaje: data.message || selectedService.value.fullDescription
  }

  siteConfig.requests.push(newReq)
  saveSiteConfig()
  showCreateModal.value = false
}

// Guardamos una copia de los requests originales para detectar cambios
const originalRequests = ref(JSON.parse(JSON.stringify(siteConfig.requests || [])))

// Computed para detectar si hay cambios
const hasChanges = computed(() => {
  if (!siteConfig.requests) return false
  return requests.value.some(r => {
    const original = originalRequests.value.find(o => o.id === r.id)
    return original && (original.hora !== r.hora || original.responsable !== r.responsable)
  })
})

const saveRequestsChanges = () => {
  if (!hasChanges.value) {
    saveModalTitle.value = 'Sin cambios'
    saveModalMessage.value = 'No se realizaron modificaciones en las solicitudes.'
    showSaveModal.value = true
    return
  }

  if (currentRole.value === 'admin') {
    saveSiteConfig()
  } else {
    requests.value.forEach(r => {
      const idx = siteConfig.requests.findIndex(req => req.id === r.id)
      if (idx !== -1) {
        siteConfig.requests[idx].hora = r.hora
        siteConfig.requests[idx].responsable = r.responsable
      }
    })
    saveSiteConfig()
  }

  // Actualizar la copia original
  originalRequests.value = JSON.parse(JSON.stringify(siteConfig.requests || []))

  saveModalTitle.value = 'Éxito'
  saveModalMessage.value = 'Cambios guardados correctamente'
  showSaveModal.value = true
}

// Opcional: watch para reactivar/desactivar botón si se crean/eliminan solicitudes
watch(siteConfig.requests, () => {
  originalRequests.value = JSON.parse(JSON.stringify(siteConfig.requests || []))
})


// Eliminar solicitud
const confirmDelete = (i) => { deleteIndex.value = i; showDeletePopup.value = true }
const cancelDelete = () => { showDeletePopup.value = false; deleteIndex.value = null }
const deleteRequest = () => {
  if (deleteIndex.value !== null) {
    siteConfig.requests.splice(deleteIndex.value, 1)
    saveSiteConfig()
  }
  showDeletePopup.value = false
  deleteIndex.value = null
}

// Refrescar listado
const refreshRequests = () => console.log("🔄 Refrescando solicitudes (placeholder)")

// Formato fecha
const formatDate = (d) => {
  if (!d) return '—'
  const date = new Date(d)
  return date.toLocaleString('es-ES', { dateStyle: 'short', timeStyle: 'short' })
}
</script>


<style scoped>
.table th, .table td {
  vertical-align: middle;
}

.custom-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.custom-modal {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  width: 420px;
  max-width: 90%;
  box-shadow: 0 0 15px rgba(0,0,0,0.3);
  animation: fadeIn 0.25s ease;
}
.custom-modal.large { width: 800px; }

.modal-content {
  position: relative;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 15px;
  border: none;
  background: none;
  font-size: 1.25rem;
  cursor: pointer;
}
.message-box {
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 10px;
  white-space: pre-wrap;
  font-size: 0.9rem;
  color: #333;
}
@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
</style>
