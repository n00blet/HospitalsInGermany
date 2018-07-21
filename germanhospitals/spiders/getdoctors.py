# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from germanhospitals.items import *

def complete_url(string):
	delimiter = ";"
	if delimiter in string:
		clean_url = string.split(delimiter)
		return clean_url[0]
	else:
		return string

class GetdoctorsSpider(scrapy.Spider):
    name = 'getdoctors'
    allowed_domains = ['www.german-hospital-directory.com']
    start_urls = ['https://www.german-hospital-directory.com/search/Regional.html']

    def parse(self, response):
    	state_urls = response.xpath("//dl/dd/a/@href").extract()
    	for i in range(len(state_urls)):
    		yield Request(complete_url(state_urls[i]), callback = self.parse_each_state)
    	

    def parse_each_state(self,response):
        total_hospitals = response.xpath("//h2[@class='result_list_headline']/strong/text()").extract()
        count = int(total_hospitals[0])//10
        for i in range(count):
            yield Request(
                url="https://www.german-hospital-directory.com/search/_files/main-search/Suchergebnis.jsf?page=%d" %i,
                callback=self.parse_each_hospital
                )

    def parse_each_hospital(self,response):
        #Should be completed
        print("the resulting url--> ", response.url)
        pass

        

        

    
        





    


        
