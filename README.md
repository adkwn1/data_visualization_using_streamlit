# p4_dev_tools
Project 4 - Software Development Tools

# Introduction

This project notebook performs very rudimentary exploratory data analysis and visualization of a coffee quality score dataset. The original data was derived from the Coffee Quality Institute (CQI), downloaded from Kaggle.com (https://www.kaggle.com/datasets/volpatto/coffee-quality-database-from-cqi). The data visualization and filtering widgets were created using plotly.express and streamlit for a web application to be deployed via Render.

The dataset contains just over 1,300 entries of Arabica bean varieties from all over the world. Most of the meta data that was beyond the scope of this project was removed during the data cleaning. Some of the farm meta data was preserved for informational purposes.

In general, coffee scores are calculated based on a number of criteria such as aroma, acidity, and flavor. Additionally, points are deducted for defects in the coffee bean sample. Overall score is out of 100 and is assigned into one of the following ratings:
- 65-79: Commodity coffee.
- 80-89: Specialty coffee
- 90+: Presidential Award
