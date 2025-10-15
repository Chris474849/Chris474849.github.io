<template>
  <section id="portfolio" class="py-5 bg-light">
    <div class="container">
      <h2 class="text-center section-title">Nuestro Portafolio</h2>
      <div class="row g-4">
        <div class="col-md-4" v-for="image in portfolioImages" :key="image.id">
          <img 
            :src="image.src" 
            :alt="image.alt" 
            class="img-fluid gallery-img rounded"
            @click="openImage(image)"
          >
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const portfolioImages = ref([
  {
    id: 1,
    src: 'https://via.placeholder.com/600x400/e67e22/ffffff?text=Retrato',
    alt: 'Fotografía de retrato'
  },
  {
    id: 2,
    src: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Evento',
    alt: 'Fotografía de evento'
  },
  {
    id: 3,
    src: 'https://via.placeholder.com/600x400/e67e22/ffffff?text=Comercial',
    alt: 'Fotografía comercial'
  },
  {
    id: 4,
    src: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Producto',
    alt: 'Fotografía de producto'
  },
  {
    id: 5,
    src: 'https://via.placeholder.com/600x400/e67e22/ffffff?text=Boda',
    alt: 'Fotografía de boda'
  },
  {
    id: 6,
    src: 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=Arte',
    alt: 'Fotografía artística'
  }
])

const openImage = (image) => {
  // En una implementación futura, aquí se puede abrir un modal o lightbox
  console.log('Abriendo imagen:', image.alt)
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

.gallery-img {
  height: 250px;
  object-fit: cover;
  cursor: pointer;
  transition: all 0.3s ease;
}

.gallery-img:hover {
  opacity: 0.8;
}
</style>