from colorama import init, Fore
init(autoreset=True)


def red(txt):
   return Fore.RED + txt + Fore.RESET


class ConfigurationError(Exception):
   "notify user of configuration problem"

   def __init__(self, configurable, item):
      self.configurable = configurable
      self.item = item

   def __str__(self):
      msg = "There is no %s titled '%s' in your configuration"
      return red(msg % (self.configurable, self.item))


class ComponentLoadingError(Exception):
   "notify user of component loading problem"

   def __init__(self, module, name, package=""):
      if package:
         package = "(%s)" % package
      self.fullname = "%s%s.%s" % (package, module, name)

   def __str__(self):
      return red("There is no component '%s' installed." % self.fullname)
