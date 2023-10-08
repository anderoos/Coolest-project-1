# Group 1 Project Proposal
## Property Investment Opportunities in 2025 

## Description

Using median sale prices from Zillow, can we use historic prices to predict the best cities to move to in the next few years.?

## Data Sources and APIs
Zillow and Census (to normalize prices with population)

## Approaches and Tasks
- [ ] Get census data from 2008 to 2023, clean and sort data**
- [x] Clean Zillow Data
- [ ] Summary Statistics #Riya
  - [ ] Average median price of each city over all timepoints
  - [ ] Average median prices across all cities per month
  - [ ] Deviation of average median prices (Did we see any abnormal % changes in each city?) (Use box plots)
  - [ ] What is the central tendency (the median of medians)
  - [ ] Where are all the priciest cities located geographically?

- [ ] Exploratory/ Inferential #Paul
  - [ ] Calculate monthly moving averages of median housing prices across all cities and observe which cities move the slowest and fastest
    - [ ] Calculate 3 month moving average (df.rolling())
    - [ ] Calculate 1 month moving average(df.rolling())
  - [ ] How does population affect the median value of properties?*
    - [ ] Use census data to normalize average price of the year/10000 people*

  - [ ] Calculate % change per month #Andrew
    - [ ] Which cities has the most volatile housing markets?(df_means.groupby(state)[‘year’].max()
      * ie the highest number of large % changes
    - [ ] Which cities has the most stable hosing markets?
      * ie the lowest number of large % changes
    - [ ] How does seasons affect prices across states? #Mads
      - [ ] Box plots of % change across all cities, grouped by season  
  - [ ] Use the data to predict how the cities will trend in the next few years?
    - [ ] Calculate probability?
  - [ ] Plot year over year growth of each metropolitan city #Mads
  - [ ] What the best up and coming cities to move to in each state? (Plot using hvplot) 


## Contributors
* [Andrew Cheng](https://github.com/anderoos)
* [Paul Samaniego](https://github.com/Psamaniego001)
* [Riya Gajjar](https://github.com/rgajjar111)
* [Madeline Cruz](https://github.com/Mad-Cruz)

