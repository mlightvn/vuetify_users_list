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
          USERS LIST
        </h2>

        <v-row>
          <UserEditDialog formTitle="User Edit Dialog" :users_list="users_list" :dialog="dialog" :selectedStatus="users_list.editedItem.status" />

<!-- 
          <v-dialog v-model="dialog" max-width="700px">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 sm12 md12 color="grey">
                        <v-text-field v-model="users_list.editedItem.id" label="ID" readonly="readonly" disabled></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm12 md12>
                        <v-text-field v-model="users_list.editedItem.name" label="名前"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm12 md12>
                        <v-text-field v-model="users_list.editedItem.email" label="email" type="email"></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm12 md12>
                      <v-select
                        label="状態"
                        v-model="users_list.editedItem.status.value"
                        item-text="text"
                        item-value="value"
                        :items="status_list.items"
                        no-data-text="<No data was gathered!>"
                        dense
                      >
                      </v-select>

                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click.native="close">Cancel</v-btn>
                <v-btn color="primary" @click.native="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
 -->


<!-- 
          <v-data-table
            v-model="users_list.selected"
            :headers="users_list.headers"
            :items="users_list.items"
            :items-per-page="10"
            item-key="id"
            :show-select="false"
            :multi-sort="true"
            :item-class="itemRowClass"
          >
          </v-data-table>
 -->
        </v-row>

        <v-row>
          <v-col
            class="mb-1"
            cols="12"
          >
            <div class="text-right">
              <!-- https://materialdesignicons.com/ -->
              <v-btn color="primary" fab dark class="mb-0" @click="showAddDialog()"><v-icon color="white">mdi-account-multiple-plus</v-icon></v-btn>
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

  // Vue.prototype.$axios = axios
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
        items: [
          // {id: 0, name: 'Nam', email:"nam@vue.nam", status:{value:'valid', text:'有効'}},
          // {id: 1, name: 'Nguyen', email:"nguyen@vue.nam", status:{value:'invalid', text:'無効'}},
          // {id: 2, name: 'Tester 1', email:null, status:{value:'valid', text:'有効'}},
          // {id: 3, name: 'Tester 2 - deleted', email:null, status:{value:'deleted', text:'削除'}},
          // {id: 4, name: 'Tester 3', email:null, status:{value:'valid', text:'有効'}},
          // {id: 5, name: 'Tester 4', email:null, status:{value:'valid', text:'有効'}},
          // {id: 6, name: 'Tester 5', email:null, status:{value:'valid', text:'有効'}},
          // {id: 7, name: 'Tester 6', email:null, status:{value:'valid', text:'有効'}},
          // {id: 8, name: 'Tester 7', email:null, status:{value:'valid', text:'有効'}},
          // {id: 9, name: 'Tester 8', email:null, status:{value:'valid', text:'有効'}},
          // {id: 10, name: 'Tester 9 - deleted', email:null, status:{value:'deleted', text:'削除'}},
          // {id: 11, name: 'Tester 10', email:null, status:{value:'valid', text:'有効'}},
          // {id: 12, name: 'Tester 11', email:null, status:{value:'valid', text:'有効'}},
          // {id: 13, name: 'Tester 12', email:null, status:{value:'valid', text:'有効'}},
          // {id: 14, name: 'Tester 13', email:null, status:{value:'valid', text:'有効'}},
          // {id: 15, name: 'Tester 14', email:null, status:{value:'valid', text:'有効'}},
          // {id: 16, name: 'Tester 15', email:null, status:{value:'valid', text:'有効'}},
          // {id: 17, name: 'Tester 16', email:null, status:{value:'valid', text:'有効'}},
          // {id: 18, name: 'Tester 17', email:null, status:{value:'valid', text:'有効'}},
          // {id: 19, name: 'Tester 18', email:null, status:{value:'valid', text:'有効'}},
          // {id: 20, name: 'Tester 19', email:null, status:{value:'valid', text:'有効'}},
          // {id: 21, name: 'Tester 20', email:null, status:{value:'valid', text:'有効'}},
          // {id: 22, name: 'Tester 21', email:null, status:{value:'valid', text:'有効'}},
        ]
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

    // ,watch: {
    //   dialog(val) {
    //     val || this.close()
    //   },
    // }

    ,computed: {
      ...mapGetters({ 
        tableItems: 'tableItems'
      })

      , formTitle() {
        return ((this.users_list.editedIndex === -1) || (this.users_list.editedIndex === this.users_list.items.length)) ? 'New Item' : 'Edit Item'
      }
      // ,indexedItems () {
      //   return this.users_list.items.map((item, index) => ({
      //     id: index,
      //     ...item
      //   }))
      // }
    }

    ,methods: {
      initialise() {
      }
      ,itemRowClass: function (item) {
         return (item.status.value == "deleted") ? 'grey--text text--lighten-1' : (item.status.value == "invalid" ? 'deep-orange--text text--darken-1' : '')
      }

      , fetchAPIData() { 
        axios
          .get(this.users_list.api.url)
          .then(response => {
            this.users_list.items = response.data
          })
      }

      ,showAddDialog:function() {
          this.users_list.editedIndex = this.users_list.items.length
          // this.users_list.editedItem = Object.assign({}, this.users_list.defaultItem)
          this.users_list.editedItem = {...this.users_list.defaultItem}
          this.users_list.editedItem.id = this.users_list.editedIndex
          this.dialog = true

      }

      ,showEditDialog:function(item) {
// console.log("showEditDialog", item)
          this.users_list.editedIndex = this.users_list.items.indexOf(item)
          // this.users_list.editedItem = Object.assign({}, item)
          this.users_list.editedItem = {...item}
// console.log("showEditDialog", this.users_list.editedItem)
          this.dialog = true

      }

      ,showDeleteDialog:function(item) {
          axios
            .delete(this.users_list.api.url + "/" + item.id)
            .then(() => {
              this.fetchAPIData()
            })

          // const index = this.users_list.items.indexOf(item)
          // if (index > -1) {
          //   confirm('Are you sure you want to delete this item?') && this.users_list.items.splice(index, 1)
          // }
      }

//       ,close() {
//         this.dialog = false
//         // setTimeout(() => {
//         //   // this.users_list.editedItem = Object.assign({}, this.users_list.defaultItem)
//         //   this.users_list.editedItem = {...this.users_list.defaultItem}
//         //   this.users_list.editedIndex = -1
//         // }, 300)

//         this.users_list.editedItem = {...this.users_list.defaultItem}
//         this.users_list.editedIndex = -1
// // console.log("close()", this.users_list.editedItem)
//       }
//       ,save() {
//         if (0 <= this.users_list.editedIndex && this.users_list.editedIndex < this.users_list.items.length) { // Update
//           this.users_list.items[this.users_list.editedIndex] = {...this.users_list.editedItem}
//           // Vue.set(this.users_list.items, {...this.users_list.editedItem}, this.users_list.editedIndex)
// // console.log("save()")
// // console.log(this.users_list.editedItem)
//         } else { // Insert
//           this.users_list.items.push({...this.users_list.editedItem})
//           // Vue.set(this.users_list.items, {...this.users_list.editedItem}, this.users_list.editedIndex)
//         }

//         this.users_list.editedIndex = -1

//         this.close()
//       }

    }
  }
</script>
