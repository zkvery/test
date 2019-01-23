/**
 * Created by fuyang on 2018/11/18.
 */
var vm = new Vue({
    el:'#app',
    data:{
        error_username: false,
        error_pwd:false,
        username:'',
        password:'',

        error_name_message:'',
        error_pwd_message:'',
        remember:false
    },

    methods:{
        // 获取url路径参数
        get_query_string: function(name){
            var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
            var r = window.location.search.substr(1).match(reg);
            if (r != null) {
                return decodeURI(r[2]);
            }
            return null;
        },

        // 检查用户名
        check_username: function () {
            if (!this.username){
                this.error_username = true;
                this.error_name_message = '请填写用户名';
                console.log(this.username.length)

            }else {
                this.error_username = false
            }
        },

        // 检查密码
        check_pwd:function () {
            if (!this.password){
                this.error_pwd = true
                this.error_pwd_message = '请填写密码'
            }else {
                this.error_pwd = false
            }
        },

        // 发起登录请求
        on_submit:function () {
            this.check_username()
            this.check_pwd()
            if (this.error_username == false && this.error_pwd == false){
                axios.post('http://127.0.0.1:8000/authorizations/',{
                    username:this.username,
                    password:this.password,
                },{
                    responseType:'json'
                }).then(response => {
                    // 使用浏览器本地存储保存token,localStorage浏览器关闭，仍然有效，sessionStorage关闭就没了
                    // console.log(response.data.user_name,response.data.user_id)

                    if (this.remember){
                        sessionStorage.clear()

                        localStorage.username=response.data.user_name
                        localStorage.user_id=response.data.user_id
                        localStorage.token=response.data.token
                    }else {
                        localStorage.clear()
                        sessionStorage.username=response.data.user_name
                        sessionStorage.user_id=response.data.user_id
                        sessionStorage.token=response.data.token
                    }
                    var return_url = this.get_query_string('next')
                    if (!return_url){
                        location.href='/index.html'
                    }else {
                        location.href=return_url
                    }

                }).catch(error => {
                    if(error.response.status==400)
                    this.error_pwd = true;
                    this.error_pwd_message='用户名或者密码错误'
                    console.log(this.error_pwd_message)
                })
            }
        },

        // 第三方登录
        qq_login:function () {
            var state = this.get_query_string('next') || '/';
            axios.get(this.host + '/oauth/qq/authorization/?state=' + state, {
                responseType:'json'
            }).then(respone => {
                location.href = respone.data.auth_url;
            }).catch(error => {
                console.log(error)
            })
        },

        //第三方微博登录
        weibo_login:function () {
            var state = this.get_query_string('next') || '/';
            axios.get('http://127.0.0.1:8000/weibo/authorization/', {
                responseType:'json'
            }).then(respone => {
                console.log(respone.data)
                location.href = respone.data.auth_url;


            }).catch(error => {
                console.log(error)
            })
        },



    }

})