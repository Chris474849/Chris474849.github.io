<template>
  <div class="card shadow p-4">
    <h4 class="mb-3">Gestión de Solicitudes</h4>

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
import { siteConfig, saveSiteConfig, loadSiteConfig } from '@/config/siteConfig'
import { computed, ref, onMounted } from 'vue'

onMounted(() => {
  loadSiteConfig()
})

const requests = computed(() => siteConfig.requests || [])
const personal = computed(() => siteConfig.contact.staff.map(s => s.name))

// Estado para modal "Ver Todo"
const showModal = ref(false)
const selectedRequest = ref({})

// Estado para popup de eliminación
const showDeletePopup = ref(false)
const deleteIndex = ref(null)

// Funciones del modal
const viewRequest = (req) => {
  selectedRequest.value = { ...req }
  showModal.value = true
}
const closeModal = () => {
  showModal.value = false
}

// Funciones de eliminación con confirmación
const confirmDelete = (index) => {
  deleteIndex.value = index
  showDeletePopup.value = true
}
const cancelDelete = () => {
  showDeletePopup.value = false
  deleteIndex.value = null
}
const deleteRequest = () => {
  if (deleteIndex.value !== null) {
    siteConfig.requests.splice(deleteIndex.value, 1)
    saveSiteConfig()
  }
  showDeletePopup.value = false
  deleteIndex.value = null
}

// Formatear hora
const formatDate = (datetime) => {
  if (!datetime) return '—'
  const date = new Date(datetime)
  return date.toLocaleString('es-ES', {
    dateStyle: 'short',
    timeStyle: 'short'
  })
}
</script>

<style scoped>
.table th,
.table td {
  vertical-align: middle;
}

.custom-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
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
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  animation: fadeIn 0.25s ease;
}

.modal-content-body p {
  margin-bottom: 6px;
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
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
