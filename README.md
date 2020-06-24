# airbnbspider

## Please notice, this project is not actively maintained and was just quickly written for another project. Hence, some of the code is not used at all and there's a lot of code that's completely commented out.

A simple airbnb spider example. If you use this project, you'll need to configure the URL defined in the air_spider.py file. To get the spider to work, you may need to get a new API key by going on the airbnb website, doing a search for a city/place while having the network tab in your browser's developer tools open. When you click the search button, you should see a request being made to an URL something like this "autocompletes?country=...". By clicking it, and finding the request URL under headers, you should see a URL to the API airbnb uses to show the results to its users. The API key being used in the request is in the request URL, "key=d306zoyjsyarp7ifhu67rjxn52tv0t20&":

```
https://www.airbnb.com/api/v2/autocompletes?country=FI&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&language=en&locale=en&num_results=5&user_input=Helsinki%2C%20Finland&api_version=1.1.1&satori_config_token=EhIiJQAiEiIiMhISMgA&autocomplete_vertical=homes&vertical_refinement=homes&region=-1&options=should_filter_by_vertical_refinement%7Chide_nav_results%7Cshould_show_stays%7Csimple_search
```
The only real takeaway from this URL is the api key, which you plug into the URL being used the air_spider.py. The address is above is not the same as the one used by the spider. By default, airbnb uses API v3, which is more difficult to use similarly. **Luckily, you can just plug all the variables you want into this address**:

```
https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&_intents=p1&auto_ib=false&client_session_id=6c7f3e7b-c038-4d92-b2b0-0bc7c25f1054%C2%A4cy=EUR&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en-CA&luxury_pre_launch=false&metadata_only=false&place_id=ChIJ21P2rgUrTI8Ris1fYjy3Ms4&query=Helsinki%2C%20Finland&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=b7cT9Z3U&satori_version=1.1.9&screen_height=948&screen_size=medium&screen_width=1105&search_type=section_navigation&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-240&version=1.5.7&checkin=2020-04-28&checkout=2020-04-29&adults=1
```

[Screenshot](docs/finding_api_key.png) of where you'll see the api key, if you're using chrome.

To get results, you'll need to change:
* API key: already mentioned above, change this part of the URL: "&key=d306zoyjsyarp7ifhu67rjxn52tv0t20". Alternativey, you can also generate api keys by using the [airbnb module](https://pypi.org/project/airbnb/) in python.
* The checkin and checkout dates: (trying to find free apartments to rent in the past is beyond the scope of this project). 
* guest amounts: To get listings with prices, you should also set adults=1 (or some other integer). 
* (city): Additionally, if you'll want to get listings from a city other than Helsinki, you'll need to change that as well, by setting "&query=Helsinki%2C%20Finland" in the URL to something else.
* Prices can be changed into another currency by changing the EUR in the URL into another currency abbreviation (USD, for example).

To view the first page of search results, you can also open the above URL in your browser. To get the search results in a more readable format, using a browser extension like JSONView in Chrome/Chromium is very useful.

Before trying to use this project to download airbnb data, it's a good idea to check whether insideairbnb.com has already collected airbnb data about whichever city you're interested in.