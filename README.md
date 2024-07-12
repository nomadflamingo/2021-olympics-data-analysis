# 🏅 Predicting 2024 Olympics Gold Medal Winners for Women's Athletics

## 📚 Introduction

This project aims to predict the number of gold medals that each country might win in women's athletics events at the 2024 Paris Olympics. The prediction is based on historical data from previous Olympic games. Using machine learning techniques, we analyze the historical performance of countries in women's athletics to forecast their success in the upcoming Olympics.

<img src=https://res.cloudinary.com/df9uihxz1/image/upload/v1720799299/2024-07-12_18.46.16_szu0w8.jpg alt="Plot" width="800">

## 📝 Project Overview

### 📊 Resources

1. [**Historical Olympics Data (1986-2018)**](https://www.kaggle.com/code/piterfm/olympic-games-1986-2022-data-visualization#How-is-data-look-like):
    - 📈 Contains information about the medals won by athletes and teams in past Olympic games.
    - Includes details such as the discipline, event, gender, medal type, and country.

2. [**2024 Paris Olympics Events**](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games):
    - 📅 Contains information about the events planned for the 2024 Paris Olympics.
    - Includes details such as the event name, sport, and associated URLs.

3. [**Wikipedia**](https://en.wikipedia.org/wiki/2024_Summer_Olympics):
    - Wiki page of 2024 Summer Olympics
    - Web-scraped to find out countries-participants

### 🎯 Objective

- To predict the number of gold medals each country will win in women's athletics events in the 2024 Paris Olympics based on historical performance data.

## 🛠️ Steps Involved

1. **📥 Data Collection and Preprocessing**:
    - Load and clean the historical Olympics data.
    - Filter the data to include only gold medals in women's athletics.

2. **📊 Data Aggregation**:
    - Aggregate the gold medal counts to ensure unique combinations of countries and sports.
    - Pivot the table to have sports as columns and countries as rows, filling missing values with zeros.

3. **🤖 Model Training**:
    - Use linear regression to train a model on the historical gold medal counts.
    - Features include the number of gold medals won in women's athletics by each country.

4. **🔮 Prediction**:
    - Predict the number of gold medals for each country in women's athletics events in the 2024 Olympics.
    - Visualize the predictions using bar charts.

## 🏆 Results

- The model predicts the number of gold medals each country might win in women's athletics events at the 2024 Paris Olympics.
- The predictions are visualized using bar charts to compare the performance of different countries.
