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


// Add ingredient functions // 

function add_ingredient() {
    let newInputHTML = $(document.createElement('div')).attr("id", 'recipe_ingredient_' + ingredientCounter);
    newInputHTML.after().html('<input type="text" name="recipe_ingredient" + id="ingredient_' + ingredientCounter + '" value="" required>');
    newInputHTML.appendTo("#ingredient-inputs");
    ingredientCounter++;
}

function remove_ingredient() {
    if (ingredientCounter > 1) {
        $('#ingredient-inputs > div:last-child').remove();
        ingredientCounter--;
    } else {
        $('#ingredient-inputs div').children('input').val('');
    }
}

function reset_ingredients() {
    $('#ingredient-inputs > div').not(':first').remove();
    $('#ingredient-inputs div').children('input').val('');
    ingredientCounter = 1;
}

// Add steps functions // 

function add_step() {
    let newInputHTML = $(document.createElement('div')).attr("id", 'recipe_step_' + stepCounter);
    newInputHTML.after().html('<input type="text" name="recipe_method" + id="step_' + stepCounter + '" value="" required>');
    newInputHTML.appendTo("#method-steps");
    stepCounter++;
}

function remove_step() {
    if (stepCounter > 1) {
        $('#method-steps > div:last-child').remove();
        stepCounter--;
    } else {
        $('#method-steps div').children('textarea').val('');
    }
}

function reset_steps() {
    $('#method-steps > div').not(':first').remove();
    $('#method-steps div').children('input').val('');
    stepCounter = 1;
}