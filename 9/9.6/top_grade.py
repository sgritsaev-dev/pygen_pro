def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    grades['top_grade'] = max(grades['grades'])
    grades.pop('grades')
    return grades


print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

print(*top_grade.__annotations__.values())
