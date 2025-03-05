import os
from PyFlow.Core.PackageBase import PackageBase

class PyFlowOpenCv(PackageBase):
	"""OpenCv pyflow package
	"""	
	def __init__(self):
		super(PyFlowOpenCv, self).__init__()
		self.analyzePackage(os.path.dirname(__file__))

