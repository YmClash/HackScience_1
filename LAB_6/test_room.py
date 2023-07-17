import gradio
import torch
from torchvision.transforms import transforms
from PIL import Image
#
torch_version = torch.__version__
print(torch_version)


# marie_claire = torch.load('Marie_Claire_model_3_10.pth')
# marie_claire.eval()
#
#
#
# preprocess = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0,224,0.225])
# ])
#
#
# def prediction(image):
#     img = Image.fromarray(image.astype('uint8'),'RGB')
#     img = preprocess(img)
#     img = img.unsqueeze(0)
#
#
#     with torch.no_grad():
#         outputs = marie_claire(img)
#
#     _, predicted = torch.max(outputs.data,1)
#     predicted_label = str(predicted._idx.item())
#
#     return predicted_label
#
#
#
# test_lab= gradio.Interface(fn=prediction,inputs="image",outputs="label",description="")
#
#
#
# test_lab.launch()
#
