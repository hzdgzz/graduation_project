// 浏览器写入cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function () {
    // 获取元素登录或注册
    var addbtn = $('#addbtn')
    var editbtn = $('#editbtn')
    var addform = $('.pop_main')
    var editform = $('.pop_main1')
    var pop_text_btn = $('.pop_text_btn')
    var pop_text_btn1 = $('.pop_text_btn1')
    var exit = $('#exit')
    var changepsw = $('#changepsw')
    // var editbtn=document.querySelectorAll('#editbtn');

    // 表单默认隐藏
    addform.hide()
    editform.hide()
    // 监控增加按钮
    addbtn.click(function () {
        addform.show()
    })
    // 监控编辑按钮
    editbtn.click(function () {
        var editbtnlist = document.getElementsByTagName("button");
        for (var i = 1; i <= editbtnlist.length; i++) {
            editbtnlist[i].onclick = function () {
                editform.show()
            }
        }
        editform.show()
    })

    // 增加弹框操作
    // 监听灰色背景的点击
    $(".pop_main").click(function () {
        $(".pop_main").hide();// 隐藏页面
    })

    // 阻止白色内容展示部分事件冒泡
    $(".pop_con").click(function (event) {
        return false;
    })

    // 监听白色右上角,x按钮的点击
    $("#shutoff").click(function () {
        $(".pop_main").hide();// 隐藏页面
    })

    // 编辑弹框操作
    // 监听灰色背景的点击
    $(".pop_main1").click(function () {
        $(".pop_main1").hide();// 隐藏页面
    })

    // 阻止白色内容展示部分事件冒泡
    $(".pop_con1").click(function (event) {
        return false;
    })

    // 监听白色右上角,x按钮的点击
    $("#shutoff1").click(function () {
        $(".pop_main1").hide();// 隐藏页面
    })

    // 监听增加弹框的按钮
    // 事件委托,监控点击登录和注册
    pop_text_btn.delegate('input', 'click', function () {
        if ($(this).prop('type') == 'submit') {
            // 发送ajax请求
            // e.preventDefault();//阻止默认的表单提交

            var admin_id = $("#admin_id").val()
            var admin_psw = $("#admin_psw").val()

            // 发起新增请求
            var params = {
                'admin_id': admin_id,
                'admin_psw': admin_psw
            };
            // 发起ajax请求
            $.ajax({
                url: '/add_admin',
                type: 'post',
                data: JSON.stringify(params),
                contentType: 'application/json',
                headers: {
                    "X-CSRFToken": getCookie('csrf_token')
                },
                success: function (data) {
                    if (data.errno == 0) {
                        //刷新当前页面
                        window.location.reload()
                    } else {
                        alert('保存管理员数据失败!')
                    }
                }
            })
        } else if ($(this).prop('type') == 'reset') {
            // 发送ajax请求
            document.getElementById("supersonsform").reset();
        }
    })
    // 监听编辑弹框的按钮
    // 事件委托,监控保存和删除
    pop_text_btn1.delegate('input', 'click', function () {
        if ($(this).prop('type') == 'submit') {
            // 发送ajax请求
            alert('f')
        } else if ($(this).prop('type') == 'reset') {
            // 发送ajax请求
            alert('b')
        }
    })

    // 监控修改密码按钮
    changepsw.click(function () {
        // 发送ajax请求
        alert('changepsw')
    })
    // 监控退出登录按钮
    exit.click(function () {
        // 发送ajax请求
        alert('exit')
    })
})
