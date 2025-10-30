<template>
  <section id="home" class="hero-section" :style="heroBackgroundStyle">
    <div class="container text-center">
      <h1 class="display-3 fw-bold mb-4">{{ siteConfig.hero.title }}</h1>
      <h2 class="h3 mb-5">{{ siteConfig.hero.subtitle }}</h2>
      <a href="#contact" @click="scrollToContact" class="btn btn-primary btn-lg px-5 py-3">
        {{ siteConfig.hero.ctaText }}
      </a>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { siteConfig, loadSiteConfig } from '@/config/siteConfig'

onMounted(() => {
  loadSiteConfig()
})

const heroBackgroundStyle = computed(() => ({
  background: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('${siteConfig.hero.backgroundImage}') no-repeat center center/cover`
}))

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
