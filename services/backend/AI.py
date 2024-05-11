from PIL import Image

from backend.network.get_network import create_network
from backend.network.processing.transforms import get_transforms

WEIGHTS_PATH = "network/weights/checkpoint_85_ADAMW.pth"

class AI_process():
    def __init__(self):
        self.model = create_network(WEIGHTS_PATH)

    def process(self, image_file):
        origin_image = Image.open(image_file)

        _, val_transform = get_transforms()
        image = val_transform(origin_image)

        predicted_mask = self.model(image)

        return predicted_mask