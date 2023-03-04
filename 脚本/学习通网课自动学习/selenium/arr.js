a = ['America', 'Greece', 'Britain', 'Canada', 'China', 'Egypt']
num = 0
a.forEach(element => {
    if (element.indexOf('a') >= 0 || element.indexOf('A') >= 0) num++
});
console.log('共有' + num + '个字符串中包含a或A');