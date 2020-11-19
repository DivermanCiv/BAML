function afficheMenu() {

    var x = document.getElementById("mobile");
    if (x.style.display === "flex") {
        x.style.display = "none";
    } else {
        x.style.display = "flex";
    }
}

function openModalHeader() {

    overlayHeader.style.display = 'block';
}

var btnCloseHeader = document.getElementById('btnCloseHeader');
btnCloseHeader.addEventListener('click', closeModalHeader());
function closeModalHeader() {

    overlayHeader.style.display = 'none';
}

function openModalFooter() {

    overlayFooter.style.display = 'block';
}

var btnCloseFooter = document.getElementById('btnCloseFooter');
btnCloseHeader.addEventListener('click', closeModalHeader());
function closeModalFooter() {

    overlayFooter.style.display = 'none';
}