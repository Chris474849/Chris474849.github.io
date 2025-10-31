<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div class="toast show" role="alert">
      <div class="toast-header">
        <i :class="icon + ' me-2'"></i>
        <strong class="me-auto">{{ title }}</strong>
        <button @click="$emit('close')" type="button" class="btn-close"></button>
      </div>
      <div class="toast-body">{{ message }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  message: String,
  icon: String
})
</script>
