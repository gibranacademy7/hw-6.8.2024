# hw1:  מילון עבור מדינת ישראל
israel = {'name': 'Israel',
    'birth': 1948,
    'population_millions': 9.3,
    'capital': 'Jerusalem',
    'language': 'Hebrew',
    'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
    'currency': 'ILS',
    'area_Kilometer': 22.145,
    'gdp_billion': 450
}

# hw1a:  מצא והדפס את עיר הבירה
capital_city = israel.get('capital');
print(f"Capital City of Israel is: {capital_city}");

# hw1b: הדפס את כל המפתחות
keys = israel.keys();
print(f"Keys are: {keys}");

# hw1c: צור רשימה המכילה רק את המפתחות באותיות גדולות
keys_uppercase = [key.upper() for key in keys];
print(f"Keys in uppercase are: {keys_uppercase}");

# hw1d: הדפס את כל הערכים
All_values = israel.values();
print(f"All Values are: {All_values}");

# hw1e: values -צור רשימה המכילה רק את אורכי ה
values_lengths = [len(str(value)) for value in All_values];
print(f"Lengths of values: {values_lengths}");

# hw1f: הדפס את כל זוגות הערכים
All_items = israel.items();
print(f"Items: {All_items}");

# hw1g: העתק את המילון שעשית למילון חדש
israel_copy = israel.copy();
print(f"Copied dictionary of israel = {israel_copy}");

# hw1h: נקה את המילון החדש מערכים
israel_copy.clear();
print(f"Cleared dictionary of israel = {israel_copy}");
#--------------

# hw1i: (None) צור מילון חדש עם אותם המפתחות אבל הערכים יהיו
israel_new_none = dict.fromkeys(israel.keys(), None);
                        # פונקציה זו (fromkeys) יוצרת מילון חדש
                        # הפונקציה מקבלת שני פרמטרים:
         #         רשימת המפתחות למילון החדש
         #   ערך ברירת המחדל שיינתן לכל מפתח
print(f"Dictionary with None values: {israel_new_none}");
#-------------

# hw1j: (currency)  מחק את המפתח (והערך) של
del israel['currency'];
print(f"Dictionary after deleting 'currency' = {israel}");

# hw1k: Kilometer_area משוך ומחק את המפתח (והערך) של
area_Kilometer = israel.pop('area_Kilometer');
print(f"Dictionary after popping 'area_Kilometer': {israel}")
print(f"Popped value: {area_Kilometer}");

# hw1l: update :בפעולה אחת, רמז
# 1.'Soccer ':' sport_national' הוסף מפתח וערך חדש
# 2. 'population_millions': 9.4  עדכן מפתח
israel.update({'Soccer': 'sport_national', 'population_millions': 9.4});
print(f"Updated dictionary of israel: {israel}");


