import math
import scipy.stats as sc
import numpy as np
import pandas as pd

import matplotlib as mplpip 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

expected_value = st.sidebar.slider("Выберите значение математического ожидания", 1, 50, 5)
dispersion = st.sidebar.slider("Выберите значение дисперсии ", 1, 10, 1)
lam = st.sidebar.slider("Выберите значение Лямбды ", 1, 10, 1)
puas_lam = st.sidebar.slider ("Выберите значение Лямбды для графика Пуассона ", 1, 10, 1)
for_lin_pic1 = st.sidebar.slider("Выберите начальное значение для массива ", 1, 100, 25)
for_2lin_pic1 = st.sidebar.slider("Выберите конечное значение для массива  ", 1, 300, 50)
for_3lin_pic1 = st.sidebar.slider("Выберите количество элементов равномерно распределенных  ", 1, 300, 50)

x = np.linspace(for_lin_pic1, for_2lin_pic1, for_3lin_pic1)
mu = expected_value
sigma = dispersion
norm_distr = sc.norm(mu, sigma)
pic1 = plt.figure(figsize = (10,6))
plt.plot(x, norm_distr.pdf(x))
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('График нормального распределения с долей')
st.pyplot(pic1)


lam1 = lam
y = np.linspace(lam1, for_2lin_pic1, for_3lin_pic1)
dens_exp = sc.expon(lam1).pdf(y)
pic2 = plt.figure(figsize = (10,6))
plt.plot(y, dens_exp, label=f'λ = {lam1}')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('График экспоненциального распределения');
st.pyplot(pic2)


lam2 = puas_lam

# Создайте массив значений x (целые числа)
z = np.arange(for_lin_pic1, for_2lin_pic1)

# Вычислите вероятности для каждого значения x
poisson = sc.poisson.pmf(z, lam2)

# Постройте график распределения Пуассона в виде кривой
pic3 = plt.figure(figsize=(10, 6))
plt.plot(z, poisson, marker='o', linestyle='-')
plt.xlabel('Значение')
plt.ylabel('Вероятность')
plt.title('График распределения Пуассона')
st.pyplot(pic3)