<template>
  <div>
    <PageLayout>
      <v-card-title>
        <h1>Данные об учениках</h1>
      </v-card-title>
      <v-card-text>
        <div class="text--primary">
          <span><b>Минимальная сумма баллов:</b> {{ stat.min }}</span> <br>
          <span><b>Максимальная сумма баллов:</b> {{ stat.max }}</span> <br>
          <span><b>Средняя сумма баллов:</b> {{ stat.average }}</span> <br>
          <span><b>Медианная сумма баллов:</b> {{ stat.median }}</span> <br>
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
