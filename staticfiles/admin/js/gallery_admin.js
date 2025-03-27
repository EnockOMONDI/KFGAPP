document.addEventListener('DOMContentLoaded', function() {
    const uploadTypeSelect = document.getElementById('id_upload_type');
    const singleImageDiv = document.querySelector('.field-single_image');
    const multipleImagesDiv = document.querySelector('.field-multiple_images');

    function toggleFields() {
        if (uploadTypeSelect.value === 'single') {
            singleImageDiv.style.display = 'block';
            multipleImagesDiv.style.display = 'none';
        } else {
            singleImageDiv.style.display = 'none';
            multipleImagesDiv.style.display = 'block';
        }
    }

    if (uploadTypeSelect) {
        uploadTypeSelect.addEventListener('change', toggleFields);
        // Initial state
        toggleFields();
    }
});