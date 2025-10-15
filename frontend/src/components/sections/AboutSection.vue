<template>
  <section id="about" class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 mb-4 mb-lg-0">
          <img 
            src="https://via.placeholder.com/800x600/2c3e50/ffffff?text=Nuestro+Equipo" 
            alt="Nuestro equipo" 
            class="img-fluid rounded"
          >
        </div>
        <div class="col-lg-6">
          <h2 class="section-title text-start">Sobre DY Prods</h2>
          <p class="lead">
            Somos un equipo apasionado de fotógrafos y videógrafos comprometidos con la excelencia.
          </p>
          <p>
            Fundado en 2015, DY Prods se ha convertido en uno de los estudios fotográficos 
            más reconocidos de la región. Nuestro enfoque se centra en capturar la belleza 
            auténtica en cada toma, ya sea para eventos personales, corporativos o proyectos 
            creativos.
          </p>
          <p>
            Trabajamos con equipos de última generación y técnicas innovadoras para 
            garantizar resultados excepcionales en cada proyecto.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// No se necesita lógica adicional para este componente
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