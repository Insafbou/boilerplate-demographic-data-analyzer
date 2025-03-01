import pandas as pd

def calculate_demographic_data(print_data=True):
    # قراءة البيانات
    df = pd.read_csv("adult.data.csv")
    
    # عدد الأشخاص من كل عرق
    race_count = df["race"].value_counts()
    
    # متوسط عمر الرجال
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    
    # نسبة الحاصلين على شهادة البكالوريوس
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)
    
    # نسبة الذين يكسبون أكثر من 50K حسب مستوى التعليم
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round((df[advanced_education & (df["salary"] == ">50K")].shape[0] / df[advanced_education].shape[0]) * 100, 1)
    lower_education_rich = round((df[~advanced_education & (df["salary"] == ">50K")].shape[0] / df[~advanced_education].shape[0]) * 100, 1)
    
    # الحد الأدنى لعدد ساعات العمل أسبوعيًا
    min_work_hours = df["hours-per-week"].min()
    
    # نسبة من يعملون الحد الأدنى من الساعات ويكسبون أكثر من 50K
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers[min_workers["salary"] == ">50K"].shape[0] / min_workers.shape[0]) * 100, 1)
    
    # الدولة ذات أعلى نسبة من الأشخاص الذين يكسبون أكثر من 50K
    countries_rich = df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts() * 100
    highest_earning_country = countries_rich.idxmax()
    highest_earning_country_percentage = round(countries_rich.max(), 1)
    
    # أكثر وظيفة شيوعًا في الهند للأشخاص الذين يكسبون أكثر من 50K
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].mode()[0]
    
    # طباعة النتائج إذا طُلب ذلك
    if print_data:
        print("Number of each race:", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
