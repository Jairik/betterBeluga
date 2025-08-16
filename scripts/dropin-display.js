/** Image dropper with display feature */
(function () {

    // Read in arguments/ids from the tags
    const scriptElement = document.getElementById("app-script");
    const dropId = scriptElement?.dataset.drop;
    const fileInputId = scriptElement?.dataset.fileInput;
    const display = (scriptElement?.dataset.display || "true") === "true";
    const previewId = display ? scriptElement?.dataset.preview : undefined;

    // Resolve the elements from the extracted ids
    const dropArea = dropId ? document.getElementById(dropId) : null; 
    const fileInput = fileInputId ? document.getElementById(fileInputId) : null;
    const preview = previewId ? document.getElementById(previewId) : null;

    if (!dropArea || !fileInput){
        console.warn("<dropin-display> Missing drop area or file input element");
        return;
    }

    // Onclick listener to upload file
    dropArea.addEventListener('click', () => fileInput.click());

    // Listeners for drag & drop (visuals)
    ["dragenter", "dragover"].forEach(evt => 
        dropArea.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
            dropArea.classList.add("hover");
        })
    );
    ["dragleave", "drop"].forEach(evt => 
        dropArea.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
            dropArea.classList.remove("hover");
        })
    );

    // Handle dropped files
    dropArea.addEventListener("drop", e => {
        const file = e.dataTransfer?.files?.[0];
        if (file && file.type.startsWith("image/")){ displayImage(file); }
    })

    // Handle chooser
    fileInput.addEventListener("change", () => {
        const file = fileInput.files?.[0];
        if(file && file.type.startsWith("image/")){ displayImage(file); }
    })

    // Display the image
    function displayImage(file) {
        if (!preview){ return; }  // Skip if no preview is selected
        const reader = new FileReader();
        reader.onload = (event) => {
            preview.src = event.target.result;
        };
        reader.readAsDataURL(file);
    }
})();