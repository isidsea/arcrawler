from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "siamsubaru"
	CRAWLER_NAME = "Siamsubaru Crawler"
	LINK_TO_CRAWL = [
		"http://www.siamsubaru.com/subaruboard/index.php/board,1.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,12.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,2.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,11.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,26.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,34.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,27.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,28.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,29.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,30.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,31.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,32.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,35.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,38.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,15.0.html",
		"http://www.siamsubaru.com/subaruboard/index.php/board,6.0.html"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagesection']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//div[@class='pagesection']//strong)[last()-1]/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//h5[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//div[@class='poster']/h4//text()"
		}},		
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigate_section']//li[@class='last']/a//text()"
		}}       
	]
	CONDITIONS={
		"has_to_have_content":{
			"condition":'"content" in document',
			"exception":'"Content is not defined"'
		},
		"content_cannot_be_empty":{
			"condition":'len(document["content"]) > 0',
			"exception":'"Content cannot be empty"'
		}
	}
#end class
