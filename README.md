# COVID-19 Vaccine Providers in Texas
This repo documents some work I did to try and help during the initial rollout of the COVID-19 vaccine.

### Background
In December 2020, the Texas Department of State Health Services [released a dashboard](https://twitter.com/texasdshs/status/1344047679756763136) where users could find vaccine providers near them. This was helpful, but for actually figuring out if one could get the vaccine at a location, the recommendation was to just call the provider and ask.

I saw a [post](https://old.reddit.com/r/Dallas/comments/kpt90g/website_to_crowdsource_info_about_the_covid_19/) in the /r/Dallas subreddit from someone who had created a website to crowdsource information on the vaccine providers. 

Things like
 - which phases they were serving (1A or 1B)
 - if there was a waitlist
 - what the experience was like

Users could help add locations and report what information they might have gotten from calling a location so that others wouldn't have to. This was a brilliant use of technology to make things more efficient and reduce frustration.

I learned from the Reddit comments that the creator, Carri ([@ccgirl](https://twitter.com/ccgirl)), was entering the provider data herself and working tirelessly to ask others to help. Some commenters suggested finding a way to scrape the data, but it seemed no one had found an obvious or convenient way to do so.

### My contribution
I found this [StackOverflow](https://stackoverflow.com/questions/50161492/how-do-i-scrape-data-from-an-arcgis-online-map) answer that was helpful, and by looking through the Network tab in the dev console while browsing the dashboard, I found a URL that would let me query the data. I wrote this simple Python script to make the right REST requests and generate a CSV for Carri.

You can see mention of me at https://www.findvaccineusa.com/thank-you. The original site was `https://covid19vaccinetx.com` -- see it at [archive.org](https://web.archive.org/web/20210130053916/https://www.covid19vaccinetx.com/). Thank you to Carri for providing me with this opportunity to help.
