<template>
  <section id="contact" class="py-5 bg-light">
    <div class="container">
      <h2 class="text-center section-title">Reserva tu Sesión</h2>
      <div class="row justify-content-center">
        <div class="col-lg-8">
          <form @submit.prevent="submitForm" class="contact-form">
            <div class="row g-3">
              <div class="col-md-6">
                <label for="name" class="form-label">Nombre *</label>
                <input 
                  type="text" 
                  :class="['form-control', { 'is-invalid': hasError('name') }]" 
                  id="name" 
                  v-model="formData.name"
                  @blur="validateField('name')"
                  @input="handleNameInput"
                  @keypress="preventInvalidNameChars"
                  required
                >
                <div v-if="hasError('name')" class="invalid-feedback">
                  {{ errors.name }}
                </div>
              </div>
              <div class="col-md-6">
                <label for="email" class="form-label">Email *</label>
                <input 
                  type="email" 
                  :class="['form-control', { 'is-invalid': hasError('email') }]" 
                  id="email" 
                  v-model="formData.email"
                  @blur="validateField('email')"
                  @input="hasAttemptedSubmit && validateField('email')"
                  required
                >
                <div v-if="hasError('email')" class="invalid-feedback">
                  {{ errors.email }}
                </div>
              </div>
              <div class="col-md-6">
                <label for="phone" class="form-label">Teléfono *</label>
                <input 
                  type="tel" 
                  :class="['form-control', { 'is-invalid': hasError('phone') }]" 
                  id="phone" 
                  v-model="formData.phone"
                  @blur="validateField('phone')"
                  @input="hasAttemptedSubmit && validateField('phone')"
                  required
                >
                <div v-if="hasError('phone')" class="invalid-feedback">
                  {{ errors.phone }}
                </div>
              </div>
              <div class="col-md-6">
                <label for="service" class="form-label">Servicio *</label>
                <select 
                  :class="['form-select', { 'is-invalid': hasError('service') }]" 
                  id="service" 
                  v-model="formData.service"
                  @blur="validateField('service')"
                  @change="validateField('service')"
                  required
                >
                  <option value="" disabled>Selecciona un servicio</option>
                  <option value="retrato">Fotografía de Retrato</option>
                  <option value="evento">Fotografía de Evento</option>
                  <option value="comercial">Fotografía Comercial</option>
                  <option value="video">Videografía</option>
                </select>
                <div v-if="hasError('service')" class="invalid-feedback">
                  {{ errors.service }}
                </div>
              </div>
              <div class="col-12">
                <label for="date" class="form-label">Fecha preferida *</label>
                <input 
                  type="date" 
                  :class="['form-control', { 'is-invalid': hasError('date') }]" 
                  id="date" 
                  v-model="formData.date"
                  @blur="validateField('date')"
                  @change="validateField('date')"
                  :min="new Date().toISOString().split('T')[0]"
                  required
                >
                <div v-if="hasError('date')" class="invalid-feedback">
                  {{ errors.date }}
                </div>
              </div>
              <div class="col-12">
                <label for="message" class="form-label">Mensaje *</label>
                <textarea 
                  :class="['form-control', { 'is-invalid': hasError('message') }]" 
                  id="message" 
                  rows="5" 
                  v-model="formData.message"
                  @blur="validateField('message')"
                  @input="hasAttemptedSubmit && validateField('message')"
                  placeholder="Cuéntanos más detalles sobre lo que necesitas..."
                  required
                ></textarea>
                <div v-if="hasError('message')" class="invalid-feedback">
                  {{ errors.message }}
                </div>
                <div class="form-text">
                  {{ formData.message.length }}/500 caracteres
                </div>
              </div>
              <div class="col-12 text-center mt-4">
                <button 
                  type="submit" 
                  class="btn btn-primary btn-lg px-5"
                  :disabled="isSubmitting"
                >
                  {{ isSubmitting ? 'Enviando...' : 'Enviar Solicitud' }}
                </button>
              </div>
            </div>
          </form>
          
          <!-- Pop-up de éxito -->
          <SuccessPopup 
            :is-visible="showSuccessPopup"
            :message="successMessage"
            :auto-close="6000"
            @close="closeSuccessPopup"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import SuccessPopup from '../common/SuccessPopup.vue'

const isSubmitting = ref(false)
const hasAttemptedSubmit = ref(false)
const showSuccessPopup = ref(false)
const successMessage = ref('')

const formData = reactive({
  name: '',
  email: '',
  phone: '',
  service: '',
  date: '',
  message: ''
})

