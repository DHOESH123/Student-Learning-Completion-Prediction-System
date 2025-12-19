# 🎓 Student Learning Completion Prediction System

An AI-powered system that predicts whether a student will **COMPLETE** or **NOT COMPLETE** a course based on learning behavior patterns such as time spent, score performance, and learning progression.

The system provides:
✔️ Interactive Analytics Dashboard  
✔️ Student Insights & Trends  
✔️ AI Completion Prediction  
✔️ Risk Classification with Recommendations  
✔️ Streamlit UI with Dark Mode  

---

## 🚀 Features
- 📊 Dashboard showing overall learning statistics
- 🤖 Student completion prediction with probability
- 🧑‍🎓 Student insights explorer
- 📈 Interactive charts using Plotly
- 🎨 Modern UI with Dark Theme
- 💾 Supports uploading new student data

---

## 🧾 Input Features
The model takes the following **5 input features** for prediction:

- 🧑‍🎓 **Student ID**  
  Unique identifier for the student (supports new unseen students)

- 📘 **Course ID**  
  Identifies the course the student belongs to

- 📖 **Chapter Order**  
  Indicates the current chapter / learning stage

- ⏳ **Time Spent**  
  Amount of learning time engaged

- 📚 **Score**  
  Assessment or performance score

> ⚠️ Note:
> - **Completion Status is NOT provided by the user**
> - The system PREDICTS whether the student will complete or not

---

## 🧠 Model
The system uses a Machine Learning model trained on historical learning dataset.

✔️ Random Forest Classifier  
✔️ Student-level aggregated training  
✔️ Feature engineering applied:
- Score per time
- Engagement rate
- Performance efficiency

---

## 📂 Project Structure
