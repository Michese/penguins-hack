import { createRouter, createWebHistory } from 'vue-router'
import DataProject from '../views/DataProject.vue'
import About from "../views/About.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: DataProject
    },
    {
      path: '/',
      name: 'about',
      component: About
    },
  ]
})

export default router
