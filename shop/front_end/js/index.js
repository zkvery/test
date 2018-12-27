var vm = new Vue({
    el :'#app',
    data:{
        host:'http://127.0.0.1:8000',
        username:sessionStorage.getItem('username')||localStorage.getItem('username'),
        mobile:'',
        address:'',


    },

    methods:{
        logout: function(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
    }

});