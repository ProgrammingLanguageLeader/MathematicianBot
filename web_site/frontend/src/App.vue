<template>
<div id="app">
  <b-navbar type="dark" variant="info">
    <b-container>
      <b-navbar-brand href="#">
        Mathematician Bot
      </b-navbar-brand>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">
            Web
          </b-nav-item>
          <b-nav-item href="https://t.me/clever_mathematician_bot">
            Telegram
          </b-nav-item>
          <b-nav-item href="#" disabled>
            VK
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-container>
  </b-navbar>
  <router-view />
</div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
</style>
