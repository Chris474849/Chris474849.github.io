import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:9670", // tu backend FastAPI
})

export const fetchRequests = () => api.get("/requests/")
export const createRequestAPI = (data) => api.post("/requests/", data)
export const updateRequestAPI = (id, data) => api.put(`/requests/${id}/`, data)
export const deleteRequestAPI = (id) => api.delete(`/requests/${id}/`)

