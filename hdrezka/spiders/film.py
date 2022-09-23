import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from scrapy.utils.project import get_project_settings
import pandas as pd


class FilmSpider(scrapy.Spider):
    name = "film"
    allowed_domains = ["rezka.ag"]
    start_urls = ["https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html"]

    def parse(self, response: Response, **kwargs):
        yield {
            "title": response.xpath(
                "//h1[@itemprop='name']/text()").get(),
            "orig_title": response.xpath(
                "//div[@itemprop='alternativeHeadline']/text()").get(),
            "imdb": response.xpath(
                "//span[contains(@class, 'imdb')]/span/text()").get(),
            "country": response.xpath(
                "//tr/td/h2[normalize-space(.)='Страна']/../../td/a/text()").get(),
            "running_time": response.xpath(
                "//td[@itemprop='duration']/text()").get(),
            "description": response.xpath(
                "//div[contains(@class, 'b-post__description_text')]/text()").get(),
        }


if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(FilmSpider)
    process.start()
    df = pd.read_csv("film.csv")
    print(df.head())
