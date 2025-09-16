<template>
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="h5 mb-4">DY Prods</h3>
          <p>Tu estudio fotográfico de confianza para capturar los momentos más importantes de tu vida.</p>
          <div class="social-icons">
            <a href="#" class="me-2" aria-label="Facebook">
              <i class="fab fa-facebook"></i>
            </a>
            <a 
              href="https://www.instagram.com/DY_Prods/" 
              @click="openInstagram" 
              target="_blank" 
              rel="noopener noreferrer" 
              class="me-2"
              aria-label="Instagram"
            >
              <i class="fab fa-instagram"></i>
            </a>
            <a href="#" class="me-2" aria-label="Twitter">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="#" class="me-2" aria-label="LinkedIn">
              <i class="fab fa-linkedin"></i>
            </a>
          </div>
        </div>
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="h5 mb-4">Contacto</h3>
          <p>
            <a 
              href="https://wa.me/5356601651" 
              @click="openWhatsApp('5356601651', $event)"
              target="_blank" 
              rel="noopener noreferrer"
              class="whatsapp-link"
              title="Contactar por WhatsApp"
            >
              <i class="fab fa-whatsapp me-2"></i> +53 56601651
            </a>
          </p>
          <p>
            <a 
              href="https://wa.me/5355494545" 
              @click="openWhatsApp('5355494545', $event)"
              target="_blank" 
              rel="noopener noreferrer"
              class="whatsapp-link"
              title="Contactar por WhatsApp"
            >
              <i class="fab fa-whatsapp me-2"></i> +53 55494545
            </a>
          </p>
          <p><i class="fas fa-envelope me-2"></i> dyprods0581@gmail.com</p>
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

const openWhatsApp = (phoneNumber, event) => {
  // Detecta si es un dispositivo móvil
  const esMovil = /Android|webOS|iPhone|iPad|iPod|blackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
  
  if (esMovil) {
    event?.preventDefault() // evitar abrir el enlace web inmediatamente
    
    // Intenta abrir la aplicación de WhatsApp
    window.location.href = `whatsapp://send?phone=${phoneNumber}&text=¡Hola! Me interesa conocer más sobre sus servicios fotográficos.`
    
    // Si la app no está instalada, redirige a WhatsApp Web después de un tiempo
    setTimeout(() => {
      window.open(`https://wa.me/${phoneNumber}?text=¡Hola! Me interesa conocer más sobre sus servicios fotográficos.`, '_blank')
    }, 500)
  }
  // En desktop, abre WhatsApp Web directamente
}
</script>

<style scoped>
footer {
  background-color: var(--dark-color, #1a252f);
  color: white;
  padding: 50px 0;
}

.social-icons a {
  color: white;
  font-size: 2rem; /* Aumentado de 1.5rem a 2rem */
  margin-right: 25px; /* Aumentado de 15px a 25px */
  transition: color 0.3s ease;
  text-decoration: none;
  display: inline-block; /* Para mejor control del spacing */
}

.social-icons a:hover {
  color: var(--secondary-color, #e67e22);
}

/* Instagram hover effect with gradient colors */
.social-icons a:hover .fa-instagram {
  background: linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  transform: scale(1.1);
  transition: all 0.3s ease;
}

/* Fallback for browsers that don't support background-clip: text */
@supports not (-webkit-background-clip: text) {
  .social-icons a:hover .fa-instagram {
    color: #E4405F; /* Instagram pink as fallback */
  }
}

/* Add transition to Instagram icon */
.social-icons .fa-instagram {
  transition: all 0.3s ease;
}

/* Facebook hover effect */
.social-icons a:hover .fa-facebook {
  color: #1877F2; /* Facebook blue */
  transform: scale(1.1);
}

/* Twitter hover effect */
.social-icons a:hover .fa-twitter {
  color: #1DA1F2; /* Twitter blue */
  transform: scale(1.1);
}

/* LinkedIn hover effect */
.social-icons a:hover .fa-linkedin {
  color: #0A66C2; /* LinkedIn blue */
  transform: scale(1.1);
}

/* Add transition to all social icons */
.social-icons i {
  transition: all 0.3s ease;
}

/* Remove margin from last social icon */
.social-icons a:last-child {
  margin-right: 0;
}

/* Add some padding to social icons container for better touch targets */
.social-icons {
  padding: 10px 0;
}

.whatsapp-link {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;
  display: inline-flex;
  align-items: center;
}

.whatsapp-link:hover {
  color: #25D366; /* Color oficial de WhatsApp */
  text-decoration: none;
}

.whatsapp-link i {
  color: #25D366; /* Icono siempre verde WhatsApp */
  font-size: 1.2em;
  transition: transform 0.3s ease;
}

.whatsapp-link:hover i {
  transform: scale(1.1);
}
</style>