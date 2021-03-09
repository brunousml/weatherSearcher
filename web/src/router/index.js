import Vue from 'vue';
import Router from 'vue-router';
import Weather from '../components/Weather.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Weather',
      component: Weather,
    },
  ],
});
