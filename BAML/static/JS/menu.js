// show content of burger menu
function afficheMenu() {

    var x = document.getElementById("burger-menu-content");
    if (x.style.display === "flex") {
        x.style.display = "none";
    } else {
        x.style.display = "flex";
    }
}

// popup RGPD
function openModalFooter() {
    console.log()
    overlayFooter.style.display = 'block';
}

function closeModalFooter() {

    overlayFooter.style.display = 'none';
}

// popup contact
function openModalFooterContact() {

    overlayFooterContact.style.display = 'block';
}

// close cross
function closeModalFooterContact() {

    overlayFooterContact.style.display = 'none';
}

