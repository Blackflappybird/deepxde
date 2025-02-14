"""Package for tensorflow.compat.v1 NN modules."""

__all__ = [
    "DeepONet",
    "DeepONetCartesianProd",
    "FNN",
    "FourierDeepONetCartesianProd",
    "MfNN",
    "MfONet",
    "MIONet",
    "MIONetCartesianProd",
    "MsFFN",
    "NN",
    "PFNN",
    "ResNet",
    "STMsFFN",
]

from .deeponet import DeepONet, DeepONetCartesianProd, FourierDeepONetCartesianProd
from .fnn import FNN, PFNN
from .mfnn import MfNN
from .mfonet import MfONet
from .mionet import MIONet, MIONetCartesianProd
from .msffn import MsFFN, STMsFFN
from .nn import NN
from .resnet import ResNet
