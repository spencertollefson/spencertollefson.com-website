For my second overall and first solo project at [Metis](https://thisismetis.com), the task was to web scrape data and then use it to conduct a Linear Regression analysis. As a big fan of hiking and recently coming back from an overnight weekend backpacking trip, I thought I would turn this task into something of interest to me: **predicting a hike's "rating" as voted on by hikers themselves**.

## Project Design
[WTA.org](https://wta.org) is a website that has a database of 3,555 hikes (at the time of scraping) which includes hike details, trip reports, and a voting system allowing users to rate a hike on a scale of 1-5. The goal of this project was to use the given information in the database to create a model able to accurately predict a hike's rating based on its attributes. A good model potentially could aid trail planning authorities with the foresight to predict how well-liked a newly opened hike would be before they invested in creating the trail.

## Approach
  
#####   1. Scrape data from all 3,555 hike pages on [wta.org](https://wta.org)
#####   2. Clean "dirty" data to be ready for model use
#####   3. Perform Linear Regression modeling
<br>

Although I originally hoped to use nearly all the scraped features as well as engineer some new ones, time constraints and incomplete data did not allow for it. Chiefly, the lat/long coordinates and sub-region (location) of the hikes both offered unique insights and were not incorporated in the models. Additionally, using other sources of data such as weather patterns/history and [alltrails.com](https://alltrails.com) were passed on due to time constraints.

Initially, I wanted to create the model without using features that a trail planner would not have access to: such as how many times people had rated a trail and the number of trip reports that were left for a trail. After some simple linear regressions built with those features excluded, it became clear the model had little value. Thus, I decided to use all data available to me for this project.

## Process
-----

### Scraping

This was my first foray into scraping. I think I'm hooked. I used the `requests` and `BeautifulSoup` python libraries to get the job done. I took a look at `selenium` as well, but then recognized the aforementioned tools would be just as good in this case. 

<img src="/static/blog/images/003-wta-predict-post/wta_page.png" class="img-fluid" alt="Screenshot of a typical WTA hiking page" title="Every Seattleite's favorite: Rattlesnake Ledge" style="border:1px solid black;height:700px">
<p style="text-align: center;font-size:80%"><b>Orange circles: some of the hike attributes scraped -- Blue box: the hike's rating</b></p>

The WTA pages had well labeled HTML tags consistent across the different hike pages. Once I thoroughly dissected a few pages and identified how the hike attributes (elevation gain, length of hike, region, and presence of coasts/lakes/mountains/etc) were encoded, I wrote a python script that found those features, pulled their information, and saved it to a table in a `pandas DataFrame`. In all, the script ran for over an hour and ended up accessing all 3,555 hike pages.

### Cleaning

As the sage old data science lore has it: *there is no such thing as clean data*. (Mostly true, unless it's from [kaggle.com](https://kaggle.com) or another similar source). I found this to be the case with my data. Many hike pages were incomplete and missing some attributes information. My script sometimes correctly identified these fields as "missing", while other times it substituted an **incorrect** value into the field where the **missing** value was. An example is entering the *starting elevation* in both the *starting elevation* and *elevation change* fields.

Upon combing through the table I had downloaded, I identified these errors and corrected them by either correctly updating the errant values or labeling the bad fields as missing data.

As I began to prepare for modeling, I recognized that only a subset of hikes in my downloaded table had all features I would be comparing. Thus, I ultimately reduced my table to 1,015 hikes (of the original 3,555) that were suitable for modeling.

<img src="/static/blog/images/003-wta-predict-post/pandas_df.png" class="img-fluid" alt="Sample table of scraped WTA data" title="Hikes aren't quite as fun when they're just words and numbers, huh?" style="border:1px solid black;">
<p style="text-align: center;font-size:80%"><b>Small sample of the table containing all the hikes' data</b></p>

## Modeling

This was also my first time using a Linear Regression model. I used the `sklearn` libraries to implement the modeling techniques. However, more important to me in this experience was understanding exactly what was happening beneath the hood of the code I was writing. My class received extensive lectures for a few weeks discussing the concepts behind Linear Regression modeling and what was going on at a granular level. This proved quite helpful for both interpreting model results and debugging issues.

To begin, I used the customary method of randomly splitting my modeling data into two subsets: the **training** set used for modeling and the **test** set only used afterward to evaulate how well the model does on data it has never seen.

I began by testing with a simple Ordinary Least Squares regression. This essentially tries to draw a "best-fit line" through all the data points. Unfortunately, but quite expectedly, this model performed poorly. The next approach was to transform the simple line model by viewing what happened if certain features were multiplied by each other. Essentially, this would help weight hikes if they had both a "Coast" and were "Kid friendly" at the same time, as opposed to the previous model **only** looking at "Coast" and "Kid friendly" individually.

<img src="/static/blog/images/003-wta-predict-post/hike_bar.png" class="img-fluid" alt="Bar chart of number of hikes containing certain features" title="News alert: Washington has a lot of mountains." style="border:1px solid black;height:450px">
<p style="text-align: center;font-size:80%"><b>Bar chart showing the number of hikes (out of 1,015) that contained these features</b></p>

Ultimately, a 2nd degree polynomial transformation was used as well as a *regularization* technique called Elastic Net, which affectively dampens some of the features in the model and amplifies others based on how meaningful the model determines them to be.

This model scored an R<sup>2</sup> of 0.24 on the training data and 0.18 on the holdout test set (to see how well it did against unseen this data). Two big insights jump out from this.

* Firstly, a score of 0.18 on new data implies the model **only** explains 18% of the variability of the predicted "rating". Thus, it doesn't explain the other 82%. Essentially, the model doesn't do a great job. However, it does hold some predictive value and is better than a random guess.

* Secondly, the difference in R<sup>2</sup> values between test and training sets is relatively small. This indicates the model is not *overfitting* too greatly, and thus can be applied to hikes it has never seen before and still be of use.

<img src="/static/blog/images/003-wta-predict-post/spencer_pondering.png" class="img-fluid" alt="Me on a hike, pondering what a perfect model looks like." title="Extra points for the view? Subtract points for the clouds?" style="border:1px solid black;height:450px">
<p style="text-align: center;font-size:80%"><b>Pondering a perfect model to predict this hike's rating</b></p>

## Future Work

Although time constraints and the pace of this [Metis](https://thisismetis.com) program do not allow me to currently improve the model (we're already on the next project!), there are some clear steps I would like to take in the future:

1. Transform both the target (rating) and continuous features before modeling. This would aid in "unpacking" a high concentration of features that are skewing the model toward predicting between 3-5, and not so much between 1-3.

2. Instead of predicting rating, trying to predict either the number of votes or the number of trip reports. These two variables could be considered "proxies" for popularity of the hike.

3. [Alltrails.com](https://Alltrails.com) has quite a bit of extra data for many of the hikes in the [wta.org](https://wta.org) database and may be helpful to scrape its data as well.

4. More tuning of the models and attempting to use more models. After this project was completed, I spent a little bit of time using a Random Forest Regressor model, which prematurely was displaying better results than the Elastic Net model!

I hope you enjoyed! Although a lot of my modeling process stands to be improved, it was a blast and an accomplishment to both scrape a website and use the data to create my first Linear Regression model.

All code for this model may be found [here](https://github.com/spencertollefson/WA-trails-rating-prediction).
