import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Dashboard',
        meta: {'layout': 'main'},
        component: () => import('../views/Dashboard')
    },
    {
        path: '/login',
        name: 'login',
        meta: {layout: 'empty'},
        component: () => import('../views/Login')
    },
    {
        path: '/register',
        name: 'register',
        meta: {layout: 'empty'},
        component: () => import('../views/Register')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
