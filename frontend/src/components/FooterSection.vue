<template>
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="h5 mb-4">DY Prods</h3>
          <p>Tu estudio fotográfico de confianza para capturar los momentos más importantes de tu vida.</p>
          <div class="social-icons">
            <a href="#" class="social-link facebook" aria-label="Facebook">
              <i class="fab fa-facebook-f"></i>
            </a>
            <a 
              href="https://www.instagram.com/DY_Prods/" 
              @click="openInstagram" 
              target="_blank" 
              rel="noopener noreferrer" 
              class="social-link instagram"
              aria-label="Instagram"
            >
              <i class="fab fa-instagram"></i>
            </a>
            <a href="#" class="social-link twitter" aria-label="Twitter">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="#" class="social-link linkedin" aria-label="LinkedIn">
              <i class="fab fa-linkedin-in"></i>
            </a>
          </div>
        </div>
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="h5 mb-4">Contacto</h3>
          <div class="contact-info">
            <a 
              href="https://wa.me/5356601651" 
              class="contact-link whatsapp" 
              target="_blank" 
              rel="noopener noreferrer"
              aria-label="Contactar por WhatsApp +53 56601651"
            >
              <i class="fab fa-whatsapp me-2"></i> +53 56601651
            </a>
            <a 
              href="https://wa.me/5355494545" 
              class="contact-link whatsapp" 
              target="_blank" 
              rel="noopener noreferrer"
              aria-label="Contactar por WhatsApp +53 55494545"
            >
              <i class="fab fa-whatsapp me-2"></i> +53 55494545
            </a>
            <a 
              href="mailto:dyprods0581@gmail.com" 
              class="contact-link email"
              aria-label="Enviar email a dyprods0581@gmail.com"
            >
              <i class="fas fa-envelope me-2"></i> dyprods0581@gmail.com
            </a>
          </div>
        </div>
        <div class="col-lg-4">
          <h3 class="h5 mb-4">Horario</h3>
          <p>Lunes a Viernes: 9:00 AM - 6:00 PM</p>
          <p>Sábados: 10:00 AM - 3:00 PM</p>
          <p>Domingos: Cerrado</p>
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
const openInstagram = (event) => {
  // Detecta si es un dispositivo móvil
  const esMovil = /Android|webOS|iPhone|iPad|iPod|blackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
  
  if (esMovil) {
    event.preventDefault() // evitar abrir el enlace web inmediatamente
    window.location.href = "instagram://user?username=DY_Prods" // Intenta abrir la aplicación
    
    // Si la app no está instalada, redirige al enlace web después de un tiempo
    setTimeout(() => {
      window.location.href = "https://www.instagram.com/DY_Prods/"
    }, 500)
  }
}
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

.contact-link:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateX(5px);
  color: white;
}

.contact-link.whatsapp:hover {
  background: #25d366;
  color: white;
}

.contact-link.email:hover {
  background: var(--secondary-color, #e67e22);
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