### File-Format-Converter
# Overview

The objective of this project is to develop solutions based on the design provided. In this case, the source data was obtained in the form of CSV files from a MySQL DB.

To improve the efficiency of our data engineering pipelines, we need to convert these CSV files into JSON files, since JSON is better to use in downstream applications than CSV files. The scope of this project involves converting CSV files into JSON files.

# Data Model Details

![image](https://github.com/v4760/File-Format-Converter/assets/77496027/0767622f-83fe-4200-9a7e-383b35b71373)

# Design

![image](https://github.com/v4760/File-Format-Converter/assets/77496027/5479a798-a307-45c2-83b6-fd5073090183)


# Setup Instructions
1. Setup the Project Using VSCode
2. Make sure you have set up a virtual environment (creating venv, requirements.txt, etc.,) and installed dependencies for the project.
3. It is essential that you deploy the application with the core logic.
4. Run the project after setting all the environment variables.
5. Take appropriate steps to handle the exception

# Validation Steps
1. You should check whether the data in the files has been converted properly.
2. Make sure the target folder has been created and populated with JSON files and confirm that the schema structure was accurately reflected from the CSV file. (Hint: Refer to schemas.json)

# Technologies Used
Programming Language – Python
Pandas – For Converting CSV to Dataframe and then Dataframe into JSON.

