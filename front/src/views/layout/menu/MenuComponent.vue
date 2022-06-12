<template>
  <aside id="sidebar" class="sidebar">

    <ul class="sidebar-nav" id="sidebar-nav">

      <li class="nav-item mb-4">
        <router-link :to="{ name: 'home' }"  active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Главная</span>
        </router-link>
      </li>

      <li><span class="blue-color">Аналитика</span></li>

      <li class="nav-item">
        <router-link  :to="{ name: 'user' }" active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Пользователи</span>
        </router-link>
      </li>

      <li class="nav-item">
        <router-link  :to="{ name: 'сlassmates' }" active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Одноклассиники</span>
        </router-link>
      </li>

      <li class="nav-item">
        <router-link  :to="{ name: 'telegramm' }" active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Телеграмм</span>
        </router-link>
      </li>

      <li class="nav-item">
        <router-link  :to="{ name: 'vk' }" active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Вконтакте</span>
        </router-link>
      </li>
    </ul>

  </aside>
</template>

<script>
import { RouterLink } from 'vue-router'
export default {
  name: "MenuComponent",
  components: {
    RouterLink,
  },
}
</script>

<style lang="scss" scoped>
.blue-color {
  color: #012970;
}
</style>