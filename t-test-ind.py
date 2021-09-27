import numpy as np
import streamlit as st


st.title("Independent samples t-test calculator")

m1 = st.number_input("Mean value of the first group:", min_value=float(-10000000000), max_value=float(10000000000), value=float(0), step=float(1))
m2 = st.number_input("Mean value of the second group:", min_value=float(-10000000000), max_value=float(10000000000), value=float(0), step=float(1))
s1 = st.number_input("Standard deviation of the first group:", min_value=0.00000000000001, max_value=float(10000000000), value=float(1), step=float(1))
s2 = st.number_input("Standard deviation of the second group:", min_value=0.00000000000001, max_value=float(10000000000), value=float(1), step=float(1))
n1 = st.number_input("Size of the first group:", min_value=float(1), max_value=float(10000000000), value=float(100), step=float(1))
n2 = st.number_input("Size of the second group:", min_value=float(1), max_value=float(10000000000), value=float(100), step=float(1))

t = (m1 - m2) / np.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)

st.write(t)

#tabela za znacajnost - videti kako se odredjuju stepeni slobode
