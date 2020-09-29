<template>
  <v-app>
    <notifications group="app" position="top right" />
    <vue-confirm-dialog></vue-confirm-dialog>

    <v-system-bar color="deep-purple darken-3" v-if="false"></v-system-bar>

    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Users list demo"
          class="shrink mr-2"
          contain
          :src="require('./assets/logo/logo_64.png')"
          transition="scale-transition"
          width="40"
        />
      </div>

      <v-toolbar-title>{{app_name}}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/namtenten"
        target="_blank"
        text
      >
        <span class="mr-2">Nguyen Ngoc Nam</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-filter</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

    </v-app-bar>

    <v-main>
      <v-container fluid>
        <v-row>
          <v-col sm="4" md="4">
            <SideBar />
          </v-col>
          <v-col sm="8" md="8">
            <UsersList/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

    <v-footer app>
          &copy;2020 — <strong><a href="https://github.com/namtenten" target="_blank" class="success--text">Nguyen Ngoc Nam</a></strong>
    </v-footer>

    <v-bottom-navigation app v-if="false"></v-bottom-navigation>

  </v-app>
</template>

<script>
import UsersList from './components/UsersList';
import SideBar from './components/SideBar';


export default {
  name: 'App',

  components: {
    UsersList,
    SideBar,
  },

  data: () => ({
    app_name:'USERS LIST DEMO',
  }),
};
</script>
