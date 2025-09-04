# MINDSIGHT_AI
(Mental health emotion &amp; sentiment analysis using AI)
🧠 MindSight AI v7.0
A scratch-built NLP project to analyze emotional and mental health sentiment from raw text. Designed to align with SDG 3: Good Health and Well-being.

🚀 Overview
MindSight AI v7.0 is an AI system that analyzes mental health signals using Natural Language Processing. Unlike typical emotion models, this system is built entirely from scratch — without using pre-trained models or APIs — ensuring full transparency and academic integrity.

🎯 Objectives
Detect emotional and mental states (e.g., happy, sad, angry) from user-written text.

Enable early emotional pattern detection using AI.

Address SDG 3 – Good Health and Well-being.

🧰 Technologies Used
Tool	Purpose
Python	Core programming language
Pandas	Data handling
Regex	Text cleaning
Sklearn	TF-IDF vectorizer, model, metrics
Matplotlib/Seaborn	Visualization

📂 Folder Structure
MINDSIGHT_AI/
├── data/
│   └── emotion_dataset.csv
├── utils/
│   └── preprocess.py
├── MindSight_AI_.ipynb
├── README.md
└── requirements.txt
🔄 How It Works
Input: Raw user text (e.g., journal, social post)

Clean: Text is lowercased, stripped of symbols

Vectorize: TF-IDF converts it to machine-readable form

Predict: A Logistic Regression model classifies the emotion

Output: Emotion label (e.g., joy, sadness, fear)

📊 Model Performance
Model: Logistic Regression

Accuracy: ~93% on balanced test set

Precision/Recall/F1 per emotion class included in report

🧪 Dataset
Format: CSV (2 columns: Text, Emotion)

Sample size: ~10–15 entries (for demonstration; scalable)

Labels used: joy, sadness, anger, etc.

📝 How to Run
Clone the repo

Ensure Python 3.10+ is installed

Install requirements:
pip install -r requirements.txt
Run the notebook:

jupyter notebook notebooks/mindsight_ai_final.ipynb
📚 SDG Alignment
SDG 3: Good Health and Well-being
MindSight AI promotes mental well-being through early emotion signal detection.

🙌 Team & Credits
👤 Developer: Manveet (Solo Developer, Scratch Built)

🏆 Built for: [INTEL BOOT CAMP]

📅 Date: June 2025

📌 Notes
Entire model and logic built from scratch (no API or pretrained help)

Ready for extension to full-scale apps or web interfaces

Visualizations, evaluation, and ethical alignment included
