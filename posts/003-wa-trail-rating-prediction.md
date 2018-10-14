For my second overall and first solo project at Metis, the task was to web scrape data and then use it to conduct a Linear Regression analysis. As a big fan of hiking and recently coming back from an overnight weekend backpacking trip, I thought I would turn this task into something of interest to me: **how to predict a hike's "rating"**.

## Project Design
WTA.org is a website that has a database of 3,555 hikes (at the time of scraping) which includes hike details, trip reports, and a voting system allowing users to rate a scale on a scale of 1-5. The goal of this project was to use the given information in the database to create a model able to accurately predict a hike's rating based on its attributes. A good model potentially could aid "trail planners" with the foresight to predict how well-liked a newly opened hike would do before they invested in creating the trail.

## Approach

### 1. Scrape data from all 3,555 hike pages on wta.org
### 2. Clean data within a `pandas DataFrame` to be ready for model use
### 3. Perform Linear Regression modeling

Although I originally hoped to use nearly all the scraped as well as engineer some new ones, time constraints did not allow for it. Chiefly, the lat/long coordinates and sub-region (location) of the hikes both offered unique insights and were not incorporated in the models. Additionally, using other sources of data such as weather patterns/history and alltrails.com were passed on due to time constraints.

Initially, I wanted to create the model without using features that a trail planner would not have access to: such as how many times people had rated a trail and the number of trip reports that were left for a trail. After some simple linear regressions built with those features excluded, it became clear the model had little value. Thus, I decided to use all data available to me for this project.

## Process
<br>

### Scraping

This was my first foray into scraping. I think I'm hooked. I used the `requests` and `BeautifulSoup` python libraries to get the job done. I took a look at `selenium` as well, but then recognized the aforementioned tools would be just as good in this case. 

<<<< IMAGE OF CIRCLED ITEMS ON THE POWERPOINT PAGE HERE>>>>

The WTA pages had well labeled HTML tags consistent across the different hike pages. Once I thoroughly dissected a few pages and identified how the hike attributes (elevation gain, length of hike, region, and presence of coasts/lakes/mountains/etc) were encoded, I wrote a python script that found those features, pulled their information, and saved it to a table in a `pandas DataFrame`. In all, the script ran for over an hour and ended up accessing all 3,555 hike pages

### Cleaning

