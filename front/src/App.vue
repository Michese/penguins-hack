<template>
  <HeaderComponent />
  <MenuComponent />
  <main id="main" class="main">
    <RouterView />
  </main>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import MenuComponent from "./views/layout/menu/MenuComponent.vue";
import HeaderComponent from "./views/layout/header/HeaderComponent.vue";

export default {
  name: 'App',
  components: {
    MenuComponent,
    RouterView,
    HeaderComponent,
  },
}
</script>

<style lang="scss">
@import "./assets/base.scss";
@import "~bootstrap";
</style>
