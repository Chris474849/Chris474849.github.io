<template>
  <section id="home" class="hero-section">
    <div class="container text-center">
      <h1 class="display-3 fw-bold mb-4">DY Prods</h1>
      <h2 class="h3 mb-5">Capturando momentos, creando recuerdos</h2>
      <a href="#contact" @click="scrollToContact" class="btn btn-primary btn-lg px-5 py-3">
        Reserva ahora
      </a>
    </div>
  </section>
</template>

<script setup>
const scrollToContact = (event) => {
  event.preventDefault()
  const target = document.querySelector('#contact')
  if (target) {
    target.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  }
}
</script>

<style scoped>
.hero-section {
  min-height: 100vh;
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
              url('https://via.placeholder.com/1920x1080/2c3e50/ffffff?text=DY+Prods') no-repeat center center/cover;
  display: flex;
  align-items: center;
  color: white;
}

section {
  scroll-margin-top: 80px;
}

.btn-primary {
  background-color: var(--secondary-color, #e67e22);
  border-color: var(--secondary-color, #e67e22);
}

.btn-primary:hover {
  background-color: #d35400;
  border-color: #d35400;
}
</style>