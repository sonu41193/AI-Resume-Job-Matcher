def generate_recommendations(matching_skills, missing_skills, score):

    recommendations = []

    if matching_skills:
        recommendations.append(
            "Highlight your relevant skills: "
            + ", ".join(matching_skills)
            + ". Include specific projects or experiences "
            "that demonstrate them."
        )

    if missing_skills:
        recommendations.append(
            "Consider learning or developing projects involving: "
            + ", ".join(missing_skills[:5])
            + "."
        )

    if score < 60:
        recommendations.append(
            "Review the job requirements and highlight your "
            "most relevant coursework, projects, and experiences."
        )

        recommendations.append(
            "Use clear, specific descriptions of your actual "
            "achievements. Do not add skills or experiences "
            "you do not have."
        )

    return recommendations