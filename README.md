# Credit Card Upgrade Prediction Project
The following project is a (very) simple assignment done for the module CET023 for the NTU Fleximasters in Business and Financial Analytics Programme.
The app was deployed using Streamlit Cloud and can be accessed [here](https://share.streamlit.io/ashwinphilipgeorge/credit_card_prediction/main/streamlit.py)

## Project Details
The app uses two features:
1. Number of purchases made by the user
2. Whether the user has a supplementary credit card
to predict whether the user will or will not upgrade their credit card. Predictions will be made by 4 models as described below.

### Models Used
1) Decision Tree (CART)
2) Random Forest Classifier
3) Gradient Boosting Classifier
4) Logistic Regression

### Deployment Technique
The app's front-end was created with the python package `streamlit`, which generates an intuitive and user friendly UI for users. Refer to the documentation [here](https://docs.streamlit.io/) to find out more about how streamlit can be used to create and customised user interfaces and forms.

On top of the python package, Streamlit Cloud is a platform (similar to heroku) that allows users to seamlessly deploy applications that make use of the streamlit package. An app can be deployed very quickly by folowing the deployment documentation [here](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app)

### Dependencies
The app uses `joblib`, `sklearn` and `pandas`. Version numebr not specified as the app is a very simple one using very basic functionalities that should not be affected by package version.

