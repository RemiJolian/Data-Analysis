import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('boilerplate-demographic-data-analyzer/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['fnlwgt'].sum()

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    total_bachelors = df[df['education'] == 'Bachelors']['fnlwgt'].sum()
    total_population = df['fnlwgt'].sum()
    percentage_bachelors = (total_bachelors/total_population) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
   
    
    filtered_df = df[
        ((df['education'] == 'Bachelor') |
        (df['education'] == 'Master') |
        (df['education'] == 'Doctorate')) & 
        (df['salary'] == '>50K')
    ]
    advance_edu_people = filtered_df['fnlwgt'].sum()
    total_population = df['fnlwgt'].sum()

    higher_edu_pop = df[
        ((df['education'] == 'Bachelor') |
        (df['education'] == 'Master') |
        (df['education'] == 'Doctorate'))
    ]['fnlgwt'].sum()
    
    total_pop = df['fnlwgt'].sum()

    lower_edu_pop = total_pop - higher_edu_pop

    # percentage with salary >50K
    higher_edu_pop = (advance_edu_people / higher_edu_pop) * 100
    lower_edu_pop = 100 - higher_edu_pop

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['salary'] == '>50K']['hours-per-week'].min()

    rich_percentage = (num_min_workers/total_population) * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_edu_pop}%")
        print(f"Percentage without higher education that earn >50K: {lower_edu_pop}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_edu_pop': higher_edu_pop,
        'lower_edu_pop': lower_edu_pop,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
