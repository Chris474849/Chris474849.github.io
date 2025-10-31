<template>
  <div class="col-md-3">
    <div class="card">
      <div class="card-header"><h5 class="mb-0">Secciones del Sitio</h5></div>
      <div class="list-group list-group-flush">
        <button
          v-for="section in sections"
          :key="section.id"
          @click="$emit('changeSection', section.id)"
          :class="[
            'list-group-item list-group-item-action',
            activeSection === section.id ? 'active' : ''
          ]"
        >
          <i :class="section.icon + ' me-2'"></i>{{ section.name }}
        </button>
      </div>
    </div>

    <div class="card mt-3">
      <div class="card-body text-center">
        <button @click="$emit('save')" class="btn btn-success btn-lg mb-2 w-100">
          <i class="fas fa-save me-2"></i>Guardar Cambios
        </button>
        <button @click="$emit('reset')" class="btn btn-warning w-100">
          <i class="fas fa-undo me-2"></i>Restaurar Por Defecto
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  sections: Array,
  activeSection: String
})
</script>
