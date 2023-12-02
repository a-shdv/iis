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
      for (let [key, value] of Object.entries(data)) {
        let plotTitles = [...Object.values(value.dict)].map(el => `${el} ${this.labelDict[key]}`)
        let plotValues = [...Object.values(value.stat).map(el => `${el}`)]
        let correlatedArray = plotTitles.map((title, index) => {
          return {title, value: plotValues[index]};
        });
        this.value = [...this.value, ...Object.values(value.stat)]
        this.labels = [...this.labels, ...correlatedArray.flatMap(obj => `${obj.title}: ${obj.value}`).sort()]
      }
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
