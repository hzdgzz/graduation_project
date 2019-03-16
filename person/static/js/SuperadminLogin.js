// 浏览器写入cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function(){
     // var superadminloginform = $('#superadminloginform')
    // form表单提交
    $("#superadminloginform").submit(function(e){

        e.preventDefault()
        var superadmin_id = $("#supadminuser").val()
        var superadmin_password = $("#supadminpsw").val()


        // 发起登录请求
        var params = {
            'superadmin_id':superadmin_id,
            'superadmin_password':superadmin_password
        };
        // 发起ajax请求
        $.ajax({
            url:'/login',
            type:'post',
            data:JSON.stringify(params),
            contentType:'application/json',
            headers: {
                    "X-CSRFToken": getCookie('csrf_token')
                },
            success:function(data){
                if (data.errno == 0){
                    window.location.href='/Supersons.html'
                    alert('success')
                }else{
                    alert('用户名或密码错误!')
                }
            }
        })


    })


})