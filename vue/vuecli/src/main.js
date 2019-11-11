import Vue from 'vue' // vue
import App from './App.vue' // vue 파일(내가 만든)

new Vue({
    el: '#app',
    render: function(createElement) {
        return createElement(App)
    }

})