# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that recommends similar movies using **Content-Based Filtering** and **Cosine Similarity**. The application is built with **Python**, **Streamlit**, **Pandas**, and **Scikit-learn** to provide a fast and interactive movie recommendation experience.

---

## 📌 Features

- 🎥 Recommend similar movies instantly
- 🔍 Search movies by title
- 🤖 Content-Based Recommendation System
- 📊 Cosine Similarity for finding similar movies
- 🌐 Interactive Streamlit Web Interface
- ⚡ Fast prediction using pre-trained model

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```
Movie-recommended-system/
│
├── app.py
├── model.pkl
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── assets/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/ChiragVyas15/Movie-recommended-system.git
cd Movie-recommended-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📖 How It Works

1. User selects a movie.
2. The system converts movie information into feature vectors.
3. Cosine Similarity is calculated between movies.
4. The top similar movies are retrieved.
5. Recommended movie titles (and posters if available) are displayed.

---

## 📊 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Feature Engineering
- Text Vectorization
- Cosine Similarity Matrix
- Recommendation Generation
- Streamlit Deployment

---

## 📷 Demo

Add screenshots of your application here.

```
images/home.png
images/result.png
```

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

Typical libraries include:

- streamlit
- pandas
- numpy
- scikit-learn
- pickle

---

## 📈 Future Improvements

- User Authentication
- Hybrid Recommendation System
- Collaborative Filtering
- Deep Learning Recommendation Model
- TMDB API Integration
- Movie Posters & Trailers
- User Ratings and Reviews

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Chirag Vyas**

- GitHub: https://github.com/ChiragVyas15
- LinkedIn: *(Add your LinkedIn profile here)*

---

⭐ If you found this project useful, don't forget to **Star** the repository!
