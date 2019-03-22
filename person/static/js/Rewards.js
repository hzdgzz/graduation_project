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
    var userId;
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
        userId = $(this).parent().parent().children().eq(0).text();
    })
    // 增加弹框操作
    // 监听灰色背景的点击
    $(".pop_main").click(function () {
        $(".pop_main").hide();// 隐藏页面
        document.getElementById("addrewardsfrom").reset();
    })

    // 阻止白色内容展示部分事件冒泡
    $(".pop_con").click(function (event) {
        event.stopPropagation();
    })

    // 监听白色右上角,x按钮的点击
    $("#shutoff").click(function () {
        $(".pop_main").hide();// 隐藏页面
        document.getElementById("addrewardsfrom").reset();
    })

    // 编辑弹框操作
    // 监听灰色背景的点击
    $(".pop_main1").click(function () {
        $(".pop_main1").hide();// 隐藏页面
        document.getElementById("edirewardsfrom").reset();
    })

    // 阻止白色内容展示部分事件冒泡
    $(".pop_con1").click(function (event) {
        event.stopPropagation();
    })

    // 监听白色右上角,x按钮的点击
    $("#shutoff1").click(function () {
        $(".pop_main1").hide();// 隐藏页面
        document.getElementById("edirewardsfrom").reset();
    })

    // 监听增加弹框的按钮
    // 事件委托,监控点击登录和注册
    pop_text_btn.delegate('input', 'click', function () {
        if ($(this).prop('type') == 'submit') {
            // 发送ajax请求
            // e.preventDefault();//阻止默认的表单提交
            var auser_id = $("#auser_id").val()
            var auser_name = $("#auser_name").val()

            var auser_tel = $("#auser_tel").val()
            var auser_reward = $("#auser_reward").val()
            var auser_punish = $("#auser_punish").val()

            // 发起新增请求
            var params = {
                'auser_id': auser_id,
                'auser_name': auser_name,
                'auser_tel': auser_tel,
                'auser_reward': auser_reward,
                'auser_punish': auser_punish
            };
            // 发起ajax请求
            $.ajax({
                url: '/add_userreward',
                type: 'post',
                data: JSON.stringify(params),
                contentType: 'application/json',
                headers: {
                    "X-CSRFToken": getCookie('csrf_token')
                },
                success: function (data) {
                    if (data.errno == '0') {
                        //刷新当前页面
                        alert('新增员工奖惩数据成功!')
                        window.location.reload()
                    } else {
                        alert('新增员工奖惩数据失败!')
                        window.location.reload()
                    }
                }
            })
            return false
        } else if ($(this).prop('type') == 'reset') {
            // 发送ajax请求
            alert('b')
        }
    })

    // 监听编辑弹框的按钮
    // 事件委托,监控点击登录和注册
    pop_text_btn1.delegate('input', 'click', function () {
        if ($(this).prop('type') == 'submit') {
            // 发送ajax请求
            // e.preventDefault();//阻止默认的表单提交

            var auser_id = $("#auser_id").val()
            var auser_name = $("#auser_name").val()

            var auser_tel = $("#auser_tel").val()
            var auser_email = $("#auser_email").val()

            // 发起新增请求
            var params = {
                'auser_id': auser_id,
                'auser_name': auser_name,
                'auser_age': auser_age,
                'auser_gender': auser_gender,
                'auser_department': auser_department,
                'auser_tel': auser_tel,
                'auser_email': auser_email
            };
            // 发起ajax请求
            $.ajax({
                url: '/add_admindepartment',
                type: 'post',
                data: JSON.stringify(params),
                contentType: 'application/json',
                headers: {
                    "X-CSRFToken": getCookie('csrf_token')
                },
                success: function (data) {
                    if (data.errno == '0') {
                        //刷新当前页面

                        window.location.reload()
                    } else {
                        alert('新增员工数据失败!')
                    }
                }
            })
            return false
        } else if ($(this).prop('type') == 'reset') {
            // 发送ajax请求
            alert('b')
        }
    })
    // 监控退出登录按钮
    exit.click(function () {
        // 发起ajax请求
        $.ajax({
            url: '/exit_rewards',
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
