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

// Adds validation to select elements // 
validateMaterializeSelect();
function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}




