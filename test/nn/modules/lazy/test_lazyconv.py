import torch
import torchex.nn as exnn


def test_conv1d():
    net = exnn.Conv1d(3, 2)
    print(net)

def test_conv1d():
    net = exnn.Conv1d(3, 2)
    x = torch.randn(10, 10, 20)
    y = net(x)
    assert list(y.shape) == [10, 3, 19]
    
def test_conv2d():
    net = exnn.Conv2d(3, 2)
    x = torch.randn(10, 20, 28, 28)
    y = net(x)
    assert list(y.shape) == [10, 3, 27, 27]

def test_conv3d():
    net = exnn.Conv3d(3, 2)
    x = torch.randn(10, 20, 28, 28, 28)
    y = net(x)
    assert list(y.shape) == [10, 3, 27, 27, 27]
    