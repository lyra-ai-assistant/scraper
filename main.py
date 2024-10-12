from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lyra_scraper.spiders.simple import SimpleSpider

from config.vars import vars
from config.dirs import check_path, create_dir


def run_spider():
    # Crawler configuration
    process = CrawlerProcess(
        settings={
            "FEED_FORMAT": vars.outputFileFormat,
            "FEED_URI": f"{vars.outputDirectory}/{vars.scraperName}_{vars.outputFileName}.{vars.outputFileFormat}",
            "LOG_ENABLED": vars.verbose,
        }
    )

    # Crawls the spider
    process.crawl(SimpleSpider)

    # Block execution until spider ends
    process.start()


if __name__ == "__main__":
    # Validations
    if not check_path(vars.outputDirectory):
        create_dir(vars.outputDirectory)

    print(
        f"Files created at: {vars.outputDirectory}/{vars.scraperName}_{vars.outputFileName}.{vars.outputFileFormat}"
    )

    run_spider()
