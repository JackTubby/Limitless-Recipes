$(document).ready(function () {
    $('.sidenav').sidenav({ inDuration: 800, outDuration: 800 });
});

$('#password, #confirm_password').on('keyup', function () {
    if ($('#password').val() == $('#confirm_password').val()) {
        $('#message').html('Password Matches').css('color', 'green');
    } else
        $('#message').html('Password Does Not Match').css('color', 'red');
});