<template>
  <div class="card">
    <h5 class="card-title">{{ title }}</h5>
    <div class="card-body">
      <scatter-graphic :series="item.series" :x-key="item.xKey" :y-key="item.yKey" />
    </div>
  </div>
</template>

<script>
import ScatterGraphic from "../../components/chartsVue/scatterGraphic/ScatterGraphic.vue";

export default {
  name: "ScatterSection",
  components: {
    ScatterGraphic,
  },
  props: {
    title: {
      type: String,
      default: 'Название',
    },
    item: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>

</style>