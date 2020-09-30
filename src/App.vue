<template>
  <v-app>
    <notifications group="app" position="top right" />
    <vue-confirm-dialog></vue-confirm-dialog>

    <v-system-bar color="deep-purple darken-3" v-if="false"></v-system-bar>

    <TopMenu />

    <v-main>
      <v-container fluid>
        <v-row>
          <v-col sm="4" md="2">
            <SideBar />
          </v-col>
          <v-col sm="8" md="10">
            <UsersList/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

    <Footer />

    <v-bottom-navigation app v-if="false"></v-bottom-navigation>

  </v-app>
</template>

<script>
import TopMenu from './components/TopMenu';
import UsersList from './components/users/List';
import SideBar from './components/SideBar';
import Footer from './components/Footer';

export default {
  name: 'App',

  components: {
    TopMenu,
    UsersList,
    SideBar,
    Footer,
  },

  data: () => ({
  }),
};
</script>
