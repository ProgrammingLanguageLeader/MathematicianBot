<template>
<div id="app">
  <b-navbar type="dark" variant="info" toggleable="sm">
    <b-container>
      <b-navbar-brand href="#">
        Mathematician Bot
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

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
  <transition name="fade">
    <router-view />
  </transition>
</div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.input-group-text {
  width: 110px;
}

.fade-enter-active, .fade-leave-active {
  position: fixed;
  transition: opacity .3s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
