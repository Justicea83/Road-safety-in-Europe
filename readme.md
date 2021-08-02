First and foremost I installed the packages: bs4, pandas, requests.

I made a http request to the URL and used Beautiful soup to parse the html.

Found all the table rows and parse the columns 

I then passed the columns into a pandas dataframe

I looped through the rest of the data to extract the table information

I dropped the unwanted columns and added the year column with a default value of 2018

I then renamed the columns to match the description and sorted the values by 'Road deaths per Million Inhabitants' column

Then I converted the dataframe into a scv using pandas library

