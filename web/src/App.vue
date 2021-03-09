<template>
  <div id="app">
    <nav class="navbar navbar-light bg-light box-shadow-cl">
      <h1 class="title">Loadsmart Weather</h1>
    </nav>
    <router-view/>
  </div>
</template>
<style>
  body {
    background-color: #eee !important;
  }
  h1.title {
    font-size: 21px;
    margin-left: 50px;
    font-weight: bold;
    margin-top: 10px;
  }
  nav.box-shadow-cl{
    box-shadow: 0 5px 5px #dfdddd;
    margin-top: 2px;
  }
</style>
