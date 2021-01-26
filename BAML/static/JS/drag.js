// https://www.youtube.com/watch?v=Wtrin7C4b7w
// https://codepen.io/dcode-software/pen/xxwpLQo



// // récupération de l'élément dropzone__input
// document.querySelectorAll('.drop-zone__input').forEach((inputElement) => {
//     const dropZoneElement = inputElement.closest(".drop-zone");
//
//     // permet d'ajouter des fichiers via gestionnaire de fichier
//     dropZoneElement.addEventListener("click", (e) => {
//         inputElement.click();
//     });
//
//     //ajout de listener en cas de drag de plusieurs fichiers
//     inputElement.addEventListener("change", (e) => {
//         if (inputElement.files.length) {
//             updateThumbnail(dropZoneElement, inputElement.files[0]);
//         }
//     });
//
//
//
//     //empeche le comportement par défaut lors d'un drag
//     // ajoute une classe pour gestion css
//     dropZoneElement.addEventListener("dragover", (e) => {
//         e.preventDefault();
//         dropZoneElement.classList.add("drop-zone--over");
//     });
//     // retire la classe drop-zone--over si le drag est annulé
//     ["dragleave", "dragend"].forEach((type) => {
//         dropZoneElement.addEventListener(type, (e) => {
//             dropZoneElement.classList.remove("drop-zone--over");
//         });
//     });
//
//     //empeche le comportement par défaut lors d'un drag
//     // permet de drop le drag
//     dropZoneElement.addEventListener("drop", (e) => {
//         e.preventDefault();
//         if (e.dataTransfer.files.length) {
//             inputElement.files = e.dataTransfer.files;
//             console.log(e.dataTransfer);
//             updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
//         }
//
//         dropZoneElement.classList.remove("drop-zone--over");
//     });
//
// });
//
// /**
//  *
//  * @param {HTMLElement} dropZoneElement
//  * @param {File} file
//  */
//
// // mise a jour de la vignette avec info du document droppé
// function updateThumbnail(dropZoneElement, file) {
//     let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");
//
//     if (dropZoneElement.querySelector(".drop-zone__prompt")) {
//        dropZoneElement.querySelector(".drop-zone__prompt").remove();
//     }
//
//
//     if (!thumbnailElement) {
//        thumbnailElement = document.createElement("div");
//        thumbnailElement.classList.add("drop-zone__thumb");
//        dropZoneElement.appendChild(thumbnailElement);
//     }
//
//     thumbnailElement.dataset.label = file.name;
//
//     if (file.type.startsWith("image/")) {
//         const reader = new FileReader();
//         reader.readAsDataURL(file);
//         reader.onload = () => {
//             thumbnailElement.style.backgroundImage = `url('${ reader.result }')`;
//         }
//     } else {
//         thumbnailElement.style.backgroundImage = null;
//
//     }
// }

class DragAndDrop {
    constructor() {
        this.filesDropped();
        this.filesChanged();
    }

    filesDropped() {
        let field = document.querySelectorAll("div.drag_drop_field");

        for (let i = 0; i < field.length; i++) {

            field[i].ondragover = field[i].ondragenter = function(e) {
                e.preventDefault();
            };

            field[i].ondrop = (e) => {

                e.preventDefault();
                let formId = e.target.getAttribute("data-form-id");
                let formField = e.target.getAttribute("data-form-field");
                let input = document.querySelector(`form#${formId} input[name='${formField}']`);
                input.files = e.dataTransfer.files;
                this.displayFileList(formId, formField);
            }
        }
    }

    filesChanged(){
        let field = document.querySelectorAll("input.file_input");

        for (let j = 0; j < field.length; j++) {
            field[j].onchange = (e) => {
                let formId = e.target.getAttribute("data-form-id");
                let formField = e.target.getAttribute("data-form-field");
                this.displayFileList(formId, formField);
            }
        }
    }

    displayFileList(formId, formField) {
        let files = document.querySelector(`form#${formId} input[name='${formField}']`).files;
        let fileList = ``;

        for (let i = 0; i < files.length; i++) {

            let fileExt = this.getFileExtension(files[i].name);
            let fileSize = this.convertBytesTo(files[i].size, 'K', 0);

            if (fileExt === 'csv') {

            }

            fileList = `
                ${fileList}
                <div class="file">
                    <div class="file_name">
                        ${files[i].name}
                    </div>
                    <div class="file_details">
                        <div class="file_extension">
                            ${fileExt}
                        </div>
                        <div class="file_size">
                            ${fileSize} KB
                        </div>
                    </div>
                </div>                 
                `;
        }

        document.querySelector(`form#${formId} div.file_list[data-form-field='${formField}']`).innerHTML = fileList;
    }
    convertBytesTo(bytes, to, decimalPlaces = 2) {
        switch (to) {
            case 'K' :
                {
                    bytes = bytes / 1024;
                    break;
                }
            case 'M' :
                {
                    bytes = bytes / 1048576;
                    break;
                }
            case 'G' :
                {
                    bytes = bytes / 1073741824;
                    break;
                }
        }
        return bytes = +bytes.toFixed(decimalPlaces);
    }


    getFileExtension(fileName) {
        return fileName.split('.').pop()
    }

}
let dd = new DragAndDrop();