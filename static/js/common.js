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


