<template>
  <v-app>
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

        USERS LIST DEMO
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/namtenten"
        target="_blank"
        text
      >
        <span class="mr-2">Nguyen Ngoc Nam</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <UsersList/>
    </v-main>

    <v-card>
      <v-card-text class="success--text pt-0" v-if="false">
        Contact Me On Social Media!
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="success--text">
        &copy;2020 — <strong><a href="https://github.com/namtenten" target="_blank" class="success--text">Nguyen Ngoc Nam</a></strong>
      </v-card-text>
    </v-card>

  </v-app>
</template>

<script>
import UsersList from './components/UsersList';

export default {
  name: 'App',

  components: {
    UsersList,
  },

  data: () => ({
    //
  }),
};
</script>
