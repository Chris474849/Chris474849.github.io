import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:9670", // tu backend FastAPI
})

export const fetchReportUsers = () => api.get("/reports/users", { responseType: "blob" })
export const fetchReportRoles = () => api.get("/reports/roles", { responseType: "blob" })
export const fetchReportRequests = () => api.get("/reports/requests", { responseType: "blob" })
export const fetchReportDefaultConfig = () => api.get("/reports/config/default", { responseType: "blob" })
export const fetchReportCurrentConfig = () => api.get("/reports/config/current", { responseType: "blob" })
