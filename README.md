# Aquascape AI Backyard Designer

This project is an experimental Flask web service that uses **OpenAI’s GPT-4 Vision** and **DALL·E image editing** tools to generate backyard Aquascape design sketches.

---

## Project Goal

The goal is to let a user upload a **photo of their backyard** and automatically receive:
- A **textual description** of Aquascape design suggestions, including:
  - Zone breakdowns (lawn, patio, shaded areas, etc.)
  - Environmental features (sunlight, slope, drainage, materials)
  - Recommended Aquascape feature (pond, fountain, waterfall, etc.)
- A **visual sketch edit** of the original backyard image using OpenAI’s image editing tools, showing the proposed design as if drawn in a conceptual site plan style.

This is intended as a creative concept tool for landscape designers, homeowners, or Aquascape enthusiasts.

---

## Project Contents

- `app.py` → Flask web server that:
  - Handles file uploads (`/upload` route)
  - Uses OpenAI GPT-4 Vision to analyze the photo
  - Uses DALL·E API for `Image.edit` to generate visual sketch edits
- `openAIKEY.env` → Local `.env` file to store the OpenAI API key securely
- `venv/` → Python virtual environment (not included in repo)
- `requirements.txt` → Python dependencies (Flask, openai, Pillow, python-dotenv)
- `systemd/` → Example `brocksdemo.service` file to run the app as a systemd service on Ubuntu

---

## Important Notes

**Authentication**
- Requires an active OpenAI API key with:
  - GPT-4 Vision access
  - DALL·E `edit` (image editing) access
- Make sure your `.env` or hardcoded key is set properly.

**API Limits**
- The DALL·E API `edit` endpoint enforces a **prompt max length** (currently ~1000 characters).
- The project’s prompt builder may need trimming or shortening to stay under this limit.

**Runtime Setup**
- Python 3.12+
- Recommended to run inside a virtual environment (`venv`)
- Deployment tested with:
  - Gunicorn
  - systemd on Ubuntu Linux

**General Prompt**
- Analyze the uploaded backyard image and output a detailed description for a proposed Aquascape landscape design, written in the style and layout of a hand-drawn site sketch plan.
Specifically provide:
  - 1. Zone Breakdown — Identify key areas (e.g., open lawn, shaded edges, patios, planting beds, walkways, structures).
  - 2. Environmental Features — Note sunlight, slope, grade, drainage, and existing materials (stone, wood, grass, fences).
  - 3. Recommended Aquascape Feature(s) — Choose from: koi pond, pondless waterfall, stacked slate fountain, basalt columns, fire + water bowls, mini container pond, or rainwater harvesting system — and explain why it fits the space.
- Describe how the edited image should visually change using the look and language of a landscape concept sketch. Include:
The rough layout: where on the site the feature is placed (e.g., upper left corner near the shade line, centered in the patio, along the rear edge slope)
  - Visual elements: textures, materials, boulders, water, planting blocks, pathways, drawn as soft colored areas or textures (green for grass, blue for water, gray for stone, etc.)
  - Annotation style: include short, sketched-style labels or markers (e.g., “New Pond Edge,” “Berm + Planting 24”,” “Stacked Slate Fountain Here”)
  - Perspective: maintain the samePerspective, plan-view sketch format (not photorealistic) with clear zone shapes and labeled features
- The output should describe the modification so it can be directly used to prompt an another GPT chat image editing.

---

## Easier Alternatives

If you don’t want to manage servers, you can:
- Use **OpenAI Assistants API** to directly chain:
  1. GPT-4 Vision image analysis
  2. DALL·E image generation or editing
- Or, use **ChatGPT web interface** (with Vision + DALL·E) to prompt the system interactively.

Let me know if you want a ready-made script or prompt for that simpler approach!

---

## Future Improvements

- Add frontend UI (HTML/JS) for easier photo upload
- Automate error handling for oversized prompts
- Support more advanced mask generation
- Add multiple design options (not just one sketch)

---

## Credits

Built using:
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Aquascape®](https://www.aquascapeinc.com/) design inspiration
- by Dylan Montgomery
