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
    // 表单默认隐藏
    addform.hide()
    editform.hide()
    // 监控增加按钮
    addbtn.click(function () {
        addform.show()
    })
    // 监控编辑按钮
    editbtn.click(function () {
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

            var department_id = $("#department_id").val()
            var department_name = $("#department_name").val()

            // 发起新增请求
            var params = {
                'department_id': department_id,
                'department_name': department_name
            };
            // 发起ajax请求
            $.ajax({
                url: '/add_department',
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
                        alert('新增部门数据失败!')
                    }
                }
            })
        } else if ($(this).prop('type') == 'reset') {

            document.getElementById("supersonsform").reset();
        }
    })

    // 监听编辑弹框的按钮
    // 事件委托,监控点击登录和注册
    pop_text_btn1.delegate('input', 'click', function () {
        if ($(this).prop('type') == 'submit') {
            // 发送ajax请求
            alert('f')
        } else if ($(this).prop('type') == 'reset') {
            // 发送ajax请求
            alert('b')
        }
    })
    // 监控退出登录按钮
    exit.click(function () {
        // 发起ajax请求
        $.ajax({
            url: '/exit_department',
            type: 'post',
            contentType: 'application/json',
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (data) {
                if (data.errno == 0) {
                    //刷新当前页面
                    window.location.href = '/'
                    alert('退出登录成功!')

                } else {
                    alert('退出登录失败!')
                }
            }
        })
    })
})
