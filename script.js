// Unlock button logic
document.getElementById('unlockButton').addEventListener('click', function() {
    const enteredCode = document.getElementById('accessCode').value;
    if (enteredCode === '1776') {
        alert('Access granted!');
        document.getElementById('uploadForm').style.display = 'block';
        document.getElementById('accessCode').style.display = 'none';
        this.style.display = 'none';
    } else {
        alert('Incorrect code. Access denied.');
    }
});

// Upload form logic
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
    formData.append('access_code', '1776'); // Add access code to backend check

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

	if (!response.ok) {
	const errorText = await response.text();
	console.error('Server error response:', errorText);
	throw new Error('Server responded with error: ' + response.status);
	}

        const data = await response.json();

        if (data.error) {
            document.getElementById('output').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('output').innerHTML = `<img src="${data.result}" alt="Generated Image">`;
        }
    } catch (error) {
        console.error('Frontend error:', error);
        document.getElementById('output').innerText = `Request failed: ${error.message}`;
    }
});
