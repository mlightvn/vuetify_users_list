<template>
  <v-container fluid>
    <v-row class="text-left">
      <v-col
        class="mb-1"
        cols="12"
      >
        <v-card>
          <v-img
            height="200px"
            :src="require('../assets/images/green_grasses.jpg')"
          >
            <v-app-bar
              flat
              color="rgba(0, 0, 0, 0)"
              v-if="false"
            >
              <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

              <v-toolbar-title class="title white--text pl-0">
                Messages
              </v-toolbar-title>

              <v-spacer></v-spacer>

              <v-btn
                color="white"
                icon
              >
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-app-bar>

            <v-card-title class="white--text mt-10">
              <v-avatar size="56">
                <img
                  :alt="author.name"
                  :src="author.avatar"
                >
              </v-avatar>
              <p class="ml-3">
                {{author.name}}
              </p>
            </v-card-title>
          </v-img>

          <v-card-title>
            🌟🌟🌟🌟🌟
          </v-card-title>

          <v-card-subtitle>
            Beautiful song...
          </v-card-subtitle>

          <v-card-title>
            Social Medias
          </v-card-title>

          <v-card-subtitle>
            <div v-if="author.social_media.linkedin">
              LinkedIn: <a :href="author.social_media.linkedin">{{author.social_media.linkedin}}</a>
            </div>
            <div v-if="author.social_media.github">
              GitHub: <a :href="author.social_media.github">{{author.social_media.github}}</a><br>
            </div>
          </v-card-subtitle>


        </v-card>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
//  import Vue from 'vue'
// import 'dotenv/config'
// require('dotenv').config();
import configuration from "@/configuration"

export default {
  name: 'Author',

  components: {
  },

  data() {
    return {
      // author : {
      //   name: process.env.VUE_APP_PROFILE_NAME,
      //   image: process.env.VUE_APP_PROFILE_AVATAR,
      //   url: process.env.VUE_APP_PROFILE_URL,
      //   social_media:{
      //     linkedin: process.env.VUE_APP_PROFILE_LINKEDIN,
      //     github: process.env.VUE_APP_PROFILE_GITHUB,
      //   }
      // },
      author: configuration.author,
    }
  },

  methods: {
    initialise() {
      // console.log({author: this.author});
    },

  },

  created() {
    this.initialise();
  },
}
</script>
