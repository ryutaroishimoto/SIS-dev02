#coding: utf-8
from mobileclip_exchange.rss_generator import RssGenerator
from mobileclip_exchange.nhk.parser import Parser

#main function
RssGenerator.set_parser(Parser)

#parse実行
generator = RssGenerator()
generator.parse()
