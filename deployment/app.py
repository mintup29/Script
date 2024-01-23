import streamlit as st
import pickle
import pandas as pd

digilib_dict = pickle.load(open("digilib.pkl", "rb"))
digilib = pd.DataFrame(digilib_dict)

st.title("Journal Recommender System")

selected_journal_name = st.selectbox(
    "Type or select a journal from the dropdown", digilib["Judul"].values
)

similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(judul):
    digilib_index = digilib[digilib["Judul"] == judul].index[0]
    distances = similarity[digilib_index]
    digilib_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    recommended_digilib = []
    for i in digilib_list:
        recommended_digilib.append(digilib.iloc[i[0]].Judul)
    return recommended_digilib


if st.button("Show Recommendation"):
    recommendations = recommend(selected_journal_name)

    for i in recommendations:
        st.write(i)
