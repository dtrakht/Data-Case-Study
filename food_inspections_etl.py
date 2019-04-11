import pandas as pd
from sodapy import Socrata
import numpy as np
import os.path

#Retrieving Food Inspections data using Socrata and converting to DF
client = Socrata("data.cityofchicago.org", None)
results = client.get("cwig-ma7x", limit=2000) #limit set for ease of processing use
inspections_df = pd.DataFrame.from_records(results)

#Iterate through to read the full dataset - uncomment when interestd in full dataset
# initial = 2000
# while results:
#     results = client.get("cwig-ma7x", limit=2000, offset=initial)
#     inspections_df = inspections_df.append(pd.DataFrame.from_records(results))
#     initial += 2000

#drop uneccesary computed columns
inspections_df = inspections_df.drop(columns=[':@computed_region_43wa_7qmu', ':@computed_region_6mkv_f3dw', ':@computed_region_awaf_s7ux'
                            ,':@computed_region_bdys_3d7i', ':@computed_region_vrxf_vc4k', 'location', 'city', 'state', 'aka_name'])

#Drop rows with null data
inspections_df.dropna()

#Checking whether there are any duplicates
#If duplicates exist, then use .drop_duplicates()
d = inspections_df.duplicated()

duplicates_amount = 0 
duplicates = []
try:
    for i in range(1,len(d)):
        if d[i] == True:
            duplicates_amount = duplicates_amount + 1
            duplicates.append(i)
            print("Duplicates Amount: ",duplicates_amount) 
except:
    print("No duplicates in this dataset")
    
#Remove trailing characters from date field
inspections_df["inspection_date"] = inspections_df.inspection_date.str.split('T').str[0]

#Exclude unsuccessful inspections
inspections_df = inspections_df[~inspections_df.results.isin(["Business Not Located", "Out of Business"])] 

#Rename columns due to sodapy conversion
inspections_df = inspections_df.rename(columns={"license_":"License", "address":"Address",
                               "dba_name":"DBA Name", "facility_type":"Facility Type", "inspection_date":"Inspection Date",
                              "inspection_id":"Inspection ID", "inspection_type":"Inspection Type", "latitude":"Latitude",
                              "longitude":"Longitude", "results":"Results", "risk":"Risk", 
                              "violations":"Violations", "zip":"Zip"})

#Separate DF into Inspections and Violations
inspections = inspections_df.loc[:, inspections_df.columns != 'Violations']
violations = inspections_df.loc[:, inspections_df.columns != 'Inspection Date']

#Create two output tables and third table with entire schema
root_path = os.path.dirname(os.getcwd())

#Export to CSV
inspections_df.to_csv(os.path.join(root_path, "Food Inspections Data/Full Food Inspections.csv"), index=False)
inspections.to_csv(os.path.join(root_path, "Food Inspections Data/Inspections.csv"), index=False)
violations.to_csv(os.path.join(root_path, "Food Inspections Data/Violations.csv"), index=False)
