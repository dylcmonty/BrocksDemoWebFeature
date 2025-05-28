import os
import traceback
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from PIL import Image, ImageDraw
import openai

openai.api_key = 'sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Load environment variables
load_dotenv('/home/ubuntu/BrocksDemo/openAIKEY.env')
print("🔥 Loaded OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

#openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

# Static prompt (can later be made dynamic with GPT-4 Vision)
AQUASCAPE_PREPROCESS_PROMPT = """
Analyze the uploaded backyard image and output a detailed description for a proposed Aquascape landscape design, written in the style and layout of a hand-drawn site sketch plan.

Specifically provide:
1️⃣ Zone Breakdown — Identify key areas (e.g., open lawn, shaded edges, patios, planting beds, walkways, structures).
2️⃣ Environmental Features — Note sunlight, slope, grade, drainage, and existing materials (stone, wood, grass, fences).
3️⃣ Recommended Aquascape Feature(s) — Choose from: koi pond, pondless waterfall, stacked slate fountain, basalt columns, fire + water bowls, mini container pond, or rainwater harvesting system — and explain why it fits the space.
4️⃣ Sketch-Style Visual Description (for Image.create_edit()) —
Describe how the edited image should visually change using the look and language of a landscape concept sketch. Include:
- The rough layout: where on the site the feature is placed.
- Visual elements: textures, materials, boulders, water, planting blocks, pathways, drawn as soft colored areas or textures.
- Annotation style: short, sketched-style labels or markers.
- Perspective: maintain a top-down, plan-view sketch format.
"""

def create_simple_center_mask(image_path, mask_output_path):
    img = Image.open(image_path)
    w, h = img.size

    # Create transparent mask (black = keep, white = edit)
    mask = Image.new('L', (w, h), 0)  # black background (keep)
    draw = ImageDraw.Draw(mask)

    # Define central rectangle (editable area)
    left = w // 4
    top = h // 4
    right = 3 * w // 4
    bottom = 3 * h // 4

    # Draw white rectangle (edit area)
    draw.rectangle([left, top, right, bottom], fill=255)

    # Save mask
    mask.save(mask_output_path)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Check access code
        access_code = request.form.get('access_code')
        if access_code != '1776':
            return jsonify({'error': 'Unauthorized access'}), 403

        # Check photo upload
        if 'photo' not in request.files:
            return jsonify({'error': 'No photo uploaded'}), 400

        photo = request.files['photo']
        temp_file = '/tmp/uploaded_backyard.png'
        mask_file = '/tmp/generated_mask.png'

        # Save uploaded image
        photo.save(temp_file)

        # Generate a simple mask (center rectangle)
        create_simple_center_mask(temp_file, mask_file)

        with open(temp_file, "rb") as image_file, open(mask_file, "rb") as mask_file_obj:
            edit_response = openai.images.edit(
                image=image_file,
                mask=mask_file_obj,
                prompt=AQUASCAPE_PREPROCESS_PROMPT,
                n=1,
                size='512x512'
            )

        # Access the generated image URL
        result_image_url = edit_response.data[0].url

        return jsonify({'result': result_image_url})

    except Exception as e:
        print('❌ Error:', e)
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500
