<script setup>
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import ServicesSection from './components/ServicesSection.vue'
import PortfolioSection from './components/PortfolioSection.vue'
import AboutSection from './components/AboutSection.vue'
import ContactSection from './components/ContactSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <div>
    <NavBar />
    <HeroSection />
    <ServicesSection />
    <PortfolioSection />
    <AboutSection />
    <ContactSection />
    <FooterSection />
  </div>
</template>

<style>
:root {
  --primary-color: #2c3e50;
  --secondary-color: #e67e22;
  --light-color: #ecf0f1;
  --dark-color: #1a252f;
}

body {
  font-family: 'Montserrat', sans-serif;
  color: var(--primary-color);
  background-color: var(--light-color);
}
</style>
