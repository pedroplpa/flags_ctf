var page = require('webpage').create();
var host = "127.0.0.1";
var port = "4444"
var path = "/messagefrom"
var url = "http://"+host+":"+port+path;
var timeout = 2000;
phantom.addCookie({
    name: 'Flag',
    value: 'TH1S_W3B_FL4G{XSS_1S_V3RY_D4NG3R0US}',
    domain: host,
    path: path,
    httponly: false
});


page.onNavigationRequested = function(url, type, willNavigate, main) {
    console.log("[URL] URL="+url);  
};
page.settings.resourceTimeout = timeout;
page.onResourceTimeout = function(e) {
    setTimeout(function(){
        console.log("[INFO] Timeout")
        phantom.exit();
    }, 1);
};
page.open(url, function(status) {
    console.log("[INFO] rendered page");
    setTimeout(function(){
        phantom.exit();
    }, 1);
});