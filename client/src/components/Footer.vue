<template>
     <v-footer app>
          &copy;2020 | <strong><a :href="author.url" target="_blank" class="orange--text mx-2">{{author.name}}</a></strong> | <a class="ml-1" :href="author.donate" target="_blank"><img src="/images/Donate-PayPal-green.svg" alt="Donate"></a>
    </v-footer>
</template>

<script>
import configuration from '../configuration'

export default {
  data () {
    return {
      author: configuration.author,
    }
  },
}
</script>
