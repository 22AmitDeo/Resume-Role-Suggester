import csv


job_skills_data = [
    {"job": "Data Scientist", "skills": "Python, Machine Learning, Statistics, Pandas, Scikit-learn, SQL"},
    {"job": "Software Engineer", "skills": "Java, C++, Data Structures, Algorithms, Git, System Design"},
    {"job": "Web Developer", "skills": "HTML, CSS, JavaScript, React, Node.js, MongoDB"},
    {"job": "DevOps Engineer", "skills": "Linux, Docker, Kubernetes, Jenkins, AWS, CI/CD"},
    {"job": "Mobile App Developer", "skills": "Flutter, Dart, Java, Kotlin, Swift, Firebase"},
    {"job": "Cloud Architect", "skills": "AWS, Azure, GCP, Cloud Security, DevOps, Terraform"},
    {"job": "Cybersecurity Analyst", "skills": "Network Security, Penetration Testing, Python, SIEM, Firewalls, Cryptography"},
    {"job": "AI/ML Engineer", "skills": "Python, TensorFlow, PyTorch, Deep Learning, NLP, Computer Vision"},
    {"job": "Business Analyst", "skills": "Excel, SQL, Tableau, Business Intelligence, Data Analysis, Communication"},
    {"job": "System Administrator", "skills": "Linux, Windows Server, Networking, Bash, PowerShell, Troubleshooting"},
    {"job": "UI/UX Designer", "skills": "Figma, Adobe XD, Wireframing, User Research, Prototyping, HTML/CSS"},
    {"job": "Product Manager", "skills": "Agile, Scrum, Roadmapping, Stakeholder Management, Market Research, JIRA"},
    {"job": "Database Administrator", "skills": "SQL, Oracle, MySQL, Backup & Recovery, Performance Tuning, DB Security"},
    {"job": "Technical Writer", "skills": "Documentation, Markdown, XML, Communication, Research, Git"},
    {"job": "Game Developer", "skills": "Unity, C#, Game Physics, 3D Modeling, Blender, Unreal Engine"}
]


file_path = "C:/Users/Amit/Desktop/Programming/DA Projects/#13 Resume Checker/Resume-Role-Suggester/job_skills.csv"

with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["skills", "job"])
    writer.writeheader()
    for entry in job_skills_data:
        writer.writerow({"skills": entry["skills"], "job": entry["job"]})

file_path
