import streamlit as st
import pandas as pd
import first_func
import second_func
import third_func

df = pd.read_csv('titanic.csv')

st.title("Лабораторная работа 7\nКоманда: Дударев А., Петров Д., Ережепов О.")

choice_list: list[int] = [1, 2, 3]
user_choice = st.selectbox("Выберите номер задания: ", choice_list)
choice: int

if user_choice != null:
    choice = int(user_choice)
else:
    choice = 1
 
match choice:
    case 1:
        first_func.avg_price_output(df)
    case 2:
        second_func.avg_age_output(df)
    case 3:
        third_func.gender_count_output(df)
