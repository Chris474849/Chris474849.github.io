<template>
  <div v-if="isVisible" class="popup-overlay" @click="closePopup">
    <div class="popup-container" @click.stop>
      <div class="popup-header">
        <div class="success-icon">
          <i class="fas fa-check-circle"></i>
        </div>
        <button class="close-btn" @click="closePopup" aria-label="Cerrar">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <div class="popup-content">
        <h3 class="popup-title">¡Mensaje Enviado!</h3>
        <p class="popup-message">{{ message }}</p>
      </div>
      <div class="popup-footer">
        <button class="btn btn-primary" @click="closePopup">
          Entendido
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  message: {
    type: String,
    default: '¡Tu solicitud ha sido recibida exitosamente!'
  },
  autoClose: {
    type: Number,
    default: 5000 // Auto cerrar en 5 segundos
  }
})

const emit = defineEmits(['close'])

let autoCloseTimer = null

const closePopup = () => {
  if (autoCloseTimer) {
    clearTimeout(autoCloseTimer)
    autoCloseTimer = null
  }
  emit('close')
}

// Auto cerrar después del tiempo especificado
watch(() => props.isVisible, (newVal) => {
  if (newVal && props.autoClose > 0) {
    autoCloseTimer = setTimeout(() => {
      closePopup()
    }, props.autoClose)
  }
})

// Cerrar con tecla Escape
const handleKeydown = (event) => {
  if (event.key === 'Escape' && props.isVisible) {
    closePopup()
  }
}

// Agregar/remover event listener cuando el popup esté visible
watch(() => props.isVisible, (newVal) => {
  if (newVal) {
    document.addEventListener('keydown', handleKeydown)
    // Prevenir scroll en el body
    document.body.style.overflow = 'hidden'
  } else {
    document.removeEventListener('keydown', handleKeydown)
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease-out;
}

.popup-container {
  background: white;
  border-radius: 15px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow: hidden;
  animation: slideIn 0.3s ease-out;
  position: relative;
}

.popup-header {
  background: linear-gradient(135deg, #28a745, #20c997);
  color: white;
  padding: 20px;
  text-align: center;
  position: relative;
}

.success-icon {
  font-size: 3rem;
  margin-bottom: 10px;
  animation: bounceIn 0.6s ease-out;
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
  text-align: center;
}

.popup-title {
  color: var(--primary-color, #2c3e50);
  margin-bottom: 15px;
  font-size: 1.5rem;
  font-weight: 600;
}

.popup-message {
  color: #666;
  line-height: 1.6;
  margin-bottom: 0;
  font-size: 1rem;
}

.popup-footer {
  padding: 0 30px 30px;
  text-align: center;
}

.btn-primary {
  background-color: var(--secondary-color, #e67e22);
  border-color: var(--secondary-color, #e67e22);
  padding: 12px 30px;
  border-radius: 25px;
  font-weight: 600;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  color: white;
}

.btn-primary:hover {
  background-color: #d35400;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(230, 126, 34, 0.4);
}

/* Animaciones */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(-50px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes bounceIn {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

/* Responsive */
@media (max-width: 576px) {
  .popup-container {
    margin: 20px;
    width: calc(100% - 40px);
  }
  
  .popup-content {
    padding: 20px;
  }
  
  .popup-title {
    font-size: 1.3rem;
  }
  
  .success-icon {
    font-size: 2.5rem;
  }
}
</style>