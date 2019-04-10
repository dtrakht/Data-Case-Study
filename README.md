# Data Case Study
By David Trakhtenberg

## Instructions
1. Install sodapy dependency using pip install sodapy
2. Run food_inspections_etl.py
3. Run test_food_inspections_etl.py to unit test
4. Tables/files will be output to C:/users/<username>/Food Inspections Data 
5. Can also view line by line input/output in Food Inspections Notebook.ipynb
6. Analyze away!
  
## Technologies Used
I used the following technologies: Github, Jupyter Notebook, and Python 3.6.8. 
I used the following Python libraries: Sodapy, numpy, and pandas.  

## Requirements
**Use a language of your choice to develop a script that reads the dataset and pushes an output to separate csv files**
Dataset: [link](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/data)

**Create 2 output tables such that:**
+Table A includes a list of all inspections
+Table B includes a list of all violations and comments associated with each inspection

I used Python to extracted the dataset, transformed it with several steps of logic, and loaded it into three output csv files. 
I also created a unit test script to validate a few parts of the ETL scipt. 

## Files Created
+food_inspections_etl.py
+test_food_inspections_etl.py
+Food Inspections Notebook.ipynb
+README.md
