
  // Initialize Firebase
var config = {
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
function sendEmailVerification() {
  // [START sendemailverification]
  firebase.auth().currentUser.sendEmailVerification().then(function() {
    // Email Verification sent!
    // [START_EXCLUDE]
    alert('Email Verification Sent!');
    // [END_EXCLUDE]
  });
  // [END sendemailverification]
}





initApp = function() {
    firebase.auth().onAuthStateChanged(function(user) {
          if (user) {
            // User is signed in.
            var displayName = user.displayName;
            var email = user.email;
            var emailVerified = user.emailVerified;
            var photoURL = user.photoURL;
            var uid = user.uid;

            var phoneNumber = user.phoneNumber;
            var providerData = user.providerData;
            user.getIdToken().then(function(accessToken) {
              //document.getElementById('SingInButton').textContent = 'Signed in';
              document.getElementById('SingInButton').textContent = 'logout';
              document.getElementById('SingInButton').setAttribute('href','/logout');
              document.getElementById('strUserNameID').textContent = displayName;
              document.getElementById('strUserImageID').src =photoURL;
              document.getElementById('strMainUserImageID').src = photoURL;

              //Send the User Token to the backend with ajax at this point with a sign in instruction
                var vstrChoice = 'login-details';
                if (emailVerified === true){
                    emailVerified = "YES"
                }else{
                    emailVerified = "NO"
                }
                var dataString ='&vstrPath=' + vstrChoice + '&vstrDisplayName=' + displayName + '&vstrEmail=' + email +
                        '&vstremailVerified=' + emailVerified + '&vstrUserID=' + uid + '&vstrPhoneNumber=' + phoneNumber +
                        '&vstrProviderData=' + providerData + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/login",
                    data: dataString,
                    cache: false,
                    success: function(data){
                        $('#loginINFDIV').html(data)
                    }});
            });
          } else {
            // User is signed out.
            //document.getElementById('sign-in-status').textContent = 'Signed out';
            document.getElementById('SingInButton').textContent = 'Sign in';

            //Send the User Token to the backend at this stage using ajax with instructions to logout the user
            var dataString = "";
            $.ajax({
                type: "post",
                url: "/logout",
                data: dataString,
                cache: false,
                success: function(data){
                    $('#logoutinfDIV').html(data)
                }});
          }
        }, function(error) {
          console.log(error);
        });
      };
initApp();
document.body.style.zoom="80%";

