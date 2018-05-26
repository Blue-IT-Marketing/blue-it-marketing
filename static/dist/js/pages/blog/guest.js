

CKEDITOR.replace('ArticleEditor');
document.getElementById("SubmitArticleButt").addEventListener("click", function () {
    var vstrChoice = 3;
    var vstrTitle = document.getElementById('strTitle').value;
    var vstrIntroduction = document.getElementById('strIntroduction').value;
    var vstrArticleEditor = CKEDITOR.instances.ArticleEditor.getData();
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrTitle=' + vstrTitle +
        '&vstrIntroduction='+ vstrIntroduction +
        '&vstrArticleEditor=' + vstrArticleEditor;
   $.ajax({
        type: "post",
        url: "/blog",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#SubmitArticleINFDIV').html(Response);
        }
    })

});