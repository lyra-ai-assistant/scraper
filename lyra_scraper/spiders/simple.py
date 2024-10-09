import scrapy

from config.vars import vars


class SimpleSpider(scrapy.Spider):
    name = vars.scraperName
    start_urls = vars.urlToScrap
    allowed_domains = vars.domainToScrap

    def extract_section(self, response, section_selector, fields):
        section_data = response.css(section_selector)
        for element in section_data:
            extracted_data = {}
            for field_name, field_selector in fields.items():
                extracted_data[field_name] = element.css(field_selector).get()
            yield extracted_data

    def parse(self, response):
        for section, selectors in vars.scraperTargets.items():
            section_data = self.extract_section(
                response, selectors['section_selector'], selectors['fields'])
            for item in section_data:
                yield item
