# KFC Data Automation
KFC Data Automation is a command line based program that collect sales data, validate and update the data; calculate

the excess and goods data within the company. The goal is to save the company a repetitive task, help to reduce the 

excess and for recommendations, and also to be able to predict the future market.

<font color = 'blue'>Here is the live version of my project</font>

![Responsive image](<assets/images/kfc data-responsive image.png>)

## How the program works

KFC Data Automation helps in the daily business. The program request data of the last business day from the user, 

which must be 13 integer numbers.

When the program gets the input data, it will update the sales worksheet. 

it will then calculate the excess and goods data, update and add them both to their separate worksheets.

## Features

## Existing Features

•	Enter data

o	The program prompt the user to key in data

o	The number of data should up to 13

![input data](<assets/images/keyindata.png>)

•	Input validation

o	The program validate the user to key in 13 numbers

o	You must enter numbers

o	Not exactly 13 numbers will invalidate the input.

o	Entering 13 integer numbers will validate the input.

![invalid input numbers](<assets/images/invaliddata.png>)

![valid input numbers](<assets/images/validdata.png>)

## Future Features

•	Add more daily business processess like expenses, profit

•	Calculate more daily business processess for enhancement 

## Testing

I have tested this program by doing the following:

•	Running the program in the power shell local terminal

•	Input both valid and invalid data 

•	Tested in Code institute heroku terminal.

## Bugs

### Solved bugs

•	The program could not run because I have forgotten to call the all_functions; which I fixed when I called it.

•	In importing libraries and credentials, I made a mistake by using small letter case for ‘c’ in credentials; which was fixed 

with upper case.

### Remaining bugs

•	Bugs remaining are whitespaces, blanks errors that did not affect the program not to run.

## Validator Testing

•	PEP8

o	Few errors returned from [PEP8](https://pep8ci.herokuapp.com/) but did not affect the program.

## Deployment

This program was deployed using Code institute's mock terminal for Heroku

•	Steps for deployment

o	Fork or clone this repository

o	Create a new Heroku app

o	Set the buildbacks to Python and NodeJs in that order

o	Link the Heroku app to the repository

o	Click on Deploy

## Credits

•	The concept style of the structure of the work and the coding was taken from Love sandwiches project

•	Code institute for deployment terminal












