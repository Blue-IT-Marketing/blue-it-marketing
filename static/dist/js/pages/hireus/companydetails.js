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

document.getElementById('UpdateCompanyDetailsButt').addEventListener("click", function () {
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

                var vstrCompanyName = document.getElementById('strCompanyName').value;
                var vstrCompanyDescription = document.getElementById('strCompanyDescription').value;
                var vstrCountry = document.getElementById('strCountry').value;
                var vstrCity = document.getElementById('strCity').value;
                var vstrAddress = document.getElementById('strAddress').value;
                var vstrWebsite = document.getElementById('strWebsite').value;
                var vstrName = document.getElementById('strName').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrCell = document.getElementById('strCell').value;
                var vstrServicesProducts = document.getElementById('strServicesProducts').value;


                var vstrPath = "update-company-details";
                var dataString = "&vstrPath=" + vstrPath + '&vstrEmail=' + email + '&vstrUserID=' + struid +
                    '&vstrAccessToken=' + accessToken + '&vstrCompanyName=' + vstrCompanyName + '&vstrCompanyDescription=' + vstrCompanyDescription +
                '&vstrCountry=' + vstrCountry + '&vstrCity=' + vstrCity + '&vstrAddress=' + vstrAddress + '&vstrWebsite=' + vstrWebsite +
                '&vstrName=' + vstrName + '&vstrSurname=' + vstrSurname + '&vstrEmail=' + vstrEmail + '&vstrCell=' + vstrCell +
                '&vstrServicesProducts=' + vstrServicesProducts;
                $.ajax({
                    type: "post",
                    url: "/hireus",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#CompanyDetailsINFDIV').html(html)
                    }
                })
            })
        }else{
            alert("Please login to create a company")
        }
    })
});
