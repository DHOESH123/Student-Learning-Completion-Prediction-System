import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
import joblib

model = joblib.load("student_completion_model.pkl")


# ============================
# LOAD MODEL
# ============================


# ============================
# LOAD DATA
# ============================
df = pd.read_csv("learning_ai_dataset_22000_plus.csv")

st.set_page_config(
    page_title="Student Learning Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ============================
# SIDEBAR
# ============================
st.sidebar.title("🎯 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["📊 Dashboard", "🤖 Prediction", "🧑‍🎓 Student Insights"]
)

st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ Smart Learning AI System")

# ============================
# DASHBOARD PAGE
# ============================
if page == "📊 Dashboard":
    st.title("📊 Student Learning Analytics Dashboard")

    col1, col2, col3, col4, col5 = st.columns(5)

    total_students = df["student_id"].nunique()
    completion_rate = round(df["completed"].mean() * 100, 2)
    avg_score = round(df["score"].mean(), 2)
    avg_time = round(df["time_spent"].mean(), 2)
    dropout_risk = round((1 - df["completed"].mean()) * 100, 2)

    col1.metric("👨‍🎓 Total Students", total_students)
    col2.metric("✅ Completion Rate", f"{completion_rate}%")
    col3.metric("⚠️ Dropout Risk", f"{dropout_risk}%")
    col4.metric("📚 Avg Score", avg_score)
    col5.metric("⏳ Avg Time Spent", avg_time)

    st.markdown("---")

    colA, colB = st.columns(2)

    with colA:
        pie = px.pie(
            df,
            names="completed",
            title="Completion Distribution",
            color="completed",
            labels={1: "Completed", 0: "Not Completed"}
        )
        st.plotly_chart(pie, use_container_width=True)

    with colB:
        scatter = px.scatter(
            df,
            x="time_spent",
            y="score",
            color="completed",
            title="Score vs Time Spent"
        )
        st.plotly_chart(scatter, use_container_width=True)

    st.markdown("---")

    st.subheader("📈 Chapter Wise Performance")
    chapter_chart = px.bar(
        df.groupby("chapter")["completed"].mean().reset_index(),
        x="chapter",
        y="completed",
        title="Completion Rate per Chapter"
    )
    st.plotly_chart(chapter_chart, use_container_width=True)

# ============================
# PREDICTION PAGE
# ============================
elif page == "🤖 Prediction":
    st.title("🤖 Student Completion Prediction")

    st.markdown("""
    ### 📝 Input Requirements
    The prediction model expects inputs similar to the training dataset:
    - **Student ID** (new student allowed)
    - **Course ID**
    - **Chapter Order**
    - **Time Spent**
    - **Score**

    ⚠️ *Completion status is NOT required here because this page predicts it.*
    """)

    st.markdown("Enter student learning details below:")

    col0, col1, col2, col3, col4 = st.columns(5)

    with col0:
        student_id = st.text_input("🧑‍🎓 Student ID", "S_TEST")

    with col1:
        course_id = st.text_input("📘 Course ID", "C1")

    with col2:
        chapter = st.number_input("📖 Chapter Order", 1, 20, step=1)

    with col3:
        time_spent = st.number_input("⏳ Time Spent", 0.0, 200.0, step=0.5)

    with col4:
        score = st.number_input("📚 Score", 0.0, 100.0, step=0.5)

    if st.button("Predict 🎯"):

        # Prepare input same as model expects
        # (use your exact training feature order)
        input_data = np.array([[time_spent, score, chapter]])

        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1] * 100

        st.write(f"### 🔍 Prediction Details")
        st.info(f"**Student ID:** {student_id} | **Course ID:** {course_id}")

        if prediction == 1:
            st.success(f"🎉 Student Likely to COMPLETE the course ({prob:.2f}%)")
        else:
            st.error(f"⚠️ High Risk of NOT Completing ({prob:.2f}%)")

        st.subheader("📌 Recommendation")

        if prob < 50:
            st.warning("""
            🔎 Suggested Support:
            ✔️ Provide mentor assistance  
            ✔️ Encourage more engagement  
            ✔️ Monitor learning behavior closely
            """)
        else:
            st.success("""
            🎯 Student is performing well. Keep them motivated!
            """)


# ============================
# STUDENT INSIGHTS PAGE
# ============================
else:
    st.title("🧑‍🎓 Student Insights Explorer")

    student_list = df["student_id"].unique()
    selected_student = st.selectbox("Select Student", student_list)

    student_data = df[df["student_id"] == selected_student]

    st.write(student_data)

    st.subheader("📈 Performance Trend")
    perf_chart = px.line(
        student_data,
        x="chapter",
        y="score",
        markers=True
    )
    st.plotly_chart(perf_chart, use_container_width=True)

    st.subheader("📊 Time Spent Trend")
    time_chart = px.bar(
        student_data,
        x="chapter",
        y="time_spent"
    )
    st.plotly_chart(time_chart, use_container_width=True)
