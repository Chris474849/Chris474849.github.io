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
          <td>{{ req.servicio }}</td>
          <td>{{ req.nombre }}</td>
          <td>{{ req.email }}</td>

          <td>
            <input
              type="date"
              v-model="req.fecha"
              class="form-control form-control-sm"
              style="max-width: 220px;"
            />
          </td>

          <td>
            <select
              v-model="req.personal"
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
          <p><strong>Tipo:</strong> {{ selectedRequest.servicio }}</p>
          <p><strong>Nombre:</strong> {{ selectedRequest.nombre }}</p>
          <p><strong>Correo:</strong> {{ selectedRequest.email }}</p>
          <p><strong>Teléfono:</strong> {{ selectedRequest.telefono || '—' }}</p>
          <p><strong>Fecha solicitada:</strong> {{ selectedRequest.fecha || '—' }}</p>
          <p><strong>Hora de registro:</strong> {{ formatDate(selectedRequest.hora) }}</p>
          <p><strong>Responsable:</strong> {{ selectedRequest.personal || 'No asignado' }}</p>
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
import { fetchRequests, createRequestAPI, updateRequestAPI, deleteRequestAPI } from '@/api/requests'

onMounted(() => {
  loadSiteConfig()
  refreshRequests()
})

const data = sessionStorage.getItem('authUser')
let parsedData = null
try { parsedData = JSON.parse(data) } catch (e) { parsedData = null }

const currentRole = ref(parsedData?.role || 'worker')
const currentUserId = ref(parsedData?.id || '')

// CORRECCIÓN 1: Asegura que siteConfig.requests es tratado como un Array vacío si es null/undefined
const requestsArray = computed(() => siteConfig.requests || [])

const requests = computed(() => {
  // Utilizamos requestsArray para acceder a los datos de forma segura
  if (currentRole.value === 'admin') return requestsArray.value
  return requestsArray.value.filter(req => req.responsable === currentUserId.value)
})

const personal = computed(() => siteConfig.contact.staff.map(s => s.name))

const showModal = ref(false)
const showCreateModal = ref(false)
const selectedRequest = ref({})
const deleteIndex = ref(null)
const showDeletePopup = ref(false)
const showSaveModal = ref(false)
const saveModalTitle = ref('')
const saveModalMessage = ref('')

const selectedService = ref({
  title: "Asesoría Legal",
  fullDescription: "Orientación profesional en materia judicial y administrativa.",
  includes: ["Consulta inicial", "Revisión de documentos", "Seguimiento de caso"],
  duration: "30-60 minutos",
  price: "Gratis",
  idealFor: "Ciudadanos en proceso judicial",
  detailImage: "/assets/img/service-legal.jpg"
})

const viewRequest = (req) => {
  selectedRequest.value = { ...req }
  showModal.value = true
}
const closeModal = () => { showModal.value = false }
const openCreateModal = () => { showCreateModal.value = true }
const closeCreateModal = () => { showCreateModal.value = false }

// Crear nueva solicitud
const handleRequestSubmit = async (data) => {
  // const newReq = {
  //   id: Date.now(),
  //   tipo: selectedService.value.title,
  //   nombre: data.name,
  //   gmail: data.email,
  //   hora: new Date().toISOString(),
  //   responsable: "", // se puede asignar después
  //   telefono: data.phone || "",
  //   fecha: data.date || "",
  //   mensaje: data.message || selectedService.value.fullDescription
  // }

  // siteConfig.requests.push(newReq)
  // saveSiteConfig()
  showCreateModal.value = false
}

const originalRequests = ref([])

const hasChanges = computed(() => {
  // CORRECCIÓN 2: Asegura que requests.value es un Array antes de llamar a .some()
  if (!Array.isArray(requests.value)) return false
  
  return requests.value.some(r => {
    const original = originalRequests.value.find(o => o.id === r.id)
    return original && (original.hora !== r.hora || original.responsable !== r.responsable)
  })
})

const saveRequestsChanges = async () => {
  if (!hasChanges.value) {
    saveModalTitle.value = 'Sin cambios'
    saveModalMessage.value = 'No se realizaron modificaciones.'
    showSaveModal.value = true
    return
  }

  try {
    // Si requests.value no es un array (aunque ya lo verificamos arriba), no iteramos.
    if (!Array.isArray(requests.value)) return
    
    for (const r of requests.value) {
      const original = originalRequests.value.find(o => o.id === r.id)
      if (!original) continue

      if (original.hora !== r.hora || original.responsable !== r.responsable) {
        await updateRequestAPI(r.id, {
          hora: r.hora,
          responsable: r.responsable
        })
      }
    }

    saveModalTitle.value = 'Éxito'
    saveModalMessage.value = 'Cambios guardados.'
    showSaveModal.value = true

    await refreshRequests()

  } catch (e) {}
}

watch(() => siteConfig.requests, (newRequests) => {
  // CORRECCIÓN 3: Asegura que originalRequests se inicializa con un Array
  originalRequests.value = JSON.parse(JSON.stringify(Array.isArray(newRequests) ? newRequests : []))
}, { deep: true, immediate: true }) // Agregado immediate: true para inicialización temprana

const confirmDelete = (i) => { deleteIndex.value = i; showDeletePopup.value = true }
const cancelDelete = () => { showDeletePopup.value = false; deleteIndex.value = null }

const deleteRequest = async () => {
  try {
    const id = requests.value[deleteIndex.value].id
    await deleteRequestAPI(id)
    // Asegura que siteConfig.requests es un array antes de splice
    if (Array.isArray(siteConfig.requests)) {
      siteConfig.requests.splice(siteConfig.requests.findIndex(r => r.id === id), 1)
      saveSiteConfig()
    }
  } catch (e) {}

  showDeletePopup.value = false
  deleteIndex.value = null
}

const refreshRequests = async () => {
  try {
    const { data } = await fetchRequests()

    // CORRECCIÓN 4: Solo actualiza siteConfig.requests si la respuesta es un Array.
    if (Array.isArray(data)) {
      siteConfig.requests = data
      saveSiteConfig()
      originalRequests.value = JSON.parse(JSON.stringify(data))
    } else {
      // Si el backend devuelve null o un objeto, lo tratamos como array vacío
      siteConfig.requests = [] 
      saveSiteConfig()
      originalRequests.value = []
    }
  } catch (e) {
    // En caso de error de API, establece la lista como array vacío para evitar fallos
    siteConfig.requests = []
  }
}


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
