import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:9670", // tu backend FastAPI
})

export const LoginAuth = (data) => api.post("/login", data)
export const RefreshAuth = (rt) => api.post("/refresh", { rt })

