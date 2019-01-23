var vm = new Vue({
    el :'#app',
    data:{
        host:'http://127.0.0.1:8000',
        username:sessionStorage.getItem('username')||localStorage.getItem('username'),
        mobile:'',
        address:'',
        typeinfo:[],
        bannerinfo:[],


    },
    mounted:function(){
        this.get_typeinfo()
        this.get_bannerinfo()
    },
    methods:{
        logout: function(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },

        get_typeinfo:function () {
            axios.get(this.host+'/typeinfo/',{
            }).then(response=>{
                console.log(response.data)
                this.typeinfo = response.data
            })
        },
        get_bannerinfo:function () {
            axios.get(this.host+'/get_banner/',{
            }).then(response=>{
                this.bannerinfo = response.data
            })

        },
        gooddetail:function (goodid,typeid) {
            location.href = '/detail.html?goodid='+goodid +'&typeid='+typeid

        },
        goodlists:function (id) {
            location.href = '/list.html?typeid='+id
        }
    }

});