<template>
  <header id="header" class="header d-flex align-items-center">

    <div class="d-flex align-items-center justify-content-between">
      <a class="logo d-flex align-items-center" href="https://www.uralsib.ru/">
        <img src="./image.png" alt="">
      </a>
      <i class="bi bi-list toggle-sidebar-btn"></i>
    </div>

  </header>
</template>

<script>
export default {
  name: "HeaderComponent"
}
</script>

<style lang="scss" scoped>
#header {
  position: sticky;
  top: 0;
}
</style>