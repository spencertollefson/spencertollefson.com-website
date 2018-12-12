I love the NBA. Evening time and I'm at home? Flip on a basketball game. Out with friends on a weekend? Let's watch a game. Visiting a city that ACTUALLY HAS an NBA team (rip Sonics, I'll never forget you)? See if I can score tickets. It's a hobby. And why shouldn't it be? I don't think I'm over reaching when I say the NBA has never been more marketable and has more recognizable players than ever before. Heads and shoulders above all the other current players when it comes to stardom, however, is LeBron James. I admire the man for what he demonstrates on the court night after night, but also for the way he, generally (but not without exceptions), tastefully and impactfully wields his voice to weigh in on issues outside of basketball.

<img src="/static/blog/images/005-lebron-images/lebron_shorts_suit.jpg" class="img-fluid" alt="LeBron James." title="" style="width:1000px;max-width:98%">
<p style="text-align: center;font-size:80%">

LeBron lives under a microscope. His tweets, post-game interviews, family outings, nightly basketball performances, choice of suit (see his "shorts suit", above), and other rudimentary activities are all discussed by television talking heads, in internet forums, and by people in casual conversation everywhere on a 24/7 basis. Knowing this, I decided I wanted to use machine learning techniques to see what kind of insights I could pry from **what people are discussing when they discuss LeBron**.  I got my hands on LeBron-centered reddit comments and put Natural Language Processing (NLP) techniques to the task at hand.

Continue reading for my exploration of the types of words, language, and topics that  internet denizens discuss when they're talking about LeBron.

## Data

While I heavily considered analyzing Twitter tweets about LeBron due to the quantity of and ease of accessing its data, I chose to pull comments from [reddit.com/r/nba](https://www.reddit.com/r/nba) as my data source. I have a good intuition for the data as I often read and occasionally post on the platform. The r/nba subreddit is quite popular with over 1.42 million subscribers at the time of writing - making it the most subscribed to sports subreddit.

People discuss all things NBA related on the subreddit, and unsurprisingly that means LeBron is discussed often. Using some awesome tools which I reference in the [github repo](https://github.com/spencertollefson/lebron_james_nlp) for this project, I pulled over 45,000 reddit comments to analyze. The comments selected were the most highly "upvoted" comments (a reddit user-based scoring system) from submissions with "LeBron", a variation of his name, or one of his nickname's in the title. I intended for this method of selecting comments to be a proxy of the general pulse of how the entire r/nba community feels about LeBron.

## Topic Modeling

After obtaining the data, the next step was to transform it into a suitable format for NLP techniques. This is referred to as *preprocessing*. Convert all text to lowercase, remove most punctuation, limit to English language words, ignore non-important words (dubbed *stop words*), then *lemmatize* and *stem* all remaining words. Lemmatization and stemming essentially boil a word down to its root form. *Running*, *ran*, and *runs* all are distilled into *run* for consistency.

#### Latent Dirichlict Allocation (LDA)

Next, the data is converted into a document-term matrix of numbers in a *bag of words* friendly-format. Numbers means we can model it! I applied the popular generative statistical model **LDA** to the matrix to squeeze out the best results. LDA, in a simplified sense, discovers topics within text. I liked the explanation of LDA [by Edwin Chen in his post here](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/).  After supplying my LDA model with all of the reddit comments and the number of topics I am seeking, I eventually got some meaningful (and not meaningful... aka garbage) topics:

<img src="/static/blog/images/005-lebron-images/lda_topics_list.png" class="img-fluid" alt="List of a few example LDA topics and documents" title="GOAT = Greatest of All Time" style="width:1000px;max-width:98%">
<p style="text-align: center;font-size:80%"><b>4 topics with sample keywords and sample reddit comments. These match pretty well!</b></p>

As you can see there are some of the key topic words and a few example comments that correspond. Also, to be fair, there were 12 other topics. Half of them were meaningful, but 6 of them did not make sense at all. This leaves room for future improvement.

Since I have data from about a 7 year period, I wanted to see how the proportion of topics discussed changed over time. Plotted below is a comparative proportion of the volume of comments on the 4 topics - grouped annually - over time:

<img src="/static/blog/images/005-lebron-images/dark_annual_lda_proportion.png" class="img-fluid" alt="Comparison of the proportion of different topics of posts over time" title="" style="width:1000px;max-width:98%">
<p style="text-align: center;font-size:80%"><b>Annual proportional comparison of the frequency of these 4 topics having comments.</b></p>

Nothing terribly exciting to see there. Truthfully I was hoping to find an increase or decrease in some topics over time, but alas - you don't always get what you want.

#### Non-negative Matrix Factorization (NMF)

Continuing with the topical modeling approach, I applied **NMF**, a linear algebra based approach, to my vector of words as well to gather topics. The results weren't bad either, but nothing more interpretable than the LDA.

#### K-Means Clustering

To keep going with this unsupervised learning tear, I went back to my LDA output and applied a K-Means clustering to the probability distribution. This categorized each of my reddit comments into one of 17 categories. Upon looking at various comments from each categories - I again was able to clearly find themes for some categories, but garbage for the others. Interestingly, *jokes/puns/quips* type of comments made up a sizable chunk of all comments.

<img src="/static/blog/images/005-lebron-images/dark_annual_kmeans_proportion.png" class="img-fluid" alt="K-Means cluster comparison time series." title="Redditors love to joke." style="width:1000px;max-width:98%">
<p style="text-align: center;font-size:80%"><b>5 of the 17 K-Means clusters and their frequency of comments on an annual basis.</b></p>

## Sentiment Analysis

Finally, I wanted to take a different approach than topic modeling and was curious to gauge the general sentiment of commenters over time. I used a pre-trained sentiment analyzer model, vader, to gauge the **positive, neutral, and negative** content within each comment. The chart below shows the average sentiment for the comments grouped by week.

<img src="/static/blog/images/005-lebron-images/dark_weekly_sentiment.png" class="img-fluid" alt="Sentiment polarity analysis of the comments on a weekly basis" title="Notice the two positive peaks in 2012: that's when LeBron won his first championship." style="width:1000px;max-width:98%">
<p style="text-align: center;font-size:80%"><b>Sentiment Polarity Analysis Time Series</b></p>

 At any given week, the 3 lines will sum to a value of 1. As you can see, most weeks the comments tend to be about 80% neutral, meaning they don't have much positive nor negative expression in them. They also tend to be generally a little more positive than negative.

 A real interesting insight can be found at the two weeks in summer of 2012 where **positivity** spikes. This corresponds to when Lebron won his first NBA finals championship. It seems r/nba redditors were full of saying good things then!

## Conclusion

 It was fun to get my hands on some of the reddit data I frequently read myself. While I initially dove into this project thinking that NLP techniques would be simple to apply, I found that was not the case! It took some wrangling, munging, cursing, exasperated hand waving, and clever techniques to eventually get the text data into a format that played nicely with NLP. Even then, tweaking different *stop words*, stemming techniques, and the number of LDA topics was a time consuming process that often resulted in partially but not fully satisfying results.

 In the future I would like to improve upon some of the aforementioned technicalities in implementing NLP techniques with topic modeling. Additionally, limiting my data to longer comments would likely reduce the number of jokes and increase the ratio of insightful comments. My heuristic of choosing posts with "LeBron" in the title isn't entirely representative of how the r/nba community feels about LeBron, and it would behoove the generalization value of my models to look at all r/nba posts - not LeBron only ones - and then focus on comments referencing LeBron.

 [Github code for this project and all acknowledgements can be found here](https://www.github.com/spencertollefson/lebron-james-nlp).

 Remember, we're lucky to live in an age where we can watch LeBron James play basketball. Don't miss out! *#WeAreAllWitnesses*