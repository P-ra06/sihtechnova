from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .predict import predict_image
from .disease_info import get_disease_guide
from .metrics import load_metrics


def _home_context(**extra):
    context = {"metrics": load_metrics()}
    context.update(extra)
    return context


def index(request):
    return render(request, "myapp/index.html", _home_context())


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

        return render(request, "myapp/login.html", {
            "error": "Invalid username or password",
            "metrics": load_metrics(),
        })

    return render(request, "myapp/login.html", {
        "metrics": load_metrics(),
    })


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "myapp/signup.html", {
                "error": "Username already exists",
                "metrics": load_metrics(),
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")

    return render(request, "myapp/signup.html", {
        "metrics": load_metrics(),
    })


def logout_view(request):
    logout(request)
    return redirect("index")


def predict(request):
    if request.method == "POST":
        image = request.FILES.get("image")

        if not image:
            return redirect("index")

        try:
            disease, confidence, top_predictions = predict_image(image)

            # Automatically get crop from the predicted class
            crop_name = disease.split(" - ")[0]
            guide = get_disease_guide(disease)

            return render(request, "myapp/index.html", _home_context(
                prediction={
                    "crop_name": crop_name,
                    "disease": disease,
                    "confidence": confidence,
                    "top_predictions": top_predictions,
                    "prevention": guide["prevention"],
                    "management": guide["management"],
                    "is_healthy": guide["is_healthy"],
                }
            ))

        except Exception as e:
            return render(request, "myapp/index.html", _home_context(
                error=str(e)
            ))

    return redirect("index")