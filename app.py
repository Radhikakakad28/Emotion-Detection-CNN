import gradio as gr
import tensorflow as tf
import numpy as np
import cv2

# Load trained model
model = tf.keras.models.load_model("emotion_model.h5")

# Emotion labels (auto-update based on your training)
labels = ["angry", "happy", "sad", "neutral"]

IMG_SIZE = (48, 48)

def predict_emotion(img):
    img_resized = cv2.resize(img, IMG_SIZE)
    img_norm = img_resized / 255.0
    img_input = np.expand_dims(img_norm, axis=0)

    preds = model.predict(img_input)[0]
    return {labels[i]: float(preds[i]) for i in range(len(labels))}

demo = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Image(type="numpy", label="Upload Image"),
    outputs=gr.Label(num_top_classes=len(labels)),
    title="AI Emotion Detection",
    description="Upload any face image to predict emotion using a CNN model."
)

demo.launch()
