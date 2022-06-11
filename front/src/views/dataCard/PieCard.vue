<template>
  <div class="card">
    <h5 class="card-title">{{ title }}</h5>
    <div class="card-body">
      <pie-graphic :data="item.data" :angle-key="item.angleKey" :label-key="item.labelKey" />
    </div>
  </div>
</template>

<script>
import PieGraphic from "../../components/chartsVue/pieGraphic/PieGraphic.vue";

export default {
  name: "PieSection",
  components: {
    PieGraphic,
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