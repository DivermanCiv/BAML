// https://www.youtube.com/watch?v=Wtrin7C4b7w
// https://codepen.io/dcode-software/pen/xxwpLQo



// récupération de l'élément dropzone__input
document.querySelectorAll('.drop-zone__input').forEach(inputElement => {
    const dropZoneElement = inputElement.closest(".drop-zone");

    // permet d'ajouter des fichiers via gestionnaire de fichier
    dropZoneElement.addEventListener("click", e => {
        inputElement.click();
    });

    //ajout de listener en cas de drag de plusieurs fichiers
    inputElement.addEventListener("change", e => {
        if (inputElement.files.lenght) {
            updateThumbnail(dropZoneElement, inputElement.file[0])
        }
    })



    //empeche le comportement par défaut lors d'un drag
    // ajoute une classe pour gestion css
    dropZoneElement.addEventListener("dragover", e => {
        e.preventDefault();
        dropZoneElement.classList.add("drop-zone--over");
    });
    // retire la classe drop-zone--over si le drag est annulé
    ["dragleave", "dragend"].forEach(type => {
        dropZoneElement.addEventListener(type, e => {
            dropZoneElement.classList.remove("drop-zone--over");
        })
    });

    //empeche le comportement par défaut lors d'un drag
    // permet de drop le drag
    dropZoneElement.addEventListener("drop", e => {
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            inputElement.files = e.dataTransfer.files;
            console.log(e.dataTransfer);
            //console.log(e.dataTransfer)
            updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
        }

        dropZoneElement.classList.remove("drop-zone--over");
    })

});


// mise a jour de la vignette avec info du document droppé
function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb")

    if (dropZoneElement.querySelector(".drop-zone__prompt")) {
        dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }


    if (!thumbnailElement) {
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("drop-zone__thumb");
        dropZoneElement.appendChild(thumbnailElement);
    }

    thumbnailElement.dataset.label = file.name;
    if (file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
        }
    } else {
        thumbnailElement.style.backgroundImage = null

    }
}