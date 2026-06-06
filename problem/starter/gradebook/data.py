"""gradebook.data — hardcoded sample grade records.

This module exists so the rest of the package has data to work on without
needing any file I/O. In a real project this might be a database query or
an API call; here it's just a Python list of dicts.
"""

RECORDS: list[dict] = [
    {"name": "Alice",   "subject": "Math",    "score": 88},
    {"name": "Alice",   "subject": "Science", "score": 92},
    {"name": "Alice",   "subject": "English", "score": 79},
    {"name": "Bob",     "subject": "Math",    "score": 72},
    {"name": "Bob",     "subject": "Science", "score": 85},
    {"name": "Bob",     "subject": "English", "score": 90},
    {"name": "Charlie", "subject": "Math",    "score": 95},
    {"name": "Charlie", "subject": "Science", "score": 88},
    {"name": "Charlie", "subject": "English", "score": 91},
    {"name": "Diana",   "subject": "Math",    "score": 60},
    {"name": "Diana",   "subject": "Science", "score": 70},
    {"name": "Diana",   "subject": "English", "score": 65},
]
def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score."""

    scores = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        scores.setdefault(name, []).append(score)

    averages = {}

    for name, marks in scores.items():
        averages[name] = round(sum(marks) / len(marks), 2)

    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return unique subjects."""

    return {record["subject"] for record in records}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (student_name, average_score)."""

    averages = average_per_student(records)

    return max(averages.items(), key=lambda item: item[1])


def passing_students(
    records: list[dict],
    threshold: float = 60.0
) -> list[str]:
    """Return students whose average >= threshold."""

    averages = average_per_student(records)

    passed = [
        name
        for name, avg in averages.items()
        if avg >= threshold
    ]

    return sorted(passed)
