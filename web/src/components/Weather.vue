<template>
  <div class="container">
    <br/>
    <div class="row">
      <div class="col-sm-5 search-box">
          <form id="demo" @click.prevent="getAddress()">
            <p>
              <input
                type="text"
                ref="my_input"
                class="form-control search-input"
                placeholder="enter an address"
              >
            </p>
            <p>
             <input
               type="submit"
               class="container-fluid search-btn"
               value="show me the current temperature"
             >
            </p>
            <p>{{ loading }}</p>
          </form>
      </div>
      <div class="col"></div>
      <div class="col-sm-3 temperature-box">
        <h6>{{ city }}</h6>
        <h1>{{ temperature }}</h1>
      </div>
      <div class="col"></div>
    </div>
    <br/>
    <br/>
    <div class="row">
      <table class="table table">
        <thead>
          <tr>
            <th scope="col">Search logs</th>
          </tr>
        </thead>
        <tbody v-for="log in logs" :key="log.message">
          <tr>
            <td>{{ log.address }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
  .temperature-box {
    background-color: #FFF;
    padding-left: 50px !important;
    padding-top: 15px;
    box-shadow: 0 4px 8px 0 silver, 0 6px 20px 0 silver;
    height: 120px;
    width: 120px !important;
  }
  .temperature-box h1 {
    font-size:50px;
    font-weight: bold;
  }
  .temperature-box h6 {
    font-size: 16px;
    font-weight: bolder;
  }
  .search-btn {
    background-color: #65b8a0;;
    color: #fff;
    padding: 5px;
    border:0;
  }
  .search-input {
    border: 2px silver;
  }
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      demo: {
        address: '',
      },
      loading: '', // todo: use an icon
      city: 'New York City, NY',
      temperature: '10° C',
      logs: [],
    };
  },
  methods: {
    getAddress() {
      if (this.$refs.my_input.value.length > 3) {
        this.loading = 'Loading...';
        const path = 'http://0.0.0.0:5000/api/temperature'; // Todo: move to a environ variable
        const logsPath = 'http://0.0.0.0:5000/api/logs'; // Todo: move to a environ variable
        const data = new FormData();
        data.append('address', this.$refs.my_input.value); // Todo: get it by input
        const headers = {
          headers: {
            'Content-type': 'application/json',
          },
        };

        axios.post(path, data, headers)
          .then((res) => {
            const response = res.data;
            this.temperature = response.temp;
            this.city = response.city;
            this.loading = '';
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });

        axios.get(logsPath)
          .then((res) => {
            const response = res.data;
            this.logs = response;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
  },
};
</script>