// Reglas de validación
const validationRules = {
  name: (value) => {
    if (!value || !value.trim()) return 'El nombre es obligatorio'
    if (value.trim().length < 2) return 'El nombre debe tener al menos 2 caracteres'
    if (value.length > 50) return 'El nombre no puede tener más de 50 caracteres'
    
    // Verificar que no contenga números
    if (/\d/.test(value)) {
      return 'El nombre no puede contener números'
    }
    
    // Solo permitir letras (incluye acentos) y espacios
    const allowedPattern = /^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$/
    if (!allowedPattern.test(value)) {
      return 'El nombre solo puede contener letras y espacios'
    }
    
    // Verificar que no tenga espacios múltiples consecutivos
    if (/\s{2,}/.test(value)) {
      return 'El nombre no puede tener espacios múltiples consecutivos'
    }
    
    // Verificar que no empiece o termine con espacios
    if (value !== value.trim()) {
      return 'El nombre no puede empezar o terminar con espacios'
    }
    
    return null
  },
  email: (value) => {
    if (!value || !value.trim()) return 'El email es obligatorio'
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(value)) return 'Por favor ingresa un email válido'
    return null
  },
  phone: (value) => {
    if (!value || !value.trim()) return 'El teléfono es obligatorio'
    
    // Limpiar el número de espacios para validación
    const cleanPhone = value.replace(/\s/g, '')
    
    // Validar formato de teléfono (permitir +, -, (), espacios y números)
    const phoneRegex = /^[\d\s+()-]{8,15}$/
    if (!phoneRegex.test(value)) {
      return 'Por favor ingresa un teléfono válido (8-15 dígitos)'
    }
    
    // Verificar que tenga al menos 8 dígitos
    const digitCount = cleanPhone.replace(/[^\d]/g, '').length
    if (digitCount < 8) {
      return 'El teléfono debe tener al menos 8 dígitos'
    }
    
    return null
  },
  service: (value) => {
    if (!value) return 'Seleccionar un servicio es obligatorio'
    return null
  },
  date: (value) => {
    if (!value) return 'Seleccionar una fecha es obligatorio'
    const selectedDate = new Date(value)
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    if (selectedDate < today) return 'La fecha debe ser posterior al dia de hoy'
    return null
  },
  message: (value) => {
    if (!value || !value.trim()) return 'El mensaje es obligatorio'
    if (value.trim().length < 10) return 'El mensaje debe tener al menos 10 caracteres'
    if (value.length > 500) return 'El mensaje no puede tener más de 500 caracteres'
    return null
  }
}

// Errores de validación
const errors = reactive({})

// Validar campo individual
const validateField = (fieldName) => {
  const error = validationRules[fieldName](formData[fieldName])
  if (error) {
    errors[fieldName] = error
    hasAttemptedSubmit.value = true // Marcar que ya se intentó validar
  } else {
    delete errors[fieldName]
  }
  return !error
}

// Validar todos los campos
const validateForm = () => {
  let isValid = true
  Object.keys(validationRules).forEach(field => {
    if (!validateField(field)) {
      isValid = false
    }
  })
  return isValid
}

// Función para verificar si un campo tiene error
const hasError = (fieldName) => {
  return hasAttemptedSubmit.value && !!errors[fieldName]
}

// Escuchar eventos de pre-selección de servicio
onMounted(() => {
  window.addEventListener('preselect-service', (event) => {
    formData.service = event.detail.service
    if (event.detail.message) {
      formData.message = event.detail.message
    }
    // Limpiar errores si se pre-rellena
    if (hasAttemptedSubmit.value) {
      validateField('service')
      if (event.detail.message) {
        validateField('message')
      }
    }
  })
})

const submitForm = async () => {
  hasAttemptedSubmit.value = true
  
  // Validar todo el formulario
  if (!validateForm()) {
    // Si hay errores, hacer scroll al primer campo con error
    const firstErrorField = Object.keys(errors)[0]
    if (firstErrorField) {
      const element = document.getElementById(firstErrorField)
      if (element) {
        element.focus()
        element.scrollIntoView({ behavior: 'smooth', block: 'center' })
      }
    }
    return
  }
  
  isSubmitting.value = true
  
  // Simular envío de formulario (como en el original)
  setTimeout(() => {
    // Mostrar pop-up de éxito
    successMessage.value = `¡Gracias ${formData.name}! Tu solicitud ha sido recibida exitosamente. Te contactaremos pronto a ${formData.email} para confirmar tu reserva de ${formData.service}.`
    showSuccessPopup.value = true
    
    // Limpiar el formulario y estados
    Object.keys(formData).forEach(key => {
      formData[key] = ''
    })
    Object.keys(errors).forEach(key => {
      delete errors[key]
    })
    hasAttemptedSubmit.value = false
    isSubmitting.value = false
  }, 1000)
}

