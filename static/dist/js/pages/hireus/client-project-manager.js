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


document.getElementById('ProjectButt').addEventListener("click", function () {
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

                var vstrProjectID = document.getElementById('strProjectID').value;

                var vstrPath = "client-manager-project-details";
                var dataString = '&vstrPath=' + vstrPath + '&vstrProjectID=' + vstrProjectID;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectManagerINFDIV').html(html)
                    }
                })


            })
        }
    })
});

document.getElementById('ProjectProgressButt').addEventListener("click", function () {
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
                var vstrProjectID = document.getElementById('strProjectID').value;

                var vstrPath = "client-manager-project-progress";
                var dataString = '&vstrPath=' + vstrPath + '&vstrProjectID=' + vstrProjectID + '&vstrUserID=' + struid +
                '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectManagerINFDIV').html(html)
                    }
                })


            })
        }
    })
});

document.getElementById('ProjectFilesButt').addEventListener("click", function () {
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
                //vstrEmail = self.request.get('vstrEmail')
                //vstrUserID = self.request.get('vstrUserID')
                //vstrAccessToken = self.request.get('vstrAccessToken')
                var vstrProjectID = document.getElementById('strProjectID').value;


                var vstrPath = "client-manager-project-files";
                var dataString = '&vstrPath=' + vstrPath + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken +
                '&vstrProjectID=' + vstrProjectID;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectManagerINFDIV').html(html)
                    }
                })
            })
        }
    })
});
