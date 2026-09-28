
from recommendations import generate_recommendations
import streamlit as st
from PyPDF2 import PdfReader
from matcher import calculate_similarity
from skills import extract_skills

st.title("🤖 AI Resume & Job Matcher")

st.write(
    "Upload your resume and compare it with a job description"
)

# Resume upload
uploaded_file = st.file_uploader(
    "📄 Upload your Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        resume_text += page.extract_text() or ""

    st.success("Resume uploaded successfully!")


# Job description
job_description = st.text_area(
    "💼 Paste the Job Description",
    height=300,
    placeholder="Paste the internship or job description here..."
)


# Analyze button
if st.button("🔍 Analyze Resume"):

    if not resume_text.strip():
        st.warning("Please upload a readable PDF resume.")

    elif not job_description.strip():
        st.warning("Please paste a job description.")

    else:
        with st.spinner("Analyzing your resume..."):

            # 1. Calculate AI similarity score
            score = calculate_similarity(
                resume_text,
                job_description
            )

            # 2. Extract skills
            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_description)

            # 3. Find matching and missing skills
            matching_skills = [
                skill for skill in job_skills
                if skill in resume_skills
            ]

            missing_skills = [
                skill for skill in job_skills
                if skill not in resume_skills
            ]

            # 4. Generate recommendations
            recommendations = generate_recommendations(
                matching_skills,
                missing_skills,
                score
            )

        st.success("Analysis complete!")

        # AI match score
        st.subheader("🤖 AI Match Score")

        st.metric(
            "Resume ↔ Job Match",
            f"{score:.1f}%"
        )

        if score >= 80:
            st.success("Excellent match!")

        elif score >= 60:
            st.info(
                "Good match, but there's room for improvement."
            )

        elif score >= 40:
            st.warning("Moderate match.")

        else:
            st.error(
                "Low match. Consider improving your resume."
            )

        # Skills analysis
        st.subheader("🔎 Skills Analysis")

        st.write("### Matching Skills")

        if matching_skills:
            st.write(", ".join(matching_skills))
        else:
            st.info("No matching skills found.")

        st.write("### Missing Skills")

        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.success("🎉 No major skills missing!")

        # Required skills match
        if job_skills:
            skill_percentage = (
                len(matching_skills) / len(job_skills)
            ) * 100

            st.metric(
                "Required Skills Match",
                f"{skill_percentage:.1f}%"
            )

        else:
            st.info(
                "No skills from the current skill list "
                "were detected in this job description."
            )

        # Skills dashboard
        st.subheader("📊 Skills Dashboard")

        if job_skills:
            chart_data = {
                "Matching Skills": len(matching_skills),
                "Missing Skills": len(missing_skills)
            }

            st.bar_chart(chart_data)

            st.progress(skill_percentage / 100)

            st.write(
                f"You match {skill_percentage:.1f}% "
                "of the recognized job skills."
            )

        # Personalized recommendations
        st.subheader(
            "💡 Resume Improvement Recommendations"
        )

        if recommendations:
            for number, recommendation in enumerate(
                recommendations,
                start=1
            ):
                st.write(f"{number}. {recommendation}")

        else:
            st.info("No recommendations available.")

        # Resume preview
        st.subheader("📄 Resume Preview")
        st.write(resume_text[:2000])

        # Job description preview
        st.subheader("💼 Job Description")
        st.write(job_description[:2000])