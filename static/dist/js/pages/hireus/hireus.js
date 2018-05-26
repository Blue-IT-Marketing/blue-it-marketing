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


document.getElementById('CompanyDetailsButt').addEventListener("click", function () {
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


                var vstrPath = "company-details";
                var dataString = "&vstrPath=" + vstrPath + '&vstrEmail=' + email + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#HireUsINFDIV').html(html)
                    }
                })
            })
        }else{
                var displayName = "";
                var email = "";
                var photoURL = "";
                var isAnonymous = "";
                var providerData = "";
                var struid = "";

                var vstrPath = "company-details";

                var dataString = "&vstrPath=" + vstrPath + '&vstrEmail=' + email + '&vstrUserID=' + struid;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#HireUsINFDIV').html(html)
                    }
                })
        }
    })
});


document.getElementById('MyProjectsButt').addEventListener("click", function () {
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

                var vstrPath = "my-projects";
                var dataString = "&vstrPath=" + vstrPath + '&vstrEmail=' + email + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#HireUsINFDIV').html(html)
                    }
                });
            })
        }else{
                var displayName = "";
                var email = "";
                var photoURL = "";
                var isAnonymous = "";
                var providerData = "";
                var struid = "";

                var vstrPath = "my-projects";

                var dataString = "&vstrPath=" + vstrPath + '&vstrEmail=' + email + '&vstrUserID=' + struid;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#HireUsINFDIV').html(html)
                    }
                })
        }
    })
});
document.getElementById('PaymentsDetailsButt').addEventListener("click", function () {
    var vstrPath = "payment-details";
    var dataString = "&vstrPath=" + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#HireUsINFDIV').html(html)
                    }
        });

});
