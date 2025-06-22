# Principal Component Analysis (PCA) untuk Kompresi Gambar (Image Compression)
Project Based Learning 2 Aljabar Linear 2025  
<br/>

## Table of Contents
* [General Info](#general-information)
* [Tampilan Program](#tampilan-program)
* [How To Run](#how-to-run)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Credits](#credits)

## General Information
Kompresi gambar (Image Compression) adalah proses untuk menyederhanakan representasi gambar tanpa menghilangkan terlalu banyak informasi penting secara visual. Program kompresi gambar dapat berguna untuk mengurangi kompleksitas data, mempercepat pemrosesan, dan menghemat ruang penyimpanan dalam konteks tertentu.

Terdapat berbagai teknik untuk melakukan kompresi gambar, seperti transformasi Discrete Cosine Transform (DCT), Singular Value Decomposition (SVD), serta Principal Component Analysis (PCA). Pada tugas ini, akan dibuat sebuah program kompresi citra menggunakan metode Principal Component Analysis (PCA), yang berfokus pada reduksi data multidimensi menjadi data dengan dimensi yang lebih kecil.

## Tampilan Program
![Main View](./src/assets/tampilan1.png)
![Main View](./src/assets/tampilan2.png)

## How To Run
1. Di src, aktifkan virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/mac
venv\Scripts\activate     # Windows
```

2. Install dependency:
```bash
pip install -r requirements.txt
```

3. Jalankan program:
```bash
python app.py
```

4. Buka link localhost yang muncul di terminal.

## Tech Stack
### Backend
- **Python 3.10+**
- **Flask**
- **NumPy**
- **OpenCV (cv2)**
- **Pillow (PIL)**
- **Werkzeug**
### Frontend
- **HTML5**
- **CSS**
- **Jinja2**

## Project Structure
```bash
/ IMAGE COMPRESSION USING PCA

│
├── doc/
│   └── README.md
│
├── src/
│   ├── __pycache__/
    ├── assets/
        └── tampilan1.png
        └── tampilan2.png
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── app.py
├── PCA.py
├── test/
├── requirements.txt
```

## Credits
- Firizqi Aditya Mulya (L0124016)
- Zendinan Okbah Hasan (L0124126)
- Muhammad Daffa Ade N.(L0124127)