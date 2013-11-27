from util import yamlconfig, import_pipeparts


class Streamer:

   def __init__(self, configfile="config.yaml"):
      ""
      self.config = yamlconfig(configfile)
      configs = self.config["pipes"]
      parts = []
      for name, cfg in configs.items():
         for part in cfg:
            klass = import_klass(part["use"], package="jetstream")
            parts.append(klass)
         pipe = piped(parts)
         result = []
         for r in pipe:
            result.append(r)

   def __iter__(self):
      ""
      return self.pipe

   def __repr__(self):
      ""

