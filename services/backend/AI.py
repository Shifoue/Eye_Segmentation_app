from PIL import Image
import torch
import torchvision.transforms as transforms

from backend.network.get_network import create_network
from backend.network.processing.transforms import get_transforms

WEIGHTS_PATH = "backend/network/weights/checkpoint_85_ADAMW.pth"

class AI_process():
    def __init__(self):
        self.model = create_network(WEIGHTS_PATH)

    def process(self, image):
        _, val_transform = get_transforms()
        image = val_transform(image)

        image = torch.unsqueeze(image, 0)

        predicted_mask = self.model(image)

        return transforms.ToPILImage()(predicted_mask[0])