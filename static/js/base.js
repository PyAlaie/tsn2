let btnSubmit_signup = document.querySelector('.submit-btn-signup');
let btnSubmit_login = document.querySelector('.submit-btn-login');
let btnSubmit_forgotPassword = document.querySelector('.submit-btn-forgot-password');

let form_signup = document.querySelector('.signup-form > form');
let form_login = document.querySelector('.login-form > form');
let form_forgotPassword = document.querySelector('.forgot-password-form > form');


btnSubmit_signup.addEventListener('click', function(event) {
    // Action for signup button clicked

    let formData = new FormData(form_signup);
    let finalData = {};

    for (var pair of formData.entries()) {
        finalData[pair[0]] = pair[1]
    }

    // Use finalData as input for backend.
});

btnSubmit_login.addEventListener('click', function(event) {
    // Action for login button clicked

    let formData = new FormData(form_login);
    let finalData = {};

    for (var pair of formData.entries()) {
        finalData[pair[0]] = pair[1]
    }

    // Use finalData as input for backend.
});

btnSubmit_forgotPassword.addEventListener('click', function(event) {
    // Action for forgot_password button clicked

    let formData = new FormData(form_forgotPassword);
    let finalData = {};

    for (var pair of formData.entries()) {
        finalData[pair[0]] = pair[1]
    }

    // Use finalData as input for backend.
});