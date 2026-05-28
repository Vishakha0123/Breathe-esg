import axios from "axios";
export const api=axios.create({
    baseURL: "https://breathe-esg-backend.onrender.com/api"
})