// pages/item/item.js
var time = require('../../utils/util.js')

Page({
  data: {
    thisitem: {},
    loading: true
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    that.setData ({
      thisitem: {
        id: 101,
        photo: "https://i.loli.net/2019/07/13/5d29ecc5500f824811.jpg",
        sexy:"男",
        family:"丧偶",
        name:"张三",
        mood:"心情低落，需要安抚",
        history:[
          "2019-06-07 11:12 入营",
          "2019-06-07 11:12 入营",
          "2019-06-07 11:12 入营"
        ],
        suggestion:"处于创伤第一周，可以提供被动情感支持。典型的话术例如："
      }
    });
    wx.request({
      url: '' + options.id,//options.id是从list页面跳转过来带的参数，可以用来url拼接。比如根据id查询啊什么的
      data: {},
      method: 'POST',
      success: function (res) {
        console.log(res.data);
        var datas = res.data;
        datas["consumption_date"] = time.formatTime(new Date(datas["consumption_date"]))
        that.setData({
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
}
)
