<template>
  <div>
    <PageLayout>
      <v-card-title>
        <h1 style="color: #00DC82">Статистика</h1>
      </v-card-title>
      <v-card-text>
        <h2 class="mb-4" style="font-size: 24px;">Данные об учениках:</h2>
        <div class="text--primary" style="font-size: 18px;">
          <ul>
            <li><h4>Минимальная сумма баллов: {{ stat.min }}</h4></li>
            <li><h4>Максимальная сумма баллов: {{ stat.max }}</h4></li>
            <li><h4>Средняя сумма баллов: {{ stat.average }}</h4></li>
            <li><h4>Медианная сумма баллов: {{ stat.median }}</h4></li>
            <li><h4>Количество студентов выше медианы:  {{ stat.values_above_median }}</h4></li>
            <li><h4>Количество студентов ниже медианы:  {{ stat.values_below_median }}</h4></li>

          </ul>
        </div>
      </v-card-text>
    </PageLayout>
  </div>
</template>
<script>
import PageLayout from "~/components/PageLayout.vue"

export default {
  components: {
    PageLayout,
  },
  created() {
    this.$axios.get('api/params').then(res => {
      this.stat = res.data
    }).catch(err => console.log(err))
  },
  data() {
    return {
      stat: {
        // average: null,
        // max: null,
        // min: null,
        // median: null
      }
    }
  }

}
</script>
<style lang="">

</style>
