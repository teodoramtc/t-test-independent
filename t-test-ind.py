import numpy as np
import streamlit as st

st.title("Independent samples t-test calculator")

m1 = st.number_input("Mean value of the first group:", min_value=float(-10000000000), max_value=float(10000000000),
                     value=float(0), step=float(0.01))
m2 = st.number_input("Mean value of the second group:", min_value=float(-10000000000), max_value=float(10000000000),
                     value=float(0), step=float(0.01))
s1 = st.number_input("Standard deviation of the first group:", min_value=0.00000000000001, max_value=float(10000000000),
                     value=float(1), step=float(0.01))
s2 = st.number_input("Standard deviation of the second group:", min_value=0.00000000000001,
                     max_value=float(10000000000), value=float(1), step=float(0.01))
n1 = st.number_input("Size of the first group:", min_value=float(2), max_value=float(10000000000), value=float(100),
                     step=float(1))
n2 = st.number_input("Size of the second group:", min_value=float(2), max_value=float(10000000000), value=float(100),
                     step=float(1))

t = (m1 - m2) / np.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)

df = n1 + n2 - 2
ci = st.radio("Choose significance level: ", ('95%', '99%'))
sig_99 = 'The test is significant at the 99% level'
not_sig_99 = 'The test is not significant at the 99% level'
sig_95 = 'The test is significant at the 95% level'
not_sig_95 = 'The test is not significant at the 95% level'

