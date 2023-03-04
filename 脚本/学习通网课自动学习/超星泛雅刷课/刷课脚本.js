// ==UserScript==
// @name         🔥超星学习通小助手[章节、作业、考试] 全自动解放双手
// @namespace    http://tampermonkey.net/
// @version      3.7.8
// @description  超星全自动刷课，支持章节、作业、考试等多项任务点。
// @author       爱吃蛋炒饭
// @run-at       document-end
// @match        *://*.chaoxing.com/*
// @match        *://*.edu.cn/*
// @match        *://*.nbdlib.cn/*
// @match        *://*.hnsyu.net/*
// @connect      cx.icodef.com
// @connect      sso.chaoxing.com
// @connect      mooc1-api.chaoxing.com
// @connect      mooc1-1.chaoxing.com
// @connect      mooc1-2.chaoxing.com
// @connect      mooc2-ans.chaoxing.com
// @connect      mooc1.chaoxing.com
// @connect      fystat-ans.chaoxing.com
// @connect      api.dbask.net
// @connect      api1.dbask.net
// @connect      api2.dbask.net
// @connect      api3.dbask.net
// @connect      api4.dbask.net
// @connect      api5.dbask.net
// @icon         data:image/vnd.microsoft.icon;base64,AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////////////////f39//z8/P/19fX/2dnZ/7a2tv+lpaX/p6en/7i4uP/c3Nz/9fX1//39/f///////////////////////////////////////////////////////////////////////////////////////f39//z8/P/+/v7//Pz8/+3t7f+goKD/UlJS/yIiIv8pKSn/S0tL/1dXV/9YWFj/SEhI/yYmJv8kJCT/V1dX/6ampv/v7+///Pz8//39/f/9/f3////////////////////////////////////////////////////////////8/Pz//Pz8//T09P+QkJD/KSkp/1dXV/+FhYX/b29v/0VFRf8yMjL/JiYm/yQkJP8xMTH/RERE/29vb/+CgoL/UVFR/ywsLP+Xl5f/9vb2//z8/P////////////////////////////////////////////7+/v/+/v7//v7+//v7+//Nzc3/PDw8/1lZWf9+fn7/MjIy/wQEBP8CAgL/AgIC/wEBAf8BAQH/AQEB/wEBAf8BAQH/AgIC/wQEBP8yMjL/enp6/1NTU/9DQ0P/1tbW//7+/v/+/v7//v7+/////////////////////////////f39//v7+//6+vr/p6en/ysrK/+Ghob/PDw8/wQEBP8BAQH/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/Ozs7/4KCgv8oKCj/ra2t//v7+//+/v7////////////////////////////+/v7//Pz8/5qamv8tLS3/goKC/xQUFP8DAwP/AwMD/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/FhYW/319ff8rKyv/oaGh//7+/v/////////////////8/Pz//f39//39/f+3t7f/KCgo/4CAef8LChD/AQAE/wQDAf8CAAP/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAEA/wABAP8AAQD/AAEA/wABAP8DAAH/AAEB/wEDAP8BBAL/DQkQ/3t7e/8mJib/v7+///39/f/8/Pz///////z8/P/8/Pz/5ubm/ycnJ/+Ghof/DxAU/wMEAv8CAgH/AAMA/wAABf8AAAD/AQAA/wEAAP8BAAD/AQAA/wEAAP8BAAD/AQAA/wEAAP8BAAD/AAEA/wQAAP8AAAP/AwAE/wABAP8FAQL/ERER/4GBgf8sLCz/6enp//39/f///////v7+//z8/P9sbGz/bm5u/ycnKP8BAQn/EgIK/x4FGv8KDQr/CgoM/woKCv8MCgr/DAoK/wwKCv8MCgr/DAoK/wwKC/8MCgv/DAoL/wsKC/8KCwr/DgoL/woLDP8WDwb/AgIA/wUDAf8CAgL/KCgo/2dnZ/90dHT/+vr6//7+/v/9/f3/2dnZ/ywsLP9ubm7/AwMD/wMCAP9KE0f/2HLk//7++v/+/vz//P7+//v+/v/7/v7/+/7+//v+/v/7/v3/+/78//v+/P/6/vv/+v77//r/9//++/7//P7x/+Xte/8ICAD/AQAH/wAAAP8AAAD/bGxs/yoqKv/e3t7//f39//39/f90dHT/dXV1/xgYGP8CAgP/AwED/1cRTP/qZvP//P76//3++//++v7//vv///76/v/++v7//vr+//76/v/++v7//vr+//77/v/++v7//f34//76/v/9/u//7vRq/w0IAP8AAQP/AAAA/wAAAP8XFxf/b29v/3d3d//8/Pz/9vb2/yoqKv+Dg4P/AQEB/wEBAv8BAgT/UxFM/+9r6//7/f3//P74//779//p2db/p5SW/52Lj/+dipL/oIiW/5mKkv+biZX/tZCu/+fE4v//+vz//vz9//7+9v/07Xf/DQgA/wACAv8AAAD/AAAA/wAAAP9/f3//Li4u//X19f/Nzc3/PDw8/09PT/8AAAD/AAAA/wIABf9PEE//7mrs//z+/f/5/vj//P30//j47P/z8uz/8/Hx//Pv8v/17PP/7fHu/+3w8P/44/b/++r7//n4/v/9/P3//f72//TxcP8QCwD/AgIA/wAAAP8AAAD/AAAA/1BQUP84ODj/0tLS/5aWlv9nZ2f/FRUV/wAAAP8AAAH/AQAH/0UTSf/hcuH//vn+//n9/f/6/Pn/+v37//r9/P/7/f7/+/3+//38/v/3/vj/9v73//35/v/6+v3/9v75//v9+//+/fX/5/Jx/xAHAf8DAAP/AAAA/wAAAP8BAQH/FxcX/2VlZf+ampr/b29v/4ODg/8CAgL/AAAA/wEBAP8HAgP/Jgom/3szgf+MeY//lo6O/5mQkP+Zj5P/mI+T/5mPk/+Zj5L/mo+T/5iPkf+Xj5H/mY+T/5aQkf+WkI//kpCH/4eAb/9gaDf/CwYC/wADAP8AAAD/AAAA/wAAAP8DAwP/gYGB/3Fxcf9cXFz/g4OD/wEBAf8AAAD/BwIG/2AiX/+Ma4f/u43A/+rb7P/59/X/+vX6//r4+//6+Pv/+vj7//r4+//5+Pr/+vf7//v3+//5+fr/+vj6//v0+//4+PH/5N6//4qHff95eEP/HiEO/wAAAP8AAAD/AQEB/wEBAf+CgoL/W1tb/1NTU/94eHj/AQEB/wAAAP8DAAP/bhdy/+aO7//99fv/9fn8//n7/f/6+P///vz6//3++v/8/v7/+v78//z9/v/9/P7//Pz+//3++v/6+/7//f75//j8/P/+/fT/+PvH/7OyUf8NBQH/AAAA/wAAAP8AAAD/AQEB/3p6ev9XV1f/Wlpa/35+fv8AAAD/AAAA/wAAAP8QARD/ryyo//fB9v/79/z//Pr9//v5+v/19cf/sKmK/4NvfP9+c3X/d3dv/4Nyc/+XbZH/3aHl//v2/f/+/fv//fz8//z86//U4W3/LSIJ/wEEAv8AAAD/AAAA/wEBAf8AAAD/f39//2dnZ/9zc3P/gICA/wUFBf8AAAD/AAAA/wIEAf8uCCH/0T3X/+Vt7P/87Pn//Pr8//L99f/8+/z///37//v++//4/P7//vr+//X7+//5+vP//Pv5//75/f/6/Pr//fvl/9jdav8kJRP/AAMB/wAAAP8AAAD/AAAA/woKCv9xcXH/hoaG/56env9gYGD/JSUl/wAAAP8BAAH/BgAK/wUEAv9GDUv/mCWe/+aA5v/++vr/+fz8//v++////Pz//fz8//n9+v/4/fn//Pn+//v2/P/5+Pz//P34//r89//09br/j4Y3/wYFBf8AAQL/AAAA/wAAAP8AAAD/Kysr/1BQUP+wsLD/29vb/yoqKv9bW1v/AgIC/wABAP8LBQf/ZR1b/4Rwg/+Meon/woe5/9Cot//Ifrn/wa+7/8u0x//LpsT/1nu9/9C/1//hxND/28vJ/9Cprf+7f7j/ubKv/6iuf/96cEX/PkAR/wEDAf8AAAD/AAAA/wICAv9mZmb/ICAg/+np6f/5+fn/Ojo6/39/f/8CAgL/AwID/w0AEP+oI63/+r/4//z8+P/w/PX/9NLy/+SR4v/8+P3/+/v8//jo4v/qXNX/+ez+//35/f/3/vT/77bh//Ge7v//+vz/+/v8//T5xf+koF//LC4V/wgFAv8AAAH/AgIE/3R0dP9FRkX//Pz8//v7+/+RkZH/WFhY/zExMf8CAQL/BAAG/3gTfP/xkvH/+P77//37+//++P7//fb8//77/P/+/f3//vz4/+/C7//sx+///vz7//n+9//69/3///f7//77/f/7+/7//f30//786//b5XD/KCIK/wIDBP8wLzT/TExN/5+ioP///////Pz8/+7u7v8rKyv/hISE/wUFBf8DAQP/Qg5H/+dj5v/5+v3//vv7///3/v///fX//v71//77/v/++v3/98f0//CO7f/7/fz/+P78//r9/f/+/ff///z7//79/P/++v7//v3r/9vrdv8kIwb/BQkC/318fP80MjL/8fLz///+///9/f3//f39/56env9JSUn/UlNS/wQGAf8UAxj/vUDE//Hn8//z9O3/9PHw/+Xtxf+Sn3j/UlJS/1FTUf9rSm7/1GTd/+zx8v/z8vP/8/Tp/+Lntf90b1//U05T/09KUf9TT0n/RUYn/w8MBv9PUFD/QD09/6ypp//8/v3/////////////////9/f3/0tLS/9vbm7/Mi41/wYEBf8cABj/CAIF/wMCBf8EAwL/AwUC/wUGAf8BAQD/AAAB/wQBBP8VABX/AgQA/wgACP8HAAn/CwUA/wgDBP8DAwL/AAAD/wEDAP8EAQL/MC00/2RkbP9ZVVT/+ffz//n7+v/////////////////+/v7/4uLi/zEwMP96eHv/LC0p/wEHAf8CAAL/AAQB/wEDAv8CAAb/BAAH/wEAAf8AAAD/AAEB/wAFAf8HAQD/BQED/wADAf8CAgL/AQEH/wAEAP8AAAT/AAMA/ykoLv9ucm3/MzYz/+jn4v/9/Pv//Pz+///+//////////////39/f/8/Pz/0tLS/y8vL/91dXX/PT49/wMDA/8EBAT/AQEB/wAAAP8AAAH/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/AQIB/wICAv89PT3/bm1u/zIyMv/Z2dn//v7+///+/v///v///////////////////f39//v7+//5+fn/39/f/0hISP9ISEj/cHBw/xkZGf8CAgL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wICAv8aGhr/b29v/0ZGRv9LS0v/5OTk//v7+//+/v7////////////////////////////+/v7//f39//39/f/9/f3/9vb2/4qKiv8oKCj/ampq/2dnZ/8zMzP/BgYG/wAAAP8AAAD/AQEB/wAAAP8AAAD/AQEB/wYGBv80NDT/Z2dn/2tra/8nJyf/j4+P//b29v/9/f3//Pz8//7+/v////////////////////////////////////////////7+/v/+/v7//f39/97e3v9nZ2f/HR0d/1JSUv94eHj/cHBw/3Nzc/9ycnL/dnZ2/319ff9zc3P/eHh4/1FRUf8dHR3/aGho/9/f3//7+/v//Pz8/////////////////////////////////////////////////////////////v7+//7+/v/+/v7/+/v7//v7+//u7u7/q6ur/2lpaf87Ozv/Hx8f/w8PD/8QEBD/HR0d/zs7O/9qamr/ra2t/+3t7f/8/Pz//f39//39/f/9/f3/////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
// @grant        unsafeWindow
// @grant        GM_info
// @grant        GM_getResourceText
// @grant        GM_addStyle
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_xmlhttpRequest
// @antifeature  ads
// @require https://greasyfork.org/scripts/455606-layx-js/code/layxjs.js?version=1122546
// @require https://greasyfork.org/scripts/456170-hacktimerjs/code/hacktimerjs.js?version=1143079
// @require      https://lib.baomitu.com/jquery/3.6.0/jquery.min.js
// @require      https://cdn.jsdelivr.net/gh/photopea/Typr.js@15aa12ffa6cf39e8788562ea4af65b42317375fb/src/Typr.min.js
// @require      https://cdn.jsdelivr.net/gh/photopea/Typr.js@f4fcdeb8014edc75ab7296bd85ac9cde8cb30489/src/Typr.U.min.js
// @require      https://gcore.jsdelivr.net/gh/photopea/Typr.js@15aa12ffa6cf39e8788562ea4af65b42317375fb/src/Typr.min.js
// @require      https://gcore.jsdelivr.net/gh/photopea/Typr.js@f4fcdeb8014edc75ab7296bd85ac9cde8cb30489/src/Typr.U.min.js
// @require      https://testingcf.jsdelivr.net/gh/photopea/Typr.js@15aa12ffa6cf39e8788562ea4af65b42317375fb/src/Typr.min.js
// @require      https://testingcf.jsdelivr.net/gh/photopea/Typr.js@f4fcdeb8014edc75ab7296bd85ac9cde8cb30489/src/Typr.U.min.js
// @require      https://cdn.bootcdn.net/ajax/libs/blueimp-md5/2.18.0/js/md5.min.js
// @resource  layxcss https://greasyfork.org/scripts/455605-layx/code/layx.user.css
// @resource  layuicss https://lib.baomitu.com/layui/2.6.8/css/layui.css
// @resource  ttf https://www.forestpolice.org/ttf/2.0/table.json
// ==/UserScript==

