import re


# =====================================================
# TECHNICAL SKILLS DATABASE
# =====================================================

SKILLS = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "go",
    "rust",
    "swift",
    "kotlin",
    "scala",
    "r",

    # Frontend
    "html",
    "css",
    "bootstrap",
    "tailwind css",
    "sass",
    "react",
    "angular",
    "vue",
    "next.js",
    "jquery",

    # Backend
    "django",
    "flask",
    "fastapi",
    "spring",
    "spring boot",
    "hibernate",
    "node.js",
    "express",
    "laravel",
    "asp.net",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "oracle",
    "sqlite",
    "mongodb",
    "redis",
    "firebase",

    # Version Control
    "git",
    "github",
    "gitlab",
    "bitbucket",

    # DevOps & Cloud
    "docker",
    "kubernetes",
    "jenkins",
    "terraform",
    "ansible",
    "aws",
    "azure",
    "gcp",

    # AI / Machine Learning
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "computer vision",
    "natural language processing",
    "nlp",

    # Data Science
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "scipy",

    # Data Analytics
    "power bi",
    "tableau",
    "excel",

    # Mobile Development
    "android",
    "flutter",
    "react native",
    "xamarin",

    # Testing
    "selenium",
    "pytest",
    "junit",
    "postman",

    # Cyber Security
    "cyber security",
    "penetration testing",
    "ethical hacking",
    "network security",
    "owasp",

    # CS Fundamentals
    "data structures",
    "algorithms",
    "operating systems",
    "computer networks",
    "dbms",
    "oops",

    # APIs
    "rest api",
    "graphql",
]


# =====================================================
# SKILL EXTRACTION
# =====================================================

def extract_skills(text):
    """
    Extract technical skills from resume text
    or job description using regular expressions.
    """

    if not text:
        return []

    # Convert text to lowercase
    clean_text = text.lower()

    found_skills = set()

    for skill in SKILLS:

        skill_lower = skill.lower()

        # Special handling for single-letter programming languages
        # Prevents matching 'c' inside words like 'computer'
        # Prevents matching 'r' inside words like 'developer'
        if skill_lower in ["c", "r"]:
            pattern = (
                rf"(?<![a-zA-Z0-9])"
                rf"{re.escape(skill_lower)}"
                rf"(?![a-zA-Z0-9])"
            )
        else:
            pattern = rf"\b{re.escape(skill_lower)}\b"

        if re.search(pattern, clean_text):
            found_skills.add(skill)

    return sorted(found_skills)