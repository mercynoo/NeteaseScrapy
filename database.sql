create database scrapy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use scrapy;
CREATE TABLE NeteaseJob (
    name VARCHAR(100) NOT NULL PRIMARY KEY , # 职位名称
    url VARCHAR(200), # 职位链接
    category VARCHAR(150), # 职位类别
    type VARCHAR(150), # 工作类型
    locate VARCHAR(150), # 工作地点
    amount INTEGER(100), # 招聘人数
    time VARCHAR(150) # 发布时间
)