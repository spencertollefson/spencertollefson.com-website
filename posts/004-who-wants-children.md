OkCupid.com is an online dating platform catered toward single adults who are seeking romantic partners. For a monthly fee - varying based on the amount of bells and whistles a user desires - customers create a dating profile to present themselves to others who are (mostly) looking to date. This post covers my experience using OkCupid profiles to *predict* how likely someone is to want to raise children. Exciting? Yes. Ethical? Lots of questions there. Let's get to it.

<img src="/static/blog/images/004-images/okcupid_logo.png" class="img-fluid" alt="OkCupid.com Logo" title="'Dating deserves better.' " style="width:100%">

## Motivations

My goal was to create a classification model. Upon finding this [github repo](https://github.com/rudeboybert/JSE_OkCupid) authored by Albert Y. Kim and Adriana Escobedo-Land containing a dataset of nearly 60,000 anonymized OkCupid.com profiles, I took a deep dive through the dataset's features. Among many interesting topics of comparison such as astrology, religion, and habits of smoking tobacco, drinking, and drugs, was the optional field to indicate if one **would like to raise children** in the future.

<img src="/static/blog/images/004-images/okcupid_profile2other.png" class="img-fluid" alt="Example details from OkCupid profile" title="Definitely not a cat person." style="width:100%">
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

Next came modeling. I implemented a variety of different classifier models on the training data after conducting a standard train, test, and split procedure. I found that by upsampling the minority target class - individuals who did not want children - using the SMOTE technique provided better results. The AUC ROC scores for the various best models when used on unseen holdout data are below:

<img src="/static/blog/images/004-images/AUC_score_comparison.png" class="img-fluid" alt="Comparison of AUC scores among different models" title="While gradient boosting was best, it wasn't by much." style="width:100%">
<p style="text-align: center;font-size:80%"><b>Comparison of model performed as measured by AUC ROC.</b></p>


I plotted the best performing model, a Gradient Boosting implementation, below. For the uninitiated, the model is the pink curved line and is considered to generally score better the closer it hugs the top left corner. The grey dotted line is what one would expect from someone trying to classify if someone wants children randomly. [See here for a great explanation of the AUC ROC.](https://www.dataschool.io/roc-curves-and-auc-explained/)

<img src="/static/blog/images/004-images/best_gb_ROC_plot.png" class="img-fluid" alt="Plot of gradient boosting AUC" title="" style="width:100%">

Back to the data. I chose to exclude the knowledge of someone **already having children** from my model input, as it is likely that people who do not reveal their desire for children also do not share if they already have children.

Interestingly, training a separate model with this feature included resulted in a sizable increase in AUC ROC. This time it was a support vector machine (SVM) implementation that did best. The chart below compares the new model to the last one.

<img src="/static/blog/images/004-images/both_models_ROC_plot.png" class="img-fluid" alt="Comparison plot of AUC score" title="There's a noticeable improvement of the SVM implementation" style="width:100%">
<p style="text-align: center;font-size:80%"><b>Notice the sizable gap between the pink (original model) and blue (model using knowledge of "current children")</b></p>

# Conclusion

The model has some real value! The confusion matrix below shows how the model classified 1,395 people it had never seen before at a probability = 0.5 threshold. It correctly classified 648 "do not want children" and 438 "do want children" and had fairly balanced misclassifications.

<img src="/static/blog/images/004-images/ConfusionMatrixCount.png" class="img-fluid" alt="Confusion matrix of classifier applied to unseen data." title="Optical illusion?" style="width:100%">

It must not be forgotten that it was built upon some rather heavy assumptions, including that everyone in the dataset is also someone who:

* Is an OkCupid.com user, near San Francisco, in 2011

* Is willing to reveal on their profile if they do or do not want children

* Honestly provided their profile information

* Is certain about their child preferences

Certainly there are more assumptions too. To improve upon the robustness of the model and its ability to generalize to a greater population, more work is needed. More data from different locations, time periods, and certainty in their honest would all aid in a better model.

NOTE: As of now, I have not created an environment for people to test out the model themselves. I hope to create a website which will allow people to apply the model. If so, this post will be updated.

Checkout all my code and more explanation [here.](https://github.com/spencertollefson/okcupid_classification)