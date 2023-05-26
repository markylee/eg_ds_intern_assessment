# EG Data Science Intern Assessment

About:  
This is my EG Data Science Intern Assessment. The purpose of this project is to take the given starcraft_player_data.csv, and see if we can accurately predict LeagueIndex with the available data. There are a couple of things that are needed to be done in order to run this code yourself, such as editing the psycopg2 login credentials (dw, I'm not leaking anything). Everything is organized by the function, i.e. starcraft_eda.ipynb is the exploratory data analysis I performed. 

Contents:

| File Name | Description | 
| ------------ | --------------------------------- | 
| README.md | Read me for the project | 
| load_data.py | Loads the data from the local PostgreSQL machine to a Pandas DataFrame. | 
| starcraft_eda.ipynb | Exploratory Data Analysis on the Starcraft Player Data. |
| starcraft_etl.ipynb | Process of extracting the player data from the csv, formatting it correctly, and then inputting it into local PostgreSQL. | 
| starcraft_modeling.ipynb | Modeling with the data. Models used: Random Forests and XGBoost. Various transformations and alterations with the data were also considered. | 
| starcraft_evaluation.ipynb | Gathering my findings and reporting them back to stakeholders. I also provided suggestions to improve data gathering if possible. |
| starcraft_player_data.csv | Starcraft Player Data with 20 different features. |  
  
  
  
  
Thanks for taking the time to read this! 
