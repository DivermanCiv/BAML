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
                console.table(input.files);
                console.table(e.dataTransfer.files);
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

            if (fileExt != "csv") {
              document.getElementById("validate_csv").hidden = true;
              document.getElementById("file_extension_error").hidden = false;
            }
            else{
              document.getElementById("validate_csv").hidden = false;
              document.getElementById("file_extension_error").hidden = true;
            }

        }

        document.querySelector(`form#${formId} div.file_list[data-form-field='${formField}']`).innerHTML = fileList;

        document.getElementById("filelist_close_cross").onclick = function(){
          document.querySelector(`form#${formId} div.file_list[data-form-field='${formField}']`).innerHTML = '';
        };

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

    checkIfFileExists(){
      alert("test");
      document.getElementById("no_file_present").hidden = false;
    }

}
let dd = new DragAndDrop();
