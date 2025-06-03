import torch, transformers, datasets, evaluate

print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("Datasets:", datasets.__version__)
print("GPU Available:", torch.cuda.is_available())
