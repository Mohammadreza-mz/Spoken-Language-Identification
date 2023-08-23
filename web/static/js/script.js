document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const predictButton = document.getElementById('predictButton');
    const result = document.getElementById('result');
    const uploadText = document.getElementById('uploadText');

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            uploadText.textContent = `Your uploaded file is: ${fileInput.files[0].name}`;
        } else {
            uploadText.textContent = 'Drag and drop or click to upload';
        }
    });

    predictButton.addEventListener('click', async () => {
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        if (fileInput.files.length === 0) {
            uploadText.textContent = 'Drag and drop or click to upload';
            result.textContent = `No file selected.`;
            return;
        }

        result.textContent = `Waiting for response...`;
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            result.textContent = `Predicted Language: ${data.language}`;
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
