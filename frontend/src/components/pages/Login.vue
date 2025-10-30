<template>
  <div class="login-wrapper d-flex align-items-center justify-content-center vh-100">
    <LoginForm />
  </div>
</template>

<script setup>
import LoginForm from '@/components/login/LoginForm.vue'
</script>

<style scoped>
.login-wrapper {
  background: linear-gradient(135deg, #007bff, #6610f2);
  color: white;
}
</style>
