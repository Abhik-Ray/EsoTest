$(document).ready(function(){
    $("#theme-button").click(function(){
        let theme;
        $("html").attr("data-theme") === "light" ? theme="dark" : theme="light";
        $("html").attr("data-theme", theme);
    });
});