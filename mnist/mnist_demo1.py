import torch
import torchvision
import torchvision.transforms as transforms

# 定义数据变换
transform = transforms.Compose([
    transforms.ToTensor(),  # 将图像转换为 Tensor
    transforms.Normalize((0.5,), (0.5,))  # 归一化到 [-1, 1]
])

# 下载和加载训练集
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True, num_workers=2)

# 下载和加载测试集
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False, num_workers=2)

# 检查数据集
print("Training set size:", len(trainset))
print("Testing set size:", len(testset))

# 检查 DataLoader
for images, labels in trainloader:
    print("Batch shape:", images.shape)
    print("Labels shape:", labels.shape)
    break  # 只检查第一个批次