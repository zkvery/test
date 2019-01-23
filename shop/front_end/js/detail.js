var vm =new Vue({
    el :'#app',
    data:{
        host:"http://127.0.0.1:8000",
        goodinfo:[],
        goodid:'',
        typeid:'',
        goodprice:'',
        goodjianjie:'',
        goodname:'',
        goodimage:'',
        goodunit:"",
    } ,
    mounted:function () {
        this.goodid = this.get_query_string('goodid');
        console.log('goodid'+this.goodid);
        this.typeid = this.get_query_string('typeid');
        console.log('typeid'+this.typeid);
        this.gooddetail()
    },
    methods:{
          get_query_string: function(name){
            var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
            var r = window.location.search.substr(1).match(reg);
            if (r != null) {
                return decodeURI(r[2])
            }
                return null;
        },
          gooddetail:function () {
                axios.get(
                    this.host+'/gooddetail/'+this.goodid
                ).then(response=>{
                    this.goodinfo = response.data;
                    this.goodname = response.data.name;
                    this.goodprice = response.data.price;
                    this.goodjianjie = response.data.jianjie;
                    console.log(this.goodjianjie)
                    console.log(this.goodprice)
                    this.goodunit = response.data.unit;
                    this.goodimage = response.data.image;
                     console.log(response.data.image)


                })
        }
    }
});