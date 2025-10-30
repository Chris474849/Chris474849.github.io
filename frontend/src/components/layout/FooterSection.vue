<template>
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="h5 mb-4">{{ siteConfig.siteName }}</h3>
          <p>{{ siteConfig.footer.description }}</p>
          <div class="social-icons">
            <a 
              v-for="(social, index) in socialLinks" 
              :key="index" 
              :href="social.link" 
              :class="['social-link', social.class]" 
              :aria-label="social.label"
              target="_blank" 
              rel="noopener noreferrer"
            >
              <i :class="social.icon"></i>
            </a>
          </div>
        </div>
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="h5 mb-4">Contacto</h3>
          <div class="contact-info">
            <a 
              v-for="(contact, index) in contactLinks" 
              :key="index" 
              :href="contact.link" 
              class="contact-link" 
              :aria-label="contact.label"
              target="_blank" 
              rel="noopener noreferrer"
              :class="contact.class"
            >
              <i :class="contact.icon" class="me-2"></i> {{ contact.text }}
            </a>
          </div>
        </div>
        <div class="col-lg-4">
          <h3 class="h5 mb-4">Horario</h3>
          <p>{{ siteConfig.footer.schedule.weekdays }}</p>
          <p>{{ siteConfig.footer.schedule.saturday }}</p>
          <p>{{ siteConfig.footer.schedule.sunday }}</p>
        </div>
      </div>
      <hr class="my-4 bg-light">
      <div class="text-center">
        <p class="mb-0">&copy; 2025 DY Prods. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { siteConfig, loadSiteConfig } from '@/config/siteConfig'

onMounted(() => {
  loadSiteConfig()
})

const socialLinks = computed(() => [
  { 
    icon: 'fab fa-facebook-f', 
    link: siteConfig.footer.social.facebook, 
    label: 'Facebook', 
    class: 'facebook' 
  },
  { 
    icon: 'fab fa-instagram', 
    link: siteConfig.footer.social.instagram, 
    label: 'Instagram', 
    class: 'instagram' 
  },
  { 
    icon: 'fab fa-twitter', 
    link: siteConfig.footer.social.twitter, 
    label: 'Twitter', 
    class: 'twitter' 
  },
  { 
    icon: 'fab fa-linkedin-in', 
    link: siteConfig.footer.social.linkedin, 
    label: 'LinkedIn', 
    class: 'linkedin' 
  }
])

const contactLinks = computed(() => {
  const phones = siteConfig.footer.contact.phones
  const email = siteConfig.footer.contact.email
  
  const links = []
  
  // Agregar teléfonos
  phones.forEach(phone => {
    const cleanPhone = phone.replace(/[^\d+]/g, '')
    links.push({
      icon: 'fab fa-whatsapp',
      link: `https://wa.me/${cleanPhone}`,
      text: phone,
      label: `Contactar por WhatsApp ${phone}`,
      class: 'whatsapp'
    })
  })
  
  // Agregar email
  links.push({
    icon: 'fas fa-envelope',
    link: `mailto:${email}`,
    text: email,
    label: `Enviar email a ${email}`,
    class: 'email'
  })
  
  return links
})
</script>

<style scoped>
footer {
  background-color: var(--dark-color, #1a252f);
  color: white;
  padding: 50px 0;
}

/* Redes sociales */
.social-icons {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.social-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 45px;
  height: 45px;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  font-size: 1.3rem;
  border-radius: 50%;
  text-decoration: none;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.social-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 50%;
  transform: scale(0);
  transition: transform 0.3s ease;
  z-index: 1;
}

.social-link i {
  position: relative;
  z-index: 2;
}

/* Hover effects con colores específicos de cada red social */
.social-link.facebook:hover {
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(24, 119, 242, 0.4);
}

.social-link.facebook::before {
  background: #1877f2;
}

.social-link.facebook:hover::before {
  transform: scale(1);
}

.social-link.instagram:hover {
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(225, 48, 108, 0.4);
}

.social-link.instagram::before {
  background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
}

.social-link.instagram:hover::before {
  transform: scale(1);
}

.social-link.twitter:hover {
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(29, 161, 242, 0.4);
}

.social-link.twitter::before {
  background: #1da1f2;
}

.social-link.twitter:hover::before {
  transform: scale(1);
}

.social-link.linkedin:hover {
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 119, 181, 0.4);
}

.social-link.linkedin::before {
  background: #0077b5;
}

.social-link.linkedin:hover::before {
  transform: scale(1);
}

/* Información de contacto */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.contact-link {
  color: white;
  text-decoration: none;
  display: flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.05);
}

/* WhatsApp hover (verde) */
.contact-link.whatsapp:hover {
  background: #25d366;
  color: white;
}

/* Correo hover (amarillo) */
.contact-link.email:hover {
  background: #f1c40f;
  color: white;
}

.contact-link i {
  font-size: 1.1rem;
  width: 20px;
}

/* Responsive */
@media (max-width: 768px) {
  footer {
    padding: 30px 0;
  }
  
  .social-icons {
    justify-content: center;
    margin-bottom: 20px;
  }
  
  .contact-info {
    text-align: center;
  }
  
  .social-link {
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
}

@media (max-width: 576px) {
  footer {
    padding: 25px 0;
  }
  
  .social-link {
    width: 38px;
    height: 38px;
    font-size: 1.1rem;
  }
  
  .contact-link {
    padding: 6px 10px;
    font-size: 0.9rem;
  }
  
  h3.h5 {
    font-size: 1.1rem !important;
    margin-bottom: 15px !important;
  }
}
</style>
