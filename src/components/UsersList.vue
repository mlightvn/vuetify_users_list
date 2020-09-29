<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12" v-if="false">
        <v-img
          :src="require('../assets/logo/logo_256.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col
        class="mb-1"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-0">
          USERS LIST | RESTful
        </h2>

        <v-row>
          <UserEditDialog formTitle="User Edit Dialog" :users_list="users_list" :dialog="dialog" :selectedStatus="users_list.editedItem.status" />
        </v-row>

        <v-row>
          <v-col
            class="mb-1"
            cols="12"
          >
            <div class="text-right">
              <!-- https://materialdesignicons.com/ -->
              <v-btn color="primary" fab dark class="mb-0 mr-1" @click="fetchAPIData()"><v-icon color="white">mdi-refresh</v-icon></v-btn>
              <v-btn color="primary" fab dark class="mb-0 mr-1" @click="showAddDialog()"><v-icon color="white">mdi-account-multiple-plus</v-icon></v-btn>
            </div>

          </v-col>
        </v-row>

        <v-row justify="center">
          <v-data-table
            v-model="users_list.selected"
            :headers="users_list.headers"
            :items="users_list.items"
            class="elevation-1"
            :item-class="itemRowClass"
            :multi-sort="true"
            :items-per-page="10"
            item-key="id"
            :show-select="false"
            :search="users_list.search"
          >

            <template v-slot:top="{ pagination, options, updateOptions }">
              <v-data-footer 
                :pagination="pagination" 
                :options="options"
                @update:options="updateOptions"
                items-per-page-text="$vuetify.dataTable.itemsPerPageText"/>
            </template>

            <template slot="item" slot-scope="props">
              <tr :class="itemRowClass(props.item)">
                <td>
                  <v-layout justify-left>
                    <a @click="showEditDialog(props.item)">
                        <v-icon small color="primary">mdi-pencil</v-icon>
                        {{ props.item.name }}
                    </a>
                  </v-layout>
                </td>
                <td>
                  <v-layout justify-left>
                    <a :href="'mailto:' + props.item.email">{{ props.item.email }}</a>
                  </v-layout>
                </td>
                <td>
                  <v-layout justify-center>
                    {{ props.item.status.text }}
                  </v-layout>
                </td>
                <td>
                  <v-btn icon class="mx-0" @click="showEditDialog(props.item)">
                      <v-icon small color="primary">mdi-pencil</v-icon>
                  </v-btn>

                  <v-btn icon class="mx-0" @click="showDeleteDialog(props.item)">
                    <v-icon small color="pink">mdi-delete</v-icon>
                  </v-btn>
                </td>
              </tr>
            </template>

            <template v-slot:item.actions="{ item }" v-if="false">
              <v-btn icon class="mx-0" @click="showEditDialog(item)">
                  <v-icon small color="primary">mdi-pencil</v-icon>
              </v-btn>

              <v-btn icon class="mx-0" @click="showDeleteDialog(item)">
                <v-icon small color="pink">mdi-delete</v-icon>
              </v-btn>
            </template>

          </v-data-table>

        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // https://www.codeply.com/p/m0nip2TdUv

  // import Vue from "vue";
  import UserEditDialog from "@/components/UserEditDialog"
  import Vue from 'vue'
  import axios from 'axios'

  // import Vuex from 'vuex'
  import { mapGetters } from 'vuex'
  // import { mapActions } from "vuex"

  Vue.use(axios)

  function getTitle (vm) {
    const { title } = vm.$options
    if (title) {
      return typeof title === 'function'
        ? title.call(vm)
        : title
    }
  }

  export default {
    name: 'UsersList'
    ,title: 'Users List'

    ,components: {
      UserEditDialog,
    }

    // , mounted() {
    //   console.log("mounted: ", this.users_list.editedItem);
    // }
    ,data: () => ({
      dialog: false
      , users_list: {
        api: {url:'http://localhost:5000/api/users'},
        search: '',
        selected: [],
        headers: [
          // https://vuetifyjs.com/en/styles/colors/
          // { text: '#', value: 'id',  sortable: true, class: "primary white--text title" },
          { text: '名前', value: 'name', sortable: true, class: "primary white--text title" },
          { text: 'email', value: 'email', sortable: true, class: "primary white--text title" },
          { text: '状態', value: 'status.text', sortable: true, class: "primary white--text title" },
          { text: '', value: 'actions', sortable: false, class: "primary white--text title" }
        ],
        items: []
        ,editedIndex: -1
        ,editedItem: {id: null,  name: null, email:null, status:{value:'valid', text:'有効'}}
        ,defaultItem: {id: null,  name: null, email:null, status:{value:'valid', text:'有効'}}
      }
      , status_list : {
          default: {value:'valid', text: '有効'}
          , items: [
            {value:'valid', text: '有効'},
            {value:'invalid', text: '無効'},
            {value:'deleted', text: '削除'},
          ]
        }
    })

    , mounted () {
      axios
        .get(this.users_list.api.url)
        .then(response => {
          this.users_list.items = response.data
          // console.log(response)
        })
    }
    , created () {
      const title = getTitle(this)
      if (title) {
        document.title = title
      }
    }

    ,computed: {
      ...mapGetters({ 
        tableItems: 'tableItems'
      })

      , formTitle() {
        return ((this.users_list.editedIndex === -1) || (this.users_list.editedIndex === this.users_list.items.length)) ? 'New Item' : 'Edit Item'
      }
    }

    ,methods: {
      initialise() {
      }
      ,itemRowClass: function (item) {
         return (item.status.value == "deleted") ? 'grey--text text--lighten-1' : (item.status.value == "invalid" ? 'deep-orange--text text--darken-1' : 'green--text')
      }

      , fetchAPIData() { 
        axios
          .get(this.users_list.api.url)
          .then(response => {
            this.users_list.items = response.data
          })
      }

      ,showAddDialog:function() {
          this.users_list.editedIndex = -1
          this.users_list.editedItem = {...this.users_list.defaultItem}
          this.dialog = true

      }

      ,showEditDialog:function(item) {
          this.users_list.editedIndex = this.users_list.items.indexOf(item)
          this.users_list.editedItem = item
          this.dialog = true

      }

      ,showDeleteDialog:function(item) {
        const index = this.users_list.items.indexOf(item)
        if (index > -1) {
          let isDeleted = confirm('Are you sure you want to delete this item?')
          if(isDeleted){
            axios
              .delete(this.users_list.api.url + "/" + item.id)
              .then(() => {
                this.users_list.items.splice(index, 1)
              })
          }
        }

      }

    }
  }
</script>
