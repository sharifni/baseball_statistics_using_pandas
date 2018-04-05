# Performing statistical analysis of baseball game data using pandas


## Step 1
Loading pitch data file using pandas.read_csv
Data has 18 columns with 20067 rows
### Header 
### GameId	PitcherId	HitterId	PitcherSide	HitterSide	PrimaryEvent	PitcherTeamId	HitterTeamId	PA	AB	H	2B	3B	HR	TB	BB	SF	HBP

Opening text file containing Combinations based on which we have to perform aggregations.

## Step 2 Split
Iterating through each combination and forming dataframes by grouping based on variable mentioned(ex: HitterID)

## Step 3 Apply
Sum is calculated for each variable that we are aggregating(ex: HitterID) 

Four basic metrics are calculated from the aggregated data.
AVG – Batting average (also abbreviated AVG): hits divided by at bats (H/AB)    

OBP – On-base percentage: times reached base (H + BB + HBP) divided by at bats plus walks plus hit by pitch plus sacrifice flies (AB + BB + HBP + SF)

SLG – Slugging average: total bases achieved on hits divided by at-bats (TB/AB)

OPS – On-base plus slugging: on-base percentage plus slugging average

 

## Step 4 Combine
Combining each individual dataframe into a single one with the following column headers:
SubjectId (e.g. 108, 119, etc)
Stat (e.g. the name of the stat "AVG", "OBP", etc.)
Split (e.g. "vs LHP", "vs RHH", etc.)
Subject (e.g. "HitterId", "PitcherTeamId", etc.)
Value (e.g. the value of the Stat 0.350, 1.03, 0.5, etc)

## Step 5
Sorting the table and saving the output to a csv file.

# Terminology
**Subject:** A field that is grouped on; 
**Split:** A filter used to restrict a dataset; analogous to SQL's "WHERE"
clause.
vs LHH: "versus left-handed hitters"
vs RHH: "versus right-handed hitters"
vs LHP: "versus left-handed pitchers"
vs RHP: "versus right-handed pitchers"
**Stat:** A metric that is calculated from the aggregated data.


## References:
https://en.wikipedia.org/wiki/Baseball_statistics </br>
https://pandas.pydata.org/pandas-docs/stable/groupby.html#grouping-dataframe-with-index-levels-and-columns
