import pandas as pd
import numpy as np


def preprocess_hr_data(hr: pd.DataFrame) -> pd.DataFrame:
    hr["cele_jmeno"] = hr["First Name"] + " " + hr["Last Name"]

    hr['lokace'] = np.where(hr['State'] == 'New York', 'HQ', 'Branch')
    hr['lokace'] = hr['lokace'].astype('category')

    hr['Termdate'] = pd.to_datetime(hr['Termdate'], format="%d/%m/%Y", errors='coerce')
    hr['Hiredate'] = pd.to_datetime(hr['Hiredate'], format="%d/%m/%Y", errors='coerce')
    hr['Birthdate'] = pd.to_datetime(hr['Birthdate'], format="%d/%m/%Y")

    hr['skoncil'] = np.where(hr['Termdate'].isna(), 'ne', 'ano')
    hr['skoncil'] = hr['skoncil'].astype('category')

    hr['Termyear'] = hr['Termdate'].dt.year
    hr['Termdate2'] = hr['Termdate'].dt.strftime('%m/%d/%Y')
    hr['Hireyear'] = hr['Hiredate'].dt.year
    hr['Hiredate2'] = hr['Hiredate'].dt.strftime('%m/%d/%Y')

    today = pd.to_datetime('today')
    hr['Age'] = (today - hr['Birthdate']).dt.days // 365
    hr['Age'] = pd.to_numeric(hr['Age'], downcast='integer')

    bins = [0, 24, 34, 44, 54, float('inf')]
    labels = ['<25', '25-34', '35-44', '45-54', '54+']
    hr['Age_bins'] = pd.cut(hr['Age'], bins=bins, labels=labels, right=True, include_lowest=True)
    hr['Age_bins'] = hr['Age_bins'].astype('category')

    hr['Enddate'] = hr['Termdate'].fillna(today)
    hr['delka_prac_pomeru'] = ((hr['Enddate'] - hr['Hiredate']).dt.days / 365.25).astype(int)
    hr['delka_prac_pomeru_text'] = hr['delka_prac_pomeru'].astype(str) + ' years'
    hr.drop(columns=['Enddate'], inplace=True)

    hr['Salary'] = pd.to_numeric(hr['Salary'], downcast='float')
    hr['Salary2'] = hr['Salary'].map("${:,.0f}".format)

    hr['delka_prac_pomeru'] = pd.to_numeric(hr['delka_prac_pomeru'], downcast='integer')

    return hr


def generate_personal_info(hr: pd.DataFrame) -> pd.Series:
    """
    Generates HTML for personal information, including name, age, and education level.

    Parameters:
    hr (pd.DataFrame): HR DataFrame containing employee data.

    Returns:
    pd.Series: A series containing HTML representations of personal information.
    """
    female_symbol = '<span style="color:#03c4a1; font-size:38px; font-weight:bold; vertical-align: middle;">&#9792;</span>'
    male_symbol = '<span style="color:#03c4a1; font-size:38px; font-weight:bold; vertical-align: middle;">&#9794;</span>'

    gender_symbol = hr['Gender'].map({'Female': female_symbol, 'Male': male_symbol})
    name_block = '<div style="font-weight:bold; margin-left: 1px;">' + hr['cele_jmeno'] + '</div>'
    age_education_block = ('<div style="margin-left: 1px; color:grey;">' + hr['Age'].astype(str) + ' | ' + hr['Education Level'] + '</div>')

    info = ('<div style="display:flex; align-items:center;">' + gender_symbol + '<div>' + name_block + age_education_block + '</div></div>')

    return info


def generate_job_info(hr: pd.DataFrame) -> pd.Series:
    job_title_block = ('<div style="font-weight:bold; margin-left: 1px;">' + hr['Job Title'] + '</div>')
    department_block = ('<div style="margin-left: 1px; color:grey;">' + hr['Department'] + '</div>')

    info = ('<div style="display:flex; align-items:center;"><div>' + job_title_block + department_block + '</div></div>')

    return info


def generate_location_info(hr: pd.DataFrame) -> pd.Series:
    HQ_symbol = '<span style="color:#03c4a1; font-size:14px; vertical-align: middle;">&#11044;</span>'
    branch_symbol = '<span style="color:grey; font-size:14px; vertical-align: middle;">&#11044;</span>'
    location_symbol = hr['lokace'].map({'HQ': HQ_symbol}).fillna(branch_symbol)

    city_block = ('<div style="font-weight:bold; margin-left: 1px;">' + hr['City'] + '</div>')
    state_block = ('<div style="margin-left: 1px; color:grey;">' + hr['State'] + '</div>')

    info = ('<div style="display:flex; align-items:center;">' + location_symbol + '<div>' + city_block + state_block + '</div></div>')

    return info


def generate_employment_status(hr: pd.DataFrame) -> pd.Series:
    status_symbol_ne = '<span style="color:#03c4a1; font-size:14px; vertical-align: middle;">&#11044;</span>'
    status_symbol_else = '<span style="color:purple; font-size:14px; vertical-align: middle;">&#11044;</span>'
    status_symbol = hr['skoncil'].map({'ne': status_symbol_ne}).fillna(status_symbol_else)

    date_range_block = ('<div style="margin-left: 1px; color:grey;">' + hr['Hiredate2'].astype(str) + ' - ' + hr['Termdate2'].astype(str) + '</div>')
    status_block = ('<div style="font-weight:bold; margin-left: 1px;">' + hr['skoncil'].astype(str) + '</div>')

    info = ('<div style="display:flex; align-items:center;">' + status_symbol + '<div>' + status_block + date_range_block + '</div></div>')

    return info


hr = pd.read_csv("data/HumanResources.csv", sep=";")
hr_preprocessed = preprocess_hr_data(hr)
hr_preprocessed['personal_info'] = generate_personal_info(hr_preprocessed)
hr_preprocessed['Job Info'] = generate_job_info(hr_preprocessed)
hr_preprocessed['bydliste'] = generate_location_info(hr_preprocessed)
hr_preprocessed['pracovni_pomer'] = generate_employment_status(hr_preprocessed)
hrv = hr.loc[:,["Employee_ID","personal_info", "Job Info", "bydliste", "Salary2", "pracovni_pomer", "delka_prac_pomeru_text"]]
