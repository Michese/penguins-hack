import {defineAsyncComponent} from "vue";

export default {
    'ScatterCard': defineAsyncComponent(() => import('../views/dataCard/ScatterCard.vue')),
    'PieCard': defineAsyncComponent(() => import('../views/dataCard/PieCard.vue')),
    'LineCard': defineAsyncComponent(() => import('../views/dataCard/LineCard.vue')),
    'HistogramCard': defineAsyncComponent(() => import('../views/dataCard/HistogramCard.vue')),
}