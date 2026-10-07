import torch
import torch.nn as nn
from torchvision import models


def get_crop_disease_model(
    num_classes: int = 38,
    pretrained: bool = False
) -> nn.Module:

    weights = (
        models.ResNet18_Weights.DEFAULT
        if pretrained
        else None
    )

    model = models.resnet18(weights=weights)

    # Replace ResNet18 classification head
    in_features = model.fc.in_features
    model.fc = nn.Linear(
        in_features,
        num_classes
    )

    return model