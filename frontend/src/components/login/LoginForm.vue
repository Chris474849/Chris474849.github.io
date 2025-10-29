<template>
  <div class="popup-overlay">
    <div class="popup-container login-popup">
      <div class="popup-header">
        <h3 class="popup-title">Login de Administrador</h3>
        <button class="close-btn" @click="router.push('/')">&times;</button>
      </div>

      <div class="popup-content">
        <form @submit.prevent="handleLogin">
          <div class="mb-3 text-start">
            <label for="email" class="form-label">Correo Electrónico</label>
            <input
              type="email"
              id="email"
              v-model="email"
              class="form-control"
              placeholder="usuario@gmail.com"
              @input="sanitizeEmail"
              required
            />
          </div>

          <div class="mb-3 text-start">
            <label for="password" class="form-label">Contraseña</label>
            <input
              type="password"
              id="password"
              v-model="password"
              class="form-control"
              placeholder="Mínimo 8 caracteres"
              @input="sanitizePassword"
              required
            />
          </div>

          <div class="popup-footer">
            <button type="submit" class="btn-primary w-100">Iniciar sesión</button>
            <p v-if="error" class="text-danger mt-3">{{ error }}</p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import appConfig from '@/config/appConfig'

const router = useRouter()
const email = ref('')
const password = ref('')
const error = ref('')

const users = [
  {
    email: appConfig.defaultUser.email,
    password: appConfig.defaultUser.password,
    role: appConfig.defaultUser.role,
  },
  { email: 'user@gmail.com', password: 'password123', role: 'user' },
]

// Sanitiza caracteres peligrosos en email
const sanitizeEmail = () => {
  email.value = email.value.replace(/[<>"'`;(){}]/g, '')
}

// Sanitiza caracteres peligrosos en password
const sanitizePassword = () => {
  password.value = password.value.replace(/[<>"'`;(){}]/g, '')
}

// Validación completa
const handleLogin = () => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$/
  const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#\$%\^&\*]{8,}$/
  const forbidden = /(--|;|\/\*|\*\/|['"<>]|drop|insert|update|delete|script|select|union|--)/i

  if (!emailRegex.test(email.value)) {
    error.value = 'Correo inválido. Debe tener formato nombre@dominio.tld'
    return
  }

  if (forbidden.test(password.value)) {
    error.value = 'La contraseña contiene caracteres no permitidos.'
    return
  }

  const user = users.find(
    (u) => u.email === email.value && u.password === password.value
  )

  if (!user) {
    error.value = 'Credenciales incorrectas.'
    return
  }

  sessionStorage.setItem('authUser', JSON.stringify(user))
  error.value = ''
  router.push('/admin')
}
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease-out;
}

.popup-container.login-popup {
  background: white;
  border-radius: 15px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  max-width: 400px;
  width: 90%;
  animation: slideIn 0.3s ease-out;
  position: relative;
}

.popup-header {
  background: linear-gradient(135deg, #28a745, #20c997);
  color: white;
  padding: 20px;
  text-align: center;
  position: relative;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 35px;
  height: 35px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.1rem;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: rotate(90deg);
}

.popup-content {
  padding: 30px;
}

.popup-title {
  font-size: 1.5rem;
  font-weight: 600;
}

.form-label {
  font-weight: 600;
  color: #2c3e50;
}

.form-control {
  border-radius: 8px;
  border: 1px solid #ccc;
  padding: 10px 12px;
  transition: all 0.3s ease;
}

.form-control:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.25);
}

.btn-primary {
  background-color: #e67e22;
  border: none;
  padding: 12px 0;
  border-radius: 25px;
  font-weight: 600;
  transition: all 0.3s ease;
  color: white;
}

.btn-primary:hover {
  background-color: #d35400;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(230, 126, 34, 0.4);
}

/* Animaciones */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { opacity: 0; transform: scale(0.9) translateY(-50px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
</style>
