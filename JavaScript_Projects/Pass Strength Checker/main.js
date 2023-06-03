const checkStrength = require('./passStrengthChecker').checkStrength;
const passwordInput = document.getElementById('password');
const strengthLabel = document.getElementById('strength-label');

function checkButton() {
    const password = passwordInput.value;
    const strength = checkStrength(password);
    displayStrength(strength);
}

function checkStrength(password) {
    const strength = passStrengthChecker.checkStrength(password);
    console.log(`Password strength: ${strength}`);

    return strength;
}

function displayStrength(strength) {
    strengthLabel.textContent = `Password strength: ${strength}`;
}
