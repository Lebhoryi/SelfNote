
    var height = $(window).height();
    var top_fold = $(".main-fold").offset().top;
    var top_list = $(".main-list").offset().top;
    var top_conent = $(".main-content").offset().top;
    $(".main-fold").css("height", String(height-top_fold-5)+"px");
    $(".main-list").css("height", String(height-top_list-5)+"px");
    $(".main-content").css("height", String(height-top_conent-5)+"px");
$(window).resize(function () {
    var height = $(window).height();
    var top_fold = $(".main-fold").offset().top;
    var top_list = $(".main-list").offset().top;
    var top_conent = $(".main-content").offset().top;
    $(".main-fold").css("height", String(height-top_fold-5)+"px");
    $(".main-list").css("height", String(height-top_list-5)+"px");
    $(".main-content").css("height", String(height-top_conent-5)+"px");
});
