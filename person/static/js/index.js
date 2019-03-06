$(function(){
    // 获取元素登录或注册
    var sureperson = $('#sureperson')
    var personbtn = $('#personbtn')
    var chooseperson = $('#chooseperson')
    
    // 监控身份登录确定按钮
    sureperson.click(function(){
        // 点击进入相应的人员界面，随后输入账号和密码
        if(chooseperson.prop('value') == '0'){
            window.location.href = 'SuperadminLogin.html';
        }else{
            window.location.href = 'AdminLogin.html';
        }
        
    })
})
