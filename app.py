{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": "None",
   "id": "6c49b6d1-69b1-4bd2-bb9d-d8fbdbaa626f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify, render_template, send_file\n",
    "import random\n",
    "from io import BytesIO\n",
    "from PIL import Image, ImageDraw, ImageFont\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "def generate_business_idea():\n",
    "    ideas = [\n",
    "        \"Start a podcast editing service.\",\n",
    "        \"Create an online course.\",\n",
    "        \"Develop a mobile app.\",\n",
    "        \"Offer freelance graphic design services.\",\n",
    "        \"Launch an e-commerce store.\"\n",
    "    ]\n",
    "    return random.choice(ideas)\n",
    "\n",
    "def generate_catchphrase():\n",
    "    phrases = [\n",
    "        \"Empowering Your Future.\",\n",
    "        \"Innovation at its Best.\",\n",
    "        \"Dream Big, Achieve More.\",\n",
    "        \"Your Success, Our Commitment.\",\n",
    "        \"Where Ideas Become Reality.\"\n",
    "    ]\n",
    "    return random.choice(phrases)\n",
    "\n",
    "def generate_logo(text=\"Logo\"):\n",
    "    # Create an image with a white background\n",
    "    img = Image.new('RGB', (200, 100), color=(255, 255, 255))\n",
    "    d = ImageDraw.Draw(img)\n",
    "    \n",
    "    # Define a font\n",
    "    try:\n",
    "        font = ImageFont.truetype(\"arial.ttf\", 40)\n",
    "    except IOError:\n",
    "        font = ImageFont.load_default()\n",
    "\n",
    "    # Add text to the image\n",
    "    d.text((10, 30), text, fill=(0, 0, 0), font=font)\n",
    "    \n",
    "    # Save the image to a BytesIO object\n",
    "    img_io = BytesIO()\n",
    "    img.save(img_io, 'PNG')\n",
    "    img_io.seek(0)\n",
    "    return img_io\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/chat', methods=['POST'])\n",
    "def chat():\n",
    "    user_message = request.json['message'].lower()\n",
    "\n",
    "    if 'business idea' in user_message:\n",
    "        reply = generate_business_idea()\n",
    "    elif 'catchphrase' in user_message:\n",
    "        reply = generate_catchphrase()\n",
    "    elif 'logo' in user_message:\n",
    "        return send_file(generate_logo(\"Your Logo\"), mimetype='image/png')\n",
    "    else:\n",
    "        reply = \"Sorry, I can only provide business ideas, catchphrases, and logos.\"\n",
    "\n",
    "    return jsonify({'reply': reply})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    from waitress import serve\n",
    "    serve(app, host=\"0.0.0.0\", port=8080)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "None",
   "id": "c951d1ed-f8bd-4553-ae70-4cdf8cc5e4fc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
