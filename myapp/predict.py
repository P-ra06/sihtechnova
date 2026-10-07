import json
from pathlib import Path

from PIL import Image
import torch
from torchvision import transforms

from .model import get_crop_disease_model


# ---------------------------------------------------------
# Device
# ---------------------------------------------------------

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model.pth"
CLASSES_PATH = BASE_DIR / "class_names.json"


# ---------------------------------------------------------
# Load class names
# ---------------------------------------------------------

with open(CLASSES_PATH, "r") as f:
    class_names = json.load(f)

print("Number of classes:", len(class_names))


# ---------------------------------------------------------
# Create ResNet18 model
# ---------------------------------------------------------

model = get_crop_disease_model(
    num_classes=len(class_names),
    pretrained=False
)


# ---------------------------------------------------------
# Load trained weights
# ---------------------------------------------------------

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)

model = model.to(device)
model.eval()

print("ResNet18 model loaded successfully!")
print("Using device:", device)


# ---------------------------------------------------------
# Image preprocessing
# MUST MATCH TRAINING
# ---------------------------------------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ---------------------------------------------------------
# Prediction function
# ---------------------------------------------------------

def predict_image(image_source, top_k=5):

    """
    Run inference on a single crop/leaf image.

    image_source:
        File path or file-like object.

    top_k:
        Number of predictions to return.

    Returns:
        best_label
        best_confidence
        top_predictions
    """

    # Open image
    image = Image.open(image_source).convert("RGB")

    # Apply preprocessing
    tensor = transform(image)

    # Add batch dimension
    tensor = tensor.unsqueeze(0).to(device)

    # Model inference
    with torch.inference_mode():

        logits = model(tensor)

        probabilities = torch.softmax(
            logits,
            dim=1
        )

    # Get top predictions
    k = min(top_k, len(class_names))

    topk_prob, topk_class = torch.topk(
        probabilities,
        k
    )

    top_predictions = []

    for prob, cls in zip(
        topk_prob[0],
        topk_class[0]
    ):

        label = class_names[
            cls.item()
        ].replace("___", " - ")

        confidence = round(
            prob.item() * 100,
            2
        )

        top_predictions.append({
            "label": label,
            "confidence": confidence
        })


    # Best prediction
    best = top_predictions[0]

    return (
        best["label"],
        best["confidence"],
        top_predictions
    )


# ---------------------------------------------------------
# CLI testing
# ---------------------------------------------------------

if __name__ == "__main__":

    import sys

    if len(sys.argv) > 1:

        test_image_path = Path(
            sys.argv[1]
        ).resolve()

    else:

        test_image_path = (
            BASE_DIR / "test.jpg"
        )


    print("=" * 60)

    print(
        f"Testing image from path:\n"
        f"--> {test_image_path}"
    )

    print("=" * 60)


    if not test_image_path.exists():

        print(
            f"Error: Image not found at "
            f"{test_image_path}"
        )

        sys.exit(1)


    label, confidence, top5 = predict_image(
        test_image_path
    )


    print(
        f"\nFinal Prediction: "
        f"{label} ({confidence:.2f}%)"
    )

    print("\nTop predictions:")

    for prediction in top5:

        print(
            f"  {prediction['label']}: "
            f"{prediction['confidence']:.2f}%"
        )