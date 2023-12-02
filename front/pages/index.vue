<template >
    <div>
        <PageLayout>
            <v-card-title>
                Данные об учениках
            </v-card-title>
            <v-card-text>
                <p class="text--primary"> Минимальная сумма быллов: {{ stat.min }}</p>
            </v-card-text>
            <v-card-text>
                <p class="text--primary"> Максимальная сумма быллов: {{ stat.max }}</p>
            </v-card-text>
            <v-card-text>
                <p class="text--primary"> Средняя сумма быллов: {{ stat.average }}</p>
            </v-card-text>
            <v-card-text>
                <p class="text--primary"> Медианная сумма быллов: {{ stat.median }}</p>
            </v-card-text>
        </PageLayout>
    </div>
</template>
<script>
import PageLayout from "@/components/PageLayout"
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