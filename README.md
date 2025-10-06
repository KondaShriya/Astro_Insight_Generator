# 🔮 Astrological Insight Generator

A simple yet extensible service that generates **personalized daily astrological insights** based on a user's birth details.  
The project combines **zodiac logic** with **LLM-based text generation** to produce natural, human-like astrological predictions.

---

## 🧩 Problem Statement

Build a service that takes a user's **name**, **date**, **time**, and **location of birth** and returns a **personalized daily astrological insight**, using a combination of **zodiac inference** and **language generation logic**.

---

## 🎯 Goals

- Parse and infer zodiac sign from input date/time.  
- Use a simplified astrological rule base or dummy logic (e.g., daily prediction per zodiac).  
- Call an LLM or pseudo-LLM to generate natural language insights (e.g.,  
  `"Today, your grounded nature will help you handle unexpected work pressure."`).  
- Make the architecture modular to easily integrate **real Panchang data** or **LLM APIs** later.

---

## 🧱 Expectations

- Clean, modular code using **Python** (or Node.js).  
- A **REST API** or **CLI tool** that:
  - Accepts user birth details as input.
  - Internally infers zodiac and generates insights.
  - Returns response in JSON or text format.  
- Includes placeholder/stub logic for:
  - Embedding or prompt generation (e.g., HuggingFace/OpenAI).  
  - Optional Hindi or multilingual support.  
- Bonus:
  - Simple caching or scoring logic for personalization.

---

## 🗂️ Project Structure