def test_sig(df, t):
    if df == 1:
        if ci == '95%' and t >= 12.71:
            return sig_95
        elif ci == '95%' and t < 12.71:
            return not_sig_95
        elif ci == '99%' and t >= 63.66:
            return sig_99
        else:
            return not_sig_99
    elif df == 2:
        if ci == '95%' and t >= 4.30:
            return sig_95
        elif ci == '95%' and t < 4.30:
            return not_sig_95
        elif ci == '99%' and t >= 9.92:
            return sig_99
        else:
            return not_sig_99
    elif df == 3:
        if ci == '95%' and t >= 3.18:
            return sig_95
        elif ci == '95%' and t < 3.18:
            return not_sig_95
        elif ci == '99%' and t >= 5.84:
            return sig_99
        else:
            return not_sig_99
    elif df == 4:
        if ci == '95%' and t >= 2.78:
            return sig_95
        elif ci == '95%' and t < 2.78:
            return not_sig_95
        elif ci == '99%' and t >= 4.60:
            return sig_99
        else:
            return not_sig_99
    elif df == 5:
        if ci == '95%' and t >= 2.57:
            return sig_95
        elif ci == '95%' and t < 2.57:
            return not_sig_95
        elif ci == '99%' and t >= 4.03:
            return sig_99
        else:
            return not_sig_99
    elif df == 6:
        if ci == '95%' and t >= 2.45:
            return sig_95
        elif ci == '95%' and t < 2.45:
            return not_sig_95
        elif ci == '99%' and t >= 3.71:
            return sig_99
        else:
            return not_sig_99
    elif df == 7:
        if ci == '95%' and t >= 2.36:
            return sig_95
        elif ci == '95%' and t < 2.36:
            return not_sig_95
        elif ci == '99%' and t >= 3.50:
            return sig_99
        else:
            return not_sig_99
    elif df == 8:
        if ci == '95%' and t >= 2.31:
            return sig_95
        elif ci == '95%' and t < 2.31:
            return not_sig_95
        elif ci == '99%' and t >= 3.36:
            return sig_99
        else:
            return not_sig_99
    elif df == 9:
        if ci == '95%' and t >= 2.26:
            return sig_95
        elif ci == '95%' and t < 2.26:
            return not_sig_95
        elif ci == '99%' and t >= 3.25:
            return sig_99
        else:
            return not_sig_99
    elif df == 10:
        if ci == '95%' and t >= 2.23:
            return sig_95
        elif ci == '95%' and t < 2.23:
            return not_sig_95
        elif ci == '99%' and t >= 3.17:
            return sig_99
        else:
            return not_sig_99
    elif df == 11:
        if ci == '95%' and t >= 2.20:
            return sig_95
        elif ci == '95%' and t < 2.20:
            return not_sig_95
        elif ci == '99%' and t >= 3.11:
            return sig_99
        else:
            return not_sig_99
    elif df == 12:
        if ci == '95%' and t >= 2.18:
            return sig_95
        elif ci == '95%' and t < 2.18:
            return not_sig_95
        elif ci == '99%' and t >= 3.05:
            return sig_99
        else:
            return not_sig_99
    elif df == 13:
        if ci == '95%' and t >= 2.16:
            return sig_95
        elif ci == '95%' and t < 2.16:
            return not_sig_95
        elif ci == '99%' and t >= 3.01:
            return sig_99
        else:
            return not_sig_99
    elif df == 14:
        if ci == '95%' and t >= 2.14:
            return sig_95
        elif ci == '95%' and t < 2.14:
            return not_sig_95
        elif ci == '99%' and t >= 2.98:
            return sig_99
        else:
            return not_sig_99
    elif df == 15:
        if ci == '95%' and t >= 2.13:
            return sig_95
        elif ci == '95%' and t < 2.13:
            return not_sig_95
        elif ci == '99%' and t >= 2.95:
            return sig_99
        else:
            return not_sig_99
    elif df == 16:
        if ci == '95%' and t >= 2.12:
            return sig_95
        elif ci == '95%' and t < 2.12:
            return not_sig_95
        elif ci == '99%' and t >= 2.92:
            return sig_99
        else:
            return not_sig_99
    elif df == 17:
        if ci == '95%' and t >= 2.11:
            return sig_95
        elif ci == '95%' and t < 2.11:
            return not_sig_95
        elif ci == '99%' and t >= 2.90:
            return sig_99
        else:
            return not_sig_99
    elif df == 18:
        if ci == '95%' and t >= 2.10:
            return sig_95
        elif ci == '95%' and t < 2.10:
            return not_sig_95
        elif ci == '99%' and t >= 2.88:
            return sig_99
        else:
            return not_sig_99
    elif df == 19:
        if ci == '95%' and t >= 2.09:
            return sig_95
        elif ci == '95%' and t < 2.09:
            return not_sig_95
        elif ci == '99%' and t >= 2.86:
            return sig_99
        else:
            return not_sig_99
    elif df == 20:
        if ci == '95%' and t >= 2.09:
            return sig_95
        elif ci == '95%' and t < 2.09:
            return not_sig_95
        elif ci == '99%' and t >= 2.84:
            return sig_99
        else:
            return not_sig_99
    elif df == 21:
        if ci == '95%' and t >= 2.08:
            return sig_95
        elif ci == '95%' and t < 2.08:
            return not_sig_95
        elif ci == '99%' and t >= 2.83:
            return sig_99
        else:
            return not_sig_99
    elif df == 22:
        if ci == '95%' and t >= 2.07:
            return sig_95
        elif ci == '95%' and t < 2.07:
            return not_sig_95
        elif ci == '99%' and t >= 2.82:
            return sig_99
        else:
            return not_sig_99
    elif df == 23:
        if ci == '95%' and t >= 2.07:
            return sig_95
        elif ci == '95%' and t < 2.07:
            return not_sig_95
        elif ci == '99%' and t >= 2.81:
            return sig_99
        else:
            return not_sig_99
    elif df == 24:
        if ci == '95%' and t >= 2.06:
            return sig_95
        elif ci == '95%' and t < 2.06:
            return not_sig_95
        elif ci == '99%' and t >= 2.80:
            return sig_99
        else:
            return not_sig_99
    elif df == 25:
        if ci == '95%' and t >= 2.06:
            return sig_95
        elif ci == '95%' and t < 2.06:
            return not_sig_95
        elif ci == '99%' and t >= 2.79:
            return sig_99
        else:
            return not_sig_99
    elif df == 26:
        if ci == '95%' and t >= 2.06:
            return sig_95
        elif ci == '95%' and t < 2.06:
            return not_sig_95
        elif ci == '99%' and t >= 2.78:
            return sig_99
        else:
            return not_sig_99
    elif df == 27:
        if ci == '95%' and t >= 2.05:
            return sig_95
        elif ci == '95%' and t < 2.05:
            return not_sig_95
        elif ci == '99%' and t >= 2.77:
            return sig_99
        else:
            return not_sig_99
    elif df == 28:
        if ci == '95%' and t >= 2.05:
            return sig_95
        elif ci == '95%' and t < 2.05:
            return not_sig_95
        elif ci == '99%' and t >= 2.76:
            return sig_99
        else:
            return not_sig_99
    elif df == 29:
        if ci == '95%' and t >= 2.04:
            return sig_95
        elif ci == '95%' and t < 2.04:
            return not_sig_95
        elif ci == '99%' and t >= 2.76:
            return sig_99
        else:
            return not_sig_99
    elif 30 <= df < 40:
        if ci == '95%' and t >= 2.04:
            return sig_95
        elif ci == '95%' and t < 2.04:
            return not_sig_95
        elif ci == '99%' and t >= 2.75:
            return sig_99
        else:
            return not_sig_99
    elif 40 <= df < 60:
        if ci == '95%' and t >= 2.02:
            return sig_95
        elif ci == '95%' and t < 2.02:
            return not_sig_95
        elif ci == '99%' and t >= 2.70:
            return sig_99
        else:
            return not_sig_99
    elif 60 <= df < 120:
        if ci == '95%' and t >= 2.00:
            return sig_95
        elif ci == '95%' and t < 2.00:
            return not_sig_95
        elif ci == '99%' and t >= 2.66:
            return sig_99
        else:
            return not_sig_99
    elif df == 120:
        if ci == '95%' and t >= 1.98:
            return sig_95
        elif ci == '95%' and t < 1.98:
            return not_sig_95
        elif ci == '99%' and t >= 2.62:
            return sig_99
        else:
            return not_sig_99
    else:
        if ci == '95%' and t >= 1.96:
            return sig_95
        elif ci == '95%' and t < 1.96:
            return not_sig_95
        elif ci == '99%' and t >= 2.28:
            return sig_99
        else:
            return not_sig_99


message = test_sig(df, t)

st.write('t = ' + str(t) + ' ' + message)

# tabela za znacajnost - videti kako se odredjuju stepeni slobode
