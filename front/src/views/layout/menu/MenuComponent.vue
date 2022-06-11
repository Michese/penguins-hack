<template>
  <aside id="sidebar" class="sidebar">

    <ul class="sidebar-nav" id="sidebar-nav">

      <li class="nav-item">
        <router-link :to="{ name: 'home' }"  active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Домашняя</span>
        </router-link>
      </li>

      <li class="nav-item">
        <router-link  :to="{ name: 'about' }" active-class="collapsed" class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse">
          <span>Что-либо</span>
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

</style>