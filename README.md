# Project4

## Demystifying Machine Learning - Predicting Home Prices

### Purpose
The purpose of our project is to provide users with a visually appealing web platform where they can predict home price based on a few simple inputs while providing broader market visualizations to complement the user search.

### ETL
We obtained the initial data from Kaggle dataset derived from realtor.com. This dataset was chosen for several reasons including the following:
- The dataset was large giving the machine learning model many different homes to train and predict home prices on
- The features within the dataset were broad enough to capture many different variations of homes.

We then used S3 to house the data due to its large size which GitHub wouldn’t accept. The data was then read into a notebook through Pyspark where the rest of the team would work on the data from there. 
### ML model

For the machine learning portion of our project, further cleaning of the data was required. Outliers were removed from each feature carefully prior to training the data. Several iterations of linear regression were run with sub par accuracy before generating a random forest model which predicted home prices on the testing data with near perfect accuracy.

### Visualizations

Visualizations were created using both tableau and leaflet. The visualizations created tell stories of total real estate and average real estate values by state that are filterable based on the number of bedrooms, bathrooms, and square footage.

### Web app and bootstrap

For our project, we chose to use flask to integrate the website and machine learning model. Flask's ease of use provided a great way to quickly and easily convert a user form into a scaled model that home price predictions could be calculated against. Combining the app with bootstrap, we were able to provide users with something that was both functional and eye catching. The premade template added structure and striking design to the website that adds potential to keep users on the website longer than if the page was rendered in just HTML.

### Files

colab file: https://colab.research.google.com/drive/13i93pYDH3YeRpXDGWpL8PefKNM5s8PgC#scrollTo=bhHl3Z-U-xzA

kaggle file: https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset

## Contributors
Tanner, Hanen, Brandon, Gwen, Long
