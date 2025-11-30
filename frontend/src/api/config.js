import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:9670", // tu backend FastAPI
})

export const fetchDefaultConfig = () => api.get("/config/default")
export const fetchCurrentConfig = () => api.get("/config/current")
export const CreateDefaultConfig = (data) => api.post("/config/default", data)
export const CreateCurrentConfig = (data) => api.post("/config/current", data)
