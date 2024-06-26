# Anime-GAN: Exploring Generative Adversarial Networks

## Overview
Anime-GAN is a pioneering project that leverages the capabilities of Deep Convolutional Generative Adversarial Networks (DCGAN) to generate high-quality anime faces. Inspired by the website "[thispersondoesnotexist.com](https://thispersondoesnotexist.com)," this project aims to provide a similar experience but with a focus on anime characters. Each refresh on the project's web page presents a new set of 16 anime faces arranged in a 4x4 grid, showcasing the diversity and artistic potential of the generated characters.

## Installation

### Prerequisites
- [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) installed on your machine.

### Setting Up the Environment
To set up the project environment and run the application, follow these steps:

1. **Create and activate a new Conda environment:**
   ```bash
   conda create -n anime-gan python=3.10
   conda activate anime-gan
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask app:**
   Open a terminal and run the following command:
   ```bash
   python app.py
   ```

2. **Expose the app to the internet using Ngrok:**
   Open another terminal and run:
   ```bash
   ngrok http 5000
   ```
   This will generate a public URL that can be used to access the Flask app from anywhere.

## Usage
Navigate to the Ngrok URL or `http://localhost:5000` provided by the Ngrok output. The webpage will display 16 anime faces in a 4x4 grid. Each refresh of the page generates a new set of faces, demonstrating the model's ability to create diverse and visually appealing anime characters.

## Training the Model
For those interested in training the Anime-GAN model themselves or making modifications, a Jupyter Notebook (`training.ipynb`) is provided. You can use this notebook to train the model on Kaggle's kernel with the following dataset:
- [Anime Face Dataset on Kaggle](https://www.kaggle.com/datasets/splcher/animefacedataset)

This allows for customization and experimentation with different model parameters or datasets.

## Screenshots
![Screenshot of the generations](Screenshot.png)

## Gradio Integration

#### Setting Up the Gradio App

- **Navigate to the Gradio folder:**
   ```bash
   git clone https://github.com/TanmayDoesAI/anime-gan.git
   cd gradio-app
   ```

- **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

- **Run the Gradio app:**
   ```bash
   python app.py
   ```

#### Accessing the Gradio App

Access the app locally at `http://localhost:7860`. The Gradio interface allows you to generate and view unique anime characters.

#### Hugging Face Space

Explore AnimeGAN on Hugging Face Spaces: [AnimeGAN on Hugging Face](https://huggingface.co/spaces/Tanmay09516/animegan).

## MacBook Users

### One-Click Setup Script
For MacBook users, you can use the following shell script to simplify the setup and hosting process. Ensure that `jq` is installed on your machine.

1. **Install jq:**
   ```bash
   brew install jq
   ```

2. **Make the `run_app.sh` executable:**
   ```bash
   chmod +x run_app.sh
   ```

3. **Run the script:**
   ```bash
   ./run_app.sh
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Feel free to contribute to Anime-GAN! We welcome contributions from the community to help improve and expand the project. Whether you're interested in fixing bugs, adding new features, or enhancing documentation, your contributions are highly valued.

Enjoy exploring the fascinating intersection of AI and anime art with Anime-GAN!

---
