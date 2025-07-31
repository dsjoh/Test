import torch
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(device)

