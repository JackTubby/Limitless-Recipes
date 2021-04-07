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
    $('.recipe_description, .recipe_name').characterCounter();
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

/* Ingredient/Step add field script */
// https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery

// Ingredient input addition //
$(document).ready(function () {
    var max_fields = 20; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap_ingredient"); //Fields wrapper
    var add_button = $(".add_field_button_ingredient"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" name="recipe_ingredient" placeholder="Add Ingredient" minlength="10" maxlength="100" required/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    });
});

// Step input addition //
$(document).ready(function () {
    var max_fields = 20; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap_step"); //Fields wrapper
    var add_button = $(".add_field_button_step"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" id="recipe_method" name="recipe_method" placeholder="Add Step" minlength="10" maxlength="300" required/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    });
});

// Edit ingredient input addition //
$(document).ready(function () {
    var max_fields = 5; //maximum input boxes allowed
    var wrapper = $(".edit_input_fields_wrap_ingredient"); //Fields wrapper
    var add_button = $(".edit_add_field_button_ingredient"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" id="recipe_method" name="recipe_method" placeholder="Add Step" minlength="10" maxlength="300" required/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    });
});

// Edit step input addition //
$(document).ready(function () {
    var max_fields = 5; //maximum input boxes allowed
    var wrapper = $(".edit_input_fields_wrap_step"); //Fields wrapper
    var add_button = $(".edit_add_field_button_step"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" id="recipe_method" name="recipe_method" placeholder="Add Step" minlength="10" maxlength="300" required/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    });
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


