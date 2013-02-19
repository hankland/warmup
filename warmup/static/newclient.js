ERR_BAD_CREDENTIALS = (-1);
ERR_USER_EXISTS = (-2);
ERR_BAD_USERNAME = (-3);
ERR_BAD_PASSWORD  = (-4);

function set_message(err) {
    if (err == -1) {
        $('#message').html("Invalid username and password combination. Please try again. ");
    } else if (err == -2) {
        $('#message').html("This user name already exists. Please try again.");
    } else if (err == -3) {
        $('#message').html("The user name should not be empty and at most 128 characters long. Please try again.");
    } else if (err == -4) {
        $('#message').html("The password should be at most 128 characters long. Please try again");
    }
}

function on_error(err) {
   alert('error occurred on request');
}

function on_return(data) {
   if( data.errCode > 0) {
       $('#count').html(data.count);
       $('#page1').hide()
       $('#page2').show()
   } else {
       set_message(data.errCode);
       $('#username').val("");
       $('#password').val("");
   }
}


function one() {
    $.ajax({
        type: 'POST',
        url: '/users/login',
        data: JSON.stringify({ user: $('#username').val(), password : $('#password').val()}),
        contentType: "application/json",
        dataType: "json",
        success: on_return,
        error: on_error
        });
    $('#user').html($('#username').val());
    
}

function two() {
    $.ajax({
        type: 'POST',
        url: '/users/add',
        data: JSON.stringify({ user: $('#username').val(), password : $('#password').val()}),
        contentType: "application/json",
        dataType: "json",
        success: on_return,
        error: on_error
        });
    $('#user').html($('#username').val());
}

function three() {
    $('#username').val("");
    $('#password').val("");
    $('#message').html("Please enter your credentials below");
    $('#page2').hide();
    $('#page1').show();
}

