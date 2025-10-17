<template>
  <section id="about" class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 mb-4 mb-lg-0">
          <img 
            :src="siteConfig.about.image" 
            alt="Nuestro equipo" 
            class="img-fluid rounded"
          >
        </div>
        <div class="col-lg-6">
          <h2 class="section-title text-start">{{ siteConfig.about.title }}</h2>
          <p class="lead">
            {{ siteConfig.about.subtitle }}
          </p>
          <p v-for="paragraph in siteConfig.about.description" :key="paragraph">
            {{ paragraph }}
          </p>
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

.section-title.text-start::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 3px;
  background-color: var(--secondary-color, #e67e22);
}
</style>