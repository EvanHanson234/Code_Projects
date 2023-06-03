// Common weak passwords to check against
const commonWeakPasswords = [
    'password',
    '123456',
    'qwerty',
    // Add more weak passwords here
];
  
function checkStrength(password) {
    // Perform various checks to determine password strength
    let strength = 0;

    // Check length
    if (password.length >= 8) {
        strength += 1;
    }

    // Check for uppercase letters
    if (/[A-Z]/.test(password)) {
        strength += 1;
    }

    // Check for lowercase letters
    if (/[a-z]/.test(password)) {
        strength += 1;
    }

    // Check for numbers
    if (/\d/.test(password)) {
        strength += 1;
    }

    // Check for special characters
    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
        strength += 1;
    }

    // Check against common weak passwords
    if (!commonWeakPasswords.includes(password.toLowerCase())) {
        strength += 1;
    }

    return strength;
}

module.exports = { checkStrength };
//module.exports = checkStrength;

