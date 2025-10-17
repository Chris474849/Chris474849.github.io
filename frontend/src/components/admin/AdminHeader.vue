<template>
  <nav class="navbar navbar-dark bg-dark px-4">
    <span class="navbar-brand">Panel de Administración</span>
    <div>
      <span class="text-light me-3">{{ user?.email }}</span>
      <button class="btn btn-danger btn-sm" @click="$emit('logout')">
        Cerrar sesión
      </button>
    </div>
  </nav>
</template>

<script setup>
defineProps({ user: Object })
</script>
