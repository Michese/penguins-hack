<template>
  <ag-charts-vue :options="options"/>
</template>

<script>
import {AgChartsVue} from 'ag-charts-vue3';
import {colours, functionNames} from "../../../helper";

export default {
  name: "HistogramGraphic",
  props: {
    series: {
      type: Array,
      required: true,
    },
    xType:{
      type: String,
      default: 'number',
    },
    xKey: {
      type: String,
      default: 'x',
    },
    yKey: {
      type: String,
      default: 'y',
    },
    xName: {
      type: String,
      default: 'Интервал',
    },
  },
  components: {'ag-charts-vue': AgChartsVue,},
  computed: {
    options() {
      return {
        autoSize: true,
        series: this.series.map((obj, index) => ({
          type: 'histogram',
          xKey: this.xKey,
          yKey: this.yKey,
          xName: this.xName,
          yName: obj.yName,
          data: obj.data,
        })),
        axes: [
          {
            type: this.xType,
            position: 'bottom',
          },
          {
            type: 'number',
            position: 'left',
          },
        ],
        legend: {
          enabled: false, 
          position: 'top',
        },
      };
    }
  }
}
</script>

<style lang="scss" scoped>

</style>