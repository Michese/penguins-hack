<template>
  <h2>About</h2>
</template>

<script>
import {DataProjectApi} from "../api/dataProjectApi/DataProjectApi";

export default {
  name: "About",
  async created() {
    const result = await DataProjectApi.sayHello();
    // console.log('result', result);
    // console.log(1231);
  }
}
</script>

<style lang="scss" scoped>

</style>