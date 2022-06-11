<template>
<div class="container">
  <h1>Тест</h1>
  <form @submit.prevent="submitHandler">
    <input type="number" name="x1" placeholder="x1" class="form-control mb-1">
    <input type="number" name="x2" placeholder="x2" class="form-control mb-1">
    <input type="number" name="x3" placeholder="x3" class="form-control mb-1">
    <input type="submit" value="Вычислить" class="btn btn-primary">
  </form>
  <div v-if="answer" class="answer">
    <h2>Ответ</h2>
    <p>{{ answer }}</p>
  </div>
  <data-graphic :ckra="[{ x: 100, y: 0}, { x: 50, y: 50 }, { x: 0, y: 100 } ]" />
</div>
</template>

<script>
import {DataProjectApi} from "../api/dataProjectApi/DataProjectApi";
import DataGraphic from "../components/chartsVue/dataGraphic/DataGraphic.vue";

export default {
  name: "DataProject",
  components: {
    DataGraphic
  },
  data: () => ({
    answer: '',
  }),
  methods: {
    async submitHandler(event) {
      const formData =  new FormData(event.target);
      console.log('formData', formData.get('x1'));
      this.answer = await DataProjectApi.compute({
        x1: formData.get('x1'),
        x2: formData.get('x2'),
        x3: formData.get('x3'),
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
}
</style>