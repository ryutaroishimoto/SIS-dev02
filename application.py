#coding: utf-8
execfile("default_import.py")
from controllers.general import General

application = webapp.WSGIApplication(
  [('/', General)],
debug=True)

def main():
  run_wsgi_app(application)
if __name__ == "__main__": 
  main()
