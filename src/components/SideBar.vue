<template>
  <v-navigation-drawer
    v-model="drawer"
    absolute
    permanent
  >
    <v-list
      nav
      dense
    >
      <v-list-item-group
        v-model="group"
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

      </v-list-item-group>

    </v-list>

<!-- 
    <v-list
      nav
      dense
      v-for="item in items"
      :key="item.title"
    >

        <v-list-item-icon v-if="!item.items">
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content v-if="!item.items">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>

        <v-list-group
          :key="item.title"
          v-model="item.active"
          :prepend-icon="item.icon"
          :no-action
          v-if="item.items != null"
        >

          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </template>


          <v-list-item
            v-for="child in item.items"
            :key="child.title"
          >
            <v-list-item-content>
              <v-list-item-title v-text="child.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>

        </v-list-group>
      </v-list>
 -->

    <v-divider></v-divider>

    <Author/>

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
    app_name: 'Users Demo',
    sub_title: 'Beautiful song',
    items: [
      { title: 'Dashboard', icon: 'mdi-view-dashboard' },
      { title: 'Photos', icon: 'mdi-image' },
      { title: 'About', icon: 'mdi-help-box' },
    ],
    admins: [
      ['Management', 'mdi-account-multiple-outline'],
      ['Settings', 'mdi-cog-outline'],
    ],


    // items: [
    //     {
    //       icon: 'mdi-view-dashboard',
    //       title: 'Dashboard',
    //       active: true,
    //     },
    //     { title: 'Photos', icon: 'mdi-image' },
    //     { title: 'About', icon: 'mdi-help-box' },
    //     {
    //       icon: 'mdi-account-cog',
    //       items: [
    //         { title: 'Management', icon: 'mdi-account-multiple-outline' },
    //         { title: 'Settings', icon: 'mdi-cog-outline' },
    //       ],
    //       title: 'Administration',
    //     },
    //     {
    //       icon: 'mdi-school',
    //       items: [{ title: 'List Item' }],
    //       title: 'Education',
    //     },

    //   ],


    right: null,

    drawer: false,
    group: null,
  }),

  watch: {
    group () {
      this.drawer = false
    },
  },
}
</script>
