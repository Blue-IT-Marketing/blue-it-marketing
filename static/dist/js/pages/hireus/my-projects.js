try{
var config =
{
    apiKey: "AIzaSyAW815ZAimzXNMcAYbzIEEJTTTC-v7-OrQ",
    authDomain: "blue-it-marketing.firebaseapp.com",
    databaseURL: "https://blue-it-marketing.firebaseio.com",
    projectId: "blue-it-marketing",
    storageBucket: "blue-it-marketing.appspot.com",
    messagingSenderId: "298713482836"
};
if (!firebase.apps.length) {
    firebase.initializeApp(config);
}else {
}
}catch (err){
}

document.getElementById('CreateProjectButt').addEventListener("click", function () {
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            user.getIdToken().then(function (accessToken) {
                // User is signed in.
                var displayName = user.displayName;
                var email = user.email;
                var photoURL = user.photoURL;
                var isAnonymous = user.isAnonymous;
                var providerData = user.providerData;
                var struid = user.uid;

                var vstrProjectTitle = document.getElementById('strProjectTitle').value;
                var vstrProjectDetails = document.getElementById('strProjectDetails').value;
                var vstrBudget = document.getElementById('strBudget').value;
                var vstrExpectedDateOfDelivery = document.getElementById('strExpectedDateOfDelivery').value;


                var vstrPath = "create-project";
                var dataString = '&vstrPath=' + vstrPath + '&vstrEmail=' + email + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken +
                    '&vstrProjectTitle=' + vstrProjectTitle + '&vstrProjectDetails=' + vstrProjectDetails + '&vstrBudget=' + vstrBudget + '&vstrExpectedDateOfDelivery=' + vstrExpectedDateOfDelivery;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        $('#CreateProjectINFDIV').html(Response)
                    }
                })
            })
        }else{
            alert("Please login to create a project")
        }
    })
});







