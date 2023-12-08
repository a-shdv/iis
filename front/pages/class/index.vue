<template>
  <div>
    <PageLayout>
      <v-card-title>
        <h1 style="color: #00DC82">Классификация</h1>
      </v-card-title>
      <v-card-text>
        <h2>Агломеративная кластеризация - 1</h2>
        <h2>K-средних - 2</h2>
      </v-card-text>

      <v-sparkline :value="value" :gradient="gradient" :smooth="radius || false" :padding="padding"
                   :line-width="width" :stroke-linecap="lineCap" :gradient-direction="gradientDirection" :fill="fill"
                   :type="type" :auto-line-width="autoLineWidth" auto-draw :show-labels="true" :labels="labels"
                   :label-size="5">
      </v-sparkline>

      <v-card-text v-for="(cluster, index) in clusters" :key="index">
        <h2>{{ dict[cluster] }}: {{ values_above_median }}</h2>

        <!-- K-Means values -->
        <template v-if="cluster === 'kmeans'">
          <ul>
            <li><h4 style="font-size: 20px">kmeans_medians: {{ kmeans_clust_medians }}</h4></li>
            <li><h4 style="font-size: 20px">kmeans_above_median: {{ kmeans_clust_above_median }}</h4></li>
            <li><h4 style="font-size: 20px">kmeans_below_median: {{ kmeans_clust_below_median }}</h4></li>
          </ul>
        </template>

        <!-- Agglomerative Clustering values -->
        <template v-else-if="cluster === 'agg'">
          <ul>
            <li><h4 style="font-size: 20px">ag_clust: {{ agg_clust_medians }}</h4></li>
            <li><h4 style="font-size: 20px">ag_clust_above_median: {{ agg_clust_above_median }}</h4></li>
            <li><h4 style="font-size: 20px">ag_clust_below_median: {{ agg_clust_below_median }}</h4></li>
          </ul>
        </template>

      </v-card-text>
    </PageLayout>
  </div>
</template>
<script>
import PageLayout from "~/components/PageLayout.vue"

const gradients = [
  ['#222'],
  ['#00DC82'],
  ['red', 'orange', 'yellow'],
  ['purple', 'violet'],
  ['#00f096', '#F0F', '#FF0'],
  ['#f72047', '#ffd200', '#1feaea'],
]
export default {
  name: 'Class',
  created() {
    this.$axios.get('api/calc_classes').then(res => {
      let data = JSON.parse(JSON.stringify(res.data))
      this.clusters = Object.keys(data)
      for (let [key, value] of Object.entries(data)) {
        let plotTitles = [...Object.values(value.dict)].map(el => `${el} ${this.labelDict[key]}`)
        let plotValues = [...Object.values(value.stat).map(el => `${el}`)]

        let concatenatedArray = plotTitles.map((title, index) => {
          return {title, value: plotValues[index]};
        });

        this.value = [...this.value, ...Object.values(value.stat)]
        this.labels = [...this.labels, ...concatenatedArray.flatMap(obj => {
          // Exclude specific values from labels
          if (obj.title !== 'kmeans_clust_medians' && obj.title !== 'kmeans_clust_above_median' && obj.title !== 'kmeans_clust_below_median' && obj.title !== 'agg_clust_medians' && obj.title !== 'agg_clust_above_median' && obj.title !== 'agg_clust_below_median') {
            return `${obj.title}: ${obj.value}`;
          }
          return [];
        }).sort()]
      }

      // Set the calculated values to data properties
      this.kmeans_clust_medians = data.kmeans.kmeans_clust_medians;
      this.kmeans_clust_above_median = data.kmeans.kmeans_clust_above_median;
      this.kmeans_clust_below_median = data.kmeans.kmeans_clust_below_median;

      this.agg_clust_medians = data.agg.agg_clust_medians;
      this.agg_clust_above_median = data.agg.agg_clust_above_median;
      this.agg_clust_below_median = data.agg.agg_clust_below_median;

    }).catch(err => console.log(err))
  },
  components: {
    PageLayout,
  },
  data() {
    return {
      dict: {
        'agg': "Агломеративная кластеризация - 1",
        'kmeans': "K-средних - 2"
      },
      labelDict: {
        'agg': "1",
        'kmeans': "2"
      },
      width: 2,
      radius: 2,
      padding: 10,
      lineCap: 'round',
      gradient: gradients[1],
      value: [],
      labels: [],
      clusters: [],
      kmeans_clust_medians: 0,
      kmeans_clust_above_median: 0,
      kmeans_clust_below_median: 0,
      agg_clust_medians: 0,  // Initialize to default value
      agg_clust_above_median: 0,
      agg_clust_below_median: 0,
      gradientDirection: 'top',
      gradients,
      fill: false,
      type: 'bar',
      autoLineWidth: true,
    }
  },
}

</script>
<style lang="">

</style>
