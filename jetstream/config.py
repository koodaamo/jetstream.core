"Jetstream configuration"

from contextlib import closing
from urllib import parse, request
import yaml


def from_yaml(path_or_url):
   "load YAML configuration from path or URL"
   url = parse.urlparse(path_or_url)
   # has to be a path
   if not url.scheme:
      with open(url.netloc+url.path) as yamlfile:
         return yaml.load(yamlfile)
   else:
      with closing(request.urlopen(url.geturl())) as result:
         return yaml.load(result)


class MappingConfig:

   def __init__(self, mapping):
      self.config = mapping

   @property
   def inputs(self):
      "return the inputs configuration"
      return self.config["inputs"]

   @property
   def outputs(self):
      "return the outputs configuration"
      return self.config["outputs"]

   @property
   def inspectors(self):
      "return the inspectors configuration"
      return self.config["inspectors"]

   @property
   def transformers(self):
      "return the transformers configuration"
      return self.config["transformers"]

   @property
   def pipes(self):
      "return the pipes configuration"
      return self.config["pipes"]
