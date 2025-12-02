<template>
  <div class="popup-overlay">
    <div class="popup-container login-popup">
      <div class="popup-header">
        <h3 class="popup-title">Login de Administrador</h3>
        <button class="close-btn" @click="router.push('/login')">&times;</button>
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
import { LoginAuth } from '@/api/auth'

const router = useRouter()

const email = ref('')
const password = ref('')
const error = ref('')

const sanitizeEmail = () => {
  email.value = email.value.replace(/[<>"'`;(){}]/g, '')
}

const sanitizePassword = () => {
  password.value = password.value.replace(/[<>"'`;(){}]/g, '')
}

const handleLogin = async () => {
  error.value = ""

  try {
    const payload = {
      email: email.value,
      password: password.value
    }

    const { data } = await LoginAuth(payload)

    sessionStorage.setItem("access", data.access)
    sessionStorage.setItem("refresh", data.refresh)
    sessionStorage.setItem("authUser", JSON.stringify({ email: email.value }))
    sessionStorage.setItem("authRole", data.role)

    router.push('/admin')
  } catch (err) {
    error.value = "Credenciales incorrectas."
  }
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
