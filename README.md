# Email Sender Script

Made by:

-   Mark Achiles G. Flores Jr.
-   Rafael Louie V. Miguel
-   Xian Hui B. Cheng
-   Francine Nastassja P. Jara

## Description

This script was used for the sending of dynamic emails to the office applicants of AWS Cloud Club - PUP Manila. The scripts, written by Mark Achiles G. Flores Jr., utilizes AWS SES for the template generation and email sending. The HTML Templates and UI design was made by Rafael Louie V. Miguel and Xian Hui B. Cheng with the use of the club's official graphics made by Francine Nastassja P. Jara.

# Running the scripts

## Setting up your environment

1. Create a virtual environment
    ```
    python -m venv venv
    ```
2. Activate your virtual environment

-   Search online how to activate your virtual environment for your shell
    ```
    . venv/Scripts/activate
    ```

3. Install the necessary python packages
    ```
    pip install -r requirements.txt
    ```

## Setting up your local database

1. Setup a local database in MongoDB with 'awscc' as the database and 'members' as the collection
2. Create a few sample documents with the fields 'fullName' and 'nickname'

## Setting up your 'applicants_database'

1. Create a folder in this directory and name it 'applicants_database'
2. Create 4 CSV files inside this folder and name them 'creatives.csv', 'operations.csv', 'relations.csv', 'marketing.csv'
3. Provide the necessary data inside the CSV files
    - 'creatives.csv' and 'operations.csv' must have a 'Full Name', 'Date', 'Time', and 'Personal Email' field
    - 'marketing.csv', and 'relations.csv' must have a 'Full Name' and 'Personal Email' field
4. When creating the data for your CSV files, make sure that for every 'Full Name', there is an equivalent 'fullName' in your local MongoDB database as this field will be used to connect the records inside the CSV file to the documents inside the MongoDB database.

# Running the script

-   After finishing the setup, just run 'main.py'

### For more inquiries...

You can reach out to me (Mark) through my social media accounts if you wanna know more about the script and if you need help creating your own.

-   [Facebook](https://www.facebook.com/aki9716)
-   [LinkedIn](https://www.linkedin.com/in/aki9716/)
