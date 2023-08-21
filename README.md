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

1. Setup a local database in MongoDB with `awscc` as the database and `members` as the collection
2. Create a few sample documents with the fields `fullName` and `nickname`. The `fullName` field will be used to access the `nickname`

# Using the app

1. Create a CSV file containing a `FULLNAME` or `NICKNAME` field along with a `SUBJECT` and `EMAIL` field.
2. View the code for the HTML template that you will be using, commented at the top are the other required fields. Make sure that these fields are also satisfied in your CSV file.
    - If you're using you're own HTML templates, enclose your template variables in double curly brackets like the example below:
    ```
    {{ NICKNAME }}
    ```
3. Run `main.py` and enjoy!

## Side Note

-   I forgot that you can't use this code because I'm using AWS SES and you're gonna need credentials to connect to AWS so... yeah. It works though, on my machine...

### For more inquiries...

You can reach out to me (Mark) through my social media accounts if you wanna know more about the script and if you need help creating your own.

-   [Facebook](https://www.facebook.com/aki9716)
-   [LinkedIn](https://www.linkedin.com/in/aki9716/)
