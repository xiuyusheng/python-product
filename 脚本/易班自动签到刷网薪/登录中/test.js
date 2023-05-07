const aa=require("./smcp.min.js")
aa.initSMCaptcha(
    {
        organization: 'IY3HadrRSlgwwKWo63gi', //数美后台查看
        product: 'popup',
        appId: 'Yiban_Web',
        mode: modes[random(0, modes.length)],
        width: 300
    },
    function (instance) {
        //验证码实例，可以调用实例上的方法
        instance.onReady(function () {
            instance.verify();
        });
        instance.onSuccess(function (data) {
            if (data.pass) {
                console.log(data);
            } else {
                // return openCaptcha();
            }
        });
    }
)