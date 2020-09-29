<template>
  <v-list>
    <v-list-item-group
      active-class="deep-purple--text text--accent-4"
    >
      <v-list-item
        v-for="item in items"
        :key="item.title"
        link
      >
        <v-list-item-icon v-if="item.items == undefined">
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content v-if="item.items == undefined">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>




    </v-list-item-group>










  </v-list>

</template>

<script>

export default {
  name: 'SideBarSub',

  data: () => ({
    items: [
        {
          title: 'Dashboard',
          icon: 'mdi-view-dashboard',
          href: '/',
          active: true,
        },
        {
          title: 'Administration',
          icon: 'mdi-account-cog',
          items: [
            { title: 'Management', icon: 'mdi-account-multiple-outline', href: '/',},
            { title: 'Settings', icon: 'mdi-cog-outline', href: '/',},
          ],
        },
        {
          title: 'Education',
          icon: 'mdi-school',
          items: [{ title: 'List Item' }],
        },

      ],

  }),

}
</script>
