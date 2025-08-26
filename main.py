import pandas as pd
import numpy as np

def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)
    
    # What percentage of people with advanced education make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    # Define advanced education
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    
    # Filter for people with advanced education
    higher_education = df[df['education'].isin(advanced_education)]
    
    # Filter for people without advanced education
    lower_education = df[~df['education'].isin(advanced_education)]
    
    # Percentage with salary >50K for higher education
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1
    )
    
    # Percentage with salary >50K for lower education
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1
    )
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1
    )
    
    # What country has the highest percentage of people that earn >50K?
    # and what is that percentage?
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').sum() / len(x) * 100
    ).round(1)
    
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max()
    
    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()
    
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

# Call the function to calculate results
demographic_data = calculate_demographic_data()

# Print all results
print("Number of each race:\n", demographic_data['race_count'])
print("Average age of men:", demographic_data['average_age_men'])
print(f"Percentage with Bachelors degrees: {demographic_data['percentage_bachelors']}%")
print(f"Percentage with higher education that earn >50K: {demographic_data['higher_education_rich']}%")
print(f"Percentage without higher education that earn >50K: {demographic_data['lower_education_rich']}%")
print(f"Min work time: {demographic_data['min_work_hours']} hours/week")
print(f"Percentage of rich among those who work fewest hours: {demographic_data['rich_percentage']}%")
print("Country with highest percentage of rich:", demographic_data['highest_earning_country'])
print(f"Highest percentage of rich people in country: {demographic_data['highest_earning_country_percentage']}%")
print("Top occupations in India:", demographic_data['top_IN_occupation'])
