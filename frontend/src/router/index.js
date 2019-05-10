import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/pages/Home'
import NotFound from '@/components/pages/NotFound'
import Integral from '@/components/pages/Integral'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/integral',
      name: 'Integral',
      component: Integral
    },
    {
      path: '*',
      name: 'Not found',
      component: NotFound
    }
  ]
})

router.beforeEach((to, from, next) => {
  document.title = to.name
  next()
})

export default router