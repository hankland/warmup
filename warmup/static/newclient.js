ERR_BAD_CREDENTIALS = (-1);
ERR_USER_EXISTS = (-2);
ERR_BAD_USERNAME = (-3);
ERR_BAD_PASSWORD  = (-4);

function one() {
    alert('works1');
}

function two() {
    $('#page1').hide();
    $('#page2').show();
}

function three() {
    $('#username').val("");
    $('#password').val("");
    $('#message').html("Please enter your credentials below");
    $('#page2').hide();
    $('#page1').show();
}

