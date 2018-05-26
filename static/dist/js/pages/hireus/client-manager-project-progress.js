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

document.getElementById('SendButt').addEventListener("click", function () {
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

                var vstrPath = "progress-chat";
                var vstrProjectID = document.getElementById('strProjectID').value;
                var vstrMessage = document.getElementById('strMessage').value;
                var dataString = '&vstrPath=' + vstrPath + '&vstrMessage=' + vstrMessage + '&vstrUserName=' + displayName + '&vstrEmail=' + email + '&vstrUserID=' + struid +
                    '&vstrAccessToken=' + accessToken + '&vstrProjectID=' + vstrProjectID;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ChatMessagesINFDIV').html(html)
                    }
                })
            })
        }else{
            alert('login to send messages')
        }
    })
});