from flask import Flask, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load the saved generator model
# generator = load_model('DCGEN.h5')
generator = load_model('DCGEN_100_epochs.h5')

latent_dim = 300  # Assuming the model expects a latent dimension of 300

# Function to generate images using the generator model
def generate_images(generator, num_images, latent_dim):
    noise = tf.random.normal([num_images, latent_dim])
    generated_images = generator.predict(noise)
    generated_images = (generated_images * 127.5) + 127.5  # Denormalize
    return generated_images

# Function to convert PIL Image to base64-encoded string
def pil_to_base64(image):
    img_byte_array = io.BytesIO()
    # Explicitly specify the image format as PNG
    image.save(img_byte_array, format='PNG')
    img_byte_array = img_byte_array.getvalue()
    return base64.b64encode(img_byte_array).decode('utf-8')


@app.route('/')
def index():
    # Generate 16 random images
    generated_images = generate_images(generator, 16, latent_dim)

    # Prepare images for rendering
    images = []
    for generated_image in generated_images:
        image = Image.fromarray(np.uint8(generated_image))
        images.append(pil_to_base64(image))

    # Render the template with the images
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
