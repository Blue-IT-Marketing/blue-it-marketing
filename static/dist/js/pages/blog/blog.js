


function LoadBlogPost(articleID){
var vstrChoice = 0;
var dataString = '&vstrChoice=' + vstrChoice + '&vstrarticleID=' + articleID;
$.ajax({
    type: "post",
    url: "/blog/" + articleID,
    data: dataString,
    cache: false,
    success: function (Response) {
        $('#BlogINFDIV').html(Response);

        console.log("/blog/"+articleID);
    }
})
}

document.getElementById("GuestSubmitArticleButt").addEventListener("click", function () {
    var vstrChoice = 2;
    var dataString = '&vstrChoice=' + vstrChoice;
    $.ajax({
        type: "post",
        url: "/blog",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#BlogINFDIV').html(Response);


        }
    })

});