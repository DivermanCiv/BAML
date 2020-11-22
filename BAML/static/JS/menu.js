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


function closeModalHeader() {

    overlayHeader.style.display = 'none';
}

function openModalFooter() {

    overlayFooter.style.display = 'block';
}


function closeModalFooter() {

    overlayFooter.style.display = 'none';
}