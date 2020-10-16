<template>
  <v-app>
    <notifications group="app" position="top right" />
    <vue-confirm-dialog></vue-confirm-dialog>

    <v-system-bar color="deep-purple darken-3" v-if="false"></v-system-bar>

    <TopMenu />

    <v-main>
      <SideBar />

      <v-container>
        <router-view/>
      </v-container>
    </v-main>

    <Footer />

    <v-bottom-navigation app v-if="false"></v-bottom-navigation>

  </v-app>
</template>

<script>
import TopMenu from './components/TopMenu';
import SideBar from './components/SideBar';
import Footer from './components/Footer';

export default {
  name: 'App',

  components: {
    TopMenu,
    SideBar,
    Footer,
  },

  data: () => ({
  }),
};
</script>
