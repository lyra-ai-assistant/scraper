from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lyra_scraper.spiders.simple import SimpleSpider

from config.vars import vars


def run_spider():
    # Crawler configuration
    process = CrawlerProcess(settings={
        "FEED_FORMAT": vars.outputFileFormat,
        "FEED_URI": vars.outputDirectory + vars.scraperName + "_" + vars.outputFileName + vars.outputFileFormat
    })

    # Crawls the spider
    process.crawl(SimpleSpider)

    # Bloquear hasta que se complete el spider
    process.start()


if __name__ == '__main__':
    run_spider()
