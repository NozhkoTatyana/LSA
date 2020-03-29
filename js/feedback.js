// Input Fields
const inputName = document.getElementById('name');
//const job = document.getElementById('job');
const inputEmail = document.getElementById('inputEmail');
//const inputPhone = document.getElementById('inputPhone');
const inputText = document.getElementById('inputText');

//Form
const form = document.getElementById('feedback-form')

//Validation colors

const green = '#7ac29a';
const red = '#eb5e28';

//Handle Form
form.addEventListener('submit', function(event) {
    //Prevent default behavior
    event.preventDefault();
    if (
        validateName() && validateEmail() && validateText()
    ) {
        // var button = document.getElementById("submit");
        // button.disabled = true;
        const name = inputName.value;
        const container = document.querySelector('div.modal-body');
        const loader = document.createElement('div');
        loader.className = 'progress';
        const loadingBar = document.createElement('div')
        loadingBar.className = 'indeterminate';
        loader.appendChild(loadingBar);
        container.appendChild(loader);
        setTimeout(function() {
            const loaderDiv = document.querySelector('div.progress');
            const panel = document.createElement('div');
            panel.style = 'font-weight: 500; color: rgb(134, 217, 171);';
            const text = document.createElement('span');
            text.appendChild(document.createTextNode(``));
            panel.appendChild(text);
            container.replaceChild(panel, loaderDiv);
            var submitted = document.getElementById('submitted');
            submitted.textContent = 'Благодарим за обратную связь. Ваше сообщение отправлено.'
        }, 1000);
    }
})

//Validators
function validateName() {
    // check if is empty
    if (checkIfEmptyName(inputName)) return;
    // Must of in in certain length
    if (!meetLengthName(inputName, 3)) return;
    return true;
}

function validateEmail() {
    // check if is empty
    if (checkIfEmptyEmail(inputEmail)) return;
    // is if it has only letters
    if (!containsCharacters(inputEmail, 1)) return;
    return true;
}

function validateText() {
    // check if is empty
    if (checkIfEmptyText(inputText)) return;
    // is if it has only letters
    if (!meetLengthText(inputText, 5)) return;
    return true;
}

// Utility functions
function checkIfEmptyName(field) {
    if (isEmpty(field.value.trim())) {
        // set field invalid
        setInvalid(field);
        var smallName = document.getElementById('small-name');
        smallName.textContent = 'Поле не может быть пустым'
        return true;
    } else {
        // set field valid
        setValid(field);
        var smallName = document.getElementById('small-name');
        smallName.textContent = '';
        return false;
    }
}

function checkIfEmptyEmail(field) {
    if (isEmpty(field.value.trim())) {
        // set field invalid
        setInvalid(field);
        var smallEmail = document.getElementById('small-email');
        smallEmail.textContent = 'Пожалуйста, введите адрес электронной почты'
        return true;
    } else {
        // set field valid
        setValid(field);
        var smallEmail = document.getElementById('small-email');
        smallEmail.textContent = '';
        return false;
    }
}

function checkIfEmptyText(field) {
    if (isEmpty(field.value.trim())) {
        // set field invalid
        setInvalid(field);
        var smallInputText = document.getElementById('small-input-text');
        smallInputText.textContent = 'Поле не может быть пустым'
        return true;
    } else {
        // set field valid
        setValid(field);
        var smallInputText = document.getElementById('small-input-text');
        smallInputText.textContent = '';
        return false;
    }
}

function isEmpty(value) {
    if (value === '') return true;
    return false;
}

function setInvalid(field, message) {
    // var element = document.getElementById("name-input-group");
    // element.classList.remove("has-success");
    // element.classList.add("has-danger");
    field.parentElement.classList.remove("has-success");
    field.parentElement.classList.add("has-danger");
    //field.nextElementSibling.innerHTML = message;
}

function setValid(field) {
    // var element = document.getElementById("name-input-group");
    field.parentElement.classList.remove("has-danger");
    field.parentElement.classList.add("has-success");
    //field.className = 'valid';
    //field.nextElementSibling.innerHTML = '';
}

function meetLengthName(field, minLength) {
    if (field.value.length >= minLength) {
        setValid(field);
        return true;
    } else if (field.value.length < minLength) {
        setInvalid(field);
        var smallName = document.getElementById('small-name');
        smallName.textContent = 'Пожалуйста, введите полное имя или название организации'
        return false;
    }
}

function meetLengthText(field, minLength) {
    if (field.value.length >= minLength) {
        setValid(field);
        return true;
    } else if (field.value.length < minLength) {
        setInvalid(field);
        var smallInputText = document.getElementById('small-input-text');
        smallInputText.textContent = 'Пожалуйста, введите полное обращение'
        return false;
    }
}

function containsCharacters(field, code) {
    let regEx;
    switch (code) {
        case 1:
            // Email pattern
            regEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return matchWithRegEx(regEx, field);
        default:
            return false;
    }
}

function matchWithRegEx(regEx, field) {
    if (field.value.match(regEx)) {
        setValid(field);
        return true;
    } else {
        setInvalid(field);
        var smallEmail = document.getElementById('small-email');
        smallEmail.textContent = 'Недопустимый адрес электронной почты'
        return false;
    }
}