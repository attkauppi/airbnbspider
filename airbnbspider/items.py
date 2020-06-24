# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbspiderItem(scrapy.Item):
    """ Item we're essentially trying to scrape information about
    is defned here. This will be turned into a csv or saved in some
    other way. """
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    name = scrapy.Field()
    is_business_travel_ready = scrapy.Field()
    is_new_listing = scrapy.Field()
    is_super_host = scrapy.Field()

    kicker_content_message = scrapy.Field()


    latitude = scrapy.Field()
    longitude = scrapy.Field()
    localized_city = scrapy.Field()
    localized_neighborhood = scrapy.Field()
    neighborhood = scrapy.Field()

    person_capacity = scrapy.Field()
    picture_count = scrapy.Field()
    preview_amenities = scrapy.Field()
    property_type_id = scrapy.Field()
    reviews_count = scrapy.Field()
    room_and_property_type = scrapy.Field()
    room_type_category = scrapy.Field()
    room_type = scrapy.Field()
    space_type = scrapy.Field()
    star_rating = scrapy.Field()
    avg_rating = scrapy.Field()
    min_nights = scrapy.Field()
    max_nights = scrapy.Field()
    cancel_policy = scrapy.Field()

    # Pricing quote -osuuden hakeminen
    can_instant_book = scrapy.Field()
    monthly_price_factor = scrapy.Field()
    price_night = scrapy.Field()
    price_string = scrapy.Field()
    rate_type = scrapy.Field()
    weekly_price_factor = scrapy.Field()
    #can_instant_book = listing.get('pricing_quote').get('can_instant_book')
    cleaning_fee = scrapy.Field()
    host_verified = scrapy.Field()
    #self.parse_listing_contents(id)
    bedrooms = scrapy.Field()
    bedroom_label = scrapy.Field()
    beds = scrapy.Field()
    bathrooms = scrapy.Field()
    city = scrapy.Field()
    listing_url = scrapy.Field()
    amenity_ids = scrapy.Field()
    #amenities_list = scrapy.Field(serializer=str)
    allows_children = scrapy.Field()
    allows_infants = scrapy.Field()
    allows_pets = scrapy.Field()
    allows_smoking= scrapy.Field()
    allows_events= scrapy.Field()
    p3_summary_address= scrapy.Field()
    p3_summary_title= scrapy.Field()
    accuracy_rating= scrapy.Field()
    checkin_rating= scrapy.Field()
    cleanliness_rating= scrapy.Field()
    communication_rating= scrapy.Field()
    guest_overall_satisfaction= scrapy.Field()
    location_rating= scrapy.Field()
    value_rating= scrapy.Field()
    visible_review_count= scrapy.Field()
    requires_license= scrapy.Field()
    review_count= scrapy.Field()
    review_score= scrapy.Field()
    latest_review= scrapy.Field()

    response_rate = scrapy.Field()
    response_time = scrapy.Field()
    self_checkin = scrapy.Field()
    available_30 = scrapy.Field()
    scrape_time = scrapy.Field()

    pass
# define the fields for your item here like: