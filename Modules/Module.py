
# Here iam calling the function from the Functions Folder to Modules Folder

import importlib.util
import sys
sys.path.insert(0, "../Functions/Functions.py")
from Functions.Functions import addition

spec = importlib.util.spec_from_file_location("Functions", "../Functions/Functions.py")
module = importlib.util.module_from_spec(spec)
sys.modules["Function"] = module
spec.loader.exec_module(module)
from Functions import Functions
