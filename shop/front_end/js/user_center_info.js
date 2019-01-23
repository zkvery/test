var vm = new Vue({
    el :'#app',
    data:{
        host:'http://127.0.0.1:8000',
        user_id: sessionStorage.getItem('user_id') || localStorage.getItem('user_id'),
        token: sessionStorage.getItem('token') || localStorage.getItem('token'),
        mobile: '',
        address: '',
        username:sessionStorage.getItem('username')||localStorage.getItem('username'),

    },
        mounted: function(){
        // 判断用户的登录状态
        //     console.log(this.user_id);
        //     console.log('111'+this.token);
        if (this.user_id && this.token) {
            console.log(this.token)
            axios.get(this.host + '/user_infos/', {
                    // 向后端传递JWT token的方法
                headers: {
                        // 需要注意！！！Authorization是固定的，JWT后面有空格
                        'Authorization': 'JWT ' + this.token
                    },
                    responseType: 'json',

                })

                .then(response => {
                    // 加载用户数据
                    console.log('22'+response.data)
                    this.mobile = response.data.mobile;
                })
                .catch(error => {

                    if (error.response.status==401 || error.response.status==403) {
                        console.log('111'+error)
                    }
                });
        } else {
            location.href = '/login.html?next=/user_center_info.html';
        }
    },

    methods:{
        logout: function(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
    }

});