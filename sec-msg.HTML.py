<!DOCTYPE html>
<html>
<head>
    <title>Secret Message</title>
    <script>
        function showMessage() {
            var response = confirm("This message is from someone you know. Do you wish to continue?");
            if (response) {
                alert("I like you. You're amazing!");
            }
        }
    </script>
</head>
<body onload="showMessage()">
    <h1>Click 'OK' to see the message!</h1>
</body>
</html>
