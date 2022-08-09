var bodyStartHeight = document.body.clientHeight;

(function () {
    maximize();
}());

function maximize() {
    let mainTag = document.getElementsByTagName("main")[0];
    if (mainTag) {
        let control = mainTag.classList[0];
        if (control != "no-maximize") {
            if (bodyStartHeight <= window.innerHeight) {
                let bodyHeight = document.body.clientHeight;
                mainTag.style.height = window.innerHeight - (bodyHeight - mainTag.offsetHeight) + "px";
            }
            else {
                mainTag.style.height = "auto";
            }
        }
    }
}

function getElement(id) {
    return document.getElementById(id);
}

let searchInput = getElement("search-input");
searchInput.addEventListener("focusout", onFocusOut);

function onChange(element) {
    let searchButton = getElement("search-button");
    if (element.value == "") {
        searchButton.disabled = true;
        searchButton.style.background = "#fff";
        searchButton.style.color = "#4682B4";
        searchButton.style.border = "2px solid #4682B4";
        searchButton.style.cursor = "not-allowed";
    }
    else {
        searchButton.disabled = false;
        searchButton.style.background = "#4682B4";
        searchButton.style.color = "#fff";
        searchButton.style.border = "2px solid #4682B4";
        searchButton.style.cursor = "pointer";
    }
}

function onFocusOut(ev) {
    let searchButton = getElement("search-button");
    if (ev.path[0].value == "") {
        searchButton.style.background = "#f3f3f3";
        searchButton.style.border = "2px solid #f3f3f3";
    }
}

function onFocus(element) {
    let searchButton = getElement("search-button");
    if (element.value == "") {
        searchButton.style.background = "#fff";
        searchButton.style.border = "2px solid #4682B4";
    }
}