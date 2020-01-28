var t = getApp();

Component({
    options: {
        addGlobalClass: !0
    },
    data: {
        StatusBar: t.globalData.StatusBar,
        CustomBar: t.globalData.CustomBar,
        list: [ {
            title: "索引列表",
            img: "https://image.weilanwl.com/color2.0/plugin/sylb2244.jpg",
            url: "/indexes/indexes"
        }, {
            title: "微动画",
            img: "https://image.weilanwl.com/color2.0/plugin/wdh2236.jpg",
            url: "/animation/animation"
        }, {
            title: "全屏抽屉",
            img: "https://image.weilanwl.com/color2.0/plugin/qpct2148.jpg",
            url: "/drawer/drawer"
        }, {
            title: "垂直导航",
            img: "https://image.weilanwl.com/color2.0/plugin/qpczdh2307.jpg",
            url: "/verticalnav/verticalnav"
        } ]
    },
    methods: {
        toChild: function(t) {
            wx.navigateTo({
                url: "/pages/plugin" + t.currentTarget.dataset.url
            });
        }
    }
});