import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  }
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authAPI = {
  register: (email, password) => api.post('/auth/register', { email, password }),
  login: (email, password) => api.post('/auth/login', { email, password }),
};

export const vehiclesAPI = {
  getAll: () => api.get('/vehicles'),
  getById: (id) => api.get(`/vehicles/${id}`),
  create: (vehicle) => api.post('/vehicles', vehicle),
  update: (id, vehicle) => api.put(`/vehicles/${id}`, vehicle),
  delete: (id) => api.delete(`/vehicles/${id}`),
  search: (params) => api.get('/vehicles/search', { params }),
  purchase: (id, quantity) => api.post(`/vehicles/${id}/purchase`, { quantity }),
  restock: (id, quantity) => api.post(`/vehicles/${id}/restock`, { quantity }),
};

export default api;
