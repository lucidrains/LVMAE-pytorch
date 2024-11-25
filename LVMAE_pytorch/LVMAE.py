import torch
from torch.nn import Module, ModuleList
import torch.nn.functional as F

from vector_quantize_pytorch import FSQ

# main class

class LVAME(Module):
	def __init__(self):
		super().__init__()
