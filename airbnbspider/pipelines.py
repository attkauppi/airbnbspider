# -*- coding: utf-8 -*-

""" Loads of useless stuff commented out, as you can see.
The process_item seems to just return the item and DuplicatesPipeline
is used to ensure same information is not collected several times about
the same apartment in the Airbnb use case. """


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
#import psycopg2
import dataset
#import sqlite3
#db = dataset.connect("sqlite:///home/ari/Documents/Btsynced/opinnot/UTA/johdatusDatatieteeseen/joda-kev20/data/helsinki-instant.db")

#import dataset
#db = dataset.connect("sqlite:///data/helsinki-instant.db")
class AirbnbspiderPipeline(object):

    # def __init__(self, db):
    #     self.db = dataset.connect("sqlite:///home/ari/Documents/Btsynced/opinnot/UTA/johdatusDatatieteeseen/joda-kev20/data/helsinki-instant.db")

    # A method which could be used with postgresql
    # def open_spider(self, spider):
    #     hostname='localhost'
    #     username='scrapy'
    #     password='scrapy'
    #     database='airbnb_helsinki'

    #     self.connection = pycopg2.connect(host=hostname, user=username, password=password, dbname=database)

    #     self.cur = self.connection.cursor()
    
    def process_item(self, item, spider):

        # db = dataset.connect("sqlite:///home/ari/Documents/Btsynced/opinnot/UTA/johdatusDatatieteeseen/joda-kev20/data/helsinki-instant.db")
        # table_unq = db['unique_listings']
        # table_raw2 = db['raw2']
        # item_db = table_unq.find_one(id=item['item_id'])

        # item_raw = table_raw2.find_one(unique_listing_id=item['item_id'], last_scraped=item['scrape_time'])


        # if item_db is None:
        #     db['unique_listings'].insert(dict(id=item['item_id'], first_scarped=item['scrape_time'], last_scraped=item['scrape_time']))
        # else:
        #     db['unique_listings'].update(dict(id=item['item_id'], last_scraped=item['scrape_time']), ['id'])

        # if item_raw is None:
        #     table_raw2.insert(dict(
        #         unique_listing_id=item['item_id'],
        #         name=item['name'],#                       TEXT,
        #         is_business_travel_ready=item['is_business_travel_ready'],#   BOOLEAN,
        #         is_new_listing=item['is_new_listing'],#             BOOLEAN,
        #         is_super_host=item['is_super_host'],#              BOOLEAN,
        #         kicker_content_message=['kicker_content_message'],#     TEXT,
        #         latitude=item['latitude'],#                   FLOAT,
        #         longitude=item['longitude'],#                  FLOAT,
        #         localized_city=item['localized_city'],#             TEXT,
        #         localized_neighborhood=item['localized_neighborhood'],#     TEXT,
        #         neighborhood=item['neighborhood'],#               TEXT,
        #         person_capacity=item['person_capacity'],#            BIGINT,
        #         picture_count=item['picture_count'],#              BIGINT,
        #         preview_amenities=item['preview_amenities'],#          TEXT,
        #         property_type_id=item['property_type_id'],#           FLOAT,
        #         reviews_count=item['reviews_count'],#              BIGINT,
        #         accuracy_rating=item['accuracy_rating'],#            FLOAT,
        #         allows_children=item['allows_children'],#            BOOLEAN,
        #         allows_events=item['allows_events'],#              BOOLEAN,
        #         allows_infants=item['allows_infants'],#             BOOLEAN,
        #         allows_pets =item['allows_pets'],#               BOOLEAN,
        #         allows_smoking =item['allows_smoking'],#            BOOLEAN,
        #         amenity_ids =item['amenity_ids'],#               TEXT,
        #         available_30 =item['available_30'],#              FLOAT,
        #         avg_rating =item['avg_rating'],#                FLOAT,
        #         bathrooms =item['bathrooms'],#                 FLOAT,
        #         bedroom_label =item['bedroom_label'],#             TEXT,
        #         bedrooms =item['bedrooms'],#                  FLOAT,
        #         beds =item['beds'],#                      FLOAT,
        #         can_instant_book =item['can_instant_book'],#          BOOLEAN,
        #         cancel_policy =item['cancel_policy'],#             TEXT,
        #         checkin_rating =item['checkin_rating'],#            FLOAT,
        #         city =item['city'],#                      TEXT,
        #         cleaning_fee =item['cleaning_fee'],#              BIGINT,
        #         cleanliness_rating =item['cleanliness_rating'],#        FLOAT,
        #         communication_rating =item['communication_rating'],#      FLOAT,
        #         guest_overall_satisfaction =item['guest_overall_satisfaction'],# FLOAT,
        #         host_verified=item['host_verified'],#              BOOLEAN,
        #         latest_review =item['latest_review'],#             FLOAT,
        #         listing_url =item['listing_url'],#               TEXT,
        #         location_rating =item['location_rating'],#           FLOAT,
        #         max_nights =item['max_nights'],#                BIGINT,
        #         min_nights =item['min_nights'],#                BIGINT,
        #         monthly_price_factor =item['monthly_price_factor'],#      FLOAT,
        #         p3_summary_address =item['p3_summary_address'],#        TEXT,
        #         p3_summary_title =item['p3_summary_title'],#          TEXT,
        #         price_night =item['price_night'],#               FLOAT,
        #         price_string =item['price_string'],#              TEXT,
        #         rate_type =item['rate_type'],#                 TEXT,
        #         requires_license =item['requires_license'],#          BOOLEAN,
        #         response_rate =item['response_rate'],#             FLOAT,
        #         response_time =item['response_time'],#             FLOAT,
        #         review_count =item['review_count'],#              FLOAT,
        #         review_score =item['review_score'],#              FLOAT,
        #         room_and_property_type =item['room_and_property_type'],#    TEXT,
        #         room_type =item['room_type'],#                 TEXT,
        #         room_type_category =item['room_type_category'],#        TEXT,
        #         self_checkin =item['self_checkin'],#              FLOAT,
        #         space_type =item['space_type'],#                TEXT,
        #         star_rating =item['star_rating'],#               FLOAT,
        #         value_rating =item['value_rating'],#              FLOAT,
        #         visible_review_count =item['visible_review_count'],#      FLOAT,
        #         weekly_price_factor =item['weekly_price_factor'],#       FLOAT,
        #         extra_people =item['extra_people'],#              BIGINT,
        #         security =item['security'],#                  BIGINT,
        #         amenities =item['amenities'],#                TEXT,
        #         air_conditioning  =item['air_conditioning'],#         FLOAT,
        #         balcony =item['balcony'],#                   FLOAT,
        #         nature_and_views =item['nature_and_views'],#          FLOAT,
        #         bed_linen =item['bed_linen'],#                 FLOAT,
        #         tv =item['tv'],#                        FLOAT,
        #         coffee_machine =item['coffee_machine'],#            FLOAT,
        #         cooking_basics =item['cooking_basics'],#            FLOAT,
        #         white_goods =item['white_goods'],#               FLOAT,
        #         elevator =item['elevator'],#                  FLOAT,
        #         child_friendly =item['child_friendly'],#            FLOAT,
        #         parking =item['parking'],#                   FLOAT,
        #         outdoor_space =item['outdoor_space'],#             FLOAT,
        #         host_greeting =item['host_greeting'],#             FLOAT,
        #         internet =item['internet'],#                  FLOAT,
        #         long_term_stays =item['long_term_stays'],#           FLOAT,
        #         private_entrance =item['private_entrance'],#          FLOAT,
        #         scrape_time =item['scrape_time'],#
        #     ))
        # db.disconnect()

        return item





class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()
    
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item