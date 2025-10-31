<template>
  <div class="modal d-block" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header"><h5 class="modal-title">Confirmar Acción</h5></div>
        <div class="modal-body">
          <p>¿Estás seguro de que deseas restaurar la configuración por defecto?</p>
        </div>
        <div class="modal-footer">
          <button @click="$emit('cancel')" class="btn btn-secondary">Cancelar</button>
          <button @click="$emit('confirm')" class="btn btn-warning">Restaurar</button>
        </div>
      </div>
    </div>
    <div class="modal-backdrop show"></div>
  </div>
</template>
