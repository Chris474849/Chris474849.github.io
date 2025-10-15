<template>
  <div class="card p-4 shadow" style="width: 350px; background-color: #fff; color: #000;">
    <h3 class="text-center mb-3">Login de Administrador</h3>

    <form @submit.prevent="handleLogin">
      <div class="mb-3">
        <label for="email" class="form-label">Correo Gmail</label>
        <input
          type="email"
          id="email"
          v-model="email"
          class="form-control"
          placeholder="example@gmail.com"
          required
        />
      </div>

      <div class="mb-3">
        <label for="password" class="form-label">Contraseña</label>
        <input
          type="password"
          id="password"
          v-model="password"
          class="form-control"
          placeholder="Mínimo 8 caracteres"
          required
        />
      </div>

      <button type="submit" class="btn btn-primary w-100">Iniciar sesión</button>

      <p v-if="error" class="text-danger text-center mt-3">{{ error }}</p>
    </form>
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

const handleLogin = () => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/
  const passwordRegex = /^[A-Za-z0-9!@#\$%\^&\*]{8,}$/

  if (!emailRegex.test(email.value)) {
    error.value = 'El correo debe tener formato válido @gmail.com'
    return
  }

  if (!passwordRegex.test(password.value)) {
    error.value = 'Contraseña mínima 8 caracteres y sin símbolos inseguros'
    return
  }

  const user = users.find(
    (u) => u.email === email.value && u.password === password.value
  )

  if (!user) {
    error.value = 'Credenciales incorrectas'
    return
  }

  sessionStorage.setItem('authUser', JSON.stringify(user))
  error.value = ''
  router.push('/admin')
}
</script>