As has been told to me and others many time before: *there is no such thing as clean data*. (Mostly true, unless it's from kaggle.com or other pre-cleaned sources). I found this to be the case with my data. Many hikes were incomplete and did not contain all information. My script sometimes correctly identified these fields as "missing", while other times it substituted an **incorrect** value into the field where the **missing** value was. An example is entering the *starting elevation* in both the *starting elevation* and *elevation change* fields.

Upon combing through the table I had downloaded, I identified these errors and corrected them by either updating the values to the correct values or correctly labeling the errors as missing data.

As I began to prepare for modeling, I recognized only a subset of all the hikes in the table had all the features I would be comparing. Thus, I ultimately reduced my table to 1,015 hikes (of the original 3,555) that were suitable for my models.

## Modeling

This was also my first time using a Linear Regression model. I used the `sk-learn` libraries to implement the modeling techniques. However, more important to me in this experience was understanding exactly what was happening beneath the hood of the code I was writing.

To begin, I used the customary method of randomly splitting my modeling data into two subsets: the **training** set is used for modeling and the **test** set is only used afterward to test how well the model does on data it has never seen.

I began by testing with a simple Ordinary Least Squares regression. This essentially tries to draw a "best-fit line" through all the data points. Unfortunately, but quite expectedly, this model performed poorly. The next approach was to transform the simple line model by viewing what happened if certain features were multiplied by each other. Essentially, this would help weight hikes if they had both a "Coast" and were "Kid friendly" at the same time, as opposed to the previous model **only** looking at "Coast" and "Kid friendly" individually.

Ultimately, a 2nd degree polynomial element was used as well as a *regularization* technique called Elastic Net which affectively dampens some of the features in the model and amplifies others based on how meaningful the model determines them to be.

This model scored an R<sup>2</sup> of 0.24 on the training data and 0.18 on the holdout test set (to see how well it did against unseen this data). Two big insights jump out from this.
* Firstly, a score of 0.18 on new data implies the model **only** explains 18% of the variability of the predicted "rating". Essentially, the model doesn't do a great job. However, it does hold some predictive value and is better than a random guess.
* Secondly, the difference in R<sup>2</sup> values between test and training sets is relatively small. This indicates the model is not *overfitting* too greatly, and thus can be applied to hikes it has never seen before and still be of use.

## Future Work

Although time constraints and the pace of this [Metis](https://thisismetis.com) program do not allow me to currently improve the model (we're already on the next project!), there are some clear steps I would like to take in the future:
1. Transform both the target (rating) and continuous features before modeling. This would aid in "unpacking" a high concentration of features that are skewing the model toward predicting between 3-5, and not so much between 1-3.
2. Instead of predicting rating, trying to predict either the number of votes or the number of trip reports. These two variables could be considered "proxys" for popularity of the hike.
3. Alltrails.com has quite a bit of extra data for many of the hikes in the wta.org database and would be good additions to the dataset.
4. More tuning of the models and attempt to use more models. After this project was copmleted, I spent a little bit of time using a Random Forest Regressor, which prematurely was displaying better results than the Elastic Net model.

I hope you enjoyed! Although a lot in this model process could certainly be improved, it was a blast and an accomplishment to both scrape a website and use the data to create my first Linear Regression model.



































# Project Luther - Predicting a Hike's Rating
## Spencer Tollefson
## October 12, 2018

# Project Design
WTA.org is a website that has a database of 3,555 hikes (at the time of scraping) which includes hike details, trip reports, and a voting system allowing users to rate a scale on a scale of 1-5. The idea of this project was to see if the given information in this database would allow one to predict how highly a hike scored on the voting system. A good model potentially could aid "trail planners" with the foresight to predict how well-liked a newly opened hike would do before they invested in creating the trail.

Although I originally hoped to use nearly all the features I scraped as well as create some new ones, time constraints did not allow in time for project completion. Chiefly, the lat/long coordinates and sub-regions of the hikes both offer unique insights and were not incorporated in my models. Additionally, using other sources of data such as weather patterns/history and alltrails.com were skipped due to time constraints.

Initially, I hoped to create the model without using features that a trail planner would not have access to: such as the use of how many times people had rated a trail and the number of trip reports that were left for the trail. After some simple linear regressions built with those features excluded, it became clear the model had little value. Thus, I decided to use all data available to me.

This project, at different points, used the following models: OLS, Polynomial Regression, Lasso, Ridge Regression, Elastic net, and a taste of Random Forest Regression (with an instructor post-presentation). Cross validation with numerous folds were used on training data for each of these models and later compared with the test data to see how well the model performed on out-of-sample data. All of the best performing models adopted a Polynomial Tranformation of the 2nd degree. The best performing  model was an Elastic Net model tuned to 0.1 L1 and 0.9 L2, measured by an R^2 value of .183. Additionally, a pure Lasso regularization returned a value of .18 and a pure Ridge Regression of .16. However, the Elastic Net returned the lowest difference between training data and the hold-out test set of data with only a .04 difference in R^2. This slight difference in R^2 between test and training indicates it likely had a better fit to the data than the other models. 

The used model suggested that hikes on the coast, with summit points, and a sizable length were indiciative of people giving a high rating for the hike. However, of equal interest was how much the rest of individual features did **not* correlate to a high or low score. This leads to the belief that perhaps different features would have more predictive value than only the ones evaluated. The number of trip reports for a given hike is the strongest factor indicating a positive rating, however given this is intuitive and nearly a proxy for popularity I tried to stray away from focusing on it.

# Tools
* Python:
  *Web scraping: requests, beautifulsoup
  *Data storage: pandas, pickle
  *Data analysis: numpy, pandas, scikit-learn, Jupyter
  *Presentation: matplotlib, seaborn
* Libreoffice Impress

# Data

The data was obtained by scraping WTA.org. The website had pages for 3,555 unique hikes at the time of scraping on October 4, 2018. Each page containd the name of the hike, an embedded Google Maps window, the hiker trip reports for the hike, as well as a number of characteristics such as hike length, elevation gain, if the hike contained features such as coast/old growth forest/campsites/wildflowers, and even coordinates of the trailhead among other features.

All the features can be found in the Appendix. Notably, the Region and Fee categories required preprocessing to manipulate from one column into many one-hot encoded columns. This increased the number of features a total of 37 analyzed by the models. Scikit-learn techniques made it simple with little overhead to parse out the unique features in these columns and build the model outward.

The number of vote and number of trip report features were highly correlated. In order to prevent confusing my model, I chose to eliminate the number of votes feature due to this concern. 

# What I Would Do Differently

To give my model real value, I would have liked to remove any features which are only available post-hike creation. Ideally, this model could help "hike creators" plan where to create the trail for another hike. They would not have access to features such as the number of trip reports of a hike. However, this feature aided the model so much I chose to keep it for the sake of this project.

I would have taken a closer look at the raw distribution of "rating" pre-modeling. It turns out the rating is heavily left-skewed with a higher percentage of hikes receiving scores in the 3-5 range and fewer in the 1-3 range. By applying a transformation before modeling, it could help tease out and better understand the features that lead to sub-3 hike scores.

More charts during the modeling and EDA phase of residuals, Q-Q, and individual feature histograms would aid in understanding the underlying interaction between feature and target better.

Post-presentation I was introduced to Random Forest Regression and saw markable improvements on my model. I am interested in exploring this technique farther.
