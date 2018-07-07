import scrapy

class JobItem(scrapy.Item):
    # 职位名称
    name = scrapy.Field()
    # 职位链接
    url = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 工作类型
    type =scrapy.Field()
    # 地点
    locate = scrapy.Field()
    # 人数
    amount = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
