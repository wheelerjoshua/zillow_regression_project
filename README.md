# About this Project
To be updated as progress is achieved.

## Project Goals
The goal of this project is to identify drivers of churn for the benefit of creating a solution to reduce the rate of churn among customers. 


## Project Description
With an unsteady and increasingly competitive market, it is cheaper to retain current customers than to establish new ones. We will observe various details of customer contracts and discover what may be driving them to churn and will use the information to create a model to predict future customer churn and a recommendation in reducing rate of churn.

## Initial Questions

- Do houses with higher square footage have a higher calculated tax amount?
- Do houses with more bathrooms have a higher calculated tax amount?
- Do houses with more bedrooms have a higher calculated tax amount?
- Do houses with less bedrooms and higher square footage have a lower tax amount than houses with more bedrooms and a higher square footage?

## Data Dictionary

| variable      | meaning       |
| ------------- |:-------------:|
|df|Dataframe of raw telco data from sql server|
|train| training dataset, a major cut from the df|
|validate| validate dataset, used to prevent overfitting|
|test| test dataset, to test the top model on unseen data|
|chi2 | statistical test used to compare churn with various categories|

## Steps to Reproduce
What I did to get here?
- Create Trello Board listing tasks to completion
- Created modules with functions to acquire and clean the data
- Examined the data and came up with 4 questions
- Created visualizations relating to the quesitons
- Ran statistical tests to answer the questions
- Created a baseline model to test baseline accuracy
- Created numerous models to see how various algorithms performed
- Modified algorithms to see how changes affected performance
- Chose the 3 that performed the best and evaluated them on the validate training set
- Best performing model evaluated against test
- Decided on a recommendation and next steps

## The Plan

### Wrangle
- wrangle.py
Functions to acquire, clean, tidy, prepare, split, and scale the data for use.

### Explore
#### Ask Questions
1. Do houses with higher square footage have a higher calculated tax amount?
2. Do houses with more bathrooms have a higher calculated tax amount?
3. Do houses with more bedrooms have a higher calculated tax amount?
4. Do houses with less bedrooms and higher square footage have a lower tax amount than houses with more bedrooms and a higher square footage?

#### Visualizations
- Matplotlib and Seaborn used to create visualizations
#### Statistical Tests
Used .mean() and chi2 test to answer statistical questions
#### Summary
Wrap up all of the testing conclusions
### Modeling
#### Select Evaluation Metric

#### Evaluate Baseline
Create a series based on taxvaluedollarcnt.mean()
#### Develop 3 Models
Develop numerous models and assess top 3
#### Evaluate on Train
All models evaluated on train, but top 3 were validated
#### Evaluate on Validate
Ensure no overfitting takes place
#### Evaluate top model on Test
Top model evaluated against test dataset to see how it performed on unknown data.