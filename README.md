# Property Investment Opportunities in 2025
###### Authors: Andrew Cheng, Paul Samaniego, Riya Gajjar , Madeline Cruz
[Link to presentation](https://docs.google.com/presentation/d/1hGc5EfDDzNYhX1ClyUOcX7RNmIBS32VOmX1wYN52QlA/edit#slide=id.p)

## Abstract
We analyzed a decade of median home sale prices from Zillow (2013-2023) to examine potential cities and regions for property investment. Leveraging historical data provided by Zillow, moving averages, volatility measures, and a linear regression model, we present a data-driven approach to identify lucrative investment opportunities. Our exploratory analysis illuminates patterns and predictions in the U.S. housing market.

## Methods
* **Data Acquisition**: Extracted median home sale prices for U.S. cities from Zillow's database spanning 2013 to 2023.
* **Preliminary Analysis**: Surveyed the broad landscape of U.S. median home prices.
* **Geographical Aggregation**: Segmented data into five distinct geographic regions for a detailed study.
* **Data Exploration**:
  * Calculated monthly moving averages for each region.
  * Determined percentage price changes per month.
  * Evaluated seasonal price fluctuations.
* **Predictive Modeling**: Implemented a linear regression model to forecast city-specific housing price trends.
* **Visualization**: Charted year-over-year growth for metropolitan areas to visualize emerging patterns.
## Limitations
* Data uses MEDIAN price of homes in each city and is not an actual measure of true changes in price per individual home.
* Linear regression model may not be appropriate for time-course price predictions. ML models and other clustering techniques may provide more accurate predictions/ recommendations.
* Does not include local/ state property taxes and laws.
* Is not normalized to account for population of each city.
* Does not factor in underlying political/ social/ economic/ environmental/ related drivers in price.
  * Ie, supply/ demand, size of homes, age of home, home amenities, neighborhood qualities, population density, interest rates, etc.
* Property investments are NOT liquid investments.
  ![alt-text]()
## Conclusions 
* Average median home price has nearly doubled in the past decade.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/SummaryStatiscs/CentralT2013.png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/SummaryStatiscs/CentralT2023.png) 
* Price of homes in large metro areas (Los Angeles, CA & New York, NY, etc.) has had a steady increase in price over the past decade. Higher barrier of entry.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/SummaryStatiscs/Top5.png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Volatility/variabity_top_bottom.png)
* Price of homes in smaller metro areas experience higher volatility in prices and are more unpredictable.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/SummaryStatiscs/Bottom5.png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Volatility/variabity_top_bottom.png)
* West coast continues to dominate housing market, but has begun to show a drop in price, which may indicate a buy.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Moving%20Averages/Cities_by_Region/12MMA_West_Cities_line.png)
* East coast (north and south) is experiencing a rapid increase in price with top states moving with a factor of $1500 and $1700 per MONTH in our regression model
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Linear%20Regression/Northeast/Scatter%20Plot%20of%20Average%20House%20Prices%20in%20New%20Hampshire%20(NH).png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Linear%20Regression/Southeast/Scatter%20Plot%20of%20Average%20House%20Prices%20in%20Florida%20(FL).png)
* Price of homes can peak as much as 3% for the month of June and drop by 3% October
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Volatility/avg_price_change_by_month.png)
* We predict that the NE and SE will continue to grow in the next few years.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Moving%20Averages/Cities_by_Region/12MMA_Northeast_Cities_line.png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Moving%20Averages/Cities_by_Region/12MMA_Southeast_Cities_line.png)
* Homes on the West coast may have reached a local max and is beginning to fall back closer to our regression model.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Linear%20Regression/Midwest/Scatter%20Plot%20of%20Average%20House%20Prices%20in%20Illinois%20(IL).png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Linear%20Regression/Southwest/Scatter%20Plot%20of%20Average%20House%20Prices%20in%20Arkansas%20(AR).png)
* Our regression model shows that the highest moving city in the West is increasing at over $2500 a month in the past 10 years.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Linear%20Regression/West/Scatter%20Plot%20of%20Average%20House%20Prices%20in%20Nevada%20(NV).png)  
* Midwest and Southwest experience higher volatility but has been increasing overall based on moving averages.
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Moving%20Averages/Region/12MMA_USRegions_line.png)
    ![alt-text](https://github.com/anderoos/dv-property-investments-2025/blob/main/Images/Volatility/variability_regions.png)
## Data Sources and APIs
[Zillow Real Estate Metrics](https://www.zillow.com/research/data/)

## Tasks and Responsibilities 
- [x] Task delegation #Andrew
- [X] README file #Andrew
- [x] Clean Zillow Data #Andrew #Paul
- [x] Summary Statistics #Riya
  - [x] Average median price of each city over all timepoints
  - [x] Average median prices across all cities per month
  - [x] What is the central tendency (the median of medians)
  - [x] What are the most expensive/ affordable cities?
- [x] Exploratory #Paul
  - [x] Calculate monthly moving averages of median housing prices across all cities and observe which cities move the slowest and fastest
    - [x] Calculate 3 month moving average 
    - [x] Calculate 1 month moving average
  - [x] Calculate % change per month #Andrew
    - [x] Which cities has the highest variance in price changes?
    - [x] Which cities has the lowest variance in price changes?
  - [x] How do seasons affect prices? 
  - [x] Use linear regression to predict how the cities will trend #Mads
  - [x] Plot year over year growth of each metropolitan city 

## Contributors
* [Andrew Cheng](https://github.com/anderoos)
* [Paul Samaniego](https://github.com/Psamaniego001)
* [Riya Gajjar](https://github.com/rgajjar111)
* [Madeline Cruz](https://github.com/Mad-Cruz)

