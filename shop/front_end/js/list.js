var vm = new Vue({
    el :'#app',
    data:{
        host:'http://127.0.0.1:8000',
        islogin:false,
        user_id : sessionStorage.user_id || localStorage.user_id,
        token : sessionStorage.token || localStorage.token,
        username:sessionStorage.username||localStorage.username,
        goodlist:'',
        typename:'',
        pagecount:'',
        every_data:'',
        new_goods:'',
        type_id:'',

    },
    mounted:function () {
        this.user_islogin();
        this.type_id = this.get_query_string('typeid');//获取html页面传递过来的类id
        var search = this.get_query_string('search');//获取搜索框的关键字
        if (this.type_id && search){
            this.search = '?search='+search;
            this.goodlists(this.type_id,this.search)
        }else{
            this.search = '';
            this.goodlists(this.type_id,)
        }

    },
    methods:{
        user_islogin:function () {
            if (this.user_id||this.token){
                console.log(this.username);
                this.islogin=true
            }else {
                this.islogin=false
            }
        },
        logout:function () {
            sessionStorage.clear();
            localStorage.clear();
            location.reload()
        },
         get_query_string: function(name){
            var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
            var r = window.location.search.substr(1).match(reg);
            if (r != null) {
                return decodeURI(r[2])
            }
            return null;
        },
        goodlists:function (typeid,search='') {
            // this.newgoods(typeid);
           axios.get(
               this.host+'/goodlists/'+typeid+search
           ).then(response=>{
                console.log(response.data)
                this.goodlist = response.data;




           })
        },
         //左侧最新商品
        // newgoods:function (typeid) {
        //     axios.get(
        //         this.host+'/newgoods/'+typeid
        //     ).then(response=>{
        //         this.new_goods = response.data;
        //     })
        // },

    }
});