# hw7:

#     1: פילטור רשימה רק של מדינות עם יותר מ-30 מיליון תושבים:
countries = [
    {'name': 'Israel', 'population': 9.3, 'birth': 1948},
    {'name': 'United States', 'population': 331.9, 'birth': 1776},
    {'name': 'Japan', 'population': 125.8, 'birth': 660},
    {'name': 'Australia', 'population': 25.7, 'birth': 1901},
    {'name': 'Canada', 'population': 38.0, 'birth': 1867}
]

large_popul_countries = list(filter(lambda country: country['population'] > 30, countries));
print(large_popul_countries);

# 2. פילטור רשימה רק של מדינות שהוקמו אחרי שנת 1800:
recent_countries = list(filter(lambda country: country['birth'] > 1800, countries));
print(recent_countries);

# 3. יצירת רשימה רק של שמות המדינות:
country_names = list(map(lambda country: country['name'], countries));
print(country_names);

# 4.יצירת רשימה רק של שנות ההקמה של המדינות:
country_birth_years = list(map(lambda country: country['birth'], countries));
print(country_birth_years);

# 5.מיון הרשימה לפי שנות ההקמה:
sorted_by_birth = sorted(countries, key=lambda country: country['birth']);
print(sorted_by_birth);

# 6. מיון הרשימה לפי מספר התושבים:
sorted_by_population = sorted(countries, key=lambda country: country['population']);
print(sorted_by_population);

# 7. 




