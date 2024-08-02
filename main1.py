import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Streamlit configuration
st.set_page_config(layout="wide")
st.image('thelastofai.png')

col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.empty()

# Google Generative AI configuration
genai.configure(api_key="Your_API_Key")  # Replace with your actual API key
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)  # Use the built-in camera (index 0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    try:
        hands, img = detector.findHands(img, draw=False, flipType=True)
        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            fingers = detector.fingersUp(hand)
            return fingers, lmList
        else:
            return None
    except Exception as e:
        st.error(f"An error occurred while detecting hands: {e}")
        return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, tuple(current_pos), tuple(prev_pos), (255, 0, 255), 10)
    elif fingers == [1, 0, 0, 0, 0]:
        canvas = np.zeros_like(canvas)
    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 1, 1, 0, 0]:
        try:
            pil_image = Image.fromarray(canvas)
            response = model.generate_content(["Solve this math problem and explain it", pil_image])
            return response.text
        except Exception as e:
            st.error(f"An error occurred while sending data to AI: {e}")
            return ""

prev_pos = None
canvas = None
output_text = ""

while run:
    success, img = cap.read()
    if not success or img is None:
        st.error("Failed to capture image from camera.")
        continue

    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    info = getHandInfo(img)
    if info:
        fingers, lmList = info
        prev_pos, canvas = draw(info, prev_pos, canvas)
        if fingers == [1, 1, 1, 0, 0]:  # Only call AI when necessary
            output_text = sendToAI(model, canvas, fingers)

    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")

    if output_text:
        output_text_area.markdown(output_text.replace('\n', '  \n'))

    cv2.waitKey(1)
