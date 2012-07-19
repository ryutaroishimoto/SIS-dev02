#coding: utf-8
# package mobileclip_exchange.exchange_service
# author ohta@rhd
import feedgenerator
from datetime import datetime
class ExchangeService :
  parser = None #please set parser strategy

  #set parse strategy
  @classmethod
  def set_strategy(cls, parser) :
    cls.parser = parser

  #initialize
  def __init__(self, uri) :
    self.uri = uri
    self.exchanged_array = None

  #delegate parser class
  def parse(self) :
    if self.parser != None :
      parser = self.parser(self.uri)
      #XMLの中身を取得
      xml = parser.parse().exchange()
      self.exchanged_array = xml
      return self

  #make mobileclip rss
  #return rss
  def to_rss(self) :
    #TODO: mock
    feed = feedgenerator.Rss201rev2Feed(
             title = u"sample",
	     link = ur"http://example.com",
	     feed_url = ur"http://example.com",
	     description = u"RSS2feed",
	     language = u"ja"
	)

    feed.add_item(
             title = u"sample_example",
	     link = ur"http://example.com",
	     description = u"example",
	     pubdate = datetime.now()
	)
    return feed.writeString("utf-8")

  #永続化
  #return t/f
  def save(self) :
    print "hoge"
