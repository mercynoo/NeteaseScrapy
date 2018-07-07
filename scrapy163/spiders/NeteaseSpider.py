import scrapy

from scrapy163.JobItems import JobItem

class NeteaseSpider(scrapy.Spider):
    # 设置name
    name = "NeteaseSpider"
    # 设置域名
    allowed_domains = ["hr.163.com"]
    # 填写爬去地址
    start_urls = ["https://hr.163.com/position/list.do"]
    # 爬取
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = JobItem()

        # 先获取一条招聘的div
        for box in response.xpath('//*[@id="position-table-25841"]/tbody'):
        #     # 获取每个div中的课程路径
        #     item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
        #     # 获取div中的课程标题
        #     item['title'] = box.xpath('.//h3/text()').extract()[0].strip()
        #     # 获取div中的标题图片地址
        #     item['image_url'] = "http:" + box.xpath('.//@src').extract()[0]
        #     # 获取学生数量信息
        #     item['student'] = box.xpath('.//span/text()').extract()[0].strip()
        #     # 获取div中的课程简介
        #     item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
        #     # 返回信息
        #     yield item
        #
        #     # url跟进开始
        #     # 获取下一页的url信息
        # url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        # if url:
        #     # 将信息组合成下一页的url
        #     page = 'http://www.imooc.com' + url[0]
        #     # 返回url
        #     yield scrapy.Request(page, callback=self.parse)
        # # url跟进结束

