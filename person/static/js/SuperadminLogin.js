$(function(){
     // var superadminloginform = $('#superadminloginform')
    // form表单提交
    $("#superadminloginform").submit(function(e){

        e.preventDefault()
        var mobile = $("#supadminuser").val()
        var password = $("#supadminpsw").val()


        // 发起登录请求
        var params = {
            'mobile':mobile,
            'password':password
        };
        // 发起ajax请求
        $.ajax({
            url:'/login',
            type:'post',
            data:JSON.stringify(params),
            contentType:'application/json',
            // headers: {
            //         "X-CSRFToken": getCookie('csrf_token')
            //     },
            success:function(data){
                if (data.errno == 0){
                    window.location.href='/Supersons.html'
                    alert('success')
                // if (data.errno == '0'){
                //     location.reload()
                }else{
                    alert('error!')
                }
            }
        })


    })


})