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
        active-class="deep-purple--text text--accent-4"
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
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
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Administration</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in admins"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>

      </v-list-item-group>

    </v-list>

    <v-divider></v-divider>

    <SideBarSub />

    <v-divider></v-divider>

    <Author/>

  </v-navigation-drawer>

</template>

<script>
import Author from './Author';
import SideBarSub from './SideBarSub';

export default {
  name: 'SideBar',

  components: {
    Author,
    SideBarSub,
  },

  data: () => ({
    app_name: 'Users Demo',
    items: [
      { title: 'Dashboard', icon: 'mdi-view-dashboard', active: true, },
      { title: 'Photos', icon: 'mdi-image' },
      { title: 'About', icon: 'mdi-help-box' },
    ],
    admins: [
      ['Management', 'mdi-account-multiple-outline'],
      ['Settings', 'mdi-cog-outline'],
    ],

  }),

}
</script>
