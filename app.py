from pytest import param
from flask import Flask
# from logging.config import dictConfig

import logging

# # # implement filter subclass
# # class SampleFilter(logging.Filter):
# #     def __init__(self, param=None):
# #         self.param = param

# #     def filter(self, record):
# #         if self.param in None:
# #             allow = True
# #         else:
# #             allow = self.param not in record.msg
# #         if allow:
# #             record.msg = 'changed: ' + record.msg
# #         return allow


# """"logging configuration"""
# dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     # set filter
#     # 'myfilter': {
#     #     '()': SampleFilter,
#     #     'param': 'noshow',
#     # },

#   #  log messages formatter
#    'formatters' : {
#      'default':{
#        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s '
#       },
#       'simpleformatter': {
#         'format': '%(asctime)s - %(name)s  %(levelname)s: %(message)s'
#       },
#    },

#   # Handlers
#   'handlers':{
#     'custom_handler': {
#         'class' : 'logging.FileHandler',
#         'formatter': 'default',
#         'filename' : 'warnings.log',
#         'level': 'WARN',
#         # pass the filter to handler
#         # 'filters' : ['myfilter']
#     }
#   },

#   # logger
#   'root': {
#     'level': 'WARN',
#     'handlers': ['custom_handler'],
    
#   },

# })

# logging.basicConfig(filename='record.log', level=logging.DEBUG)
logging.basicConfig(filename='record.log', 
                level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)

@app.route('/')
def main():
  # showing different logging levels
  app.logger.debug("debug log info")
  app.logger.info("Info log information")
  app.logger.warning("Warning log info")
  app.logger.error("Error log info")
  app.logger.critical("Critical log info")
  return "testing logging levels."


if __name__ == '__main__':
  app.run(debug=True)
