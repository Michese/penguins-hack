<template>
  <div class="card">
    <h5 class="card-title ps-3">{{ title }}</h5>
    <div class="card-body">
      <histogram-graphic :series="series" :y-key="item.yKey" :x-key="item.xKey" :x-name="item.xName" :x-type="item.xType" />
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
  },
  computed: {
    series(){
      return this.item.series.map(data =>{
        return{
          ...data,
          data:data.data.map(item =>({
            [this.item.xKey]:typeof item[this.item.xKey] === 'string' ? new Date(item[this.item.xKey]):item[this.item.xKey],
            [this.item.yKey]:typeof item[this.item.yKey] === 'string' ?new Date(item[this.item.yKey]):item[this.item.yKey]

          }))
        }
      })
    }
  }
}
</script>

<style scoped>

</style>