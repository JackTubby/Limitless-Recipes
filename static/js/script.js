// Materialize jQuery
$(document).ready(function () {
    $('.sidenav').sidenav({ inDuration: 800, outDuration: 800 });
    $(".dropdown-trigger").dropdown(
        {
            'closeOnClick': false
        });
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
    $('.materialboxed').materialbox();
    $('.recipe_description, .recipe_name, .username, #recipe_review').characterCounter();
    $('.tooltipped').tooltip({
        'transitionMovement': 80
    });
    $('input.autocomplete').autocomplete({
        data: {
            "Indian": null,
            "Chinese": null,
            "Italian": null
        },
    });
});

// Limit amount of characters for recipe inputs
var max_chars = 3;

$('.add_recipe_times').keydown( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

$('.add_recipe_times').keyup( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

var max_chars_serves = 2;

$('.recipe_serves').keyup( function(e){
    if ($(this).val().length >= max_chars_serves) { 
        $(this).val($(this).val().substr(0, max_chars_serves));
    }
});

// To top button view page //

var btn = $('#top_button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});


