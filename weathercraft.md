---
layout: page
title: WeatherCraft
subtitle: The past decade's weather and climate from anywhere in the USA
permalink: /weathercraft/
---

Blogs:

[WeatherCraft Blog part 1](https://mikemerin.github.io/WeatherCraft-blog-1/)

[WeatherCraft Blog part 2](https://mikemerin.github.io/WeatherCraft-blog-2/)

[WeatherCraft Blog part 4](https://mikemerin.github.io/WeatherCraft-blog-4/)

Github links:

[Front End Application](https://github.com/mikemerin/WeatherCraft)

[Back End API](https://github.com/mikemerin/WeatherCraftAPI)


# WeatherCraftApp

![KNYC 20160123 Front End](http://imgur.com/APiZxP0.png)

This React application allows a user to view all data of weather conditions that occurred for any date and location in the US over the past 10 years, including clear weather graphs to help visualize the weather breakdowns.

For any date and location, a user can view the main info for that day, including its daily and weekly data.

The API creates neat JSON data for stations:

![Central Park Station](http://imgur.com/RW9IPSb.png)

Daily data:

![Central Park on January 23, 2016](http://imgur.com/BK1dZCW.png)

And much more, which is easily viewed on the front end.

This application also allows you to view historical data for each year's given date.

![KNYC 20160123 Front End Historical](http://imgur.com/FwLXU9X.png)

With soon-to-be-released monthly climatological information, including trend lines to view how the weather may look like in the future.

### Future updates
- Navigation - Buttons near date to easily go forward/backward a day/year
- Navigation - Clear data button
- Media - queries for #weather tweets/images based on date/location
- Favorites - save your favorite stations for quick loading
- Forecasts - show comparisons to MOS forecasts for that day
- Nearby - show a map with nearby locations to load in data for
-
### Future bug fixes
- Fix primary rendering bug
- Fix state/station section not loading in information on refresh

# WeatherCraftAPI

This Rails/ActiveRecord API is a collection of all hourly/daily/monthly data from every NWS-certified station in the USA. Main information has been pulled into the SQL database accessed by this API, if you would like to pull this information yourself and seed your own database please visit the [NCEI](https://www.ncdc.noaa.gov/orders/qclcd/) site and view the `QCLCDdate.zip` links.

* Run `bundle` to install Ruby gems for the API
* Run `npm install` to install Javascript files for the app

* Database creation
  * `rake db:scrape_stations` pulls all station data
  * `rake db:scrape_hourlies` pulls all hourly data
  * `rake db:scrape_dailies` pulls all daily data
  * `rake db:scrape_monthlies` pulls all monthly data
