export REPLICATE_API_TOKEN=[657dae1d294bc323ddde8aaed9c643e75c78c898]
import replicate
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")
output = version.predict(prompt="a photo of an astronaut riding a horse on mars")