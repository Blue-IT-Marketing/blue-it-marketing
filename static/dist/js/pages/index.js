
document.getElementById('SubscribeButt').addEventListener("click", function () {

    var vstrName = document.getElementById('strName').value;
    var vstrSurname = document.getElementById('strSurname').value;
    var vstrCell = document.getElementById('strCell').value;
    var vstrEmail = document.getElementById('strEmail').value;

    var vstrPath = "subscribe";
    var dataString = "&vstrName=" + vstrName + "&vstrSurname=" + vstrSurname + "&vstrCell=" + vstrCell + "&vstrEmail=" + vstrEmail +
    "&vstrPath=" + vstrPath;
        $.ajax({
            type: "post",
            url: "/newsletters",
            data: dataString,
            cache: false,
            success: function (Response) {
                $('#NewsletterINFDIV').html(Response)
            }
        });
});

