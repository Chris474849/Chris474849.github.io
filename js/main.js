   // Smooth scrolling for anchor links
   document.querySelectorAll('a[href^="#"]').forEach(anchor => {
       anchor.addEventListener('click', function(e) {
           e.preventDefault();

           const target = document.querySelector(this.getAttribute('href'));
           if (target) {
               target.scrollIntoView({
                   behavior: 'smooth',
                   block: 'start'
               });
           }
       });
   });

   // Form submission (simulated)
   document.getElementById('booking-form').addEventListener('submit', function(e) {
       e.preventDefault();

       // Get form values
       const name = document.getElementById('name').value;
       const email = document.getElementById('email').value;

       // Show success message (in production, you would handle this with backend processing)
       alert(`¡Gracias ${name}! Tu solicitud ha sido recibida. Te contactaremos pronto en ${email} para confirmar tu reserva.`);
       this.reset();
   });

   function abrirInstagram(event) {
       //Detecta si es un dispositivo movil
       const esMovil = /Android|webOS|iPhone|iPad|iPod|blackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

       if (esMovil) {
           event.preventDefault(); //evitar abrir el enlace web inmediatamente
           window.location.href = "instagram://user?username=DY_Prods"; //Intenta abrir la aplicacion

           //Si la app no esta instalada , redirige al enlace web despues de un tiempo
           setTimeout(() => {
               window.location.href = "https://www.instagram.com/DY_Prods/";
           }, 500);
       }
   }