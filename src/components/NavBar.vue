<template>
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
    <div class="container">
      <a class="navbar-brand" href="#home">DY Prods</a>
      <button 
        class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarNav" 
        aria-controls="navbarNav" 
        aria-expanded="false" 
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link" href="#home" @click="scrollToSection">Inicio</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#services" @click="scrollToSection">Servicios</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#portfolio" @click="scrollToSection">Portafolio</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#about" @click="scrollToSection">Nosotros</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#contact" @click="scrollToSection">Contacto</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { onMounted } from 'vue'

let navbarCollapse = null

onMounted(() => {
  // Get reference to Bootstrap collapse instance
  navbarCollapse = document.getElementById('navbarNav')
})

const scrollToSection = (event) => {
  event.preventDefault()
  const target = document.querySelector(event.target.getAttribute('href'))
  if (target) {
    target.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  }
  
  // Close mobile menu after navigation
  closeNavbar()
}

const closeNavbar = () => {
  if (navbarCollapse && navbarCollapse.classList.contains('show')) {
    // Use Bootstrap's collapse method to close the menu
    const bsCollapse = new window.bootstrap.Collapse(navbarCollapse, {
      toggle: false
    })
    bsCollapse.hide()
  }
}
</script>

<style scoped>
.navbar {
  background-color: var(--primary-color, #2c3e50);
}
</style>