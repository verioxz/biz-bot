from flask import Flask, request, jsonify, render_template, send_file
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import google.generativeai as palm
{"model": "models/chat-bison-001"}
from urllib.parse import quote
from werkzeug.urls import url_quote_plus
import os

app = Flask(__name__)

# Initialize MakerSuite with API Key from environment variable

palm.configure(api_key="AIzaSyDQegtx6ycbXTp7treDwhdzmba2V6WdSQ0")

def generate_business_idea():
    ideas = [
        "Start a podcast editing service.",
        "Create an online course.",
        "Develop a mobile app.",
        "Offer freelance graphic design services.",
        "Launch an e-commerce store.",
        "Provide virtual assistant services.",
        "Start a social media marketing agency.",
        "Create a subscription box service.",
        "Offer personal coaching services.",
        "Develop a software as a service (SaaS) product.",
        "Start a blog and monetize through ads and affiliate marketing.",
        "Launch a YouTube channel and monetize through ads and sponsorships.",
        "Offer web development services.",
        "Create a dropshipping business.",
        "Start a digital marketing consultancy.",
        "Provide online bookkeeping services.",
        "Create an online tutoring service.",
        "Develop a niche product and sell it online.",
        "Start a local delivery service.",
        "Offer home cleaning services."
    ]
    return random.choice(ideas)

def generate_catchphrase():
    phrases = [
        "Empowering Your Future.",
        "Innovation at its Best.",
        "Dream Big, Achieve More.",
        "Your Success, Our Commitment.",
        "Where Ideas Become Reality.",
        "Think Different, Act Different.",
        "Excellence in Every Step.",
        "Your Vision, Our Mission.",
        "Creating Tomorrow Today.",
        "Experience the Difference.",
        "Unlock Your Potential.",
        "Success Redefined.",
        "Together Towards Tomorrow.",
        "Inspire, Innovate, Ignite.",
        "Transforming Dreams into Reality.",
        "Your Partner in Progress.",
        "Leading with Innovation.",
        "Building a Better Future.",
        "Commitment to Excellence.",
        "Imagine the Possibilities."
    ]
    return random.choice(phrases)

def generate_logo(text="Logo"):
    # Create an image with white background
    img = Image.new('RGB', (200, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Define a font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Add text to the image
    d.text((10, 30), text, fill=(0, 0, 0), font=font)

    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    if 'business idea' in user_message.lower():
        reply = generate_business_idea()
    elif 'catchphrase' in user_message.lower():
        reply = generate_catchphrase()
    elif 'logo' in user_message.lower():
        return send_file(generate_logo("Your Logo"), mimetype='image/png')
    else:
        # Use MakerSuite to get a response
        response = client.completions.create(
            prompt=user_message,
            max_tokens=150
        )
        reply = response.choices[0].text.strip()

    return jsonify({'reply': reply})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
