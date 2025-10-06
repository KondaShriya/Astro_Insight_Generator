# Astrological Insight Generator

A simple yet extensible service that generates **personalized daily astrological insights** based on a user's birth details.  
The project combines **zodiac logic** with **LLM-based text generation** to produce natural, human-like astrological predictions.

## Project Structure
├── main.py # Entry point of the app (FastAPI / Flask)
├── utils.py # Zodiac inference logic
├── llm_stub.py # Mock LLM or text generation module
├── translator.py # Dummy translation (Hindi / multilingual support)
├── cache.py # Optional caching logic
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/KondaShriya/Astro_Insight_Generator.git
cd Astro_Insight_Generator
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install fastapi uvicorn pydantic scikit-learn numpy python-dateutil
```
### 4. How to Run
```bash
python main.py
```
While the terminal is running, open - [http://localhost:8000/docs] , by clicking "Try it out" section under predict you check for output by giving the input in JSON.

### Sample input
```bash
{
  "name": "Shriya",
  "birth_date": "2002-09-29",
  "birth_time": "14:30",
  "birth_place": "Nizamabad, India"
}
```
### Sample Output
```bash
{
  "cached": false,
  "zodiac": "Libra",
  "insight": "Seek balance today, Shriya. A small compromise at work can open a door socially. Be kind to yourself today.",
  "language": "en",
  "score": 0.6,
  "generated_at": "2025-10-06T15:11:10.883609Z",
  "retrieved_context": [
    [
      "relationships",
      "Honest talk clears tension.",
      0
    ]
  ]
}
```
