function afficheMenu() {
    console.log('coucou')
    var x = document.getElementById("mobile");
    if (x.style.display === "flex") {
        x.style.display = "none";
    } else {
        x.style.display = "flex";
    }
} 