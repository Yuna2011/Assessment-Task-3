# Assessment-Task-3
## Requirements Outline  
### Functional Requirements :   
Data Loading:
The system must be able to load data from the CSV file.
It must check if the file exists and is in the correct format before loading.
If the file is missing or the format is wrong, the system should show an error message and ask the user to try again.


Data Cleaning:
The system should handle missing or empty values
It must allow the user to filter the data
The system should support sorting and grouping data by relevant fields like country or region.


Data Analysis:
The system must calculate the relation between Talent scores and Total AI Index scores.
It should also be able to calculate simple statistics like mean, median, and mode for selected data fields.


Data Visualisation:
The system should generate tables to show relationships between variables
Visualisations should have clear labels and titles
The system should display data previews using tables.


Data Reporting:
The system must provide output in a CSV file.


### Non-Functional Requirements :  
Reliability: 
The system must detect and handle errors gracefully, such as:
Missing or corrupted dataset files.
Incorrect data formats or missing values in important columns.
Invalid user inputs (e.g., filter criteria that don’t exist).

Data integrity:
The program should validate data before processing
If missing or corrupt data is found, the program should either skip those records with a warning or prompt the user to fix the data.


### See-I Paragraph :
Talent in the AI Index refers to the strength and availability of skilled professionals in artificial intelligence to contribute to AI projects. A strong talent pool means a country can use AI systems more effectively. Skilled workers can help with the growth and research of AI technologies. For example, in the AI Index dataset, countries like the United States and Singapore have high Talent scores alongside high overall AI Index scores, suggesting that talent availability is linked to overall AI index scores. Imagine a country’s AI industry as a high-tech factory. Without enough trained engineers, researchers, and programmers, the machines can’t run at full capacity. But when there’s an abundance of skilled talent, the factory operates smoothly, producing more innovations and boosting the country’s overall AI performance.

