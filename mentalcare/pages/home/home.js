var time = require('../../utils/util.js');
//var app = getApp();
Page({
  data: {
    //全局变量
         list: [],
    //加载样式是否显示
         loading: true
  },

  onLoad: function (options) {
    var that = this;       //很重要，一定要写
    that.setData({//循环完后，再对list进行赋值
      list: [
        { id: 101, 
          photo:"https://i.loli.net/2019/07/13/5d29ecc5500f824811.jpg",
          name:"张三",
          mood:"心情低落，需要安抚",
          lastevent:"入营",
          lastdate:"2019-06-07 11:12"
        },
        {
          id: 102,
          photo: "https://i.loli.net/2019/07/13/5d29ecc5500f824811.jpg",
          name: "李四",
          mood: "心情好转，适当慰问",
          lastevent: "入营",
          lastdate: "2019-06-04 18:23"
        },
        {
          id: 103,
          photo: "https://i.loli.net/2019/07/13/5d29ecc5500f824811.jpg",
          name: "王五",
          mood: "心情变坏，特别关注！",
          lastevent: "心情低落",
          lastdate: "2019-06-08 08:07"
        },
        
        ],
      loading: false
    }),
    wx.request({
      url: '',//和后台交互的地址，默认是json数据交互，由于我的就是json，这里就没有对header进行编写
      data: {},
      method: 'POST',
      success: function (res) {
        var datas = res.data;//res.data就是从后台接收到的值
        for (var i = 0; i < datas.length; i++) {//用for循环把所有的时间戳都转换程时间格式，这里调用的是小程序官方demo中带的方法，
          datas[i]["consumption_date"] = time.formatTime(new Date(datas[i]["consumption_date"]))
        }
        that.setData({//循环完后，再对list进行赋值
          list: datas,
          loading: false
        })
      },
      fail: function (res) {
        console.log('submit fail');
      },
      complete: function (res) {
        console.log('submit complete');
      }
    })
  }
})