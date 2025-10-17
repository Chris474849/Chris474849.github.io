<template>
  <div>
    <AdminHeader :user="user" @logout="logout" />
    <AdminPanel />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import AdminPanel from '@/components/admin/AdminPanel.vue'

const router = useRouter()
const user = ref(null)

onMounted(() => {
  const data = sessionStorage.getItem('authUser')
  if (data) user.value = JSON.parse(data)
  else router.replace('/login')
})

const logout = () => {
  sessionStorage.removeItem('authUser')
  router.push('/')
}
</script>
