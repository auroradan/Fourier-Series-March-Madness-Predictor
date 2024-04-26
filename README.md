# Fourier Series March Madness Predictor
## Goal and Specifications
We aim to predict the amount of wins each march madness team will have throughout the tournament. We will use the offensive and defensive efficiency ratings found at the attached hyperlink to create a function that gives an expected amount of wins for a team based on the ratings and performance of teams from previous years. 
## Technical Approach
To approach this problem, we are going to normalize data on offensive and defensive efficiency ratings for 64 teams by dividing the offense or defense rating of each team by the largest rating experienced in that year. We are also going to normalize the amount of wins a team gets by dividing by the maximum wins a team can get in a 64 team tournament (6 wins). By normalizing this data, we will ensure that all of the data for wins, and efficiency ratings will fall between 0 and 1. We will then use a two-dimensional discrete Fourier series, which will output a function that fits the data. This Fourier series could be used with the inputs offensive and defensive efficiency to predict the output of wins for each team in the tournament. We plan to use python and Jupyter Notebooks to compute the Fourier series and produce the fitted function. Finally, we will compare how well each team actually did with our prediction. 

## Results
It is important to know that a greater offensive efficiency rating (points scored per 100 possessions) and a lower defensive efficiency (points allows per 100 possessions) is ideal.
![image](https://github.com/auroradan/Fourier-Series-March-Madness-Predictor/assets/103843222/fc2f0da7-4b71-4360-9d17-120d942cdea7)
