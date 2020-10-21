<template>
  <v-app-bar
      app
      color="orange accent-4"
      dark
      flat
  >
    <v-toolbar
      color="orange accent-4"
      dark
      flat
    >
      <v-app-bar-nav-icon v-if="false"></v-app-bar-nav-icon>

      <template class="d-flex align-center">
        <v-img
          :alt="app_name"
          class="shrink mr-2"
          contain
          :src="require('../assets/logo/logo_64.png')"
          transition="scale-transition"
          width="40"
        />
      </template>

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
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

    </v-toolbar>

    <template v-slot:extension
      v-if="true"
    >
      <v-tabs
        v-model="tab"
        align-with-title
        background-color="orange accent-3"
      >
        <v-tabs-slider color="white"></v-tabs-slider>

        <v-tab
          v-for="item in items"
          :key="item"
        >
          {{ item }}
        </v-tab>

        <v-tabs-items v-model="tab">
          <v-tab-item
            v-for="item in items"
            :key="item"
          >
            <v-card flat v-if="true">
              <v-card-text v-text="text"></v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>

      </v-tabs>
    </template>

  </v-app-bar>

</template>

<script>
  export default {
    data () {
      return {
        app_name:'USERS LIST DEMO',
        tab: null,
        items: [
          'web', 'shopping', 'videos', 'images', 'news',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>
