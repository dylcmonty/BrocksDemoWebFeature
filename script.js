document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const photoInput = document.getElementById('photoInput');
    const file = photoInput.files[0];
    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('photo', file);

    try {
        const response = await fetch('https://your-backend-url/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to get response from server');
        }

        const data = await response.json();
        document.getElementById('output').innerText = `Result: ${data.result}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('output').innerText = `Error: ${error.message}`;
    }
});

