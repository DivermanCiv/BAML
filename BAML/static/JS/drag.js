//class for drag and drop
class DragAndDrop {
    constructor() {
        this.filesDropped();
        this.filesChanged();
        this.file_exists = false;
    }
    //action when file is dropped
    filesDropped() {
        let field = document.querySelectorAll("div.drag_drop_field");

        for (let i = 0; i < field.length; i++) {

            field[i].ondragover = field[i].ondragenter = function (e) {
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
    // action when file is uploaded
    filesChanged() {
        let field = document.querySelectorAll("input.file_input");

        for (let j = 0; j < field.length; j++) {
            field[j].onchange = (e) => {
                let formId = e.target.getAttribute("data-form-id");
                let formField = e.target.getAttribute("data-form-field");
                this.displayFileList(formId, formField);
            }
        }
    }
    // DOM modification when a file is uploaded or dropped
    displayFileList(formId, formField) {
        dd.file_exists = true;
        document.getElementById("no_file_present").hidden = true;
        let files = document.querySelector(`form#${formId} input[name='${formField}']`).files;
        let fileList = ``;

        for (let i = 0; i < files.length; i++) {

            let fileExt = this.getFileExtension(files[i].name);
            let fileSize = this.convertBytesTo(files[i].size, 'K', 0);

            fileList = `
                ${fileList}
                <div class="file">
                    <span id="filelist_close_cross">X</span>
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
            //check if the uploaded file is a .csv
            if (fileExt != "csv") {
                document.getElementById("validate_csv").hidden = true;
                document.getElementById("file_extension_error").hidden = false;
            }
            else {
                document.getElementById("validate_csv").hidden = false;
                document.getElementById("file_extension_error").hidden = true;
            }
        }

        document.querySelector(`form#${formId} div.file_list[data-form-field='${formField}']`).innerHTML = fileList;

        document.getElementById("filelist_close_cross").addEventListener("click", function () {

            document.querySelector(`form#${formId} div.file_list[data-form-field='${formField}']`).innerHTML = '';
            dd.file_exists = false;
        });
    }
    // convert byte to decimal
    convertBytesTo(bytes, to, decimalPlaces = 2) {
        switch (to) {
            case 'K':
                {
                    bytes = bytes / 1024;
                    break;
                }
            case 'M':
                {
                    bytes = bytes / 1048576;
                    break;
                }
            case 'G':
                {
                    bytes = bytes / 1073741824;
                    break;
                }
        }
        return bytes = +bytes.toFixed(decimalPlaces);
    }

    // return the extension of file dropped
    getFileExtension(fileName) {
        return fileName.split('.').pop()
    }
    // return if a file is dropped
    checkIfFileExists() {
        if (dd.file_exists == false) {
            document.getElementById("no_file_present").hidden = false;
            return false;
        }
        else {
            return true;
        }
    }
}
let dd = new DragAndDrop();
