import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:9670", // tu backend FastAPI
})

export const fetchRoles = () => api.get("/roles")
export const CreateRoles = (name) => api.post("/roles", name)

