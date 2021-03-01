$(document).ready(function () {
    $('.sidenav').sidenav({ inDuration: 800, outDuration: 800});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
    $('.timepicker').timepicker();
    $('.materialboxed').materialbox();
    $('input.autocomplete').autocomplete({
        data: {
            "Indian": null,
            "Chinese": null,
            "Italian": null
        },
    });
});

// https://stackoverflow.com/questions/5371089/count-characters-in-textarea
// Add Recipe Char Countdown
function countChar(val) {
    var len = val.value.length;
    if (len >= 500) {
        val.value = val.value.substring(0, 49);
    } else {
        $('#charNum').text(49 - len);
    }
};

/*
$('#password, #confirm_password').on('keyup', function () {
    if ($('#password').val() == $('#confirm_password').val()) {
        $('#message').html('Password Matches').css('color', 'green');
    } else
        $('#message').html('Password Does Not Match').css('color', 'red');
});*/

// Save Button 
