import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors degree
    total_people = len(df)
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / total_people) * 100, 1)

    # 4. Percentage with higher education that earn >50K
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K']
    higher_education_rich = round((len(higher_edu_rich) / len(higher_edu)) * 100, 1)

    # 5. Percentage without higher education that earn >50K
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K']
    lower_education_rich = round((len(lower_edu_rich) / len(lower_edu)) * 100, 1)

    # 6. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((len(rich_min_workers) / len(min_workers)) * 100, 1)

    # 8. Country with highest percentage of rich people
    country_stats = df.groupby('native-country')
    country_percentage = country_stats.apply(
        lambda x: (x['salary'] == '>50K').mean() * 100
    )

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 9. Most popular occupation in India for those earning >50K
    india_rich = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
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
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }