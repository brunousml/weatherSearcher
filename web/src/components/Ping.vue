<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://0.0.0.0:5000/api/temperature';
      const data = new FormData();
      data.append('address', 'rua pedro sampronha piracicaba');
      const headers = {
        headers: {
          'Content-type': 'application/json',
        },
      };
      axios.post(path, data, headers)
        .then((res) => {
          console.log(res);
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
