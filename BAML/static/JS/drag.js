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
                console.log(input.files[0].Name)
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