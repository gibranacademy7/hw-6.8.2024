# hw4:

def perform_operation(word, operation):
    oper_dict = {
        "lower": lambda w: w.lower(),
        "upper": lambda w: w.upper(),
        "len": lambda w: len(w),
        "reverse": lambda w: w[::-1]
    }

# ביצוע הפעולה:
# משתמשים ב-get כדי לקבל את הפונקציה המתאימה מתוך המילון לפי שם הפעולה שהמשתמש הכניס.
# הפונקציה get מחזירה את הפונקציה מהמילון אם היא קיימת, ואם לא היא מחזירה None

    func = oper_dict.get(operation);
    if func:                    # = if func not none, then:
        return func(word);
    else:
        return "Operation not supported."

# הקוד בחלק זה מתבצע רק אם הקובץ מופעל כקובץ הראשי ולא מיובא כמודול לקובץ אחר

if __name__ == "__main__":
    word = input("Enter word: ");
    operation = input("Enter operation name (lower, upper, len, reverse): ");
    result = perform_operation(word, operation);
    print(result);
