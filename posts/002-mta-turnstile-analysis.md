#### NYC Subway Data, Grace Hopper Convention, and Recommendations 

As part of the initial week at the [Metis](https://thisismetis.com) boot camp in Seattle this fall, my cohort was tasked to obtain public data set(s), analyze them, and procure a recommendation via a presentation all within the first 4 days. *Deep breath*. The scope of the assignment sounded jarring to hear about initially, but once we got into the swing of things the project fell into place.

This post will cover the assignment overview and my team's approach to the challenge.

## Challenge

The hypothetical scenario tasked us to recommend where and when we would schedule canvassers in NYC subway stations. The goal was to seek signatures of people who would be *supportive* of a non-profit organization - the fictional WomenTechWomenYes (WTWY) - centered on empowering women in technology. More specifically, we wanted to target subway riders likely to attend WTWY's annual gala to donate and raise awareness to the cause.

The final charge was a mandate to use and analyze [NYC Metropolitan Transportation Authority (MTA) turnstile data](http://web.mta.info/developers/turnstile.html) for the project. This data provides a cumulative count of turnstile entries and exits for each individual turnstile in the entire NYC subway system.

## Approach

Our team used the MTA turnstile data and two other data sources:
  1. [Latitude and longitude coordinates of station entrances](http://web.mta.info/developers/data/nyct/subway/StationEntrances.csv)
  2. [List of top corporate donors to the 2017 Grace Hopper Convention.](https://ghc.anitab.org/2017-sponsorships/corporate-sponsors/) The annual convention bills itself as the "world's largest gathering of women technologists."

We made the assumption that top donors of the Grace Hopper Convention also employ many women interested in empowering women in technology. Thus, these employees would be *prime targets* for our canvassing.

Considering the short amount of time allowed for this project, the cleaning needed on the **messy** turnstile data, and lack of ability to ask WTWY for more clarification, we decided on a simple 3-step approach.

  1. List every subway station located within 0.5 mile of the top 14 Grace Hopper donors' Manhattan offices.
  2. Rank the subway stations
  3. Use turnstile data to create a schedule for WTWY to place canvassers by best times of day and days of the week.

## Process

#### Cleaning

Not long into our first exploration of the turnstile data from the MTA website, we quickly realized it wasn't perfect. There were errors, serious errors. Some cumulative counts iterated in a negative direction. Bogus results. Different stations with the same name. Inconsistent time sampling intervals. You name it.

To reach the point of using this data for further analysis, we set about removing "bad" data points, cleaning names and numbers that made sense, and then doing some simple math to convert cumulative passenger numbers into counts of passenger per interval.

#### Analyzing

- **STEP 1:** Based on geographical coordinates, we narrowed our list of all subway stations down to those located within a one-half mile radius of one of the corporate offices.

<img src="/static/blog/images/003-mta-turnstile-post/map-all-stations.png" class="img-fluid" alt="Manhattan map of top companies & their nearest subway stations" title="Top donor offices & subway stations in Manhattan" style="border:1px solid black" text-align="center">

- **STEP 2:** We then proceeded to create an algorithm to rank the remaining stations. The algorithm rewarded stations for high passenger throughput and for proximity to multiple companies, and it penalized stations the farther away they were from corporate offices. [(Details can be found here)](https://github.com/jason-sa/Toucans/blob/master/Station_to_company_scoring.ipynb).

- **STEP 3:** Finally, we went back to the turnstile data to find the optimal times of day and days of the week to canvass the subway stations most highly rated by our algorithm. We created heat maps for each station that emphasize at what times the highest volume of passengers are passing through the turnstiles. Taking the raw numbers behind the heat maps, we ultimately created a Gantt chart of a mock weekly volunteer schedule as our hypothetical deliverable for WTWY.

## Results

Our process produced results! We ended up narrowing our suggestion to 6 unique subway stations, and finally produced a schedule recommending the best times to canvass those stations. In the Gantt chart below you will see that typically Tuesday, Wednesday, and Thursday during the evening was our recommended time to allocate resources.

<img src="/static/blog/images/003-mta-turnstile-post/gantt-chart-schedule.jpg" class="img-fluid" alt="Gantt chart of recommended schedule for volunteers to canvass at stations" title="Take a long weekend and hit it hard Tuesday-Thursday!" style="border:1px solid black" text-align="center">

It was quite clear to our group that although we arrived at an output, we had built it upon untested assumptions and used data which we could not vouch entirely for its validity. This is important to acknowledge and to improve upon in future analysis.

<img src="/static/blog/images/003-mta-turnstile-post/map-final-6-stations.png" class="img-fluid" alt="Our recommended stations in red. The star size indicates its relative score based off our algorithm" title="Notice: Not all stations are near all the companies" style="border:1px solid black" text-align="center">

## Lessons Learned and Future Analysis

While this project has come and went and I am unlikely to expand on it anytime soon, the following lessons learned will be applicable to future projects.

- #### Data

We learned quickly that the turnstile data had many issues. While we did a fair share of cleaning that a 4 day analysis + presentation allows, it was clear that more time could and should be spent on cleaning the data to increase confidence in using it for analysis. *Bad data = bad results.*

- #### Finding the Target Audience

While on the surface it seems that employees of corporate donors to the Grace Hopper Convention would make good targets, more analysis should be made to confirm this. Additionally, different metrics could factor into the equation including company employee demographics, number of employees, remotely working employees, and examining other potential likely donors to follow.

## Wrap Up

Thanks for reading. The github repository with all the code for my group's work may be found [here](https://github.com/jason-sa/Toucans). If you have any questions, please feel free to reach out.