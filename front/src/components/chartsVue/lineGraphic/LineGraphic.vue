<template>
  <ag-charts-vue :options="options"/>
</template>

<script>
import {AgChartsVue} from 'ag-charts-vue3';
import {colours, functionNames} from "../../../helper";

export default {
  name: "LineGraphic",
  props: {
    series: {
      type: Array,
      required: true,
    },
    xKey: {
      type: String,
      default: 'x',
    },
    yKey: {
      type: String,
      default: 'y',
    },
  },
  components: {'ag-charts-vue': AgChartsVue,},
  computed: {
    options() {
      return {
        autoSize: true,
        series: this.series.map((obj, index) => ({
          data: obj.data,
          xKey: this.xKey,
          yKey: this.yKey,
          yName: obj.yName ?? functionNames[index],
          stroke: colours[index],
          marker: {
            fill: colours[index],
            stroke: colours[index],
          },
        })),
        axes: [
          {
            type: 'number',
            position: 'bottom',
          },
          {
            type: 'number',
            position: 'left',
          },
        ],
        legend: {
          position: 'top',
        },
      };
    }
  }
}
</script>

<style lang="scss" scoped>

</style>