<template>
  <v-dialog v-model="$parent.dialog" max-width="700px">
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

</template>

<script>
  // import { mapState } from "vuex";
  // import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'UserEditDialog'

    ,props: {
      formTitle: String,
      users_list: Object,
      // editedItem: Object,
      // dialog:Boolean,
      // selectedStatus: Object,
    }

    ,data: () => ({
      status_list : {
          default: {value:'valid', text: '有効'}
          , values: {
            valid  : '有効',
            invalid: '無効',
            deleted: '削除',
          }
          , items: [
            {value:'valid', text: '有効'},
            {value:'invalid', text: '無効'},
            {value:'deleted', text: '削除'},
          ]
          // , selectedStatus: {value:'valid', text: '有効'},
        }
    })

    // ,computed: {
    //   ...mapState({
    //     users_list: (state) => state.users_list,
    //   }),
    // }

    // ,watch: {
    //   dialog(val) {
    //     val || this.close()
    //   },
    // }

    ,methods: {
      initialise() {
        // if (this.status_list) {
        // }
      }
      ,close() {
        this.$parent.dialog = false

        this.users_list.editedItem = {...this.users_list.defaultItem}
        this.users_list.editedIndex = -1
      }
      ,save() {
// console.log("selectedStatus", this.$parent.selectedStatus)
console.log("status", this.users_list.editedItem)

//         this.$parent.selectedStatus = this.status_list.items.find(item => {
// // console.log("status_value", status_value)
// // console.log("item.value", item.value)
//           return this.users_list.editedItem.status.value === item.value;
//         });
// //         // console.log(this.$parent.users_list.editedItem)



        this.users_list.editedItem.status.text = this.status_list.values[this.users_list.editedItem.status.value]

        if (0 <= this.users_list.editedIndex && this.users_list.editedIndex < this.users_list.items.length) { // Update
          this.users_list.items[this.users_list.editedIndex] = {...this.users_list.editedItem}
        } else { // Insert
          this.users_list.items.push({...this.users_list.editedItem})
        }

        this.users_list.editedIndex = -1

        this.close()
      }

    }
  }
</script>
