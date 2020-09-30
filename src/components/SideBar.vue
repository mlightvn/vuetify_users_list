<template>
  <v-navigation-drawer
    absolute
    permanent
  >
    <v-list
      nav
      dense
    >

      <v-list-item-group
        active-class="orange--text text--accent-4"

        v-for="item in items"
        :key="item.title"
      >

        <v-list-item
          v-if="item.items === undefined || item.items === null"
          link
          :to="item.to"
          :href="item.href"
          :target="(item.href) ? '_blank': ''"
        >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>

        </v-list-item>


        <v-list-group
          :value="true"
          no-action
          v-else
        >
          <template v-slot:activator>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="child in item['items']"
            :key="child.title"
            :to="child.to"
          >
            <v-list-item-icon>
              <v-icon>{{ child.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="child.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>

        </v-list-group>

      </v-list-item-group>

    </v-list>

    <v-divider></v-divider>

    <Author v-if="false"/>

  </v-navigation-drawer>

</template>

<script>
import Author from './Author';

export default {
  name: 'SideBar',

  components: {
    Author,
  },

  data: () => ({
    items: [
      { title: 'Dashboard', icon: 'mdi-view-dashboard', active: true, to: '/',},
      { title: 'Users', icon: 'mdi-account-group', to: '/users',},
      // { title: 'Photos', icon: 'mdi-image', to: '/photos', },
      { title: 'About', icon: 'mdi-help-box', to: '/about', },

      {
        title: 'Administration',
        icon: 'mdi-account-cog',
        items: [
          { title: 'Management', icon: 'mdi-account-multiple-outline', to: '/admin/management',},
          { title: 'Settings', icon: 'mdi-cog-outline', to: '/admin/setting',},
        ],
      },
      { title: 'Donate', icon: 'mdi-currency-usd', href: 'https://github.com/namtenten', },

    ],

  }),

}
</script>
