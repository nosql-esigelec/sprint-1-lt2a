import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:8080/v1", // Remplacez par l'URL de votre API
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true
});
const apiClientX = axios.create({
  baseURL: 'http://localhost:8080/v1',
  headers: {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
  }
});

export default apiClient;
