import wsgiref.handlers
from google.appengine.ext import webapp
execfile("default_import.py")
class General(webapp.RequestHandler):
  def get(self) :
    hoge = {"hoge": "Hoge"}
    path = os.path.join(os.path.dirname(__file__), '../views/general/index.html')
    self.response.out.write(template.render(path, hoge))
