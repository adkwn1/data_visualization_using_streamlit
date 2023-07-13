## Software Development Tools
Author: Andrew Kwon

## Introduction

This project notebook performs very rudimentary exploratory data analysis and visualization of a coffee quality score dataset. The original data was derived from the Coffee Quality Institute (CQI), downloaded from Kaggle.com (https://www.kaggle.com/datasets/volpatto/coffee-quality-database-from-cqi). The data visualization and filtering widgets were created using plotly.express and streamlit for a web application to be deployed via Render.

The dataset contains just over 1,300 entries of Arabica bean varieties from all over the world. Most of the meta data that was beyond the scope of this project was removed during the data cleaning. Some of the farm meta data was preserved for informational purposes.

In general, coffee scores are calculated based on a number of criteria such as aroma, acidity, and flavor. Additionally, points are deducted for defects in the coffee bean sample. Overall score is out of 100 and is assigned into one of the following ratings:
- 65-79: Commodity coffee.
- 80-89: Specialty coffee
- 90+: Presidential Award

## Usage - Notebook

The notebook is a standalone version of the project that performs the aforementioned exploratory data analysis and visualization on the coffee bean dataset. Some analysis of the dataset is performed only in the notebook version, but the visualization, unlike the web app version, is on static inputs. It can be downloaded on its own with the provided dataset. To run, copy the notebook and csv file into the same directory and open via preferred notebook IDE such as Jupyter.

## Usage - Local Browser

To run the project in a local web browser, clone the repository ensuring the files are in the correct directory structure:
- app.py (top level)
- .streamlit/config.toml

The config.toml specifies the server address and port number to run the web app locally via streamlit. In command prompt or terminal, navigate to the cloned directory and run the following command:

streamlit run app.py

Open a web browser and navigate to http://localhost:10000 to interact with the project application.

## Required Libraries
- pandas
- re
- streamlit
- plotly.express

## Link to live Web App

https://coffee-bean-rating.onrender.com/

Note: Hosted via free service. Please allow time to wake by refreshing your requests to the page.

## Screenshots

![screen](https://github.com/adkwn1/p4_dev_tools/assets/119823114/e6d15ad4-9a4e-40e3-b011-2e00d0b87bd0)
![newplot(1)](https://github.com/adkwn1/p4_dev_tools/assets/119823114/8a171044-72a7-4901-ad5f-a6cad6de14fd)
