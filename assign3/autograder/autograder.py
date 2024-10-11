from utils import Autograder
import os

from pygccxml import utils as gccutils
from pygccxml import declarations
from pygccxml import parser

import logging

# This should prevent pygccxml from outputting INFO messages
gccutils.loggers.set_level(logging.WARNING)

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
AUTOGRADER_DIR = os.path.join(PATH, "autograder")

def setup():
  main_cpp_path = os.path.join(PATH, "main.cpp")
  if not os.path.isfile(main_cpp_path): raise RuntimeError("Couldn't find '{main.cpp}'. Did you delete it from the starter code?")

  # Grab the C++ parser
  generator_path, generator_name = gccutils.find_xml_generator()

  # Configure the C++ parser
  xml_generator_config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name
  )

  decls = parser.parse([main_cpp_path], xml_generator_config)
  global_namespace = declarations.get_global_namespace(decls)
  classes = global_namespace.classes()
  print(classes)


if __name__ == "__main__":
    grader = Autograder()
    grader.setup = setup
    grader.run()
