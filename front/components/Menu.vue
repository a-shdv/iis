<template>
     <v-navigation-drawer
        floating
        permanent
      >
        <v-list
          dense
          rounded
        >
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            :to="item.to"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
</template>
<script>
export default {
    data () {
      return {
        items: [
          { title: 'Статистика', icon: 'mdi-counter', to: "/" },
          { title: 'Классификация', icon: 'mdi-chart-sankey', to: "/class" },
          { title: 'Регрессия', icon: 'mdi-chart-timeline-variant', to: "/score" },
        ],
      }
    },
}
</script>
<style lang="">
    
</style>