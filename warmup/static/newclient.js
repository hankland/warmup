/* set the message displayed on error based on the error code*/
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


/* simple function to either switch to the logged in page or display an error */

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

/* function to login - does simple ajax and updates the user */

function login() {
    $.ajax({
        type: 'POST',
        url: '/users/login',
        data: JSON.stringify({ user: $('#username').val(), password : $('#password').val()}),
        contentType: "application/json",
        dataType: "json",
        success: on_return,
        error: function on_error(err) {alert('error occurred on request'); }
        });
    $('#user').html($('#username').val());
    
}

/* function to add user - does simple ajax and updates the user */
function add() {
    $.ajax({
        type: 'POST',
        url: '/users/add',
        data: JSON.stringify({ user: $('#username').val(), password : $('#password').val()}),
        contentType: "application/json",
        dataType: "json",
        success: on_return,
        error: function on_error(err) {alert('error occurred on request'); }
        });
    $('#user').html($('#username').val());
}

/* logout by reseting user, password, message and switching pages */

function logout() {
    $('#username').val("");
    $('#password').val("");
    $('#message').html("Please enter your credentials below");
    $('#page2').hide();
    $('#page1').show();
}

