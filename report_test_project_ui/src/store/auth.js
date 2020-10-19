import axios from 'axios'
import Vue from 'vue'

export default {
    state: {
        authUser: {},
        isAuthenticated: false,
        jwt: localStorage.getItem('token'),
        authEndpoints: {
            obtainJWT: 'http://127.0.0.1:8000/auth/jwt/create/',
            refreshJWT: 'http://127.0.0.1:8000/auth/jwt/refresh/',
            createUser: 'http://127.0.0.1:8000/auth/users/'
        }
    },
    actions: {
        login({dispatch, commit, state}, userData) {
            return axios.post(state.authEndpoints.obtainJWT, userData)
        },
        registration({dispatch, commit, state}, userData) {
            return axios.post(state.authEndpoints.createUser, userData)
        }
    },
    mutations: {
        setAuthUser(state, {
            authUser,
            isAuthenticated,
        }) {
            Vue.set(state, 'authUser', authUser)
            Vue.set(state, 'isAuthenticated', isAuthenticated)
        },
        updateToken(state, newToken) {
            localStorage.setItem('token', newToken)
            state.jwt = newToken
        },
        removeToken(state) {
            localStorage.removeItem('token')
            state.jwt = null
        }
    }
}