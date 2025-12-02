<template>
  <div class="card">
    <div class="card-header">
      <h5 class="mb-0">Reportes del Sistema</h5>
    </div>

    <div class="card-body">

      <p class="text-muted mb-3">
        Descarga reportes generados automáticamente desde el backend.
      </p>

      <div class="d-grid gap-3">

        <button class="btn btn-primary" @click="downloadReport('users')">
          <i class="fas fa-users me-2"></i> Reporte de Usuarios
        </button>

        <button class="btn btn-primary" @click="downloadReport('roles')">
          <i class="fas fa-id-badge me-2"></i> Reporte de Roles
        </button>

        <button class="btn btn-primary" @click="downloadReport('requests')">
          <i class="fas fa-list me-2"></i> Reporte de Solicitudes
        </button>

        <button class="btn btn-primary" @click="downloadReport('config-default')">
          <i class="fas fa-cog me-2"></i> Configuración por Defecto
        </button>

        <button class="btn btn-primary" @click="downloadReport('config-current')">
          <i class="fas fa-cog me-2"></i> Configuración Actual
        </button>

      </div>

    </div>
  </div>
</template>

<script setup>
import {
  fetchReportUsers,
  fetchReportRoles,
  fetchReportRequests,
  fetchReportDefaultConfig,
  fetchReportCurrentConfig
} from '@/api/reports'

const downloadReport = async (type) => {
  const map = {
    "users": fetchReportUsers,
    "roles": fetchReportRoles,
    "requests": fetchReportRequests,
    "config-default": fetchReportDefaultConfig,
    "config-current": fetchReportCurrentConfig,
  }

  const request = map[type]
  const filename = `${type}.pdf`

  try {
    const response = await request()

    const blob = new Blob([response.data], { type: "application/pdf" })
    const link = document.createElement("a")

    link.href = URL.createObjectURL(blob)
    link.download = filename
    link.click()

    URL.revokeObjectURL(link.href)
  } catch (e) {
    console.error(e)
  }
}
</script>
