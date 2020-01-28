Page({
    data: {
        basicsList: [ {
            icon: "usefullfill",
            name: "开始"
        }, {
            icon: "radioboxfill",
            name: "等待"
        }, {
            icon: "roundclosefill",
            name: "错误"
        }, {
            icon: "roundcheckfill",
            name: "完成"
        } ],
        basics: 0,
        numList: [ {
            name: "开始"
        }, {
            name: "等待"
        }, {
            name: "错误"
        }, {
            name: "完成"
        } ],
        num: 0,
        scroll: 0
    },
    basicsSteps: function() {
        this.setData({
            basics: this.data.basics == this.data.basicsList.length - 1 ? 0 : this.data.basics + 1
        });
    },
    numSteps: function() {
        this.setData({
            num: this.data.num == this.data.numList.length - 1 ? 0 : this.data.num + 1
        });
    },
    scrollSteps: function() {
        this.setData({
            scroll: 9 == this.data.scroll ? 0 : this.data.scroll + 1
        });
    }
});