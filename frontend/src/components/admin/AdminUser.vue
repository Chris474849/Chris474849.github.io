<template>
  <div class="card shadow p-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h4 class="mb-0">Gestión de Usuarios</h4>

      <div class="d-flex gap-2">
        <button class="btn btn-outline-primary" @click="refreshUsers">
          <i class="fas fa-sync-alt me-2"></i> Refrescar
        </button>

        <button class="btn btn-success" @click="openCreateModal">
          <i class="fas fa-plus me-2"></i> Crear Usuario
        </button>
      </div>
    </div>

    <table class="table table-striped align-middle">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Email</th>
          <th>Rol</th>
          <th>Eliminar</th>

        </tr>
      </thead>

      <tbody>
        <tr v-for="u in users" :key="u.id">
          <td>{{ u.id }}</td>
          <td>{{ u.email }}</td>
          <td>{{ u.role }}</td>
          <td>
          <button 
              class="btn btn-danger btn-sm"
              @click="confirmDelete(u.id)"
              :disabled="u.email === currentUserId"
          >
            <i class="fas fa-trash"></i>
        </button>
        </td>

        </tr>

        <tr v-if="!users.length">
          <td colspan="4" class="text-center text-muted">
            No hay usuarios registrados.
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="showCreateModal" class="custom-modal-overlay" @click.self="closeCreateModal">
      <div class="custom-modal">
        <div class="modal-content">
          <button class="close-btn" @click="closeCreateModal">✖</button>
          <h3>Crear nuevo usuario</h3>

          <div class="mt-3">
            <label class="form-label">Email</label>
            <input v-model="newUser.email" type="email" class="form-control" />

            <label class="form-label mt-3">Rol</label>
            <select v-model="newUser.role" class="form-select">
              <option disabled value="">Seleccionar...</option>
                <option 
                v-for="r in roles" 
                :key="r.id" 
                :value="r.name"
                >
                {{ r.name }}
                </option>

            </select>

            <label class="form-label mt-3" v-if="newUser.role !== 'client'">Contraseña</label>
            <input 
            v-if="newUser.role !== 'client'"
            v-model="newUser.password"
            type="password"
            class="form-control" 
            />


            <button class="btn btn-success w-100 mt-4" @click="submitUser">
              Crear Usuario
            </button>

            <p v-if="createMessage" class="mt-3 text-center" :class="messageClass">
              {{ createMessage }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showConfirmModal" class="custom-modal-overlay" @click.self="closeConfirmModal">
        <div class="custom-modal">
            <div class="modal-content">
            <h3 class="text-center mb-3">Confirmar eliminación</h3>
            <p class="text-center">¿Seguro que deseas eliminar este usuario?</p>

            <div class="d-flex justify-content-between mt-4">
                <button class="btn btn-secondary w-50 me-2" @click="closeConfirmModal">Cancelar</button>
                <button class="btn btn-danger w-50" @click="performDeleteUser">Eliminar</button>
            </div>
            </div>
        </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchUsers, createUsers } from '@/api/user'
import { fetchRoles } from '@/api/role'
import { deleteUser } from '@/api/user'


const users = ref([])
const roles = ref([])
const showConfirmModal = ref(false)
const userToDelete = ref(null)


const showCreateModal = ref(false)
const createMessage = ref('')
const messageClass = ref('')

const newUser = ref({
  email: '',
  role: '',
  password: ''
})

const session = JSON.parse(sessionStorage.getItem('authUser') || '{}')
const currentUserId = session?.email || null
console.log(session)
onMounted(() => {
  refreshUsers()
  loadRoles()
})

const loadRoles = async () => {
  try {
    const { data } = await fetchRoles()
    roles.value = data
  } catch (e) {
    roles.value = []
  }
}

const refreshUsers = async () => {
  try {
    const { data } = await fetchUsers()
    users.value = Array.isArray(data) ? data : []
  } catch (e) {
    users.value = []
  }
}

const openCreateModal = () => {
  newUser.value = { email: '', role: '', password: '' }
  createMessage.value = ''
  showCreateModal.value = true
}

const closeCreateModal = () => {
  showCreateModal.value = false
}

const confirmDelete = (id) => {
  if (id === currentUserId) return
  userToDelete.value = id
  showConfirmModal.value = true
}

const closeConfirmModal = () => {
  showConfirmModal.value = false
  userToDelete.value = null
}

const performDeleteUser = async () => {
  try {
    await deleteUser(userToDelete.value)
    refreshUsers()
  } catch (e) {}

  closeConfirmModal()
}


const submitUser = async () => {
  createMessage.value = ''
  messageClass.value = ''

  try {
    const payload = {
      email: newUser.value.email,
      role: newUser.value.role,
      password: newUser.value.password
    }

    await createUsers(payload)

    createMessage.value = 'Usuario creado correctamente'
    messageClass.value = 'text-success'

    refreshUsers()
  } catch (err) {
    createMessage.value = err.response?.data?.detail || 'Error creando usuario'
    messageClass.value = 'text-danger'
  }
}

const deleteSelectedUser = async (id) => {
  if (id === currentUserId) return

  try {
    await deleteUser(id)
    refreshUsers()
  } catch (e) {}
}

</script>

<style scoped>
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

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.text-success { color: #28a745; }
.text-danger { color: #dc3545; }
</style>
