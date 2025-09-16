# Movie-recommended-system

📌The workflow involves:
Loading preprocessed movie data (movies.pkl).
Using similarity-based algorithms (likely cosine similarity / content-based filtering) implemented in the Jupyter Notebook (movie_recommended.ipynb).
Deploying an interactive web app (app.py) that allows users to select a movie and get recommendations.


⚙️Components

**app.py**
Uses Streamlit to create a user interface.
Loads movie data from a pickle file (movies.pkl).
Displays a dropdown (selectbox) with available movie titles.
Acts as the frontend of the recommendation system.

**movie_recommended.ipynb**
Main development notebook where the recommendation model is trained.

**Handles:
Data preprocessing**
Feature extraction (movie metadata such as genre, cast, etc.)
Similarity computation (probably cosine similarity or count vectorizer)
Recommendation function definition
Serves as the backend logic builder.

**movies.pkl**
A serialized file containing the movie dataset (titles and metadata).
Loaded into both the notebook and the app for making predictions/recommendations.



🚀 Functionality
User selects a movie title from the dropdown in the Streamlit app.
The system fetches the most similar movies based on the recommendation model.
Recommended movies are displayed to the user.

📊 Key Technologies
Python
Streamlit (UI)
Pandas (data handling)
Pickle (data storage)
Machine Learning / NLP techniques (for similarity-based recommendations)
