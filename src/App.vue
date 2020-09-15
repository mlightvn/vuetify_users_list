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
          src="logo_64.png"
          transition="scale-transition"
          width="40"
        />

        Users list demo
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/namtenten/vuetify_users_list"
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
