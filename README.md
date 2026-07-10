# 🎬 CineMatch — Movie Recommendation System

An easy-to-run content-based movie recommendation demo built with Python and Streamlit. The project includes data, a training notebook, and a small Streamlit app that uses a precomputed similarity matrix to recommend movies and fetch posters from TMDB.

---

## Quick overview
- Project: content-based movie recommender using genres, keywords, cast, and crew metadata.
- Includes: `app.py`, model notebook, and the TMDB CSV datasets included in the repo.

---

## Features
- Content-based recommendations using text-derived tags
- Precomputed similarity for fast responses in the UI
- Poster fetching via TMDB API (optional)
- Notebook for preprocessing and model building: `content_based_recomended_system.ipynb`

---

## Prerequisites
- Python 3.8 or newer
- Recommended packages: `streamlit`, `pandas`, `numpy`, `scikit-learn`, `requests`

There is no `requirements.txt` in the repo; install the packages below or create one from the list above.

---

## Local setup (Windows)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Install dependencies:

```powershell
pip install streamlit pandas numpy scikit-learn requests
```

3. Run the app:

```powershell
streamlit run app.py
```

Open the URL printed by Streamlit (usually http://localhost:8501).

---

## Files of interest
- `app.py` — Streamlit frontend and recommendation UI
- `content_based_recomended_system.ipynb` — preprocessing and model notebook
- `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv.zip` — dataset files included

---

## How it works (brief)
1. Build a combined "tag" per movie from genres, keywords, cast, and crew.
2. Vectorize tags (CountVectorizer / TF-IDF) to produce movie vectors.
3. Compute cosine similarity between movie vectors and store a similarity matrix.
4. When a user selects a movie, return top-N similar movies and fetch posters via TMDB if needed.

---

## TMDB API (optional)
To display posters, set your TMDB API key as an environment variable or insert it in the app where indicated:

```powershell
setx TMDB_API_KEY "your_api_key_here"
```

Restart your shell after setting the variable so Streamlit can pick it up.

---

## Notes & next steps
- Consider adding a `requirements.txt` or `pyproject.toml` for reproducible installs.
- Add unit tests or a simple smoke test to validate the app runs.
- Optionally expand to a hybrid model (add collaborative filtering) or deploy to Streamlit Cloud.

---

## Contributing
Contributions welcome. Fork, create a feature branch, and submit a pull request. Please include a short description of changes and any setup notes.

---

## License
This repo does not include a license file. Add a `LICENSE` if you plan to open-source this project.

---

If you'd like, I can also generate a `requirements.txt`, add a `LICENSE`, or create a short `run` script to simplify starting the app.