// Función para cerrar el pop-up de éxito
const closeSuccessPopup = () => {
  showSuccessPopup.value = false
  successMessage.value = ''
}

// Prevenir caracteres inválidos en el nombre durante la escritura
const preventInvalidNameChars = (event) => {
  const char = event.key
  
  // Permitir teclas de control (backspace, delete, tab, escape, enter, etc.)
  if (event.ctrlKey || event.altKey || event.metaKey) {
    return true
  }
  
  // Permitir teclas especiales (flechas, home, end, etc.)
  if (event.key.length > 1) {
    return true
  }
  
  // Solo permitir letras (incluye acentos) y espacios
  const allowedChars = /^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]$/
  if (!allowedChars.test(char)) {
    event.preventDefault()
    return false
  }
  
  return true
}

// Manejar input del nombre con validación adicional
const handleNameInput = (event) => {
  let value = event.target.value
  
  // Limpiar caracteres no permitidos que puedan haber pasado
  value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]/g, '')
  
  // Prevenir espacios múltiples consecutivos
  value = value.replace(/\s{2,}/g, ' ')
  
  // Actualizar el valor
  formData.name = value
  
  // Validar si ya se intentó enviar el formulario
  if (hasAttemptedSubmit.value) {
    validateField('name')
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

.contact-form {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background-color: var(--secondary-color, #e67e22);
  border-color: var(--secondary-color, #e67e22);
}

.btn-primary:hover {
  background-color: #d35400;
  border-color: #d35400;
}

/* Estilos para campos con error - Reforzados */
.is-invalid,
.form-control.is-invalid,
.form-select.is-invalid {
  border: 2px solid #dc3545 !important;
  border-color: #dc3545 !important;
  box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25) !important;
  animation: shake 0.5s ease-in-out;
  background-image: none !important;
  background-color: rgba(220, 53, 69, 0.05) !important;
}

.form-control.is-invalid:focus,
.form-select.is-invalid:focus {
  border-color: #dc3545 !important;
  box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25) !important;
  outline: none;
}

/* Asegurar que el estilo se aplique incluso con validación HTML5 */
.form-control:invalid.is-invalid,
.form-select:invalid.is-invalid {
  border-color: #dc3545 !important;
}

.form-control:valid.is-invalid,
.form-select:valid.is-invalid {
  border-color: #dc3545 !important;
}

.invalid-feedback {
  display: block;
  font-size: 0.875rem;
  color: #dc3545;
  font-weight: 500;
  margin-top: 0.25rem;
}

/* Animación de shake para campos inválidos */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-2px); }
  20%, 40%, 60%, 80% { transform: translateX(2px); }
}

/* Estilos para campos válidos */
.form-control:valid:not(:placeholder-shown),
.form-select:valid:not([value=""]) {
  border-color: #28a745;
}

.form-control:valid:not(:placeholder-shown):focus,
.form-select:valid:not([value=""]):focus {
  border-color: #28a745;
  box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25);
}

/* Contador de caracteres */
.form-text {
  font-size: 0.8rem;
  color: #6c757d;
  margin-top: 0.25rem;
}

/* Labels obligatorios */
.form-label {
  font-weight: 600;
  color: var(--primary-color, #2c3e50);
  margin-bottom: 0.5rem;
}

/* Botón deshabilitado durante envío */
.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Transiciones suaves */
.form-control, .form-select {
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

/* Mejoras de responsividad para dispositivos pequeños */
@media (max-width: 576px) {
  .contact-form {
    padding: 20px 15px !important;
    margin: 0 5px;
  }
  
  .section-title {
    font-size: 1.4rem !important;
    margin-bottom: 20px !important;
  }
  
  .form-label {
    font-size: 0.9rem !important;
    margin-bottom: 0.3rem !important;
  }
  
  .form-control, .form-select {
    font-size: 0.9rem !important;
    padding: 10px 12px !important;
  }
  
  textarea.form-control {
    min-height: 100px !important;
  }
  
  .btn-lg {
    width: 100% !important;
    margin-top: 15px !important;
  }
  
  .invalid-feedback {
    font-size: 0.8rem !important;
  }
  
  .form-text {
    font-size: 0.75rem !important;
  }
}

@media (max-width: 400px) {
  .contact-form {
    padding: 15px 10px !important;
  }
  
  .section-title {
    font-size: 1.2rem !important;
  }
  
  .form-control, .form-select {
    font-size: 0.85rem !important;
    padding: 8px 10px !important;
  }
  
  .form-label {
    font-size: 0.85rem !important;
  }
}
</style>