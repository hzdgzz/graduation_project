$(function(){
    // 获取元素登录或注册
    var btn = $('.indexbtn')
    var sureperson = $('#sureperson')
    var formbox1 = $('#formbox1')
    var formbox2 = $('#formbox2')
    var personbtn = $('#personbtn')
    var chooseperson = $('#chooseperson')

    // 表单默认隐藏
    formbox1.hide()
    formbox2.hide()
    // 事件委托,监控点击登录和注册
    btn.delegate('input','click',function(){
        if($(this).prop('type') == 'submit'){
            alert('f')
        }else if($(this).prop('type') == 'reset'){
            alert('b')
        }
    })
    // 监控身份登录确定按钮
    sureperson.click(function(){
        // 点击进入相应的人员界面，随后输入账号和密码
        if(chooseperson.prop('value') == '0'){
            personbtn.hide()
            formbox2.show()

        }else{
            personbtn.hide()
            formbox1.show()
        }
        
    })
})
