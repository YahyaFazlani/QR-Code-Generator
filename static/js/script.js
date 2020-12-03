let encryption = document.getElementById('encryption');
let password = document.getElementById('password-field');
let passwordInput = document.getElementById('password');
let form = document.querySelector('form');

form.reset();

encryption.addEventListener('input', function () {
  password.style.display =
    encryption.value === 'WEP' || encryption.value === 'WPA' ? 'block' : 'none';
  encryption.value === 'WEP' || encryption.value === 'WPA'
    ? (passwordInput.required = true)
    : (passwordInput.required = false);
});

passwordInput.onchange = function () {
  console.log(passwordInput.value);
};
