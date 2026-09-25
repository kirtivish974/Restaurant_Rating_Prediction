# 🍽️ Restaurant Rating Predictor

An end-to-end Machine Learning project that predicts a restaurant's **aggregate rating** based on features like price range, votes, cuisine, location, and available services.

Built as part of the **Data Science Internship at Cognifyz Technologies**.

---

## 🔗 Live Demo

**[Try the app →](https://restaurantratingprediction-cajzw7ynk6992rshfwk7rw.streamlit.app/)**

---

## 📌 Project Overview

Restaurant ratings are influenced by a mix of price, popularity, cuisine type, and location. This project:

- Explores and cleans a dataset of **9,551 restaurants** across multiple countries.
- Performs **feature engineering** (cuisine grouping, service flags, geo-coordinates, cuisine count).
- Trains and compares **three regression models** to predict the aggregate rating.
- Deploys the best model as an interactive **Streamlit web app**.

---

## 📊 Dataset

- **Rows:** 9,551
- **Columns:** 21
- **Key features:** Country Code, City, Cuisines, Average Cost for two, Price range, Has Table booking, Has Online delivery, Aggregate rating, Votes, Longitude, Latitude
- **Target variable:** `Aggregate rating`

Rows with `Aggregate rating = 0.0` (unrated restaurants) were removed, leaving **7,394 records** for modeling.

---

## 🔍 Key Insights

| Insight | Detail |
|---|---|
| **Price ↔ Rating** | Clear positive correlation. Higher price ranges consistently average higher ratings. |
| **Table Booking** | Restaurants offering table booking average **+0.17** higher ratings. |
| **Online Delivery** | Restaurants offering delivery average **-0.08** lower ratings (counterintuitive but real). |
| **Top Cuisines** | Italian, Cafe, and Bakery/Dessert cuisines score highest on average. |
| **Location** | Weak correlation with rating (Longitude: -0.29, Latitude: -0.18). |
| **Top Feature** | `Votes` is the strongest predictor by far (feature importance ≈ 0.51). |

---

## 🧠 Model Building

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression | 0.4393 | 0.3389 | 0.3766 |
| Decision Tree | 0.4984 | 0.3581 | 0.1977 |
| **Random Forest** ✅ | **0.3587** | **0.2580** | **0.5843** |

**Final model:** Random Forest Regressor (`n_estimators=100`, `random_state=42`)

**Why R² ≈ 0.58 is a good result:** Ratings also depend on food quality, service, ambiance, and reviewer bias — factors not present in the dataset. Anything above 0.85 would indicate data leakage.

### Top 10 Predictive Features
1. Votes
2. Longitude
3. Latitude
4. Average Cost for two
5. Country Code
6. Cuisine Count
7. Price range
8. Cuisine Group (Other)
9. Has Online delivery (No)
10. Has Online delivery (Yes)

---

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Data:** pandas, NumPy
- **ML:** scikit-learn
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Web App:** Streamlit
- **Model Persistence:** pickle

---

## 📁 Repository Structure

Restaurant_Rating_Prediction/
├── app.py # Streamlit app
├── requirements.txt # Python dependencies
├── rf_model.pkl # Trained Random Forest model + feature columns
└── README.md # This file


---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/kirtivish974/Restaurant_Rating_Prediction.git
cd Restaurant_Rating_Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```
The app opens at http://localhost:8501.

## 🎯 How the App Works
Enter the following details in the sidebar:

Price range (1–4)

Average Cost for two

Votes

Country Code

Number of cuisines

Has Table booking (Yes/No)

Has Online delivery (Yes/No)

Longitude / Latitude

Click Predict Rating → the app returns a predicted rating between 0.0 and 5.0.

---

## 📌 Future Improvements
Add cuisine selection as a dropdown (instead of just a count).

Include a City-based feature using geocoding.

Try gradient boosting (XGBoost / LightGBM) for a small R² lift.

Add SHAP values for per-prediction explainability.

---

## 👤 Author
Kirti Vishwakarma
Data Science Intern — Cognifyz Technologies

GitHub: @kirtivish974

LinkedIn: linkedin.com/in/kirti-vishwakarma1

---

## 🙏 Acknowledgements
Thanks to Cognifyz Technologies for the internship opportunity and dataset.

⭐ If you found this project useful, consider starring the repo.

text

---

## Push it

```bash
git add README.md
git commit -m "Add project README"
git push
```
