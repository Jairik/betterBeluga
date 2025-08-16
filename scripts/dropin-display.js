/** Image dropper with display feature */
const dropArea = document.getElementById('drop-area');
// Get the arguments from the html file
    const args = document.getElementById("app-script");
    const fileInputID = window.args.fileInput;
    if(window.args.display === "true"){
        const previewID = window.args.preview;
    }
    const fileInput = document.getElementById(fileInputID);
    const preview = document.getElementById(previewID);

    // Onlick listener to upload file
    dropArea.addEventListener('click', () => fileInput.click());

    // Listener for dragging files into box
    dropArea.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropArea.classList.add('hover');
    });
    dropArea.addEventListener('dragleave', () => {
        dropArea.classList.remove('hover');
    });
    dropArea.addEventListener('drop', (event) => {
        event.preventDefault();
        dropArea.classList.remove('hover');
        const file = event.dataTransfer.files[0];
        if (file && file.type.startsWith('image/')) {
            displayImage(file);
        }
    });

    // Display the image, if the valid 
    if(preview){
        fileInput.addEventListener('change', () => {
            const file = fileInput.files[0];
            if (file && file.type.startsWith('image/')) {
                displayImage(file);
            }
        });
    }
    function displayImage(file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            preview.src = event.target.result;
        };
        reader.readAsDataURL(file);
    }