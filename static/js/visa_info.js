const contact_form = document.getElementById('contact_submit_from');
const errorTag = contact_form.querySelector('.error_tag');

// Regex patterns
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const phonePattern = /^[0-9\-\s]{7,15}$/;

// Hide error message on load
errorTag.style.display = 'none';

// Function to mark input field with red border
function markError(field, hasError) {
    if (hasError) {
        field.classList.add('input-error');
    } else {
        field.classList.remove('input-error');
    }
}

// Form submit event listener
contact_form.addEventListener('submit', function (event) {
    const nameField = contact_form.querySelector('input[name="name"]');
    const emailField = contact_form.querySelector('input[name="email"]');
    const phoneField = contact_form.querySelector('input[name="phone"]');
    const descriptionField = contact_form.querySelector('textarea[name="description"]');

    const name = nameField.value.trim();
    const email = emailField.value.trim();
    const phone = phoneField.value.trim();
    const description = descriptionField.value.trim();

    let hasError = false;

    // Validate Name
    if (!name) {
        markError(nameField, true);
        hasError = true;
    } else {
        markError(nameField, false);
    }

    // Validate Email
    if (!email || !emailPattern.test(email)) {
        markError(emailField, true);
        hasError = true;
    } else {
        markError(emailField, false);
    }

    // Validate Phone
    if (!phone || !phonePattern.test(phone)) {
        markError(phoneField, true);
        hasError = true;
    } else {
        markError(phoneField, false);
    }

    // Validate Description
    if (!description) {
        markError(descriptionField, true);
        hasError = true;
    } else {
        markError(descriptionField, false);
    }

    // Show or hide the error message
    if (hasError) {
        event.preventDefault(); // Stop form submission
        errorTag.style.display = 'block';
    } else {
        errorTag.style.display = 'none';
    }
});
