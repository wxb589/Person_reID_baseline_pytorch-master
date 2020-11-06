from torchvision import models
model = models.resnet50(pretrained=True)
print(model)
