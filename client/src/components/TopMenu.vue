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
          :src="profile.avatar"
          transition="scale-transition"
          width="40"
        />
      </template>

      <v-toolbar-title>{{app_name}}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
        :href="profile.url"
        target="_blank"
        text
      >
        <span class="mr-2">{{profile.name}}</span>
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
      v-if="false"
    >
      <v-tabs
        v-model="tab"
        align-with-title
        background-color="orange accent-3"
      >
        <v-tabs-slider color="white"></v-tabs-slider>

        <v-tab
          v-for="item in items"
          :key="item.value"
        >
          {{ item.value }}
        </v-tab>

        <v-tabs-items v-model="tab">
          <v-tab-item
            v-for="item in items"
            :key="item.value"
          >
            <v-card flat v-if="true">
              <v-card-text v-text="item.text"></v-card-text>
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
      app_name: process.env.VUE_APP_TITLE,
      tab: null,
      profile: {
        name: process.env.VUE_APP_PROFILE_NAME,
        avatar: require('../assets/logo/logo_64.png'),
        status: 'online',
        last_seen: 'a few seconds ago',
        url: process.env.VUE_APP_PROFILE_URL,
      },
      items: [
        {value:'web', text:'Webbbbbbbbbbbb'},
        {value:'shopping', text:'Shopping ............'},
        {value:'videos', text:'Videos ............'},
        {value:'images', text:'Images ............'},
        {value:'news', text:'News ............'},
      ],
    }
  },
}
</script>
