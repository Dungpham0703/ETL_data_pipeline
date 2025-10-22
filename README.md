# 🧩 Hugging Face ETL Pipeline

A simple **ETL (Extract, Transform, Load)** pipeline that demonstrates how to extract data from the **Hugging Face Datasets Hub**, transform it using **pandas**, and load it into a **PostgreSQL** database.

---

## 🚀 Overview

This project shows the fundamentals of data engineering by automating three core stages:

1. **Extract** – Download data from the [Hugging Face Datasets](https://huggingface.co/datasets) (e.g., MovieLens, IMDB, etc.).  
2. **Transform** – Clean and reshape the dataset with **pandas** for structured analysis.  
3. **Load** – Store the transformed dataset into a **PostgreSQL** database table.

---

## 📂 Project Structure
```bash
etl-huggingface/
│
├── src/
│ ├── extract.py # Extract dataset from Hugging Face
│ ├── transform.py # Clean and transform data using pandas
│ ├── load.py # Load final dataframe into PostgreSQL
│ ├── config.py # Environment configuration (Postgres URL, etc.)
│ └── main.py # Entry point to run the full ETL pipeline
│
├── .env # Environment variables (DATABASE_URL)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---
## ⚙️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/etl-huggingface.git
cd etl-huggingface
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Setup environment variables
```bash
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/mydatabase
```
## ▶️ Run the ETL Pipeline
```bash
python -m src.main
```
Expected output:
```bash
Starting ETL Pipeline...
Extracted 100000 rows from Hugging Face
Transformed dataframe with 4 columns
Loaded data into 'movie_ratings' table
ETL Pipeline completed successfully!
```
