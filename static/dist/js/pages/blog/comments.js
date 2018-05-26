
document.getElementById('CommentButt').addEventListener("click", function () {
   var vstrChoice = "create-comment";
   var vstrPostReference = document.getElementById('strPostReference').value;
   var vstrMyComment = document.getElementById('strMyComment').value;

   var dataString = '&vstrChoice=' + vstrChoice + '&vstrMyComment=' + vstrMyComment + '&vstrPostReference=' + vstrPostReference;
   $.ajax({
        type: "post",
        url: "/blog",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#CommentINFDIV').html(Response);
        }
    })
});