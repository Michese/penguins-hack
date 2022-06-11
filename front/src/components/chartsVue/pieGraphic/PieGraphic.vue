<template>
  <ag-charts-vue :options="options"/>
</template>

<script>
import {AgChartsVue} from 'ag-charts-vue3';
import {colours, functionNames} from "../../../helper";

export default {
  name: "PieGraphic",
  props: {
    data: {
      type: Array,
      required: true,
    },
    angleKey: {
      type: String,
      default: 'angle',
    },
    labelKey: {
      type: String,
      default: 'label',
    },
  },
  components: {'ag-charts-vue': AgChartsVue,},
  computed: {
    options() {
      return {
        autoSize: true,
        data: this.data.map((obj, index) => ({
          [this.labelKey]: functionNames[index],
          ...obj,
        })),
        series: [{
          type: 'pie',
          angleKey: this.angleKey,
          labelKey: this.labelKey,
          fills: colours,
          strokes: colours,
        }],
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