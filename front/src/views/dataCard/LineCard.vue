<template>
  <div class="card">
    <h5 class="card-title ps-3">{{ title }}</h5>
    <div class="card-body">
      <line-graphic :series="series" :x-key="item.xKey" :y-key="item.yKey" :x-type="item.xType"/>
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
  },
  computed: {
    series(){
      return this.item.series.map(data =>{
        return{
          ...data,
          data:data.data.map(item =>({
            [this.item.xKey]:this.parseData(item[this.item.xKey]),
            [this.item.yKey]:this.parseData(item[this.item.yKey])

          }))
        }
      })
    }
  },
  methods:{
    parseData(data){
      if(typeof data === 'string' && new Date(data)?.getFullYear()){
        return new Date(data)
      }        
      else{
        return data;
      }
    }
  }
}
</script>

<style scoped>

</style>