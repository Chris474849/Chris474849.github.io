<template>
  <section 
    id="portfolio" 
    class="py-5 bg-light"
    v-if="siteConfig.portfolio"
  >
    <div class="container">
      <h2 class="text-center section-title">{{ siteConfig.portfolio.title }}</h2>

      <div class="row g-4">
        <div 
          class="col-md-4" 
          v-for="image in siteConfig.portfolio.images" 
          :key="image.id"
        >
          <div class="gallery-wrapper">
            <img 
              :src="image.url" 
              :alt="image.alt" 
              class="img-fluid gallery-img rounded"
              @click="openImage(image)"
            >
          </div>
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

.gallery-wrapper {
  height: 250px; /* altura fija para todas las imágenes */
  overflow: hidden;
}

.gallery-img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* asegura que la imagen cubra todo el contenedor sin deformarse */
  cursor: pointer;
  transition: all 0.3s ease;
}

.gallery-img:hover {
  opacity: 0.8;
}
</style>