import scrapy
from scrapy_playwright.page import PageMethod


class PositionsSpider(scrapy.Spider):
    name = 'positions'
    allowed_domains = ['traf.com']
    start_urls = ['https://careers.trafigura.com/TrafiguraCareerSite/search']

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            meta=dict(
                playwright=True,
                playwright_page_methods=[
                    PageMethod("wait_for_selector",
                               'section#results div[role="list"]'),
                    PageMethod("evaluate", "some js to activate the button"),
                    PageMethod("wait_for_selector",
                               'button selector', state="detached")
                ]
            )
        )

    async def parse(self, response):
        for job in response.css('section#results div[role="list"] div[role="listitem"]'):
            yield {
                "title": job.css('a::text').get()
            }
