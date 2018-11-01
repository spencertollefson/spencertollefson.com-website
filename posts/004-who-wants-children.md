OkCupid.com is an online dating platform catered toward single adults who are seeking romantic partners. For a monthly fee - varying based on the amount of bells and whistles a user desires - customers create a dating profile to present themselves to others who are (mostly) looking to date. This post covers my experience using OkCupid profiles to *predict* how likely someone is to want to raise children. Exciting? Yes. Ethical? Lots of questions there. Let's get to it.

## Motivations

My goal was to create a classification model. Upon finding this [github repo](https://github.com/rudeboybert/JSE_OkCupid) authored by Albert Y. Kim and Adriana Escobedo-Land containing a dataset of nearly 60,000 anonymized OkCupid.com profiles, I took a deep dive through the dataset's features. Among many interesting topics of comparison such as astrology, religion, and habits with smoking tobacco, drinking, and drugs, was the optional field to indicate if one **would like to raise children** in the future.

That caught my eye. As I've been aging past the mid-20s, I've become more aware how many people in my demographic discuss making a decision on this subject. The spectrum covers the range between people certain they want kids, others adamant they never do, and of course everything in between. Relatedly, when it comes to dating, for Jane Doe the pool of eligible partners can be reduced if she knows right off the bat if her potential partner feels the same way as she does about having children. Thus, I set out to build a classifying model to predict the probability someone desires kids based on other attributes contained in online dating profiles.

-----

A model that performs well in predicting one's desire to raise children has multiple potential uses. Potential uses for a high performing model include, but are not limited to, the following:

* Available on a web app where one may input information to output the  probability that the individual wants to have children.

* Improve matchmaking capabilities of dating services.

* **Ethical alert:** Health insurance companies to decide how likely it is their customers will have children in the future.

* **Ethical alert:** HR departments of various companies to determine how likely a potential or current employee will have children and thus need paternity or maternity leave.

## Analysis

After cleaning the dataset (this occupied half of my time on the project itself), I weighed which metrics to choose to compare the various models I would create. I ended up choosing Area Under an ROC Curve (AUC ROC) as my metric of choice for the following reasons:

* My classifier was binary (want children vs. do not want children) 

* It does well with balanced data sets (my data for modeling was split 40% wanting children, 60% not wanting children)

* It accounts for all given probability thresholds, which allows various model users to choose how much tolerance for false positives they like

Next came modeling. I implemented a variety of different classifier models on the training data after conducting a standard train, test, and split procedure. I found that by upsampling the minority target class - individuals who did not want children - using the SMOTE technique provided better results. The AUC ROC scores for the various best models when used on unseen holdout data are below:

INPUT BARPLOT HERE

I plotted the best performing model, a Gradient Boosting implementation, below. For the uninitiated, the model is the pink curved line and is considered to generally score better the closer it hugs the top left corner. The grey dotted line is what one would expect from someone trying to classify if someone wants children randomly. [See here for a great explanation of the AUC ROC.](https://www.dataschool.io/roc-curves-and-auc-explained/)

INSERT AUC HERE

Back to the data. I chose to exclude using the feature of knowing if someone **already had children** from my model input, as the data showed people who had 

All features may be found in the appendix. Cleaning was applied to many columns to account for grouping of multiple subjects. This in effect became the only form of feature engineering I applied to the data. For example, the original data grouped religious intensity (serious, not serious, no care at all) and the name of the religion together. By cleaning I separated these two subjects and considered them separate features.

Ethical questions bombarded me as I dealt with this data set and the entire project. Is it ethical to create a model to help people "screen out" others while dating? How about using ethnicity, religious, and sexual orientation as features for deciding if someone wants to have children? How about the people whose profiles were used as the data observations?

While I did not delve too deeply into the implications due to time constraints and the likelihood that this project would not go viral, it did make me think about this data.