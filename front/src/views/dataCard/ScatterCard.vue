<template>
  <div class="card">
    <h5 class="card-title ps-3">{{ title }}</h5>
    <div class="card-body">
      <scatter-graphic :series="item.series" :x-key="item.xKey" :y-key="item.yKey" :x-type="item.xType"/>
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