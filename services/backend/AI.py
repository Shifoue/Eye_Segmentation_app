from PIL import Image
import torch
import torchvision.transforms as transforms

from backend.network.get_network import create_network
from backend.network.processing.transforms import get_transforms

WEIGHTS_PATH = "backend/network/weights/checkpoint_85_ADAMW.pth"

class AI_process():
    def __init__(self):
        self.model = create_network(WEIGHTS_PATH)

    def segmented_image(self, image, mask, alpha=0.7):
        segmentation = image * mask

        masked_image = segmentation + (1 - alpha) * (1 - mask) * image

        return transforms.ToPILImage()(masked_image[0])

    def process(self, image):
        _, val_transform = get_transforms()
        image = val_transform(image)

        image = torch.unsqueeze(image, 0)

        predicted_mask = torch.sigmoid(self.model(image))

        predicted_mask = (predicted_mask > 0.5).float()

        masked_image = self.segmented_image(image, predicted_mask)

        return image, transforms.ToPILImage()(predicted_mask[0]), masked_image