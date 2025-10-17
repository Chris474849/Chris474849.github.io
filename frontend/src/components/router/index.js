import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Login from '../pages/Login.vue'
import Admin from '../pages/Admin.vue'

const isAuthenticated = () => !!sessionStorage.getItem('authUser')

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) next('/admin')
      else next()
    },
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    meta: { requiresAuth: true },
  },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const loggedIn = isAuthenticated()
  if (to.meta.requiresAuth && !loggedIn) next('/login')
  else if (to.path === '/login' && loggedIn) next('/admin')
  else next()
})

export default router
