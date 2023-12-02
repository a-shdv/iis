<template>
    <div>
        <PageLayout>
            <v-card-title>
              <h1 style="color: #00DC82">Прогнозирование баллов</h1>
            </v-card-title>
            <v-card-text>
                <h2 class="mb-4">Ошибки алгоритмов MAPE:</h2>
              <div class="text--primary" style="font-size: 18px;">
              <ul>
                <li><h4>mlp - MLPRegressor</h4></li>
                <li><h4>tree - DecisionTreeRegressor</h4></li>
                <li><h4>reg - LinearRegression</h4></li>
              </ul>
              </div>
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
    name: 'Score',
    created() {
        this.$axios.get('api/score').then(res => {
            let data = JSON.parse(JSON.stringify(res.data))
            for (let [key, value] of Object.entries(data)) {
                this.value = [...this.value, value]
                this.labels = [...this.labels, `${key} ${(value * 100).toFixed(2)}%`]
            }
            console.log(this.value);
            console.log(this.labels);
            console.log(data);
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
