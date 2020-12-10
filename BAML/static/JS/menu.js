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
function openModalHeader() {

    overlayHeader.style.display = 'block';
}


function closeModalHeader() {

    overlayHeader.style.display = 'none';
}



// popup contact


function openModalHeaderContact() {

    overlayHeaderContact.style.display = 'block';
}


function closeModalHeaderContact() {

    overlayHeaderContact.style.display = 'none';
}

