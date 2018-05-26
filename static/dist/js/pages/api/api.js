


document.getElementById('SMSAPIButt').addEventListener("click", function () {
   var vstrPath = "sms-api";
   var dataString = '&vstrPath=' + vstrPath;
    $.ajax({
        type: "post",
        url: "/api",
        data: dataString,
        cache: false,
        success: function (html) {
            $('#APIinfDIV').html(html)
        }
    });
});

document.getElementById('AdvertisingAPIButt').addEventListener("click", function () {
   var vstrPath = "adverts-api";
   var dataString = '&vstrPath=' + vstrPath;
    $.ajax({
        type: "post",
        url: "/api",
        data: dataString,
        cache: false,
        success: function (html) {
            $('#APIinfDIV').html(html)
        }
    });

});

document.getElementById('SurveysAPIButt').addEventListener("click", function () {
   var vstrPath = "surveys-api";
   var dataString = '&vstrPath=' + vstrPath;
    $.ajax({
        type: "post",
        url: "/api",
        data: dataString,
        cache: false,
        success: function (html) {
            $('#APIinfDIV').html(html)
        }
    });


});
