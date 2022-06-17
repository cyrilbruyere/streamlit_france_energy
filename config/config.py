"""
Config file for Streamlit App
"""

from config.member import Member

TITLE = "L'Energie en France"

TEAM_MEMBERS = [
    Member(
        name="David Beauvais",
        linkedin_url="https://www.linkedin.com/in/david-be04/",
        github_url="https://github.com/davidbeauvais",
    ),
    Member(
        name="Jean-Yves Bernard",
        linkedin_url="https://www.linkedin.com/in/jean-yves-bernard-56aa402/",
        github_url="https://github.com/jeanyvesbernard",
    ),
    Member(
        name="Cyril Bruyère",
        linkedin_url="https://www.linkedin.com/in/cyrilbruyere/",
        github_url="https://github.com/cyrilbruyere",
    )
]

PROMOTION = "Promotion continue Data Scientist - Octobre 2021"
