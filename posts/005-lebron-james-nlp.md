I love the NBA. Evening time and I'm at home? Flip on a basketball game. Out with friends on a weekend? Let's watch a game. It's a hobby. And why shouldn't it be? I don't think I'm over reaching when I say the NBA has never been more marketable and has more recognizable players than ever before. Heads and shoulders above all the other current players when it comes to stardom, however, is LeBron James. I admire the man for what he demonstrates on the court night after night, but also for the way he, generally (but not without exceptions),  tastefully and impactfully wields his voice to weigh in on issues outside of basketball.

LeBron lives under a microscope. His tweets, post-game interviews, family outings, nightly basketball performances, choice of sneakers, are all discussed by pundits on television, on internet forums, and by people everywhere on a 24/7 basis. knowing this, I decided I wanted to use machine learning techniques to see what kind of insights I could pry from **what people are discussing when they discuss LeBron**.  I got my hands on LeBron-centered reddit comments and put Natural Language Processing (NLP) techniques to the task at hand.

Continue reading for my exploration of the types of words, language, and topics that  internet denizens discuss when they're talking about LeBron.

## Data

While I heavily considered Twitter due to the quantity of and ease of accessing its data, I chose to get posts from [reddit.com/r/nba](https://www.reddit.com/r/nba) as my data source. I hav ea good intuition for the data as I often read and occasionally post on the platform. The r/nba subreddit is quite popular with over 1.42 million subscribers at the time of writing - making it the most subscribed to subreddit. 

People discuss all things NBA related on the subreddit, and unsurprisingly that means LeBron is discussed often. Using some awesome tools which may be found in my [github repo](https://github.com/spencertollefson/lebron_james_nlp) for this project, I pulled over 45,000 reddit comments to analyze. The comments selected were the most highly upvoted (a reddit user-based scoring system) for submissions for posts with "LeBron", a variation of his name, or a nickname in the title. I intended for this heuristic of selecting comments to be a proxy for the general pulse of the entire r/nba community.

## Topic Modeling

After obtaining the data, the next step was to transform it into a suitable format for NLP techniques. This is referred to as *preprocessing*. The text is all converted to lowercase, most punctuation removed, limited to English language words, removing non-important words dubbed *stop words*, then *lemmatized* and *stemmed*. Lemmatization and stemming essentially boil a word down into it's root form. *Running*, *ran*, and *runs* all are destilled into *run* for consistency.

Next, the data is converted into a document-term matrix of numbers in a *bag of words* friendly-format. Numbers means we can model it! I applied the popular generative statistical model **Latent Dirichlict Allocation (LDA)** to the matrix to squeeze out the best results. LDA, in a simplified sense, discovers topics within text. I liked the explanation of LDA [here]().  After supplying my LDA model with all of the reddit comments and the number of topics I am seeking, I eventually got some meaningful (and not meaningful) topics out of it:

<<<<<<LDA TOPICS HERE>>>>>>

This is prety cool! You can see some of the comments prescribed to a few of the topics like this:



I applied non-negative matrix factorization (NMF), a linear algebra based approach, to my vector of words as well to gather topics. The results weren't bad either:


NMF RESULTS


To keep going with this unsupervised learning tear, I went back to my LDA output and applied a K-Means clustering to the probability distribution. This categorized each of my reddit comments into one of 17 categories. Upon looking at various comments from each categories - I again was able to clearly find themes for some categories, but garbage for the others. Interestingly, *jokes/puns/quips* type of comments made up a large majority of all comments. These things scored highly among other redditors.

<<< PLOT OF K MEANS SIMILARITIES HERE>>>

Finally, I wanted to take a different approach than topic modeling and was curious to gauge the general sentiment of commenters over time. I used a pre-trained sentiment analyzer model, vader, to gauge the **positive, neutral, and negative** content within each comment. The chart below shows the average sentiment for the comments grouped by week.

<<<<<WEEKLY SENTIMENT CHART>>>>>


 At any given week, the 3 lines will sum to a value of 1. As you can see, most weeks the comments tend to be about 80% neutral, meaning they don't have much positive nor negative expression in them. They also tend to be generally a little more positive than negative.

 A real interesting insight can be found at the two weeks in summer of 2012 where **positivity** spikes. This corresponds to when Lebron won his first NBA finals championship. It seems r/nba redditors were full of saying good things then!

 ## Conclusion

 It was fun to get my hands on some of the reddit data I frequently read myself. While I initially dove into this project thinking that NLP techniques would be simple to apply, I found that was not the case! It took some wrangling, munging, and clever techniques to eventually get the text data into a format that played nicely with NLP. Even then, tweaking with different *stop words*, stemming techniques, and the number of LDA topics was a difficult process that often resulted in partially but not fully satisfying results.

 In the future I would like to improve upon some of the aforementioned technicalities in implementing NLP techniques with topic modeling. Additionally, limiting my data to longer comments would likely reduce the number of jokes and increase the ratio of insightful comments. My heuristic of choosing posts with "LeBron" in the title likely isn't entirely representative of how the r/nba community feels about LeBron, and it would behoove the generalization value of my models to look at all r/nba posts - not LeBron only ones - and then focus on comments related to LeBron.

 [Github code for this project and all acknowledgements can be found here].

 Remember, we're lucky to live in the day and age we can watch LeBron play basketball. Don't miss out! #WeAreAllWitnesses
















<img src="/static/blog/images/004-images/okcupid_logo.png" class="img-fluid" alt="OkCupid.com Logo" title="'Dating deserves better' " style="width:400px;max-width:95%">

## Motivations

My goal was to create a classification model. Upon finding this [github repo](https://github.com/rudeboybert/JSE_OkCupid) authored by Albert Y. Kim and Adriana Escobedo-Land containing a dataset of nearly 60,000 anonymized OkCupid.com profiles, I took a deep dive through the dataset's features. Among many interesting topics of comparison such as astrology, religion, and habits of smoking tobacco, drinking, and drugs, was the optional field to indicate if one **would like to raise children** in the future.

<img src="/static/blog/images/004-images/okcupid_profile2other.png" class="img-fluid" alt="Example details from OkCupid profile" title="Definitely not a cat person." style="width:300px;max-width:88%">
<p style="text-align: center;font-size:80%"><b>Some details from a sample OkCupid.com profile. The "offspring" field optionally allows users to share if they desire children.</b></p>

That caught my eye. As I've been aging past the mid-20s, I've become more aware how many people in my demographic discuss making a decision on this subject. The spectrum covers the range between people certain they want kids, others adamant they never do, and of course everything in between. Relatedly, when it comes to dating, for Jane Doe the pool of eligible partners can be **_reduced_** if she knows right off the bat if her potential partner feels the same way about having children as she does. Thus, I set out to build a classifying model to predict the probability someone desires kids based on other attributes contained in online dating profiles.

-----

A model that performs well in predicting one's desire to raise children has multiple potential uses. Potential uses for a high performing model include, but are not limited to, the following:

* A web app where one may input information to output the  probability that the individual wants to have children

* Improve matchmaking capabilities of dating services

* **Ethical alert:** Health insurance companies to decide how likely it is their customers will have children in the future

* **Ethical alert:** HR departments to determine how likely a potential or current employee will have children and thus need paternity or maternity leave

## Analysis

Cleaning the dataset required decision making. There were various ethical questions, such as using religion, sexual orientation, ethnicity, and other features as inputs. Additionally, I wanted to create a model with as many features that people are freely willing to share. For example, sex and age. Upon cleaning the data, deriving a few new features from "messy" text (i.e. religious intensity and horoscope importance), and filtering only to people who revealed if they **do** or **do not** want children, the data was ready for modeling.

I weighed which metrics to choose to compare the various models I would create. I ended up choosing Area Under an ROC Curve (AUC ROC) as my metric of choice for the following reasons:

* My classifier was binary (want children vs. do not want children) 

* It does well with balanced data sets (my data for modeling was split 40% wanting children, 60% not wanting children)

* It accounts for all given probability thresholds, which allows whoever uses the model to choose their tolerance to false positives

Next came modeling. I implemented a variety of different classifier models on the training data after splitting the data into training set and a holdout test set. I found that by upsampling the minority target class - individuals who did not want children - using the SMOTE technique provided better results. The AUC ROC scores for the various best models when used on unseen holdout data are below:

<img src="/static/blog/images/004-images/AUC_score_comparison.png" class="img-fluid" alt="Comparison of AUC scores among different models" title="While gradient boosting was best, it wasn't by much." style="max-width:95%">
<p style="text-align: center;font-size:80%"><b>Comparison of model performed as measured by AUC ROC.</b></p>


I plotted the best performing model, a Gradient Boosting implementation, below. For the uninitiated, the model is the pink curved line and is considered to generally score better the closer it hugs the top left corner. The grey dotted line is what one would expect from someone trying to classify if someone wants children randomly. Does model does fairly well; there's a sizable gap between it and the grey line. [See here for a great explanation of widththe AUC ROC.](https://www.dataschool.io/roc-curves-and-auc-explained/)

<img src="/static/blog/images/004-images/best_gb_ROC_plot.png" class="img-fluid" alt="Plot of gradient boosting AUC" title="" style="max-width:95%">

Back to the data. I chose to exclude the knowledge of someone **already having children** from my model input, as it is likely that people who do not reveal their desire for children also do not share if they already have children.

Interestingly, training a separate model with this feature included resulted in a sizable increase in AUC ROC. This time it was a support vector machine (SVM) implementation that did best. The chart below compares the new model to the last one.

<img src="/static/blog/images/004-images/both_models_ROC_plot.png" class="img-fluid" alt="Comparison plot of AUC score" title="There's a noticeable improvement of the SVM implementation" style="max-width:95%">
<p style="text-align: center;font-size:80%"><b>Notice the sizable gap between the pink (original model) and blue (model using knowledge of "current children")</b></p>

# Conclusion

The model has some real value! The confusion matrix below shows how the model classified 1,395 people it had never seen before (probability = 0.5 threshold). It correctly classified 648 "do not want children" and 438 "do want children" and had fairly balanced misclassifications.

<img src="/static/blog/images/004-images/ConfusionMatrixCount.png" class="img-fluid" alt="Confusion matrix of classifier applied to unseen data." title="Optical illusion?" style="max-width:95%">

It must not be forgotten that this model is built upon some rather heavy assumptions, including that everyone in the dataset is also someone who:

* Is an OkCupid.com user, near San Francisco, in 2011

* Is willing to reveal on their profile if they do or do not want children

* Honestly provided their profile information

* Is certain about their child preferences

Certainly there are more assumptions too. To improve upon the robustness of the model and its ability to generalize to a greater population, more work is needed. Additional data from different locations, time periods, and certainty in their honest would all aid in a better model.

NOTE: As of now, I have not created an environment for people to test out the model themselves. I hope to create a website which will allow people to apply the model. If I do so, this post will be updated.

Checkout all my code and more explanation [here.](https://github.com/spencertollefson/okcupid_classification)