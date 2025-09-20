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
          <p><i class="fas fa-phone me-2"></i> +53 56601651</p>
          <p><i class="fas fa-phone me-2"></i> +53 55494545</p>
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
</script>

<style scoped>
footer {
  background-color: var(--dark-color, #1a252f);
  color: white;
  padding: 50px 0;
}

.social-icons a {
  color: white;
  font-size: 1.5rem;
  margin-right: 15px;
  transition: color 0.3s ease;
  text-decoration: none;
}

.social-icons a:hover {
  color: var(--secondary-color, #e67e22);
}
</style>