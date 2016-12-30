# BART Ridership

This repository shows python notebooks used for a blog post on recent changes in BART's annual weekday ridership. The final blog post can be found here: http://www.briangoggin.com/2016/09/11/remember-barts-twitter-fight-earlier-this-year-weekday-exit-numbers-back-them-up/. 

Raw data comes from BART's ridership reports here: http://www.bart.gov/about/reports/ridership. Spatial data on BART stations and tracks comes from here: http://www.bart.gov/schedules/developers/geo. 

First, I clean and prepare the data for a merge with spatial data in the "Clean and Export.ipynb" file. Next, I perform a join with spatial data based on attributes in Carto, where I also produce the map for the blog post. 


