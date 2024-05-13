from PIL import Image
import torch

from backend.network.get_network import create_network
from backend.network.processing.transforms import get_transforms

WEIGHTS_PATH = "backend/network/weights/checkpoint_85_ADAMW.pth"

class AI_process():
    def __init__(self):
        self.model = create_network(WEIGHTS_PATH)

    def process(self, image_file):
        origin_image = Image.open(image_file)

        _, val_transform = get_transforms()
        image = val_transform(origin_image)

        image = torch.unsqueeze(image, 0)

        predicted_mask = self.model(image)

        return predicted_mask