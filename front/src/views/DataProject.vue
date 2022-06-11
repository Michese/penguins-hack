<template>
<div class="container">
<!--  <h1>Тест</h1>-->
<!--  <form @submit.prevent="submitHandler">-->
<!--    <input type="number" name="x1" placeholder="x1" class="form-control mb-1">-->
<!--    <input type="number" name="x2" placeholder="x2" class="form-control mb-1">-->
<!--    <input type="number" name="x3" placeholder="x3" class="form-control mb-1">-->
<!--    <input type="submit" value="Вычислить" class="btn btn-primary">-->
<!--  </form>-->
  <div v-if="answer" class="answer">
    <h2>Ответ</h2>
    <p>{{ answer }}</p>
  </div>

  <section class="section">
    <div class="row row-cols-2 justify-content-between">
      <component class="w-49" v-for="(data, index) in graphicsData" :key="`card_${index}`" :is="data.component" :title="data.title" :item="data.item" />
    </div>
  </section>
</div>
</template>

<script>
import {DataProjectApi} from "../api/dataProjectApi/DataProjectApi";
import LineGraphic from "../components/chartsVue/lineGraphic/LineGraphic.vue";
import ScatterGraphic from "../components/chartsVue/scatterGraphic/ScatterGraphic.vue";
import PieGraphic from "../components/chartsVue/pieGraphic/PieGraphic.vue";
import HistogramGraphic from "../components/chartsVue/histogramGraphic/HistogramGraphic.vue";
import {cardComponent, functionNames} from "../helper";
import LineCard from "./dataCard/LineCard.vue";
import ScatterCard from "./dataCard/ScatterCard.vue";
import PieCard from "./dataCard/PieCard.vue";
import HistogramCard from "./dataCard/HistogramCard.vue";

export default {
  name: "DataProject",
  components: {
    LineGraphic,
    ScatterGraphic,
    PieGraphic,
    HistogramGraphic,
    LineCard,
    ScatterCard
  },
  data: () => ({
    answer: '',
    data: [
      {
        component: 'LineCard',
        title: 'График',
        item: {
          series: [{ data: [{ x: 100, y: 0}, { x: 50, y: 50 }, { x: 0, y: 100 }], yName: 'Hello' }],
          xKey: 'x',
          yKey: 'y',
        }
      },
      {
        component: 'ScatterCard',
        title: 'Точечный График',
        item: {
          series: [{ data: [{ x: 100, y: 0}, { x: 50, y: 50 }, { x: 0, y: 100 }], yName: 'Hello' }],
          xKey: 'x',
          yKey: 'y',
        }
      },
      {
        component: 'PieCard',
        title: 'Пирожок',
        item: {
          data: [{ angle: 100, label: 'fgeafg'}, { angle: 50, label: 'label21' }, { angle: 100, label: 'eg3' }, { angle: 100, label: '123' }, { angle: 100, label: 'eg3' }, { angle: 100, label: 'eg3' }, { angle: 100, label: 'eg3' }, { angle: 100, label: 'eg3' }],
          angleKey: 'angle',
          labelKey: 'label',
        }
      },
      {
        component: 'HistogramCard',
        title: 'Гистограмма',
        item: {
          series: [{ data: [{ x: 100, y: 10}], yName: 'Hello' }, { data: [{ x: 0, y: 100 }], yName: 'Hello2' }],
          angleKey: 'angle',
          labelKey: 'label',
        }
      },
      {
        component: 'HistogramCard',
        title: 'Гистограмма 2',
        item: {
          series: [{ data: [{ x: 100, y: 10}], yName: 'Hello' }, { data: [{ x: 0, y: 100 }], yName: 'Hello3' }],
          angleKey: 'angle',
          labelKey: 'label',
        }
      },
    ],
  }),
  methods: {
    async submitHandler(event) {
      const formData =  new FormData(event.target);
      console.log('formData', formData.get('x1'));
      this.answer = await DataProjectApi.compute({
        x1: formData.get('x1'),
        x2: formData.get('x2'),
        x3: formData.get('x3'),
      });
    },
  },
  created() {
    console.log('functionNames[index]', functionNames[0]);
  },
  computed: {
    graphicsData() {
      return this.data.map(obj => ({
        ...obj,
        component: cardComponent[obj.component],
      }))
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