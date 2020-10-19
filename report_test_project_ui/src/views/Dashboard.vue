<template>
  <v-container>
    <v-form v-model="valid" ref="form">
      <v-row>
        <v-col cols="2" offset="3">
          <template>
            <v-file-input
                id="file_1"
                ref="file_1"
                @change="validate"
                :rules="fileRules"
                label="cfn_inventory"
            ></v-file-input>
          </template>
        </v-col>
        <v-col cols="2">
          <template>
            <v-file-input
                id="file_2"
                ref="file_2"
                @change="validate"
                :rules="fileRules"
                label="inventory_listing"
            ></v-file-input>
          </template>
        </v-col>
        <v-col cols="2">
          <template>
            <v-file-input
                id="file_3"
                ref="file_3"
                @change="validate"
                :rules="fileRules"
                label="reserved_inventory"
            ></v-file-input>
          </template>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2" offset="5">
          <v-btn
              :disabled="!valid"
              @click="uploadFiles"
              depressed
              block
              color="primary">
            Upload
          </v-btn>

        </v-col>
      </v-row>
      <v-row v-show="file_path">
        <v-col cols="2" offset="5">
          <v-btn  block color="success">
            <a :href="file_path" download="" style="text-decoration: none; color: white">Download</a>
          </v-btn>
        </v-col>
      </v-row>
    </v-form>

  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: "Dashboard",
  title: 'Dashboard',
  data: () => ({
    report_files_id: null,
    file_path: null,
    task_id: null,
    links: [
      {title: 'Dashboard', url: '/', exact: true},
    ],
    valid: false,
    fileRules: [
      v => !!v || 'File is required',
    ]
  }),
  methods: {
    validate() {
      this.$nextTick(() => {
        this.valid = Boolean(this.$refs.file_3.$refs.input.files[0] &&
            this.$refs.file_1.$refs.input.files[0] &&
            this.$refs.file_2.$refs.input.files[0])
      })
    },
    uploadFiles() {
      let formData = new FormData()
      formData.append('cfn_inventory', this.$refs.file_1.$refs.input.files[0])
      formData.append('inventory_listing', this.$refs.file_2.$refs.input.files[0])
      formData.append('reserved_inventory', this.$refs.file_3.$refs.input.files[0])

      const headers = {
        headers: {
          Authorization: `JWT ${this.$store.state.auth.jwt}`,
        }
      }

      axios.put(`${this.$store.state.baseUrl}/reports/create/`, formData, headers).then(response => {
        this.report_files_id = response.data.report_files_id
        this.task_id = response.data.task_id
        this.file_path = `${this.$store.state.baseUrl}${response.data.file_path}`
      })
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>