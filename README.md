# AI-Based Emotion Detection using CNN  
### Python | TensorFlow | OpenCV | Gradio

This project classifies human emotions from face images using a Convolutional Neural Network (CNN).  
It includes a real-time **Gradio web interface** to upload images and view predictions instantly.

---

## 🚀 Features
- Predicts emotions such as: **Happy**, **Sad**, **Angry**, **Neutral**
- Deep Learning model trained on a large image dataset
- Gradio-based front-end for live testing
- Clean, simple code with modular structure
- Fully compatible with **Google Colab**, **Jupyter Notebook**, and **VS Code**

---

## 📁 Project Structure

Emotion-Detection/
│── Emotion_Detection_Clean.ipynb # Clean training notebook
│── emotion_model.h5 # Trained CNN model
│── app.py # Gradio app script
│── requirements.txt # Dependencies
│── README.md # Project documentation

yaml
Copy code

---

## 🧠 Model Information
The model is built using a Convolutional Neural Network with:
- 3 Convolution Layers
- Batch Normalization
- MaxPooling Layers
- Dense (Fully Connected) Layer
- Dropout (to prevent overfitting)
- Softmax output for emotion probability scores

---

## 🧪 Dataset Structure
Your dataset must follow this format:

train/
angry/
happy/
sad/
neutral/

test/
angry/
happy/
sad/
neutral/

yaml
Copy code

Supported dataset: **FER2013**, Kaggle datasets, or custom datasets.

---

## ▶️ Running the Gradio App

### **Install dependencies**
pip install -r requirements.txt

markdown
Copy code

### **Run the app**
python app.py

arduino
Copy code

Gradio will open at:

http://127.0.0.1:7860

yaml
Copy code

Upload an image → Model predicts emotion.
<img width="1670" height="657" alt="image" src="https://github.com/user-attachments/assets/f1f1538e-299c-4cf7-aeb4-b12c6af9ab15" />


---

## 👩‍💻 Developer  
**Radhika Kakad**  
AI & Data Science Student

---

## ⭐ Show Support  
If this project helped you, please 🌟 star the repository!
