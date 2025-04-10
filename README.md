# 📸 Caption It Up

**Caption It Up** is a deep learning-powered web app that automatically generates image captions. Built with Flask and a ResNet50-LSTM model pipeline, the app offers a simple, elegant UI and includes text-to-speech support for enhanced accessibility.

---

## 🔍 Demo

![Caption It Up Demo](https://github.com/piyushhh17/Caption-it-up/blob/main/static/preview.gif)  
*Example: "a dog jumping over a hurdle on a track"*

---

## 🚀 Features

- 🧠 AI-generated captions using **ResNet50 + LSTM**
- 🗣️ **Text-to-Speech** support for visually impaired users
- ☁️ **AWS S3** integrated for cloud-based image storage
- 🖼️ Responsive **Flask UI** to upload and caption images
- 🐳 Dockerized for seamless local or cloud deployment

---

## 🛠️ Tech Stack

| Category     | Technology                            |
|--------------|----------------------------------------|
| Backend      | Python, Flask                          |
| ML Model     | TensorFlow, ResNet50, LSTM             |
| Frontend     | HTML, CSS, Bootstrap                   |
| Storage      | AWS S3                                 |
| Deployment   | Docker                                 |
| Accessibility| gTTS (Google Text-to-Speech)           |

---

## 📁 Project Structure

```
Caption-it-up/
│
├── static/                  # Static assets (CSS, JS, images)
├── templates/               # HTML templates
├── app.py                   # Main Flask app
├── utils.py                 # Helper functions for preprocessing and prediction
├── model/                   # Trained ResNet50 + LSTM model and tokenizer
├── requirements.txt         # Python dependencies
└── Dockerfile               # Docker config
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/piyushhh17/Caption-it-up.git
cd Caption-it-up
```

### 2. Create a virtual environment & activate it

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download model weights & tokenizer

Place your `model.h5` and `tokenizer.pickle` inside the `model/` directory.

### 5. Run the app locally

```bash
python app.py
```

App will be available at `http://localhost:5000`

---

## 🐳 Docker Setup (Optional)

```bash
docker build -t caption-it-up .
docker run -p 5000:5000 caption-it-up
```

---

## 📈 Future Improvements

- Upload multiple images in one go
- Add multilingual TTS support
- Build a REST API for programmatic caption generation
- Switch frontend to React for a richer experience

---

## 📜 License

This project is under the [MIT License](LICENSE).

---

## 🙌 Author

**Piyush Kaushal**  
🔗 [LinkedIn](https://www.linkedin.com/in/piyushhh17/) | 🧑‍💻 [GitHub](https://github.com/piyushhh17) | 📧 piyushkaushal17@gmail.com

---

> If you like this project, leave a ⭐ on GitHub. Contributions and feedback are welcome!
