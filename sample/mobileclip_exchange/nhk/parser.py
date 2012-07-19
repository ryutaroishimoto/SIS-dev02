#coding: utf-8
# package mobileclip_exchange.nhk.parser
from xml.etree.ElementTree import ElementTree
import urllib
from mobileclip_exchange.dto_mobileclip import DTOMobileclip
class Parser :

  #initialize
  def __init__(self, uri) :
    self.uri = uri

  def parse(self) :
    array = []
    #FIXME:これは暫定です
    if self.uri != None :
      xml = ElementTree(file=urllib.urlopen(self.uri))
      #Recipe node get
      items = []
      dto = DTOMobileclip()
      e = xml.find("//Recipe")
      dto.title = e.find("Title").text.encode("utf-8")
      for author in e.find("Authors").iter() :
        dto.author = author.text.encode("utf-8")
    self.parse_result = [dto]
    return self

  #parse結果をmobileclipDTOに変換する
  def exchange(self) :
    return self.parse_result
