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
    alert(err);
}

/*
document.getElementById('strFilesUploaded').addEventListener('change', function (e) {
    var uploader = document.getElementById('strUploader');
    var file = e.target.files[0];
    var storageReference = firebase.storage().ref('/user/' + file.name);
    var task = storageReference.put();
    task.on('state_changed',
        function progress(snapshot){
            uploader.value =(snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        },
        function error (err) {

        },
        function complete() {

        }
        );
});
*/

document.getElementById('UploadFileButt').addEventListener("click", function () {
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

                var vstrFilesUploaded = document.getElementById('strFilesUploaded').files[0];
                var vstrFileDescription = document.getElementById('strFileDescription').value;
                var vstrProjectID = document.getElementById('strProjectID').value;

                var vstrFileName = vstrFilesUploaded.name;

                var uploader = document.getElementById('strUploader');
                var storageReference = firebase.storage().ref();

                var vstrFileReference = storageReference.child('/user/'+ struid + '/' + vstrProjectID + "/" + vstrFileName);
                var task = vstrFileReference.put(vstrFilesUploaded);
                task.on('state_changed',
                    function progress(snapshot){
                        uploader.value =(snapshot.bytesTransferred / snapshot.totalBytes) * 100;
                    },
                    function error (err) {
                        alert("Error Occured Uploading file : " + err )
                    },
                    function complete() {
                        var vstrPath = "client-manager-upload-files";

                        var dataString = '&vstrPath=' + vstrPath + '&vstrFileDescription=' + vstrFileDescription + '&vstrProjectID=' + vstrProjectID +
                        '&vstrFileName=' + vstrFileName + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

                            $.ajax({
                                type: "post",
                                url: "/hireus",
                                data: dataString,
                                cache: false,
                                success: function(data){
                                    $('#loginINFDIV').html(data)
                                }});
                    }
                    );
            })
        }else{
            alert('login to upload project files')
        }
    })
});


function DownloadFile(filename,projectid) {

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

                var storageRef = firebase.storage().ref();
                // Create a reference to the file we want to download
                var starsRef = storageRef.child('/user/' + struid +'/'+ projectid + "/" + filename);

                // Get the download URL
                starsRef.getDownloadURL().then(function (url) {
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', url);
                    xhr.send();

                }).catch(function (error) {

                    // A full list of error codes is available at
                    // https://firebase.google.com/docs/storage/web/handle-errors
                    switch (error.code) {
                        case 'storage/object_not_found':
                            alert("Error file not found");
                            break;

                        case 'storage/unauthorized':
                            alert("you are not authorized to download file");
                           break;

                        case 'storage/canceled':
                            alert("you have cancelled the download");
                            break;


                        case 'storage/unknown':
                            alert("An Error occured you might not be connected to the internet");
                            break;
                    }
                })
            })
        }
    })
}