/**
 * Created by feythin on 08/01/2017.
 */
function initfullscreen() {
    var screen_height = window.screen.height;

    $('.scroll_full').css('height', screen_height);

    $("#plot1").on('click', function () {
        fullScreen();
    });
    $("#plot1").on('dblclick', function () {
        exitFullScreen();
    });
}
/**
 * 全屏
 */
function fullScreen() {

    var el = document.documentElement,
        rfs = el.requestFullScreen || el.webkitRequestFullScreen || el.mozRequestFullScreen || el.msRequestFullScreen,
        wscript;

    if (typeof rfs != "undefined" && rfs) {
        rfs.call(el);
        return;
    }

    if (typeof window.ActiveXObject != "undefined") {
        wscript = new ActiveXObject("WScript.Shell");
        if (wscript) {
            wscript.SendKeys("{F11}");
        }
    }

}

/**
 * 取消全屏
 */
function exitFullScreen() {
    var el = document,
        cfs = el.cancelFullScreen || el.webkitCancelFullScreen || el.mozCancelFullScreen || el.exitFullScreen,
        wscript;

    if (typeof cfs != "undefined" && cfs) {
        cfs.call(el);
        return;
    }

    if (typeof window.ActiveXObject != "undefined") {
        wscript = new ActiveXObject("WScript.Shell");
        if (wscript != null) {
            wscript.SendKeys("{F11}");
        }
    }
}
$(function () {
    initfullscreen();

})