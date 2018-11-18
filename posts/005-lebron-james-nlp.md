<<< IMAGE OF LEBRON>>>

I love the NBA. Evening time and I'm at home? Flip on a basketball game. Out with friends on a weekend? Let's watch a game. Visiting a city that ACTUALLY HAS an NBA team (rip Sonics, I'll never forget you)? See if I can score tickets. It's a hobby. And why shouldn't it be? I don't think I'm over reaching when I say the NBA has never been more marketable and has more recognizable players than ever before. Heads and shoulders above all the other current players when it comes to stardom, however, is LeBron James. I admire the man for what he demonstrates on the court night after night, but also for the way he, generally (but not without exceptions),  tastefully and impactfully wields his voice to weigh in on issues outside of basketball.

LeBron lives under a microscope. His tweets, post-game interviews, family outings, nightly basketball performances, choice of sneakers, and other rudimentary activities are all discussed by pundits on television, on internet forums, and by people everywhere on a 24/7 basis. Knowing this, I decided I wanted to use machine learning techniques to see what kind of insights I could pry from **what people are discussing when they discuss LeBron**.  I got my hands on LeBron-centered reddit comments and put Natural Language Processing (NLP) techniques to the task at hand.

Continue reading for my exploration of the types of words, language, and topics that  internet denizens discuss when they're talking about LeBron.

## Data

While I heavily considered Twitter due to the quantity of and ease of accessing its data, I chose to get posts from [reddit.com/r/nba](https://www.reddit.com/r/nba) as my data source. I hav ea good intuition for the data as I often read and occasionally post on the platform. The r/nba subreddit is quite popular with over 1.42 million subscribers at the time of writing - making it the most subscribed to subreddit. 

People discuss all things NBA related on the subreddit, and unsurprisingly that means LeBron is discussed often. Using some awesome tools which may be found in my [github repo](https://github.com/spencertollefson/lebron_james_nlp) for this project, I pulled over 45,000 reddit comments to analyze. The comments selected were the most highly upvoted (a reddit user-based scoring system) for submissions for posts with "LeBron", a variation of his name, or a nickname in the title. I intended for this heuristic of selecting comments to be a proxy for the general pulse of the entire r/nba community.

## Topic Modeling

After obtaining the data, the next step was to transform it into a suitable format for NLP techniques. This is referred to as *preprocessing*. The text is all converted to lowercase, most punctuation removed, limited to English language words, removing non-important words dubbed *stop words*, then *lemmatized* and *stemmed*. Lemmatization and stemming essentially boil a word down into it's root form. *Running*, *ran*, and *runs* all are destilled into *run* for consistency.

Next, the data is converted into a document-term matrix of numbers in a *bag of words* friendly-format. Numbers means we can model it! I applied the popular generative statistical model **Latent Dirichlict Allocation (LDA)** to the matrix to squeeze out the best results. LDA, in a simplified sense, discovers topics within text. I liked the explanation of LDA [by Edwin Chen in his post here](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/).  After supplying my LDA model with all of the reddit comments and the number of topics I am seeking, I eventually got some meaningful (and not meaningful... aka garbage) topics:

<img src="/static/blog/images/005-lebron-images/all_lda_cluster_counts.png" class="img-fluid" alt="Plot of LDA topics vs time" title="Too. Many. Lines." style="width:300px;max-width:88%">
<p style="text-align: center;font-size:80%"><b>Sum of the number of reddit comments of the 16 LDA-derived topics grouped by month.</b></p>

<<<<<<LDA TOPICS HERE and COMMENTS>>>>>>

This is pretty cool! As you can see there are some of the key topic words and a few example comments that correspond.

Since I have data from about a 7 year period, I wanted to see how the proportion of topics discussed changed over time. Plotted below is a comparison proportion of the volume of comments by topics - grouped monthly - over time:

<TIME PLOT OF TOPICS HERE>

Nothing terribly exciting to see there. Truthfully I was hoping to find an increase or decrease in some topics over time, but nothing to see here.


Continuing with the topical modeling approach, I applied non-negative matrix factorization (NMF), a linear algebra based approach, to my vector of words as well to gather topics. The results weren't bad either, but nothing more interpretable than the LDA.

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