from flask import Flask, request, jsonify
import openai
import os

# Load API key from environment (safer than hardcoding)
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo uploaded'}), 400

    photo = request.files['photo']

    try:
        # Send image to OpenAI API (example: image variation endpoint)
        response = openai.Image.create_variation(
            image=photo,
            n=1,
            size="512x512"
        )

        # Extract the generated image URL
        image_url = response['data'][0]['url']

        return jsonify({'result': image_url})

    except Exception as e:
        print('Error:', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

