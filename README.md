# Predicting 2024 Olympics Gold Medal Winners

## Introduction

This project aims to predict the number of gold medals that each country might win in the 2024 Paris Olympics. The prediction is based on historical data from previous Olympic games and the events planned for 2024. Using machine learning techniques, we analyze the historical performance of countries in different sports to forecast their success in the upcoming Olympics.

## Project Overview

### Datasets

1. **Historical Olympics Data (1986-2018)**:
    - Contains information about the medals won by athletes and teams in past Olympic games.
    - Includes details such as the discipline, event, gender, medal type, and country.

2. **2024 Paris Olympics Events**:
    - Contains information about the events planned for the 2024 Paris Olympics.
    - Includes details such as the event name, sport, and associated URLs.

### Objective

- To predict the number of gold medals each country will win in the 2024 Paris Olympics based on historical performance data.

## Steps Involved

1. **Data Collection and Preprocessing**:
    - Load and clean the historical Olympics data.
    - Filter the data to include only gold medals.
    - Merge the historical data with the 2024 events data to align sports disciplines.

2. **Data Aggregation**:
    - Aggregate the gold medal counts to ensure unique combinations of countries and sports.
    - Pivot the table to have sports as columns and countries as rows, filling missing values with zeros.

3. **Model Training**:
    - Use linear regression to train a model on the historical gold medal counts.
    - Features include the number of gold medals won in each sport by each country.

4. **Prediction**:
    - Predict the number of gold medals for each country in the 2024 Olympics.
    - Visualize the predictions using bar charts.
