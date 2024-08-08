# hw3: כתוב פונקציה המקבלת רשימת מספרים ומחזירה מילון עם סטטיסטיקות של
# ממוצע הרשימה, מקסימום, מינימום, מספר האיברים, סכום האיברים 

def get_statistics (numbers: list[int]) -> dict:
    if not numbers:
        return {
            "sum": 0,
            "average": 0,
            "max": None,
            "min": None,
            "len": 0,
        }

    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "len": len(numbers),
    }

numbers = [1, 2, 3, 4, 5, 6]
statist = get_statistics(numbers);
print(statist)