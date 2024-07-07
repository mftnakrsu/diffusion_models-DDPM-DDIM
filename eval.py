import torch
from models import ContextUnet
from config import save_dir, device

def load_model(model_path):
    """
    Loads a pre-trained model from the given path and returns it.
    """
    model = ContextUnet(in_channels=3, n_feat=64, n_cfeat=5, height=16).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

    print("Model loaded successfully and set to evaluation mode.")

    return model

def main():
    # Load the model
    model_path = f"{save_dir}/model_trained.pth"
    nn_model = load_model(model_path)

