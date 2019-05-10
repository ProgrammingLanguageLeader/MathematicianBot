import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/pages/Home'
import NotFound from '@/components/pages/NotFound'
import Integral from '@/components/pages/Integral'
import Derivative from '@/components/pages/Derivative'
import Limit from '@/components/pages/Limit'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/integral',
      name: 'Integral',
      component: Integral
    },
    {
      path: '/derivative',
      name: 'Derivative',
      component: Derivative
    },
    {
      path: '/limit',
      name: 'Limit',
      component: Limit
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
