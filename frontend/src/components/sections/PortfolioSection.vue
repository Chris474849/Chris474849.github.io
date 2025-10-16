<template>
  <section id="portfolio" class="py-5 bg-light">
    <div class="container">
      <h2 class="text-center section-title">{{ siteConfig.portfolio.title }}</h2>
      <div class="row g-4">
        <div class="col-md-4" v-for="image in siteConfig.portfolio.images" :key="image.id">
          <img 
            :src="image.url" 
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
import { onMounted } from 'vue'
import { siteConfig, loadSiteConfig } from '@/config/siteConfig'

onMounted(() => {
  loadSiteConfig()
})

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