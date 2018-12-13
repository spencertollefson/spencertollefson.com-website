TSA. The much aligned TSA. The organization doesn't have the best reputation. People don't arrive at their destination then exclaim how *fantastic* of a time they had passing through airport security. Rather, people grumble about security wait lines, how they watched their dignity stripped away from their eyes, or perhaps what they think is pointless "security theater" that isn't serving any *real* purpose. It's less frequent that someone's carry-on or checked items are damaged or lost (maybe stolen?) at some point in the TSA screening processes. But when it does happen, what do they do?

<img src="/static/blog/images/006-tsa-claims/tsa-claims-form.png" class="img-fluid" alt="Form SF-95: the TSA Tort Claims Package" title="Receipts? Appraisal values? Insurance information? That's a lot to ask for." style="width:800px; max-width:98%; border:1px solid black;">
<p style="text-align: center;font-size:80%"><b>The 5 page TSA claims form.</b></p>

When a passenger suspects TSA is at fault for damaged or lost luggage, there is a formal claims process entailing completing a 5-page document and sending to TSA for a verdict. (Ignoring the obvious bias issue in that TSA is judge, jury, and executioner in this role, let's move on). The claims form requests standard contact information, a description of the incident and damaged/lost item(s), and how much money the claimant is seeking as compensation. But that's not all. The TSA also inquires about names and contact information of any witnesses (if there were some), the claimant's personal insurance information, purchase receipts of the property, as well as appraisal values of said items. That's a lot!  The TSA claims office then reviews the claim and either **denies** it, **approves it in full**, or **settles** it by granting a payout less than what was asked.

Whew. That's a lot. A question anyone going through this process asks themselves in some way or another at some point is "Is this worth my time and effort?" I set out to attempt and answer this question.

## Data

The *U.S. Department of Homeland Security*, TSA's parent organization, [publicly publishes all 200,000+ claims](https://www.dhs.gov/tsa-claims-data) since the organization's inception in 2002. Included in this dataset are the **date of incident** and the **date claim received by TSA**, **passenger's airline**, **airport name**, **incident type**, **item category** (if a damaged/lost item), **outcome**, and **compensation awarded** for each claim filed. I extracted the continuous variable of *days waited to file claim* by subtracting the incident date from the claim received date.

After some exploratory analysis, I decided to parse down the 370+ airports, 190+ item categories, and 170+ airlines. Most of the claims consisted of only small subset of each of these. I pulled data from the [Federal Aviation Authority (FAA)](https://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/) to prioritize the airports with most passenger boardings in 2017. I then selected the top 14 airports in the TSA dataset and consolidated similar item categories down into a list of 140.

With this slimmer set of data, I defined a **successful** claim as one where the claimant won the **amount in full** or *settled* amount of compensation. This simplified the outcomes into a binary case. After cleaning the dataset with these constraints, I ended up with about 90,000 claim requests ready for modeling.

## Modeling

Shoutout to [Yandex's Catboost Classifier](https://tech.yandex.com/catboost/)! This model performed best on my cross-validated holdout data among a variety of other models, including Logistic Regression, Random Forest, XGBoost, and Support Vector Machines. It is a Gradient Descent of Decision Trees algorithm that specializes in handling large amounts of categorical features.

Although far from perfect, the Catboost fit model showed predictive value in classifying any given claim as a success or failure. This ultimately tied back to my original question: **can someone quickly determine if filing a claim is even worth their time and effort?**

## Web App

Finally, the visual part! I used Flask and some light JavaScript code to render my model in a browser-friendly GUI. The simple webpage asks someone for features the model uses to determine probability of receiving compensation from TSA. In a visual plot, it returns to the user the probability of a refund and a recommendation of how many days to wait to file their claim. [You can try it yourself here](https://spencertollefson.com/tsa-claim-outcome-prediction).

# Conclusion

The TSA has more data. They ask form filers for witnesses, a text description of the event, any TSA statements, if the claim contains any refund or appraisal values. I'd *love* to get this data as I believe it would greatly improve model performance.

In the mean time, I'll continue to carry-on my bags to minimize the chance of any bag related issues during my travels.

[Github code for this project and all acknowledgements can be found here](https://www.github.com/spencertollefson/tsa_claims).