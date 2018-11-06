$(function () {
    var cxhr_btn = $('#cxhr_btn');
    cxhr_btn.click(function () {
        // 判断浏览器是否支持XMLHttpRequest
        if (window.XMLHttpRequest){
            console.log(new XMLHttpRequest());
            return new XMLHttpRequest();
        }else{
            console.log(new ActiveXObject());
            return new ActiveXObject('Microsoft.XMLHTTP');
        }
    });
});


$(function () {
    var ajaxBtn = $('#ajax');
    ajaxBtn.click(function () {
    // 创建/获取xhr
        var xhr = new XMLHttpRequest();
    // 创建请求 - open(method, url, async)
        xhr.open('get', '/ajax_server/', async=true);
    // 设置回调函数
        xhr.onreadystatechange = function (env) {
            // 判断xhr.readState是否为4, status是否为200
            if (xhr.readyState==4 && xhr.status==200){
                // 可以接收服务器的响应数据
                var resText = xhr.responseText;
                // 业务处理
                var showDiv = $('#show');
                showDiv.text(resText);
            }
        };
    // 发送请求
        xhr.send(null)
    });
});