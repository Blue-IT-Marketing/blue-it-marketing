document.getElementById('ChurchAdminButt').addEventListener("click", function () {
    var vstrPath = "church-admin";
    var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('CoverManButt').addEventListener("click", function () {
   var vstrPath = "cover-manager";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('HotelManButt').addEventListener("click", function () {
   var vstrPath = "hotel-manager";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });

});
document.getElementById('SMSMessagingButt').addEventListener("click", function () {
   var vstrPath = "sms-messaging";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('HRSystemsButt').addEventListener("click", function () {
   var vstrPath = "hr-systems";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('SchoolManButt').addEventListener("click", function () {
   var vstrPath = "school-management";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('LoansManButt').addEventListener("click", function () {
   var vstrPath = "loans-management";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('ClientTraceButt').addEventListener("click", function () {
   var vstrPath = "client-trace";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('P2PTradersButt').addEventListener("click", function () {
   var vstrPath = "p2p-traders";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('JobCloudButt').addEventListener("click", function () {
   var vstrPath = "job-cloud";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('FreelancingSolutionsButt').addEventListener("click", function () {
   var vstrPath = "freelancing-solutions";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('BusAdminButt').addEventListener("click", function () {
   var vstrPath = "bus-admin";
   var dataString = '&vstrPath=' + vstrPath;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProjectLoaderINFDIV').html(html)
                    }
        });
});
document.getElementById('SubmitFeatureButt').addEventListener("click", function () {
   var vstrPath = "submit-feature";
   var vstrNames = document.getElementById('strNames').value;
   var vstrSurname = document.getElementById('strSurname').value;
   var vstrAppSelect = document.getElementById('strAppSelect').value;
   var vstrFeature = document.getElementById('strFeature').value;
   var vstrCell = document.getElementById('strCell').value;
   var vstrEmail = document.getElementById('strEmail').value;
   var dataString = '&vstrPath=' + vstrPath + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
   '&vstrAppSelect=' + vstrAppSelect + '&vstrFeature=' + vstrFeature + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SubmitFeatureINFDIV').html(html)
                    }
        });
});
document.getElementById('SubmitBugButt').addEventListener("click", function () {
   var vstrPath = "submit-bug";
    var vstrBugNames = document.getElementById('strBugNames').value;
    var vstrBugSurname = document.getElementById('strBugSurname').value;
    var vstrBugCell = document.getElementById('strBugCell').value;
    var vstrBugEmail = document.getElementById('strBugEmail').value;
    var vstrBugAppSelect = document.getElementById('strBugAppSelect').value;
    var vstrBugDescription = document.getElementById('strBugDescription').value;

    var dataString = '&vstrPath=' + vstrPath + '&vstrBugNames=' + vstrBugNames + '&vstrBugSurname=' + vstrBugSurname +
    '&vstrBugCell=' + vstrBugCell + '&vstrBugEmail=' + vstrBugEmail + '&vstrBugAppSelect=' + vstrBugAppSelect +
    '&vstrBugDescription=' + vstrBugDescription;
                $.ajax({
                    type: "post",
                    url: "/projects",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SubmitBugINFDIV').html(html)
                    }
        });
});

document.getElementById('MaximizeProjectScreenButt').addEventListener("click", function () {
   var GetRightSideBar = document.getElementById('RightSideBar');
   GetRightSideBar.remove();
   $('#ProjectScreen').removeClass('col-md-6');
   $('#ProjectScreen').addClass('col-md-9');
   $('#MaximizeProjectScreenButt').remove();
});
