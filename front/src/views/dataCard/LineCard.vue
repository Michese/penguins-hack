<template>
  <div class="card">
    <h5 class="card-title ps-3">{{ title }}</h5>
    <div class="card-body">
      <line-graphic :series="item.series" :x-key="item.xKey" :y-key="item.yKey"/>
    </div>
  </div>
</template>

<script>
import LineGraphic from "../../components/chartsVue/lineGraphic/LineGraphic.vue";

export default {
  name: "LineSection",
  components: {
    LineGraphic,
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