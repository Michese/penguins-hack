<template>
  <ag-charts-vue :options="options" />
</template>

<script>
import { AgChartsVue } from 'ag-charts-vue3';
export default {
  name: "DataGraphic",
  props: [ 'ckra' ],
  components: {  'ag-charts-vue': AgChartsVue, },
  computed: {
    options() {
      return {
        autoSize: true,
        series: [
          {
            data: this.ckra,
            xKey: 'x',
            yKey: 'y',
            yName: 'ƒ(x)',
            stroke: '#C4E7D4',
            marker: {
              fill: '#C4E7D4',
              stroke: '#C4E7D4',
            },
          },
        ],
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