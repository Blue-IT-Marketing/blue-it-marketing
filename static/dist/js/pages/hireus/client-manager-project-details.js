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




document.getElementById('UpdateProjectButt').addEventListener("click", function () {
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

                var vstrProjectDetails = document.getElementById('strProjectDetails').value;
                var vstrProjectID = document.getElementById('strProjectID').value;
                var vstrPath = 'client-manager-update-project-details';


                var dataString = '&vstrPath=' + vstrPath + '&vstrProjectDetails=' + vstrProjectDetails +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken +
                '&vstrProjectID=' + vstrProjectID;

                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        alert(Response);
                    }
                })
            })
        }
    })
});



