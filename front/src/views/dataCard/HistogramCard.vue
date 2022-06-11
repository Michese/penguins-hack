<template>
  <div class="card">
    <h5 class="card-title">{{ title }}</h5>
    <div class="card-body">
      <histogram-graphic :series="item.series" :y-key="item.yKey" :x-key="item.xKey" :x-name="item.xName" />
    </div>
  </div>
</template>

<script>
import HistogramGraphic from "../../components/chartsVue/histogramGraphic/HistogramGraphic.vue";

export default {
  name: "HistogramSection",
  components: {
    HistogramGraphic,
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