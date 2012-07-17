#coding: utf-8
from mobileclip_exchange.exchange_service import ExchangeService
from mobileclip_exchange.dto_mobileclip import DTOMobileclip
from mobileclip_exchange.nhk.parser import Parser

#main function
ExchangeService.set_strategy(Parser)

#parse実行
generator = ExchangeService("https://api.depot.nhk-ed.co.jp/webapi/WebAPI.asmx/OutputMaterialXML?i_distribution=0040&i_requestXML=1000000008_KR00013745.xml")
generator.parse()
rss = generator.to_rss()
print rss
