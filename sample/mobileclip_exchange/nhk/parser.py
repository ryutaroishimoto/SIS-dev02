#coding: utf-8
from xml.etree.ElementTree import ElementTree
import urllib
from mobileclip_exchange.dto_mobileclip import DTOMobileclip
class Parser :
  def __init__(self, uri) :
    self.uri = uri
  def parse(self) :
    array = []
    #FIXME:これは暫定です
    if self.uri != None :
      xml = ElementTree(file=urllib.urlopen(self.uri))
      for e in list(xml.getroot().getiterator()):
        if e.tag != None and e.text != None :
	  array.append({ e.tag.encode("utf-8") : e.text.encode("utf-8")})
    self.parse_result = array 
    return self

  #parse結果をmobileclipDTOに変換する
  def exchange(self) :
    result = []
    if self.parse_result :
      for obj in self.parse_result :
        dto = DTOMobileclip()
	dto.hoge = obj
	result.append(dto)
    return result
