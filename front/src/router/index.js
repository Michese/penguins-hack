import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "../views/HomePage.vue";
import ClassmatesPage from '../views/ClassmatesPage.vue'
import TelegrammPage from "../views/TelegrammPage.vue";
import VKontaktePage from "../views/VKontaktePage.vue";
import UserPage from "../views/UserPage.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/user',
      name: 'user',
      component: UserPage
    },
    {
      path: '/сlassmates',
      name: 'сlassmates',
      component: ClassmatesPage
    },
    {
      path: '/telegramm',
      name: 'telegramm',
      component: TelegrammPage
    },
    {
      path: '/vk',
      name: 'vk',
      component: VKontaktePage
    },
  ]
})

export default router
