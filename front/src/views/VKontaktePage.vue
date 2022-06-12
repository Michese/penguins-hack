<template>
  <div class="container">
    <div v-if="isLoading" class="d-flex justify-content-center">
      <loader />
    </div>
    <section v-else class="section">
      <div>
        <div class="d-flex justify-content-between gap-2" v-for="(dataRow, indexRow) in graphicsData" :key="`indexRow_${indexRow}`" >
          <component :class="`col-${12/dataRow.length}`" v-for="(dataCol, indexCol) in dataRow" :key="`card_${indexCol}`" :is="dataCol.component" :title="dataCol.title" :item="dataCol.item" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import {cardComponent} from "../helper";
import Loader from "../components/loader/Loader.vue";
import {DataProjectApi} from "../api/dataProjectApi/DataProjectApi";

export default {
  name: "VKontaktePage",
  components: {
    Loader,
  },
  data: () => ({
    isLoading: true,
    data: [],
  }),
  async created() {
    this.data =  await DataProjectApi.vk();
    this.isLoading = false;
  },
  computed: {
    graphicsData() {
      return this.data.map(dataRow => dataRow.map(dataCol => ({
        ...dataCol,
        component: cardComponent[dataCol.component],
      })))
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.w-49 {
  width: 49%;
}
</style>