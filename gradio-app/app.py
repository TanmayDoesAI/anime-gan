import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import gradio as gr

# Load the saved generator model
generator = load_model('DCGEN_50_epochs.h5')

latent_dim = 300  # Assuming the model expects a latent dimension of 300

# Function to generate images using the generator model
def generate_images(generator, num_images, latent_dim):
    noise = tf.random.normal([num_images, latent_dim])
    generated_images = generator.predict(noise)
    generated_images = (generated_images * 127.5) + 127.5  # Denormalize
    return generated_images

# Function to convert generated images to a list of PIL Images
def generate_pil_images():
    generated_images = generate_images(generator, 16, latent_dim)
    pil_images = [Image.fromarray(np.uint8(image)) for image in generated_images]
    return pil_images

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_pil_images,
    inputs=[],
    outputs=gr.Gallery(label="Generated Images",columns=4, height="fill"),
    title="Generated Images",
    description="This Gradio app generates 16 random images using a pre-trained generator model whenever the interface is refreshed."
)

# Launch the Gradio app
iface.launch()
