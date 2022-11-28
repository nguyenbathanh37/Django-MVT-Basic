$(document).ready(function() {
    $('.btn-back').click(function() {
        location.href = "index.html"
    })

    $('.message a').click(function(){
        $('.form form').animate({height: "toggle", opacity: "toggle"}, "slow");
    });
})
