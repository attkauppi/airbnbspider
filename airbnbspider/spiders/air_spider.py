# -*- coding: utf-8 -*-
import scrapy

# -*- coding: utf-8 -*-
import json
import collections
import re
import numpy as np
import logging
import sys
import scrapy
#from scrapy import JsonRequest
from scrapy_splash import SplashRequest
from scrapy.exceptions import CloseSpider
from datetime import datetime, date, timedelta

#from scrapy.utils.project import get_project_settings
from scrapy.loader import ItemLoader
#from myproject.items import Product

import json
import re
import scrapy

from datetime import date, timedelta
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

#from airbnb.items import AirbnbItem
#import items
from airbnbspider.items import AirbnbspiderItem

from datetime import datetime, date, timedelta

import requests
from scrapy.selector import Selector


class AirSpiderSpider(scrapy.Spider):
    name = 'air_spider'
    allowed_domains = ['www.airbnb.com']
    start_urls = ['https://www.airbnb.com/']
    #url = ['https://www.airbnb.com/s/Helsinki/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&query=Helsinki&place_id=ChIJkQYhlscLkkYRY_fiO4S9Ts0&checkin=2020-04-14&checkout=2020-04-15&adults=1&source=structured_search_input_header&search_type=search_query']
    url =['https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&_intents=p1&auto_ib=false&client_session_id=6c7f3e7b-c038-4d92-b2b0-0bc7c25f1054%C2%A4cy=EUR&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en-CA&luxury_pre_launch=false&metadata_only=false&place_id=ChIJ21P2rgUrTI8Ris1fYjy3Ms4&query=Helsinki%2C%20Finland&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=b7cT9Z3U&satori_version=1.1.9&screen_height=948&screen_size=medium&screen_width=1105&search_type=section_navigation&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-240&version=1.5.7&checkin=2020-04-28&checkout=2020-04-29&adults=1']
    default_currency = 'EUR'
    #item = None

    offset_str = '&items_offset='
    listing_url_beginning = 'https://www.airbnb.com/api/v2/pdp_listing_details/'

    listing_url_end = '?_format=for_rooms_show&key=d306zoyjsyarp7ifhu67rjxn52tv0t20'
    listing_url_checkin_checkout = '&checkin=2020-04-28&checkout=2020-04-29'
    guests = '&adults=1'

    date = str(datetime.now().date())
    feeduri = 'test_'+date+'.csv'

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': feeduri
        #'FEED_URI': 'test.csv'
    }
    

    def __init__(self):
        """ Constructor for the spider, mainly used to define the
        item model so that it's usable in every method in this class,
        which makes passing information collected in various stages
        considerably easier. """
        # item, and its fields/properties, is defined in items.py
        self.item = AirbnbspiderItem()
        # The scraping time is defined here so it'll be the same for all items scraped at any one time.
        self.scraping_time = str(datetime.now().date())
   


    def start_requests(self):
        # To scrape airbnb, you have to get a url like this. To get this to work for testing purposes,
        # you may need to change the checkin and checkout date (for airbnb apartment, you'd want to rent
        # for your holiday or whatever), this can be done using these parameters in the URL: "&checkin=2020-04-28&checkout=2020-04-29" .
        # Another thing you may need to change is the API key, also defined in the URL. You can get a new API
        # key by going to the site airbnb website (airbnb.com), searching for something and
        # following the responses sent back by the airbnb servers while doing the search. This can be done in the network 
        # tab in your browser's the developer tools. You need to have the network tab open while doing the search.
        # As mentioned above, the API key is defined in the url and it looks like this:
        ## "&client_session_id=6c7f3e7b-c038-4d92-b2b0-0bc7c25f1054"
        url =('https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&_intents=p1&auto_ib=false&client_session_id=6c7f3e7b-c038-4d92-b2b0-0bc7c25f1054%C2%A4cy=EUR&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en-CA&luxury_pre_launch=false&metadata_only=false&place_id=ChIJ21P2rgUrTI8Ris1fYjy3Ms4&query=Helsinki%2C%20Finland&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=b7cT9Z3U&satori_version=1.1.9&screen_height=948&screen_size=medium&screen_width=1105&search_type=section_navigation&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-240&version=1.5.7&checkin=2020-04-28&checkout=2020-04-29&adults=1')
        #url = ('https://www.airbnb.ca/api/v2/explore_tabs?_format=for_explore_search_web&_intents=p1&auto_ib=false&client_session_id=6c7f3e7b-c038-4d92-b2b0-0bc7c25f1054%C2%A4cy=CAD&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en-CA&luxury_pre_launch=false&metadata_only=false&place_id=ChIJ21P2rgUrTI8Ris1fYjy3Ms4&query=Helsinki%2C%20Finland&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=b7cT9Z3U&satori_version=1.1.9&screen_height=948&screen_size=medium&screen_width=1105&search_type=section_navigation&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-240&version=1.5.7')
        #url = ['https://www.airbnb.com/s/Helsinki/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&query=Helsinki&place_id=ChIJkQYhlscLkkYRY_fiO4S9Ts0&checkin=2020-04-14&checkout=2020-04-15&adults=1&source=structured_search_input_header&search_type=search_query']
        #url = ('https://www.airbnb.com/s/Helsinki/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&query=Helsinki&place_id=ChIJkQYhlscLkkYRY_fiO4S9Ts0&checkin=2020-04-12&checkout=2020-04-13&adults=1&source=structured_search_input_header&search_type=search_query')
        #url = ('https://www.airbnb.com/s/helsinki/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=search_query')
        #first = False
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ Scrapes the search results page """
        data = json.loads(response.body)
        #data = json.loads(response.text)
        tab = data['explore_tabs'][0]

        ## Handling pagination
        next_section = {}
        pagination = tab['pagination_metadata']
        has_next_page = self.has_next_page(data)
        print("************* NEXT PAGE: ", has_next_page)
        offset = data.get('explore_tabs')[0]['pagination_metadata']['items_offset']

        #gen_listings = data.get('explore_tabs')[0].get('sections')[2]
        listings = None
        if offset > 18:
            # When on first page, offset is 18. After this, the listings are in another section.
            listings = data.get('explore_tabs')[0].get('sections')[0].get('listings')
        else:
            listings = data.get('explore_tabs')[0].get('sections')[1].get('listings')

        j = 0
        for i in listings:
            i = i.get('listing')
            # Pricing quote is not under listings, so we need to do this
            pricing_quote = listings[j].get('pricing_quote')
            # Information about the host, like whether they're verified
            verified = listings[j].get('verified')
            id = i.get('id')
            listing_url = self.get_listing_url(id)

            self.item['id'] = i.get('id')
            self.item['name'] = i.get('name')
            self.item['is_business_travel_ready'] = i.get('is_business_travel_ready')
            self.item['is_new_listing'] = i.get('is_new_listing')
            self.item['is_super_host'] = i.get('is_superhost')

            self.item['kicker_content_message'] = i.get('kicker_content').get('messages')[0]


            self.item['latitude'] = i.get('lat')
            self.item['longitude'] = i.get('lng')
            self.item['localized_city'] = i.get('localized_city')
            self.item['localized_neighborhood'] = i.get('localized_neighborhood')
            self.item['neighborhood'] = i.get('neighborhood')

            self.item['person_capacity'] = i.get('person_capacity')
            self.item['picture_count'] = i.get('picture_count')
            self.item['preview_amenities'] = i.get('preview_amenities')
            self.item['property_type_id'] = i.get('property_type_id')
            self.item['reviews_count'] = i.get('reviews_count')
            self.item['room_and_property_type'] = i.get('room_and_property_type')
            self.item['room_type_category'] = i.get('room_type_category')
            self.item['room_type'] = i.get('room_type')
            self.item['space_type'] = i.get('space_type')
            self.item['star_rating'] = i.get('star_rating')
            self.item['avg_rating'] = i.get('avg_rating')
            self.item['min_nights'] = i.get('min_nights')
            self.item['max_nights'] = i.get('max_nights')
            self.item['cancel_policy'] = i.get('cancel_policy')

            # Pricing quote -osuuden hakeminen
            self.item['can_instant_book'] = pricing_quote.get('can_instant_book')
            self.item['monthly_price_factor'] = pricing_quote.get('monthly_price_factor')
            self.item['price_string'] = pricing_quote.get('price_string')
            self.item['rate_type'] = pricing_quote.get('rate_type')
            self.item['weekly_price_factor'] = pricing_quote.get('weekly_price_factor')

            self.item['host_verified'] = verified.get('enabled')
            self.item['bedrooms'] = i.get('bedrooms')
            self.item['bedroom_label'] = i.get('bedroom_label')
            self.item['beds'] = i.get('beds')
            self.item['bathrooms'] = i.get('bathrooms')
            self.item['city'] = i.get('city')
            self.item['amenity_ids'] = i.get('amenity_ids')

            # Fetches an address for the listing page.
            self.item['listing_url'] = self.get_listing_url(id)
            self.item['scrape_time'] = self.scraping_time

            # Sends the scraper to the listing page - or course page, for example. Method used to parse listing page is
            # called "parse_listing_contents"
            yield response.follow(listing_url, callback=self.parse_listing_contents)#, meta={'airbnb': item['airbnb']})
            yield self.item
            j = j +1

        if has_next_page:
            url = self.url[0]+self.offset_str+str(offset)
            print()
            print("***************URL: ", url)
            yield scrapy.Request(url=url, callback=self.parse)

        _file_ = "first_page_nyt.json"
        with open(_file_, 'wb') as f:
            f.write(response.body)


    def get_listing_url(self, listing_id):
        listing_url = self.listing_url_beginning+str(listing_id)+self.listing_url_end+self.listing_url_checkin_checkout+self.guests
        print("_________LISTINGURL")
        print(listing_url)
        return listing_url

    def get_listing_page(self, listing_id):
        listing_url = self.get_listing_url(listing_id)
        
        return scrapy.Request(listing_url, self.parse_listing)

    
    def parse_listing_contents(self, response):
        """
        Collects information from each listing's page
        """

        item = AirbnbspiderItem()
        print("************LISTING CONTENTS")
        data = json.loads(response.body)
        pdp = data.get('pdp_listing_detail')
        amenities = pdp.get('listing_amenities')

        guest_controls = pdp.get('guest_controls')

        allows_children = guest_controls.get('allows_children')
        print("allows_children: ", allows_children)
        allows_infants = guest_controls.get('allows_infants')
        allows_pets = guest_controls.get('allows_pets')
        allows_smoking = guest_controls.get('allows_smoking')
        allows_events = guest_controls.get('allows_events')

        p3_summary_address = pdp.get('p3_summary_address')
        p3_summary_title = pdp.get('p3_summary_title')

        p3_event = pdp.get('p3_event_data_logging')
        accuracy_rating = p3_event.get('accuracy_rating')
        checkin_rating = p3_event.get('checkin_rating')
        cleanliness_rating = p3_event.get('cleanliness_rating')
        communication_rating = p3_event.get('communication_rating')
        guest_overall_satisfaction = p3_event.get('guest_overall_satisfaction')
        location_rating = p3_event.get('location_rating')
        value_rating = p3_event.get('value_rating')
        visible_review_count = p3_event.get('visible_review_count')
        requires_license = pdp.get('requires_license')
        review_count = pdp.get('review_details_interface').get('review_count')
        review_score = pdp.get('review_details_interface').get('review_score')

        self.item['allows_children'] = guest_controls.get('allows_children')
        self.item['allows_infants'] = guest_controls.get('allows_infants')
        self.item['allows_pets'] = guest_controls.get('allows_pets')
        self.item['allows_smoking'] = guest_controls.get('allows_smoking')
        self.item['allows_events'] = guest_controls.get('allows_events')
        self.item['p3_summary_address'] = pdp.get('p3_summary_address')
        self.item['p3_summary_title'] = pdp.get('p3_summary_title')
        self.item['accuracy_rating'] = p3_event.get('accuracy_rating')
        self.item['checkin_rating'] = p3_event.get('checkin_rating')
        self.item['cleanliness_rating'] = p3_event.get('cleanliness_rating')
        self.item['communication_rating'] = p3_event.get('communication_rating')
        self.item['guest_overall_satisfaction'] = p3_event.get('guest_overall_satisfaction')
        self.item['location_rating'] =p3_event.get('location_rating')
        self.item['value_rating'] = p3_event.get('value_rating')
        self.item['visible_review_count'] = p3_event.get('visible_review_count')
        self.item['requires_license'] = pdp.get('requires_license')
        self.item['review_count'] = pdp.get('review_details_interface').get('review_count')
        self.item['review_score'] = pdp.get('review_details_interface').get('review_score')   

        print("allows_events: ", allows_events)

        additional_house_rules = pdp.get('additional_house_rules')

        print("**********************PARSE LISTING CONTENTS")

        ident = self.item['id']
        availability_url = self.get_availability_url(ident)

        

    def get_availability_url(self, id):
        url_alku = 'https://www.airbnb.com/api/v2/homes_pdp_availability_calendar?currency=EUR&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=fi&listing_id='
        curr_year = int(date.today().year)
        curr_month = int(date.today().month)

        url_middle = '&locale=fi&listing_id=23676465&month='+str(curr_month)
        url_middle2 = '&year='+str(curr_year)
        url_end= '&count=2'

        url = url_alku + url_middle + url_middle2 + url_end

        return url
        #'&locale=fi&listing_id=23676465&month=4&year=2020&count=2'


    def get_availability(self, response):
        data = json.loads(response.body)

        now = datetime.now().date()
        end = now + timedelta(days=30)

        month1_days = data.get('calendar_months')[0].get('days')

        month2_days = data.get('calendar_months')[1].get('days')

        days_available_30 = 0
        
        for i in month1_days:
            i_date = i.get('date')
            i_avail = i.get('available')

            i_dated = datetime.strptime(i_date, "%Y-%m-%d")
            i_dated = i_dated.date()

            if (i_dated >= now and i_dated <= end) and i_avail:
                days_available_30 += 1

        for i in month2_days:
            i_date = i.get('date')
            i_avail = i.get('available')

            i_dated = datetime.strptime(i_date, "%Y-%m-%d")
            i_dated = i_dated.date()

            if (i_dated >= now and i_dated <= end) and i_avail:
                days_available_30 += 1
        print("**************AVAILABLE_30: ", days_available_30)

        self.item['available_30'] = days_available_30
            

    def read_data(self, response):
        self.logger.debug(f"Parsing {response.url}")
        data = json.loads(response.body)
        return data


    def parse_listing(self, listing, pricing_quote, verified):
        item = AirbnbspiderItem()

        item['id'] = listing.get('id')
        item['name'] = listing.get('name')
        item['is_business_travel_ready'] = listing.get('is_business_travel_ready')
        item['is_new_listing'] = listing.get('is_new_listing')
        item['is_super_host'] = listing.get('is_superhost')

        item['kicker_content_message'] = listing.get('kicker_content').get('messages')[0]


        item['latitude'] = listing.get('lat')
        item['longitude'] = listing.get('lng')
        item['localized_city'] = listing.get('localized_city')
        item['localized_neighborhood'] = listing.get('localized_neighborhood')
        item['neighborhood'] = listing.get('neighborhood')

        item['person_capacity'] = listing.get('person_capacity')
        item['picture_count'] = listing.get('picture_count')
        item['preview_amenities'] = listing.get('preview_amenities')
        item['property_type_id'] = listing.get('property_type_id')
        item['reviews_count'] = listing.get('reviews_count')
        item['room_and_property_type'] = listing.get('room_and_property_type')
        item['room_type_category'] = listing.get('room_type_category')
        item['room_type'] = listing.get('room_type')
        item['space_type'] = listing.get('space_type')
        item['star_rating'] = listing.get('star_rating')
        item['avg_rating'] = listing.get('avg_rating')
        item['min_nights'] = listing.get('min_nights')
        item['max_nights'] = listing.get('max_nights')
        item['cancel_policy'] = listing.get('cancel_policy')

        # Pricing quote -osuuden hakeminen
        item['can_instant_book'] = pricing_quote.get('can_instant_book')
        item['monthly_price_factor'] = pricing_quote.get('monthly_price_factor')
        item['price_string'] = pricing_quote.get('price_string')
        item['rate_type'] = pricing_quote.get('rate_type')
        item['weekly_price_factor'] = pricing_quote.get('weekly_price_factor')
        #can_instant_book = listing.get('pricing_quote').get('can_instant_book')
        
        ## UUSI LISÄYS
        
        item['cleaning_fee'] = pricing_quote.get('price').get('price_items')[1].get('total_amount')


        item['host_verified'] = verified.get('enabled')
        #self.parse_listing_contents(id)
        item['bedrooms'] = listing.get('bedrooms')
        item['bedroom_label'] = listing.get('bedroom_label')
        item['beds'] = listing.get('beds')
        item['bathrooms'] = listing.get('bathrooms')
        item['city'] = listing.get('city')

        #item = 


        item['listing_url'] = self.get_listing_url(id)
        #yield scrapy.Request(listing_url, callback=self.parse_listing_contents)

        #listing_url = self.get_listing_url(id)

        # print("********** id: ", id)
        # print('********* Name: ', name)
        # print("********* is business travel ready: ", is_business_travel_ready)
        # print("********* new? ", is_new_listing)
        # print("********* is_super_host: ", is_super_host)
        # print("********* kicker: ", kicker_content_message)
        # print("*********bedrooms: ", bedrooms)
        # print("********* bedroom_label: ", bedroom_label)
        # print("********* beds: ", beds)
        # print("*********BATHROOMS2 METODISTA:", bathrooms2)
        # print("********* city: ", city)
        # print("********* can_instant_book: ", can_instant_book)
        # print("********* monthly: ", monthly_price_factor)
        # print('********* pricing_string: ', price_string)
        # print("********* rate_type: ", rate_type)
        # print("********* weekly: ", weekly_price_factor)
        # print("********* host verified: ", host_verified)
        #print(item)
        #yield (item)
        #yield {'id': id}

        

    #def parse_listing_results_page(self, response):
    #def has_next_page(self, )

    def get_pricing_quote(self, response, number):
        pricing_quote = response[number].get('pricing_quote')
        return pricing_quote

    def get_pricing_quote(self, listing):
        quote = listing.get('pricing_quote')
        return quote

    def has_next_page(self, data):
        return data.get('explore_tabs')[0]['pagination_metadata']['has_next_page']


    
    def get_listings(self, data):

        print("SAATTOI HAKEA LISTINGSIT=================0")

        data.get('explore_tabs')[0].get('sections')
        listings = data.get('explore_tabs')[0].get('sections')[2].get('listings')

        #print('__________-------------_______________________')
        #print(listings)
        #logging.log(logging.DEBUG, '***************LISTINGS***************' , listings)
        #print('__________-------------_______________________')
        return listings

    #def parse_listings(self, data):



    def last_page_in_search(self, response):
        try:
            last_page_number = int(response
                               .xpath('//ul[@class="list-unstyled"]/li[last()-1]/a/@href')
                               .extract()[0]
                               .split('page=')[1]
                               )
            return last_page_number
        except IndexError: #If only one page of results

            # Get reason from the page
            reason = response.xpath('//p[@class="text-lead"]/text()').extract()
            # and if it contains the keywords set last page equal to 0
            if reason and ('find any results that matched yours criteria' in reason[0]):
                logging.log(logging.DEBUG, 'No results on page' + response.url)
                return 0
            else:
                # Otherwise we can conclude that the page has resulsts but that there is only
                # one page of them
                return 1

    # def _api_requests(self, params=None, response=None, callback=None):
    #     """ Perform API request."""
    #     if response:
    #         request = response.follow
    #     else:
    #         request = scrapy.Request
        
    #     callback = callback or self.parse

    #     return request(self.get_sear)

    # def _get_search_api_url(self, params=None):
    #     _api_path = '/api/v2/explore_tabs'
    #     if self._api_key is None:
    #         self._api_key = self.settings.get("AIRBNB_API_KEY")

    #     query = {
    #         '_format':                       'for_explore_search_web',
    #         'auto_ib':                       'true',  # was false?
    #         'currency':                      self._currency,
    #         'current_tab_id':                'home_tab',
    #         'experiences_per_grid':          '20',
    #         # 'federated_search_session_id': '',
    #         'fetch_filters':                 'true',
    #         'guidebooks_per_grid':           '20',
    #         'has_zero_guest_treatment':      'false',
    #         'hide_dates_and_guests_filters': 'false',
    #         'is_guided_search':              'true',
    #         'is_new_cards_experiment':       'true',
    #         'is_standard_search':            'true',
    #         # 'items_offset': '0',
    #         'items_per_grid':                '50',
    #         'key':                           self._api_key,
    #         # 'last_search_session_id': '',
    #         'locale':                        'en',
    #         'metadata_only':                 'false',
    #         # 'neighborhood_ids[]': ,
    #         # 'place_id': '',
    #         # 'price_max': None,
    #         # 'price_min': 10,
    #         'query':                         self._place,
    #         'query_understanding_enabled':   'true',
    #         'refinement_paths[]':            '/homes',
    #         'room_types[]':                  'Entire home/apt',
    #         'satori_version':                '1.2.0',
    #         # 'section_offset': '0',
    #         'screen_height':                 635,
    #         'screen_size':                   'large',
    #         'screen_width':                  2040,
    #         'show_groupings':                'true',
    #         'supports_for_you_v3':           'true',
    #         'timezone_offset':               '-480',
    #         'version':                       '1.6.5'
    #     }

    #     if params:
    #         query.update(params)

    #     if self.settings.get('PROPERTY_AMENITIES'):
    #         amenities = self.settings.get('PROPERTY_AMENITIES').values()
    #         query = list(query.items())  # convert dict to list of tuples because we need multiple identical keys
    #         for a in amenities:
    #             query.append(('amenities[]', a))

    #     return self._build_airbnb_url(_api_path, query)
