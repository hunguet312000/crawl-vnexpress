import scrapy

class Baomoi (scrapy.Spider):
    name = "vn"
    base_urls = "https://vnexpress.net/so-hoa/cong-nghe-p"
    start_urls = []

    for i in range(1, 300):
        start_urls.append(base_urls + str(i))

    def parse(self, response):
        for i in response.css('h2.title-news'):
            link = i.css('a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(link), callback=self.parse2)

    def parse2(self, response):
        def getbody(query):
            s = ""
            for i in response.css(query):
                p_body = i.get()
                s = s + p_body + '\n'
            return s
        yield {
            "Tiêu đề": response.css("h1.title-detail::text").get(),
            "Thời gian": response.css("span.date::text").get(),
            "Nội dung": getbody("p::text"),
        }

