import torch

from backend.network.model.Unet import myUNET

WEIGHTS_PATH = "weights/checkpoint_85_ADAMW.pth"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def create_network(weights=WEIGHTS_PATH, device=DEVICE):
    UNET = myUNET(in_channels=3, out_channels=1).to(device)

    checkpoint = torch.load(weights,  map_location=torch.device(device))

    UNET.load_state_dict(checkpoint["state_dict"])

    return UNET