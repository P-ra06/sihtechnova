import json
import math
from pathlib import Path

_METRICS_PATH = Path(__file__).resolve().parent / "metrics.json"


def _ring(value):
    return round(float(value), 2)


def _radar_points(metrics, size=220, min_val=90):
    """Map accuracy/precision/recall/F1 onto a 4-spoke radar (90–100% scale)."""
    keys = ("accuracy", "precision", "f1_score", "recall")
    cx = cy = size / 2
    radius = size * 0.38
    points = []
    for index, key in enumerate(keys):
        fraction = (float(metrics[key]) - min_val) / (100 - min_val)
        fraction = max(0.05, min(1.0, fraction))
        angle = (index / 4) * 2 * math.pi - math.pi / 2
        x = cx + radius * fraction * math.cos(angle)
        y = cy + radius * fraction * math.sin(angle)
        points.append(f"{x:.1f},{y:.1f}")
    return " ".join(points)


def _history_polyline(history, key, width=520, height=180, y_min=60, y_max=100):
    if not history:
        return ""
    n = len(history)
    pts = []
    for i, row in enumerate(history):
        x = 16 + (width - 32) * (i / max(n - 1, 1))
        value = float(row[key])
        y = height - 20 - (height - 36) * ((value - y_min) / (y_max - y_min))
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def load_metrics():
    with open(_METRICS_PATH, "r", encoding="utf-8") as handle:
        data = dict(json.load(handle))

    for key in ("accuracy", "precision", "recall", "f1_score"):
        value = float(data[key])
        data[f"{key}_label"] = f"{value:.2f}%"
        data[f"{key}_ring"] = _ring(value)

    data["radar_points"] = _radar_points(data)
    history = data.get("history", [])
    data["acc_line"] = _history_polyline(history, "accuracy")
    data["f1_line"] = _history_polyline(history, "f1_score")
    data["prec_line"] = _history_polyline(history, "precision")
    data["rec_line"] = _history_polyline(history, "recall")
    data["class_metrics"] = [
        {**row, "f1_width": _ring(row["f1"])}
        for row in data.get("class_metrics", [])
    ]
    return data
