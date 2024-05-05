var sound;
var morse_code;
var morse_code_p;
var currentTime, startTime, elapsedTime, finishTime;

window.onload = function () {
    sound = document.getElementById("hoverSound");
    morse_code = document.getElementById("morse_code");
    morse_code_p = document.getElementById("morse_code_p");
    dit_duration = document.getElementById("dit_duration").value;
    letters_duration = document.getElementById("letters_duration").value;
    words_duration = document.getElementById("words_duration").value;
    finishTime = 0;
}

function beep() {
    if (finishTime > 0) {
        wrtSeparators();
    }
    startTime = new Date();
    sound.play();
}

function stopBeep() {
    sound.pause();
    sound.currentTime = 0;
    finishTime = new Date();
    wrtSymbol();
}

function wrtSymbol() {
    elapsedTime = finishTime - startTime;
    if (elapsedTime <= parseInt(dit_duration)) {
        morse_code.value += ".";
    }
    else {
        morse_code.value += "-";
    }
    morse_code_p.textContent = morse_code.value;
}

function wrtSeparators() {
    currentTime = new Date();
    elapsedTime = currentTime - finishTime;
    if (elapsedTime > parseInt(letters_duration) && elapsedTime < parseInt(words_duration)) {
        morse_code.value += " ";
    } else if (elapsedTime >= parseInt(words_duration)) {
        morse_code.value += " / ";
    }
    morse_code_p.textContent = morse_code.value;
}