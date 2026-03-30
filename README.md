# face_recognition_project

# 🎯 Smart Face Recognition Attendance System

A real-time face recognition-based attendance system built using Python, OpenCV, and Machine Learning (KNN). This project automates attendance marking by detecting and recognizing faces through a webcam.

---

## 🚀 Features

- 📷 Real-time face detection using OpenCV
- 🧠 Face recognition using K-Nearest Neighbors (KNN)
- 💾 Stores face data using Pickle files
- 📊 Automatic attendance marking in CSV format
- 🌐 Streamlit-based live attendance dashboard
- 🔄 Auto-refresh attendance display

---

## 🛠️ Technologies Used

- Python 🐍
- OpenCV 📷
- NumPy
- Scikit-learn 🤖
- Pandas 📊
- Streamlit 🌐

---

## 📂 Project Structure
FACE_RECOGNITION_PROJECT/
│
├── Attendance/
│ └── Attendance_<date>.csv
│
├── data/
│ ├── faces_data.pkl
│ ├── names.pkl
│ └── haarcascade_frontalface_default.xml
│
├── add_faces.py # Collect face data
├── app.py # Face recognition & attendance
├── test.py # Testing and debugging
├── background.png # UI background
├── README.md


---

## ⚙️ How It Works

1. **Data Collection**
   - Run `add_faces.py`
   - Capture 100 face images
   - Store in `.pkl` files

2. **Face Recognition**
   - Run `app.py`
   - Detect and recognize faces using KNN

3. **Attendance Marking**
   - Press `'O'` to mark attendance
   - Data saved in CSV file

4. **Dashboard**
   - Run Streamlit app to view attendance

---

## ▶️ How to Run

### Step 1: Install dependencies

---

### Step 2: Collect face data

---

### Step 3: Run face recognition

---

### Step 4: Run dashboard

---

## 📊 Output

- Displays recognized face with name
- Stores attendance in CSV file
- Shows attendance in web dashboard

---

## ⚠️ Limitations

- Sensitive to lighting conditions
- Uses basic ML (not deep learning)
- Accuracy depends on training data

---

## 🔮 Future Improvements

- Deep learning models (FaceNet, CNN)
- Database integration (MySQL)
- Mobile/Web deployment
- Multi-face tracking improvement

---

## 🎯 Conclusion

This project demonstrates how computer vision and machine learning can be used to automate real-world tasks like attendance, improving efficiency and accuracy.

---

## 👨‍💻 Author

- Govardhan

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!