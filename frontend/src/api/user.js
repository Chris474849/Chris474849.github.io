import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:9670", // tu backend FastAPI
})

export const fetchUsers = () => api.get("/users")
export const createUsers = (data) => api.post("/users", data)
export const fetchUser = (email) => api.get("/user-id", email)
export const deleteUser = (user_id) => api.delete(`/users/${user_id}`)

