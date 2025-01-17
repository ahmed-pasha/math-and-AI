# Hand Gesture Recognition and AI Integration

This project integrates hand gesture recognition with AI capabilities using various libraries such as OpenCV, cvzone, and Google's generative AI. The project captures hand gestures through a webcam, processes them, and interacts with a generative AI model to provide relevant outputs based on detected gestures.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project aims to create an interactive application that recognizes hand gestures using computer vision and provides AI-generated responses. It utilizes a combination of OpenCV for video capture, cvzone for hand gesture detection, and Google's generative AI for producing responses.

## Features

- Real-time hand gesture recognition using OpenCV and cvzone.
- AI integration to generate responses based on specific gestures.
- Drawing and erasing functionality based on hand gestures.
- Streamlit for creating a web-based user interface.

## Installation
### Clone the Repository
  `git clone https://github.com/ahmed-pasha/math-and-AI.git`
  `cd math-and-AI`

### Prerequisites
  Ensure you have the following installed:

- Python 3.6+
- pip (Python package installer)
- Git
## Create and Activate a Virtual Environment
   python -m venv .venv
   source .venv/bin/activate  
## On Windows, use 
  `.venv\Scripts\activate`

## Install Dependencies
  `pip install -r requirements.txt`

## Running the Application
  - Activate the virtual environment if not already activated:
  # On Windows, use 
  `.venv\Scripts\activate`
## Run the Streamlit application:
  `streamlit run app.py`
## Application Functionality
  - Hand Gesture Detection: The application uses the webcam to detect hand gestures.
  - Drawing: Draw on the screen using specific hand gestures.
  - Erasing: Clear the canvas with a hand gesture.
  - AI Integration: Certain gestures trigger AI responses, which are displayed on the interface.
## Contributing
  -We welcome contributions! Please follow these steps to contribute:

## Fork the repository.
  - Create a new branch (git checkout -b feature-branch).
  - Make your changes and commit them (git commit -m 'Add some feature').
  - Push to the branch (git push origin feature-branch).
  - Open a Pull Request.

## Acknowledgments
  - OpenCV for the computer vision library.
  - cvzone for the hand detection module.
  - Google Generative AI for AI capabilities.
  - Streamlit for the web interface framework.