var defaultConfig = {
    ua: 'Dalvik/2.1.0 (Linux; U; Android 12; M2102K1AC Build/SKQ1.211006.001) (schild:1b39227c6f3c3b7d95c59ad476567cdb) (device:M2102K1AC) Language/zh_CN com.chaoxing.mobile/ChaoXingStudy_3_6.1.0_android_phone_906_100 (@Kalimdor)_cc0454aaa3b7439daf7cebe7e43f62ba',
    interval: 3000,
    autoVideo: true,
    autoRead: true,
    autoAnswer: true,
    videoSpeed: 1,
    matchRate: 0.8,
    autoSubmitRate: 0.9,
    autoSubmit: true,
    randomAnswer: true,
    notice: '本脚本仅供学习研究，请勿使用于非法用途！<br>近期遭到频繁DDOS攻击，若出现不能使用，请耐心等待<br>交流群: 633087348',
    otherApi:'http://cx.icodef.com/wyn-nb?v=4',
    debugger: true,
    types: {
        '单选题': '0',
        '多选题': '1',
        '填空题': '2',
        '判断题': '3',
        '简答题': '4',
        '名词解释': '5',
        '论述题': '6',
        '计算题': '7',
    },
    script_info : GM_info.script,
},_self = unsafeWindow,top = _self;
var reqUrl ={
    "api":null,
    "headers":{
        'host': 'www.baidu.com',
    }
}
var baseUrls=[
    {
        url:'http://api.dbask.net:2333/',
        headers:{
            'host': 'www.baidu.com',
        }
    },
    {
        url:'http://api1.dbask.net:2333/',
        headers:{
            'host': 'www.baidu.com',
        }
    },
    {
        url:'http://api2.dbask.net:2333/',
        headers:{
            'host': 'www.baidu.com',
        }
    },
    {
        url:'http://api3.dbask.net:2333/',
        headers:{
            'host': 'www.baidu.com',
        }
    },
    {
        url:'http://api4.dbask.net:2333/',
        headers:{
            'host': 'www.baidu.com',
        }
    },
    {
        url:'http://api5.dbask.net/',
        headers:{
        }
    },
];
defaultConfig=GM_getValue('dcf_config6')||defaultConfig;
const log = msg => defaultConfig.debugger && console.log(msg);
(function () {
    'use strict';
    String.prototype.cl=function(){return this.replace(/\[.*?]|【.*?】|\d+\.\s*|\s*（\d+\.\d+分）|^\s*|\s*$/g,'')};
    var utils = {
        apiCheck: async ()=> {
            let res = await Promise.allSettled(baseUrls.map(async (item) => {
                return await utils.ping(item);
            }));
        },
        ping: async (item)=> {
            return new Promise(resolve => {
                GM_xmlhttpRequest({
                    method: 'GET',
                    url: item.url+"ping",
                    headers: item.headers,
                    timeout: 3000,
                    onload: function (response) {
                        if(response.status===200&&reqUrl.api==null){
                            reqUrl.api = item.url;
                            reqUrl.headers = item.headers;
                        }
                        resolve(response.status === 200);
                    },
                    ontimeout: function () {
                        resolve(false);
                    },
                    onerror: function () {
                        resolve(false);
                    }
                });
            });
        },
        apiWatch: async ()=> {
            return new Promise(resolve => {
                let timer = setInterval(() => {
                    if (reqUrl.api != null) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        },
        randomUA: ()=> {
            let device = ["Pixel 3", "Galaxy S10", "OnePlus 9", "Xiaomi Mi 11"];
            let version = ["12.0.0", "11.0.0", "10.0.0"];
            let schild = ["1b39227c6f3c3b7d95c59ad476567cdb", "2a6aeb95f9d4c3834a6a02b6c674a7a4", "d704ebf7c8688c3df3f0a035e20e1d77"];
            let deviceId = ["ee2d23e98a7d2e9d", "b76b5c5c5a5b3e3e", "8a1a924df6173905"];
            let randDevice = device[Math.floor(Math.random() * device.length)];
            let randVersion = version[Math.floor(Math.random() * version.length)];
            let randSchild = schild[Math.floor(Math.random() * schild.length)];
            let randDeviceId = deviceId[Math.floor(Math.random() * deviceId.length)];
            return `Dalvik/2.1.0 (Linux; U; Android ${randVersion}; ${randDevice} Build/SKQ1.211006.001) (schild:${randSchild}) (deviceId:${randDeviceId}) Language/zh_CN com.chaoxing.mobile/ChaoXingStudy_3_6.1.0_android_phone_906_100 (@Kalimdor)_cc${Math.floor(Math.random() * 100000000000000000000000000000000).toString(16)}`;
        },
        notify: (level, msg)=> {
            let data={
                level: level,
                msg: msg
            }
            return JSON.stringify(data);
        },
        sortData: (data)=> {
            const arr = [];
            data.forEach(item => {
              const parent = data.find(item2 => item2.id === item.parentnodeid);
              parent ? (parent.children || (parent.children = [])).push(item) : arr.push(item);
            });
            return arr;
        },
        toOneArray: (arr)=> {
            return arr.reduce((newArr, item) => newArr.concat(item, item.children ? utils.toOneArray(item.children) : []), []);
        },
        sleep: (time)=> {
            return new Promise(resolve => setTimeout(resolve, time));
        },
        getUrlParam: (name)=> {
            const reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
            const r = window.location.search.substr(1).match(reg);
            return r ? unescape(r[2]) : null;
        },
        toQueryString: (obj)=> {
            return obj ? Object.keys(obj).sort().map(key => {
              const val = obj[key];
              return Array.isArray(val) ? val.sort().map(val2 => encodeURIComponent(key) + '=' + encodeURIComponent(val2)).join('&') : encodeURIComponent(key) + '=' + encodeURIComponent(val);
            }).join('&') : '';
        },
        getInputParam: (name)=> {
            const input = document.getElementsByName(name)[0];
            return input ? input.value : null;
        },
        getVideoEnc: (clazzid,uid,jobid,objectId,playingTime,duration)=> {
            return md5( "["+clazzid+"]["+uid+"]["+jobid+"]["+objectId+"]["+(playingTime * 1000)+"][d_yHJ!$pdA~5]["+(duration * 1000)+"][0_"+duration+"]");
        },
        getTimestamp: ()=> {
            return new Date().getTime();
        }
        ,removeHtml: (html)=> {
            return html.replace(/<((?!img|sub|sup|br)[^>]+)>/g, '').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').replace(/<br\s*\/?>/g, '\n').trim();
        },
        setConfig: (config)=> {
            for (var key in config) {
                defaultConfig[key] = config[key];
                GM_setValue(key, config[key]);
            }
        }
        ,cache: (key, value, time)=> {
            var cache = GM_getValue(key);
            if (cache) {
                if (cache.time + time > utils.getTimestamp()) {
                    return cache.value;
                }
            }
            GM_setValue(key, {value: value, time: utils.getTimestamp()});
            return value;
        },
        matchIndex: (options,answer)=> {
            var matchArr=[];
            for(var i=0;i<answer.length;i++){
                for(var j=0;j<options.length;j++){
                    if(answer[i]==options[j]){
                        matchArr.push(j);
                    }
                }
            }
            return matchArr;
        }
        ,similarity: (s, t)=>{
            let l = Math.max(s.length, t.length);
            let n = s.length;
            let m = t.length;
            let d = Array.from({length: n + 1}, (_, i) => [i]);
            for (let j = 0; j <= m; j++) d[0][j] = j;
            for (let i = 1; i <= n; i++)
              for (let j = 1; j <= m; j++) {
                let cost = s[i - 1] === t[j - 1] ? 0 : 1;
                d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost);
              }
            return (1 - d[n][m] / l);
        }
        ,fuzzyMatchIndex: (options,answer)=> {
            const matchArr = [];
            for (const ans of answer) {
                let maxSim = 0, index = 0;
                for (let i = 0; i < options.length; i++) {
                const sim = similarity(ans, options[i]);
                if (sim > maxSim) {
                    maxSim = sim;
                    index = i;
                }
                }
                if (maxSim > defaultConfig.matchRate) matchArr.push(index);
            }
            return matchArr;
        }
        ,strContain:  (str, arr) => arr.some((item) => str.includes(item))
    };
    var api = {
        monitorVerify: (responseText,url, method, data, ua)=> {
            return new Promise((resolve, reject) => {
                try {
                    let obj = JSON.parse(responseText);
                    let divHtml='<img src="'+obj.verify_png_path+'"/> <input type="text" class="code_input" placeholder="请输入图中的验证码" /><button id="code_btn">验证</button>';
                        layx.prompt(divHtml,"请输入验证码",function(id,value,textarea, button, event){
                            let url=obj.verify_path+"&ucode="+value;
                            window.open(url);
                        });
                    } catch (error) {
                        let domain = url.match(/:\/\/(.[^/]+)/)[1];
                        let urlShowVerify = "https://"+domain+"/antispiderShowVerify.ac";
                        window.open(urlShowVerify);
                        let timer = setInterval(() => {
                            api.defaultRequest(url, method, data, ua,true).then((response) => {
                                if (response.responseText && !response.responseText.includes('输入验证码')) {
                                    clearInterval(timer);
                                    page.layx_log('验证码验证成功！', 'success');
                                    resolve(response);
                                }else{
                                    page.layx_log('验证码验证失败！将在5s后重新验证', 'error');
                                }
                            })
                        }, 5000);
                    }
            });
        },
        defaultRequest: async (url, method, data={}, ua=defaultConfig.ua,verify=false) => {
            try {
              const response = await new Promise((resolve, reject) => {
                GM_xmlhttpRequest({
                  url,
                  method,
                  headers: {
                    'User-Agent': ua,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Sec-Fetch-Site': 'same-origin',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                  },
                  data: utils.toQueryString(data),
                  onload: resolve,
                  onerror: reject
                });
              });
              if (!verify&&response.responseText && response.responseText.includes('输入验证码')) {
                page.layx_log('检测到验证码！将弹出新页面自行验证验证码（出现验证码多为间隔频率过短，或者请求过多，请根据自己情况调高运行间隔）', 'error');
                await api.monitorVerify(response.responseText,url, method, data, ua);
                return await api.defaultRequest(url, method, data);
              }
              return response;
            } catch (err) {
              return Promise.reject(err);
            }
        }
        ,  
        getCourseList:async ()=> {
            let result = await api.defaultRequest("https://mooc1-api.chaoxing.com/mycourse/backclazzdata?view=json&mcode=", 'GET');
            return JSON.parse(result.responseText);
        },
        getCourseChapter:async (courseId,classId)=> {
            let result = await api.defaultRequest("https://mooc1-api.chaoxing.com/gas/clazz?id="+classId+"&personid="+courseId+"&fields=id,bbsid,classscore,isstart,allowdownload,chatid,name,state,isfiled,visiblescore,begindate,coursesetting.fields(id,courseid,hiddencoursecover,coursefacecheck),course.fields(id,name,infocontent,objectid,app,bulletformat,mappingcourseid,imageurl,teacherfactor,jobcount,knowledge.fields(id,name,indexOrder,parentnodeid,status,layer,label,jobcount,begintime,endtime,attachment.fields(id,type,objectid,extension).type(video)))&view=json", 'GET');
            return JSON.parse(result.responseText);
        },
        getChapterList:async (courseid,clazzid,nodes,userid,cpi)=> {
            let data={
                "view":"json",
                "nodes":nodes,
                "clazzid":clazzid,
                "userid":userid,
                "cpi":cpi,
                "courseid":courseid,
                "time":(new Date()).valueOf()
            }
            let result = await api.defaultRequest("https://mooc1-api.chaoxing.com/job/myjobsnodesmap", 'post',data);
            return JSON.parse(result.responseText);
        },
        getCourseConfig:async (courseId,classId,cpi)=> {
            let result = await api.defaultRequest("https://mooc1-api.chaoxing.com/course/phone/get-course-setting?clazzId="+classId+"&courseId="+courseId+"&cpi="+cpi, 'GET');
            return JSON.parse(result.responseText);
        },
        getChapterInfo:async (id,courseid)=> {
            let data={
                "id":id,
                "courseid":courseid,
                "fields":"id,parentnodeid,indexorder,label,layer,name,begintime,createtime,lastmodifytime,status,jobUnfinishedCount,clickcount,openlock,card.fields(id,knowledgeid,title,knowledgeTitile,description,cardorder).contentcard(all)",
                "view":"json",
            }
            let url = "https://mooc1-api.chaoxing.com/gas/knowledge?"+utils.toQueryString(data);
            let result = await api.defaultRequest(url, 'get');
            return JSON.parse(result.responseText);
        },
        getChapterDetail:async (courseid,clazzid,knowledgeid,num,cpi)=> {
            let url = "https://mooc1-api.chaoxing.com/knowledge/cards?clazzid="+clazzid+"&courseid="+courseid+"&knowledgeid="+knowledgeid+"&num="+num+"&isPhone=1&control=true&cpi="+cpi;
            let result = await api.defaultRequest(url, 'get');
            return result.responseText;
        },
        uploadStudyLog:async (courseid,clazzid,knowledgeid,cpi)=> {
            let url = `${location.origin}/mooc2-ans/mycourse/studentcourse?courseid=${courseid}&clazzid=${clazzid}&cpi=${cpi}&ut=s&t=${utils.getTimestamp()}`
            let text=await api.defaultRequest(url,'get',{},navigator.userAgent);
            let match = text.responseText.match(/encode=([\w]+)/);
            if (match) {
                const encode = match[1];
                let url = `https://fystat-ans.chaoxing.com/log/setlog?personid=${cpi}&courseId=${courseid}&classId=${clazzid}&encode=${encode}&chapterId=${knowledgeid}`;
                let result = await api.defaultRequest(url, 'get',{},navigator.userAgent);
                return result.responseText;
            } 
            return false;
        },
        docStudy:async (jobid,knowledgeid,courseid,clazzid,jtoken)=> {
            let url = "https://mooc1-api.chaoxing.com/ananas/job/document?jobid="+jobid+"&knowledgeid="+knowledgeid+"&courseid="+courseid+"&clazzid="+clazzid+"&jtoken="+jtoken+"&_dc="+new Date().valueOf();
            let result = await api.defaultRequest(url, 'get');
            return JSON.parse(result.responseText);
        },
        videoStudy:async (data,cpi,dtoken)=> {
            let url = "https://mooc1-api.chaoxing.com/multimedia/log/a/"+cpi+"/"+dtoken+"?"+utils.toQueryString(data);
            let result = await api.defaultRequest(url, 'get');
            return JSON.parse(result.responseText);
        },
        getVideoConfig:async (objectId)=> {
            let url = "https://mooc1-1.chaoxing.com/ananas/status/"+objectId+"?k=&flag=normal&";
            let result = await api.defaultRequest(url, 'get');
            return JSON.parse(result.responseText);
        },
        unlockChapter:async (courseid,clazzid,knowledgeid,userid,cpi)=> {
            let url = `https://mooc1-api.chaoxing.com/job/submitstudy?node=${knowledgeid}&userid=${userid}&clazzid=${clazzid}&courseid=${courseid}&personid=${cpi}&view=json`;
            let result = await api.defaultRequest(url, 'get');
            return result.status;
        }
    };
    var ServerApi = {
        search:async function (data) {
            await utils.apiWatch();
            data.key=defaultConfig.token||'';
            $(".layx_status").html("正在搜索答案");
            let params = {
                "z":data.workType,
                "t":data.type,
                "token":defaultConfig.token||'',
                "u":_self.uid||'',
            }
            var url = reqUrl.api + 'answer?' + utils.toQueryString(params);
            return new Promise(function (resolve, reject) {
                GM_xmlhttpRequest({
                    method: 'post',
                    url: url,
                    data: JSON.stringify(data),
                    headers:  Object.assign({
                        'Content-Type': 'application/json',
                        'v': defaultConfig.script_info.version,
                        'referer': location.href,
                        't': utils.getTimestamp(),
                    },reqUrl.headers),
                    onload: function (response) {
                        resolve(response);
                    },
                    onerror: function (response) {
                        reject(response);
                    },
                    ontimeout: function (response) {
                        reject(response);
                    }
                });
            });
        },
        configRequest:function (url) {
            return new Promise(function (resolve, reject) {
                GM_xmlhttpRequest({
                    method: "get",
                    url: url,
                    headers: {
                        'referer': location.href,
                    },
                    onload: function (response) {
                        resolve(JSON.parse(response.responseText));
                    },
                    onerror: function (response) {
                        reject(response);
                    },
                    ontimeout: function (response) {
                        reject(response);
                    }
                });
            });
        },
        get_msg: async function(){
            await utils.apiWatch();
            var url = reqUrl.api + 'def/autoMsg';
            return new Promise(function(resolve, reject) {
                GM_xmlhttpRequest({
                    method: 'get',
                    url: url,
                    headers: Object.assign({
                        'referer': location.href,
                        't': utils.getTimestamp(),
                    },reqUrl.headers),
                    onload: function(response) {
                        try {
                            let reqData=JSON.parse(response.responseText);
                            resolve(reqData.data);
                        } catch (e) {
                            resolve(defaultConfig.notice);
                        }
                    },
                    onerror: function() {
                        resolve(defaultConfig.notice);
                    }
                });
            });
        }
        ,searchOther: function(data) {
            return new Promise((resolve, reject) => {
              GM_xmlhttpRequest({
                method: 'POST',
                url: defaultConfig.otherApi,
                data: `question=${encodeURIComponent(data.question)}`,
                headers: {
                  'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
                },
                onload: response => {
                  try {
                    const res = JSON.parse(response.responseText);
                    if (res.code === 1) {
                      let data = res.data.replace(/javascript:void\(0\);/g, '').trim().replace(/\n/g, '');
                      if (utils.strContain(data, ['叛逆', '公众号', '李恒雅', '一之'])) {
                        resolve([]);
                      } else {
                        resolve(data.split('#'));
                      }
                    } else {
                      reject([]);
                    }
                  } catch (error) {
                    reject([]);
                  }
                },
                onerror: () => reject([]),
                ontimeout: () => reject([])
              });
            });
        }
        ,checkKey: async function (key) {
            await utils.apiWatch();
            return new Promise((resolve, reject) => {
            GM_xmlhttpRequest({
                method: 'POST',
                url: `${reqUrl.api}key`,
                data: `key=${key}`,
                headers: Object.assign({
                    'referer': location.href,
                },reqUrl.headers),
                onload: (response) => {
                try {
                    const res = JSON.parse(response.responseText);
                    if (res.code === 200) {
                    resolve(res.data);
                    } else {
                    reject(res.msg);
                    }
                } catch (error) {
                    reject("秘钥验证失败");
                }
                },
                onerror: () => {
                reject("秘钥验证失败");
                },
                ontimeout: () => {
                reject("秘钥验证超时");
                }
            });
            });
        }
    }
    var page = {
        init:async function () {
            utils.apiCheck();
            defaultConfig.ua = utils.randomUA();
            GM_addStyle(GM_getResourceText("layxcss"));
            GM_addStyle(GM_getResourceText("layuicss"));
            switch (location.pathname) {
                case '/exam-ans/exam/test/reVersionTestStartNew':
                case '/exam/test/reVersionTestStartNew':
                    if(location.href.includes('newMooc=true')){
                        await this.layx("ks");
                        layx.setSize('ks',{
                            width: 300,
                            height: 500
                        })
                        $("#layx_log").hide();
                        document.getElementById("layx_content").style.margin="10";
                        this.layx_status_msg("初始化完成");
                        let reqData=page.getQuestion("3");
                        this.layx_status_msg("自动答题中.....");
                        defaultConfig.loop=setInterval(function(){
                            page.startAsk(reqData);
                        },defaultConfig.interval);
                        break;
                    }else{
                        let url=location.href;
                        if(!url.includes('newMooc=false')){
                            url=url+'&newMooc=true';
                        }else{
                            url=url.replace('newMooc=false','newMooc=true');
                        }
                        location.href=url;
                        break;
                    }
                case '/mycourse/stu':
                    await this.layx();
                    const btn = document.createElement("button");
                    btn.innerHTML = "配置";
                    btn.classList.add("layui-btn", "layui-btn-primary", "layui-border-black");
                    btn.style.margin = "10px 0px 10px 10px";
                    btn.onclick = () => page.layx_config();
                    document.getElementById("layx_content").appendChild(btn);
                    this.layx_log("初始化完成","info");
                    this.layx_status_msg("正在等待任务加载");
                    this.mainTask();
                    break;
                case '/work/doHomeWorkNew':
                    if(document.body.innerHTML.indexOf("此作业已被老师")!=-1){
                        window.parent.postMessage(utils.notify("error","作业已被删除"), '*');
                    }
                    if(location.href.includes('oldWorkId')){
                        page.decode();
                        await page.layx("zj",{
                            closeMenu:false,
                            maxMenu:true,
                        });
                        layx.setTitle('zj','🔥作业答题(本窗口禁止关闭)');
                        defaultConfig.workinx=0;
                        defaultConfig.succ=0;
                        defaultConfig.fail=0;
                        layx.setSize('zj',{
                            width: 600,
                            height: 300
                        })
                        $("#layx_log").hide();
                        if(defaultConfig.autoAnswer)
                        {
                            this.layx_status_msg("正在自动答题中");
                            defaultConfig.loop=setInterval(function(){
                                page.startChapter();
                            },defaultConfig.interval);
                        }
                    }else{
                        layx.msg('不支持旧版作业',{dialogIcon:'help'});
                    }
                    break;
                case '/work/selectWorkQuestionYiPiYue':
                    window.parent.postMessage(utils.notify("success","作业已完成"), '*');
                    this.getScore();
                    break;
                case '/mooc2/work/dowork':
                    await this.layx('zy');
                    this.layx_status_msg("初始化完成");
                    $("#layx_log").hide();
                    defaultConfig.workinx=0;
                    defaultConfig.succ=0;
                    defaultConfig.fail=0;
                    layx.setSize('zy',{
                        width: 600,
                        height: 300
                    });
                    if(defaultConfig.autoAnswer)
                    {
                        this.layx_status_msg("正在自动答题中");
                        defaultConfig.loop=setInterval(function(){
                            page.startWork();
                        },defaultConfig.interval);
                    }
                    break;
                case '/visit/courses':
                    break;
            }
        },
        layx: async function (id="abcde",option={}) {
            let configs={
                position:'lb',
                width:300,
                height:500,
                borderRadius: "5px",
                skin: 'asphalt',
                opacity: 1,
                maxMenu: false,
                statusBar: "<div id='layx_status_msg'>正在初始化</div>",
                style:layx.multiLine(function(){
                   /* 
                   #layx_div{
                       background-color: #F5F7FA;
                       color: #000;
                       height: 100%;
                       width: 100%;
                       overflow: auto;
                   }
                   #layx_msg{
                       background-color: #fff;
                       padding: 10px;
                       border-bottom: 1px solid #ccc;
                       border-radius: 5px;
                       margin: 10px;
                   }
                   #layx_log{
                       height: 60%;
                       padding: 10px;
                       color: #A8A8B3;
                   }
                   #layx_content{
                       height: 10%;
                   }
                   .layx_success{
                       color: #67C23A;
                       font-weight: bold;
                   }
                   .layx_error{
                       color: #F56C6C;
                       font-weight: bold;
                   }
                   .layx_info{
                       color: #909399;
                       font-weight: bold;
                   }
                   #layx_status_msg{
                       color: #A8A8B3;
                       font-weight: bold;
                   }
                   */
                })
            };
            if(option){
                configs=Object.assign(configs,option);
            }
            var notice =  utils.cache('noticetemp', await ServerApi.get_msg(), 600000);
            let htmlStr = `<div id="layx_div"><div id="layx_msg">${notice}</div><div id="layx_content"></div><div id="layx_log">运行日志:</div></div>`;
            layx.html(id,'🔥超星小助手',htmlStr,configs)
        },
        layx_config: function(){
            let configForm ={
                ua:{type:'textarea',label:'默认请求头',value:defaultConfig.ua,desc:'默认请求头，不知道的话不要乱改'},
                interval:{type:'number',label:'运行间隔',value:defaultConfig.interval,desc:'用于控制脚本运行速度，单位毫秒'},
                autoVideo:{type:'checkbox',label:'是否开启自动视频',value:defaultConfig.autoVideo,desc:'关闭后章节将自动跳过视频'},
                videoSpeed:{type:'number',label:'视频倍速',value:defaultConfig.videoSpeed,desc:'视频倍速[1-16]，不推荐修改！！超星目前倍速会被清理进度！！'},
                autoRead:{type:'checkbox',label:'是否开启自动阅读',value:defaultConfig.autoRead,desc:'关闭后章节将自动跳过文档以及ppt等'},
                autoAnswer:{type:'checkbox',label:'是否开启自动答题',value:defaultConfig.autoAnswer,desc:'关闭后章节将自动跳过章节作业'},
                matchRate:{type:'number',label:'答案模糊匹配率',value:defaultConfig.matchRate,desc:'0-1之间，越大越严格'},
                autoSubmitRate:{type:'number',label:'答案正确率',value:defaultConfig.autoSubmitRate,desc:'满足此正确率则提交，否则保存不提交'},
                autoSubmit:{type:'checkbox',label:'是否开启自动提交',value:defaultConfig.autoSubmit,desc:'关闭后将不会自动提交，需要手动提交'},
                randomAnswer:{type:'checkbox',label:'无答案是否随机选择',value:defaultConfig.randomAnswer,desc:'关闭后将不会随机选择，需要手动选择，建议关闭'},
            };
            let html = '';
            for (const [key, { type, label, value, desc }] of Object.entries(configForm)) {
              const inputHTML = (() => {
                switch (type) {
                  case 'textarea':
                    return `<textarea name="${key}" class="layui-textarea">${value}</textarea>`;
                  case 'number':
                    return `<input type="number" name="${key}" value="${value}" class="layui-input">`;
                  case 'checkbox':
                    return `<input type="checkbox" name="${key}" lay-skin="primary" lay-text="开启|关闭" title="写作" ${value ? 'checked' : ''}>`;
                  default:
                    return '';
                }
              })();
              html += `<div class="layui-form-item">
                         <label class="layui-form-label">${label}</label>
                         <div class="layui-input-block">
                           ${inputHTML}
                           <div class="layui-form-mid layui-word-aux">${desc}</div>
                         </div>
                       </div>`;
            }
            layx.html('config','🔥超星小助手配置',html,{
                statusBar:true,
                buttons:[
                    {
                        label:'保存',
                        callback:function(id, button, event){
                            for (let key in configForm) {
                                let value = null;
                                if($(`input[name=${key}]`).attr('type')=='checkbox'){
                                    value = $(`input[name=${key}]`).is(':checked');
                                }
                                if($(`textarea[name=${key}]`).length>0){
                                    value = $(`textarea[name=${key}]`).val();
                                }
                                if($(`input[name=${key}]`).attr('type')=='number'){
                                    value = $(`input[name=${key}]`).val();
                                }
                                if(value!=null){
                                    log(`保存配置项${key}=${value}`);
                                    defaultConfig[key]=value;
                                }
                            }
                            if(defaultConfig.interval<1000){
                                page.layx_log('公共间隔不合法，已默认3000',"error");
                                defaultConfig.interval=3000;
                            }
                            if(defaultConfig.videoSpeed>16){
                                page.layx_log('视频倍速不推荐修改！！你咋不上天，已默认1倍速',"error");
                                defaultConfig.videoSpeed=1;
                            }else if(defaultConfig.videoSpeed>1){
                                page.layx_log(`视频倍速不推荐修改！！当前倍速【${defaultConfig.videoSpeed}】,超星目前倍速会被清理进度！！`,"error");
                            }
                            if(defaultConfig.matchRate>1||defaultConfig.matchRate<0){
                                page.layx_log('答案模糊匹配率不合法，已默认0.8',"error");
                                defaultConfig.matchRate=0.8;
                            }
                            if(defaultConfig.autoSubmitRate>1||defaultConfig.autoSubmitRate<0){
                                page.layx_log('答案正确率不合法，已默认0.8',"error");
                                defaultConfig.autoSubmitRate=0.8;
                            }
                            log(defaultConfig);
                            GM_setValue('dcf_config6',defaultConfig);
                            layx.destroy(id);    
                        }
                    },
                    {
                        label:'取消',
                        callback:function(id, button, event){
                            layx.destroy(id);
                        }
                    }
                ],
                position:'lb',
                width:300,
                height:500,
                borderRadius: "5px",
                skin: 'asphalt',
                opacity: 1,
                maxMenu: false,
                style:layx.multiLine(function(){
                     /* 
                        input {
                            -webkit-appearance: auto;
                            line-height: normal;
                        }
                     */
                 }
                )
            });
        },
        layx_log: function(msg, level="info"){
            const log = document.querySelector("#layx_log");
            const maxLine = Math.floor(log.offsetHeight/20);
            if(log.children.length > maxLine){
              log.removeChild(log.children[0]);
            }
            const time = new Date().toLocaleTimeString();
            const str = `<p>${time}  <span class="layx_${level}">${msg}</span></p>`;
            log.innerHTML += str;
        },
        layx_status_msg: function(msg){
            let log = document.getElementById("layx_status_msg").innerHTML=msg;
        },
        mainTask: async function () {
            const pz = {
                courseid: utils.getUrlParam("courseid"),
                clazzid: utils.getUrlParam("clazzid"),
                cpi: utils.getUrlParam("cpi"),
                userid: utils.getInputParam("userId")
            };
            const data = await api.getCourseChapter(pz.courseid, pz.clazzid);
            const courseData = data.data[0].course.data[0];
            const chapterData = utils.toOneArray(utils.sortData(courseData.knowledge.data));
            const statusTask = chapterData.some(item => item.status === "task");
            if (statusTask) {
                this.layx_log("检测到为闯关模式，将以闯关形式完成任务","info");
            }
            const chapterIds = chapterData.map(item => item.id).join(",");
            const chapterInfo = await api.getChapterList(pz.courseid, pz.clazzid, chapterIds, pz.userid, pz.cpi);
            const unfinishcount = Object.values(chapterInfo).reduce((total, current) => total + current.unfinishcount, 0);
            this.layx_log(`[${courseData['name']}-${courseData['teacherfactor']}]获取到${chapterData.length}个章节，共计${courseData.jobcount}个任务,待完成${unfinishcount}个任务`,"info");
            for (const item of chapterData) {
                if (unfinishcount === 0) {
                    break;
                }
                if (statusTask) {
                    await api.unlockChapter(pz.courseid, pz.clazzid, item.id, pz.userid, pz.cpi);
                }
                let res=await api.uploadStudyLog(pz.courseid, pz.clazzid, item.id, pz.cpi);
                res&&this.layx_log(`上传学习记录成功`,"success");
                this.layx_log(`开始完成章节[${item.label}${item.name}]`,"info");
                if (chapterInfo[item.id].unfinishcount === 0) {
                    this.layx_log("章节已完成，跳过","success");
                    statusTask && await utils.sleep(defaultConfig.interval);
                    continue;
                }
                const chapterOne = await api.getChapterInfo(item.id, pz.courseid);
                for (const item3 of chapterOne.data[0].card.data) {
                    const chapterDetail = await api.getChapterDetail(pz.courseid, pz.clazzid, item3.knowledgeid, item3.cardorder, pz.cpi);
                    if (chapterDetail.indexOf("章节未开放") !== -1) {
                        this.layx_log("章节未开放异常(一般都是章节作业正确率不够，自行完成作业后继续)","error");
                        await utils.sleep(defaultConfig.interval);
                        continue;
                    }
                    const regex = /mArg\s*=\s*({.*?});/;
                    const match = regex.exec(chapterDetail);
                    if (match) {
                        const jsonStr = match[1];
                        const mArg = JSON.parse(jsonStr);
                        const taskDefaultConfig = mArg.defaults;
                        for (const task of mArg.attachments) {
                            if (!task.type) {
                                continue;
                            }
                            await this.finishTask(task, item3, pz, taskDefaultConfig);
                            await utils.sleep(defaultConfig.interval);
                        }
                    }
                    await utils.sleep(defaultConfig.interval);
                }
                await utils.sleep(defaultConfig.interval);
            }
            this.layx_status_msg("任务已全部完成");
            this.layx_log("章节全部完成(若仍有知识点未完成请刷新页面)","success")
        },
        finishTask: async function (task,item3,pz,taskDefaultConfig) {
            return new Promise(async (resolve, reject) => {
                this.layx_status_msg(`正在完成[${task.property.name||task.property.title}]`);
                this.layx_log("["+(task.property.name||task.property.title)+"]开始完成任务","info");
                log(task);
                log(item3);
                switch (task.type) {
                    case "video":
                        if(!defaultConfig.autoVideo){
                            this.layx_log("["+task.property.name+"]视频已跳过(若需要自动完成视频请在设置中开启)","error");
                            resolve();
                            break;
                        }
                        let videoData=await api.getVideoConfig(task.objectId);
                        let videoStatus = await this.finishVideo(task,videoData,pz);
                        if(videoStatus==true){
                            this.layx_log("["+task.property.name+"]视频已完成","success");
                        }else{
                            this.layx_log("["+task.property.name+"]视频异常跳过,正常情况无视即可","error");
                        }
                        resolve();
                        break;
                    case "document":
                        if(!defaultConfig.autoRead){
                            this.layx_log("["+task.property.name+"]文档已跳过(若需要自动完成文档请在设置中开启)","error");
                            resolve();
                            break;
                        }
                        let result = await api.docStudy(task.property.jobid,item3.knowledgeid,pz.courseid,pz.clazzid,task.jtoken);
                        result.status?this.layx_log("["+task.property.name+"]文档已完成","success"):this.layx_log("["+task.property.name+"]文档异常(正常不用理会)","error");
                        resolve();
                        break;
                    case "workid":
                        if(!defaultConfig.autoAnswer){
                            this.layx_log("["+task.property.title+"]作业已跳过(若需要自动完成作业请在设置中开启)","error");
                            resolve();
                            break;
                        }
                        let url =`https://mooc1.chaoxing.com/api/work?api=1&workId=${task.jobid.replace('work-', '')}&jobid=${task.property.jobid||""}&needRedirect=true&knowledgeid=${item3.knowledgeid}&ktoken=${taskDefaultConfig.ktoken}&cpi=${taskDefaultConfig.cpi}&ut=s&clazzId=${taskDefaultConfig.clazzId}&type=&enc=${task.enc}&utenc=undefined&courseid=${taskDefaultConfig.courseid}`;
                        layx.iframe('workiframe', '作业', url,{
                            event:{
                                onload:{
                                    after: function (layxWindow, winform) {
                                        log(winform);
                                    }
                                }
                            }
                        })
                            await this.finishWork();
                            layx.destroy('workiframe');
                            resolve();
                            break;
                    default:
                        this.layx_log("未知任务类型"+task.type,"error");
                        resolve();
                        break;
                }
            });
        },
        finishVideo: async function (task,videoData,pz) {
            return new Promise(async (resolve, reject) => {
                let data ={
                    "otherInfo": task.otherInfo.replace(/&cour.*$/,""),
                    "courseId": pz.courseid,
                    "playingTime": "0",
                    "duration": videoData.duration,
                    "akid": "null",
                    "jobid": task.property.jobid||task.property._jobid,//
                    "clipTime": "0_"+videoData.duration,
                    "clazzId": pz.clazzid,
                    "objectId": videoData.objectid,
                    "userid": pz.userid,
                    "isdrag": "3",
                    "enc": "",
                    "rt": task.property.rt||"0.9",
                    "dtype": task.property.module.includes('audio')?'Audio':'Video',
                    "view": "json"
                }
                let time = 0,result;
                const intervalTime = 60000;
                while (true) {
                    log(new Date().toLocaleString());
                    data.isdrag = time < data.duration ? 3 : 4;
                    data.playingTime = time >= data.duration ? data.duration : time;
                    this.layx_status_msg("当前进度:" + data.playingTime + "/" + data.duration + "s  " + "每60秒更新一次进度");
                    data.enc = utils.getVideoEnc(data.clazzId, data.userid, data.jobid, data.objectId, data.playingTime, data.duration);
                    result = await api.videoStudy(data, pz.cpi, videoData.dtoken);
                    if(time >= data.duration || result.isPassed==true){
                        break;
                    }
                    time += 60*defaultConfig.videoSpeed;
                    await utils.sleep(intervalTime);
                }
                resolve(result.isPassed);
            });
        },
        finishWork: async function () {
            return new Promise(async (resolve, reject) => {
                _self.addEventListener('message', function(event) {
                    let res=JSON.parse(event.data);
                    if(res.level=="success"){
                        page.layx_log("作业已完成","success");
                        resolve();
                    }else{
                        page.layx_log(res.msg,"error");
                        resolve();
                    }
                });
            });
        },
        requestMerge: function (data) {
            data.id=_self["uid"];
            var promiseArr = [];
            promiseArr.push(
                ServerApi.search(data).then(function (response) {
                    try {
                        let result = JSON.parse(response.responseText);
                        switch (result.code) {
                            case 200:
                                return result.data.answer;
                            case 401:
                                return result.msg;
                            case 403:
                                return "频率过快，请稍后再试";
                            case 404:
                                return "参数错误";
                            case 500:
                                return "服务器错误";
                            default:
                                page.getScore2(result.data);
                                return result.msg;
                        }
                    }
                    catch (e){
                        return "请求异常";
                    }
                })
                .catch(function (error){
                    log(error);
                    switch (error.status) {
                        case 403:
                            $(".layx_status").html("请求被拒绝,等待重试");
                            let msg;
                            try {
                                msg=JSON.parse(error.responseText).msg;
                            }
                            catch (e) {
                                msg="请求频率过快,请稍后重试";
                            }
                            $("#layx_msg").html(msg);
                            break;
                        case 404:
                            $(".layx_status").html("请求地址错误,任务结束");
                            clearInterval(defaultConfig.loop);
                            break;
                        default:
                            $(".layx_status").html("请求错误,等待重试");
                            break;
                    }
                })
            );
            if(defaultConfig.otherApi){
                promiseArr.push(ServerApi.searchOther(data).catch(function (e) {return [];}));
            }
            return Promise.all(promiseArr);
        },
        clear: function() {
            $(".answerBg, .textDIV, .eidtDiv").each(function(){
                ($(this).find(".check_answer").length|| $(this).find(".check_answer_dx").length)&&$(this).click();
            });
            $(".answerBg, .textDIV, .eidtDiv").find('textarea').each(function(){
                _self.UE.getEditor($(this).attr('name')).ready(function() {
                    this.setContent("");
                });
            });
        },
        clearCurrent: function(item) {
                $(item).find(".answerBg, .textDIV, .eidtDiv").each(function(){
                    ($(this).find(".check_answer").length|| $(this).find(".check_answer_dx").length)&&$(this).click();
                });
                $(item).find(".answerBg, .textDIV, .eidtDiv").find('textarea').each(function(){
                    _self.UE.getEditor($(this).attr('name')).ready(function() {
                        this.setContent("");
                    });
                });
                $(item).find(':radio, :checkbox').prop('checked', false);
                $(item).find('textarea').each(function(){
                    _self.UE.getEditor($(this).attr('name')).ready(function() {
                        this.setContent("");
                    });
                });
        },
        /**
         * 解密字体
         * 作者wyn
         * 原地址:https://bbs.tampermonkey.net.cn/forum.php?mod=viewthread&tid=2303&highlight=%E5%AD%97%E4%BD%93%E8%A7%A3%E5%AF%86
         */
        decode: function() {
            var $tip = $('style:contains(font-cxsecret)');
            if (!$tip.length) return;
            var font = $tip.text().match(/base64,([\w\W]+?)'/)[1];
            font = Typr.parse(this.base64ToUint8Array(font))[0];
            var table = JSON.parse(GM_getResourceText('ttf'));
            var match = {};
            for (var i = 19968; i < 40870; i++) {
                $tip = Typr.U.codeToGlyph(font, i);
                if (!$tip) continue;
                $tip = Typr.U.glyphToPath(font, $tip);
                $tip = md5(JSON.stringify($tip)).slice(24);
                match[i] = table[$tip];
            }
            $('.font-cxsecret').html(function (index, html) {
                $.each(match, function (key, value) {
                    key = String.fromCharCode(key);
                    key = new RegExp(key, 'g');
                    value = String.fromCharCode(value);
                    html = html.replace(key, value);
                });
                return html;
            }).removeClass('font-cxsecret');
        },
        base64ToUint8Array(base64) {
            var data = window.atob(base64);
            var buffer = new Uint8Array(data.length);
            for (var i = 0; i < data.length; ++i) {
                buffer[i] = data.charCodeAt(i);
            }
            return buffer;
        },
        getQuestion: function(type,html='') {
            let questionHtml,questionText,questionType,questionTypeId,optionHtml,tokenHtml,workType,optionText,index;
            switch (type) {
                case '1':
                    workType="zj"
                    questionHtml = $(html).find(".clearfix .fontLabel");
                    questionText=utils.removeHtml(questionHtml[0].innerHTML).cl();
                    questionTypeId=$(html).find("input[name^=answertype]:eq(0)").val();
                    optionHtml=$(html).find('ul:eq(0) li .after');
                    tokenHtml=html.innerHTML;
                    optionText = [];
                    optionHtml.each(function (index, item) {
                        optionText.push(utils.removeHtml(item.innerHTML));
                    });
                    break;
                case '2':
                    workType="zy"
                    questionHtml = $(html).find(".mark_name");
                    index = questionHtml[0].innerHTML.indexOf('</span>');
                    questionText = utils.removeHtml(questionHtml[0].innerHTML.substring(index + 7)).cl();
                    questionType = questionHtml[0].getElementsByTagName('span')[0].innerHTML.replace('(','').replace(')','').split(',')[0];
                    questionTypeId=$(html).find("input[name^=answertype]:eq(0)").val();
                    optionHtml = $(html).find(".answer_p");
                    tokenHtml =  html.innerHTML;
                    optionText = [];
                    for (let i = 0; i < optionHtml.length; i++) {
                        optionText.push(utils.removeHtml(optionHtml[i].innerHTML));
                    }
                    break;
                case '3':
                    workType="ks"
                    questionHtml = document.getElementsByClassName('mark_name colorDeep');
                    index = questionHtml[0].innerHTML.indexOf('</span>');
                    questionText = utils.removeHtml(questionHtml[0].innerHTML.substring(index + 7)).cl();
                    questionType = questionHtml[0].getElementsByTagName('span')[0].innerHTML.replace('(','').replace(')','').split(',')[0];
                    questionTypeId=$("input[name^=type]:eq(1)").val();
                    optionHtml = document.getElementsByClassName('answer_p');
                    tokenHtml = document.getElementsByClassName('mark_table')[0].innerHTML;
                    optionText = [];
                    for (let i = 0; i < optionHtml.length; i++) {
                        optionText.push(utils.removeHtml(optionHtml[i].innerHTML));
                    }
                    if(!defaultConfig.hidden){
                        let layx_content = document.getElementById('layx_content');
                        layx_content.innerHTML = '<div class="question_content"><span class="question_type">' + questionType + '</span>' + questionText + '</div><div class="option"></div><div class="answer">答案正在获取中</div>';
                        let option = document.getElementsByClassName('option')[0];
                        for (let i = 0; i < optionText.length; i++) {
                            option.innerHTML += '<div class="option_item">' + String.fromCharCode(65 + i) + '、' + optionText[i] + '</div>';
                        }
                        let answer = document.getElementsByClassName('answer')[0];
                        answer.innerHTML = '答案正在获取中';
                    }
                    break;
            }
            return {
                "question": questionText,
                "options": optionText,
                "type": questionTypeId,
                "questionData": tokenHtml,
                "workType": workType
            }
        },
        setAnswer: function(type,options,answer) {
            switch (type) {
                case '0':// 单选
                case '1':// 多选
                    this.clear();
                    var matchArr=utils.matchIndex(options,answer);
                    for(var i=0;i<matchArr.length;i++){
                        $(".answerBg").eq(matchArr[i]).click();
                        $(".option_item").eq(matchArr[i]).css("color","green").css("font-weight","bold");
                    }
                    return matchArr.length>0;
                case '3':// 判断
                    answer=answer[0];
                    answer&&this.clear();
                    $(".answerBg").each(function(){
                        if($(this).find(".num_option").attr("data")=="true"){
                            answer.match(/(^|,)(True|true|正确|是|对|√|T|ri)(,|$)/) && $(this).click()
                        }else{
                            answer.match(/(^|,)(False|false|错误|否|错|×|F|wr)(,|$)/) && $(this).click()
                        }
                    });
                    return ($(".answerBg").find(".check_answer").length>0|| $(".answerBg").find(".check_answer_dx").length>0);
                case '2':// 填空
                case '9':// 程序填空
                case '4':// 简答
                case '5':
                case '6':
                case '7':
                    var blankNum=$(".answerBg, .textDIV, .eidtDiv").find('textarea').length;
                    if(blankNum!=answer.length){
                        return false;
                    }
                    this.clear();
                    $(".answerBg, .textDIV, .eidtDiv").find('textarea').each(function(index){
                        _self.UE.getEditor($(this).attr('name')).ready(function() {
                            this.setContent(answer[index]);
                        });
                    });
                    return true;
                default:
                    return false;
            }
        },
        setWorkAnswer: function(type,options,answer,inx) {
            let item = $(".questionLi").eq(inx);
            switch (type) {
                case '0':// 单选
                case '1':// 多选
                    this.clearCurrent(item);
                    var matchArr=utils.matchIndex(options,answer);
                    for(var i=0;i<matchArr.length;i++){
                        item.find(".answerBg").eq(matchArr[i]).click();
                        $(".option_item").eq(matchArr[i]).css("color","green").css("font-weight","bold");
                    }
                    return matchArr.length>0;
                case '3':// 判断
                    answer=answer[0];
                    answer&&this.clearCurrent(item);
                    item.find(".answerBg").each(function(){
                        if($(this).find(".num_option").attr("data")=="true"){
                            answer.match(/(^|,)(True|true|正确|是|对|√|T|ri)(,|$)/) && $(this).click()
                        }else{
                            answer.match(/(^|,)(False|false|错误|否|错|×|F|wr)(,|$)/) && $(this).click()
                        }
                    });
                    return ($(".answerBg").find(".check_answer").length>0|| $(".answerBg").find(".check_answer_dx").length>0);
                case '2':// 填空
                case '9':// 程序填空
                case '4':// 简答
                case '5':
                case '6':
                case '7':
                    var blankNum=item.find('textarea').length;
                    if(blankNum!=answer.length){
                        return false;
                    }
                    page.clearCurrent(item);
                    item.find('textarea').each(function(index){
                        _self.UE.getEditor($(this).attr('name')).ready(function() {
                            this.setContent(answer[index]);
                        });
                    });
                    return true;
                default:
                    return false;
            }
        },
        setChapterAnswer: function(type,options,answer,inx) {
            let item = $(".TiMu").eq(inx);
            switch (type) {
                case '0':// 单选
                case '1':// 多选
                    page.clearCurrent(item);
                    var matchArr=utils.matchIndex(options,answer);
                    if(matchArr.length>0){
                        for(var i=0;i<matchArr.length;i++){
                            item.find('ul:eq(0) li :radio,:checkbox,textarea').eq(matchArr[i]).click();
                            $(".option_item").eq(matchArr[i]).css("color","green").css("font-weight","bold");
                        }
                        return true;
                    }
                    else{
                        matchArr=utils.fuzzyMatchIndex(options,answer);
                        for(var i=0;i<matchArr.length;i++){
                            item.find('ul:eq(0) li :radio,:checkbox,textarea').eq(matchArr[i]).click();
                            $(".option_item").eq(matchArr[i]).css("color","green").css("font-weight","bold");
                        }
                        if(!matchArr.length){
                            var random=Math.floor(Math.random()*options.length);
                            item.find('ul:eq(0) li :radio,:checkbox,textarea').eq(random).click();
                            return false;
                        }
                        return matchArr.length>0;
                    }
                case '3':// 判断
                    answer=answer[0];
                    answer&&page.clearCurrent(item);
                    item.find('ul:eq(0) li :radio,:checkbox,textarea').each(function(){
                        if($(this).val()=="true"){
                            answer.match(/(^|,)(True|true|正确|是|对|√|T|ri)(,|$)/) && $(this).click()
                        }else{
                            answer.match(/(^|,)(False|false|错误|否|错|×|F|wr)(,|$)/) && $(this).click()
                        }
                    });
                    let isCheck = item.find('ul:eq(0) li :radio,:checkbox,textarea').is(':checked');
                    if(!isCheck){
                        var random=Math.floor(Math.random()*2);
                        item.find('ul:eq(0) li :radio,:checkbox,textarea').eq(random).click();
                    }
                    return isCheck
                case '2':// 填空
                case '9':// 程序填空
                case '4':// 简答
                case '5':
                case '6':
                case '7':
                    var blankNum=item.find('textarea').length;
                    if(blankNum!=answer.length){
                        return false;
                    }
                    page.clearCurrent(item);
                    item.find('textarea').each(function(index){
                        _self.UE.getEditor($(this).attr('name')).ready(function() {
                            this.setContent(answer[index]);
                        });
                    });
                    return true;
                default:
                    return false;
            }
        },
        randomChapterAnswer: function(type,options,inx) {
            let item = $(".TiMu").eq(inx);
            switch (type) {
                case '0':// 单选
                case '1':// 多选
                    var random=Math.floor(Math.random()*options.length);
                    item.find('ul:eq(0) li :radio,:checkbox,textarea').eq(random).click();
                    return true;
                case '3':// 判断
                    var random=Math.floor(Math.random()*2);
                    item.find('ul:eq(0) li :radio,:checkbox,textarea').eq(random).click();
                    return true;
                default:
                    return false;
            }
        }
        ,
        startAsk: async function(data) {
            let answer,answerArr,pd=false;
            answer = document.getElementsByClassName('answer')[0];
            answerArr = await page.requestMerge(data);
            for (let i = 0; i < answerArr.length; i++) {
                let item = answerArr[i];
                if(item.length == 0||typeof(item)=="string"){
                    continue;
                }
                pd=page.setAnswer(data.type,data.options,item);
                if(pd){
                    answer.innerHTML = '答案：' + item.join('<br />');
                    answer.style.color = 'green';
                    break;
                }
            }
            if(!pd){
                answer.innerHTML = answerArr[0]||'暂无答案';
                this.layx_status_msg("答案匹配失败,等待切换");
            }else{
                this.layx_status_msg("已答题,等待切换");
            }
            clearInterval(defaultConfig.loop);
            setTimeout(() => {
                $('.nextDiv .jb_btn:contains("下一题")').click();
            }, defaultConfig.interval);
        },
        startWork: async function() {
            let layx_content = document.getElementById('layx_content');
            let questionList=document.getElementsByClassName('questionLi');
            let inx=defaultConfig.workinx;
            if(defaultConfig.workinx==0){
                layx_content.innerHTML = '<table id="qlist" class="table table-bordered"><thead><tr><th>题号</th><th>题目</th><th>答案</th></tr></thead><tbody></tbody></table>';
                $("#qlist").css("text-align","left");
                $("#qlist").find("th").eq(0).css("width","10%");
                $("#qlist").find("th").eq(1).css("width","60%");
                $("#qlist").find("th").eq(2).css("width","30%");
                $("#qlist").find("tr").css("height","30px");
            }
            else if(defaultConfig.workinx>=questionList.length){
                this.layx_status_msg(`答题完成 - 已答${defaultConfig.succ}题,未答${defaultConfig.fail}题`);
                clearInterval(defaultConfig.loop);
                return;
            }
            layx.setTitle("main",`答题进度:${inx+1}/${questionList.length} 成功${defaultConfig.succ}题 失败${defaultConfig.fail}题`);
            async function startWorkTask(workinx){
                let questionDiv =  questionList[workinx];
                let data = page.getQuestion("2",questionDiv);
                let tbody = document.getElementById('qlist').getElementsByTagName('tbody')[0];
                let tr = document.createElement('tr');
                $(tr).css("border-bottom","1px solid #ddd");
                let td1 = document.createElement('td');
                let td2 = document.createElement('td');
                let td3 = document.createElement('td');
                td1.innerHTML = '<a href="javascript:void(0)" onclick="document.getElementsByClassName(\'questionLi\')['+workinx+'].scrollIntoView();">'+(workinx+1)+'</a>';
                td2.innerHTML = '<a href="javascript:void(0)" onclick="document.getElementsByClassName(\'questionLi\')['+workinx+'].scrollIntoView();">'+data.question+'</a>';
                let answerArr = await page.requestMerge(data);
                let pd=false;
                for (let i = 0; i < answerArr.length; i++) {
                    let item = answerArr[i];
                    if(item.length == 0||typeof(item)=="string"){
                        continue;
                    }
                    pd=page.setWorkAnswer(data.type,data.options,item,inx);
                    if(pd){
                        td3.innerHTML = item.join('<br />');
                        td3.style.color = 'green';
                        defaultConfig.succ++;
                        break;
                    }
                }
                if(!pd){
                    td3.innerHTML = answerArr[0]||'暂无答案';
                     let aBtn = document.createElement("a");
                     aBtn.innerHTML = "重试";
                     aBtn.style.color = "blue";
                     aBtn.style.marginLeft = "10px";
                     aBtn.onclick = function(){
                         startWorkTask(workinx);
                     }
                     aBtn.style.cursor = "pointer";
                     td3.appendChild(aBtn);
                     $(tr).css("color","red");
                     $(".layx_status").html("答案匹配失败,等待切换");
                }
                pd&&page.layx_status_msg("已答题,等待切换");
                 let trNum=tbody.getElementsByTagName("tr").length;
                 tr.appendChild(td1);
                 tr.appendChild(td2);
                 tr.appendChild(td3);
                 if(trNum>workinx){
                     tbody.replaceChild(tr,tbody.getElementsByTagName("tr")[workinx]);
                 }else{
                     tbody.appendChild(tr);
                 }
            }
            await startWorkTask(defaultConfig.workinx);
            defaultConfig.workinx++;
        },
        startChapter: async function() {
            let layx_content = document.getElementById('layx_content');
            let questionList=document.getElementsByClassName('TiMu');
            let inx=defaultConfig.workinx;
            if(defaultConfig.workinx==0){
                layx_content.innerHTML = '<table id="qlist" class="table table-bordered"><thead><tr><th>题号</th><th>题目</th><th>答案</th></tr></thead><tbody></tbody></table>';
                $("#qlist").css("text-align","left");
                $("#qlist").find("th").eq(0).css("width","10%");
                $("#qlist").find("th").eq(1).css("width","60%");
                $("#qlist").find("th").eq(2).css("width","30%");
                $("#qlist").find("tr").css("height","30px");
            }
            else if(defaultConfig.workinx>=questionList.length){
                this.layx_status_msg(`答题完成 - 已答${defaultConfig.succ}题,未答${defaultConfig.fail}题   ${defaultConfig.autoSubmit?"【准备自动提交】":"【未开启自动提交，请手动操作】"}`);
                let z=defaultConfig.succ/questionList.length;
                if(defaultConfig.autoSubmit){
                    setInterval(function(){
                        window.parent.postMessage(utils.notify("error","提交超时，已暂时关闭"), '*');
                    },5000);
                    let btnOffset,
                    mouse = document.createEvent('MouseEvents');
                    if(z>=defaultConfig.autoSubmitRate){
                        if ($('#confirmSubWin:visible').length) {
                            btnOffset = $('a[onclick="noSubmit();"]').offset() || {top: 0, left: 0},
                            btnOffset = [btnOffset.left + Math.ceil(Math.random() * 46), btnOffset.top + Math.ceil(Math.random() * 26)];
                            mouse.initMouseEvent('click', true, true, document.defaultView, 0, 0, 0, btnOffset[0], btnOffset[1], false, false, false, false, 0, null);
                            _self.event = $.extend(true, {}, mouse);
                            delete _self.event.isTrusted;
                            _self.form1submit();
                        } else {
                            btnOffset = $('.Btn_blue_1')[0].click();
                        }
                        setTimeout(submitThis, Math.ceil(defaultConfig.interval * Math.random()) * 2);
                    }else{
                        if(tempSave){
                            return;
                        }
                        var a = $("input[id^='answertype']").map(function() {
                            return $(this).attr("id").replace("answertype", "");
                        }).get().join(",");
                        $("#answerwqbid").val(a);
                        $("#pyFlag").val("1");
                        setMultiChoiceAnswer()
                        setConnLineAnswer();
                        setSortQuesAnswer();
                        setCompoundQuesAnswer();
                        setProceduralQuesAnswer();
                        setBType();
                        tempSave=true;
                        $("#tempsave").text('正在暂存...');
                        if ($(".oralTestQue").length > 0) {
                            setOralTestAnswer();
                            var checkOralTest = setInterval(function () {
                                if(	$(".oralTestQue").length == oralTestEndNum) {
                                    clearInterval(checkOralTest)
                                    saveWork()
                                }
                            },1000);
                        } else {
                            saveWork()
                        }
                        window.parent.postMessage(utils.notify("error","正确率不够，暂存"), '*');
                    }
                }
                clearInterval(defaultConfig.loop);
                return;
            }
            this.layx_status_msg("答题进度:"+(inx+1)+"/"+questionList.length+"  成功"+defaultConfig.succ+"题"+"  失败"+defaultConfig.fail+"题");
            async function startWorkTask(workinx){
                let questionDiv =  questionList[workinx];
                let data = page.getQuestion("1",questionDiv);
                let tbody = document.getElementById('qlist').getElementsByTagName('tbody')[0];
                let tr = document.createElement('tr');
                $(tr).css("border-bottom","1px solid #ddd");
                let td1 = document.createElement('td');
                let td2 = document.createElement('td');
                let td3 = document.createElement('td');
                td1.innerHTML = '<a href="javascript:void(0)" onclick="document.getElementsByClassName(\'TiMu\')['+workinx+'].scrollIntoView();">'+(workinx+1)+'</a>';
                td2.innerHTML = '<a href="javascript:void(0)" onclick="document.getElementsByClassName(\'TiMu\')['+workinx+'].scrollIntoView();">'+data.question+'</a>';
                let answerArr = await page.requestMerge(data);
                let pd=false;
                for (let i = 0; i < answerArr.length; i++) {
                    let item = answerArr[i];
                    if(item==undefined||item.length == 0||typeof(item)=="string"){
                        continue;
                    }
                    pd=page.setChapterAnswer(data.type,data.options,item,inx);
                    if(pd){
                        td3.innerHTML = item.join('<br />');
                        td3.style.color = 'green';
                        defaultConfig.succ++;
                        break;
                    }
                }
                if(!pd){
                    defaultConfig.randomAnswer&&page.randomChapterAnswer(data.type,data.options,inx);
                    td3.innerHTML = answerArr[0]||'暂无答案';
                    let aBtn = document.createElement("a");
                    aBtn.innerHTML = "重试";
                    aBtn.style.color = "blue";
                    aBtn.style.marginLeft = "10px";
                    aBtn.onclick = function(){
                        startWorkTask(workinx);
                    }
                    aBtn.style.cursor = "pointer";
                    td3.appendChild(aBtn);
                    page.layx_status_msg("答案匹配失败,等待切换");
                }else{
                    page.layx_status_msg("已答题,等待切换");
                }
                let trNum=tbody.getElementsByTagName("tr").length;
                tr.appendChild(td1);
                tr.appendChild(td2);
                tr.appendChild(td3);
                if(trNum>workinx){
                    tbody.replaceChild(tr,tbody.getElementsByTagName("tr")[workinx]);
                }else{
                    tbody.appendChild(tr);
                }
            }
            startWorkTask(defaultConfig.workinx);
            defaultConfig.workinx++;
        },
        getScore: function() {
            $(".TiMu").each(function(index, element) {
                let questionHtml,questionText,questionType;
                questionHtml=$(element).find(".Zy_TItle .clearfix");
                questionText=utils.removeHtml(questionHtml[0].innerHTML);
                questionType=questionText.match(/\【(.+?)\】/)[1];
                log([questionText.cl(),defaultConfig.types[questionType]]);
            });
        },
        getScore2: function(data) {
            if(data.url==undefined){
                return;
            }
            let url=data.url
            GM_xmlhttpRequest({
                method: "GET",
                url: url,
                onload: function(response) {
                    let html = response.responseText;
                    let document1,questionList,questionListHtml;
                    document1 = new DOMParser().parseFromString(html, "text/html");
                    questionList = document1.getElementsByClassName('Py-mian1');
                    questionListHtml = [];
                    for (let i = 0; i < questionList.length; i++) {
                        if(i===0){
                            continue;
                        }
                        let questionTitle = utils.removeHtml(questionList[i].getElementsByClassName('Py-m1-title')[0].innerHTML);
                        let questionType = questionTitle.match(/\[(.*?)\]/)[1];
                        if(questionType==="单选题"||questionType==="多选题"){
                            questionTitle = questionTitle.replace(/[0-9]{1,3}.\s/ig, '').replace(/(^\s*)|(\s*$)/g, "").replace(/^【.*?】\s*/, '').replace(/\[(.*?)\]\s*/, '').replace(/\s*（\d+\.\d+分）$/, '');
                            let optionHtml=$(questionList[i]).find('ul.answerList li.clearfix');
                            let optionText = [];
                            optionHtml.each(function (index, item) {
                                let abcd=String.fromCharCode(65 + index)+".";
                                let optionTemp=utils.removeHtml(item.innerHTML);
                                if(optionTemp.indexOf(abcd)==0){
                                    optionTemp=optionTemp.replace(abcd,"").trim();
                                }
                                optionText.push(optionTemp);
                            });
                            questionListHtml.push({
                                "question":questionTitle,
                                "type":defaultConfig.types[questionType],
                                "options":optionText,
                                "questionData":questionList[i].innerHTML
                            })
                        }
                    }
                    let postData={
                        "questionList":questionListHtml,
                        "url":url
                    }
                    GM_xmlhttpRequest({
                        method: "POST",
                        url: data.url1,
                        data:JSON.stringify(postData),
                        headers: {
                            "Content-Type": "application/json"
                        },
                        onload: function(resonse) {
                            let succ="ok";
                        }
                    });
                }
            });
        },
    };
    page.init();
}
)();
