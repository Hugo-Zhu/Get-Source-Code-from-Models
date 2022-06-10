import os
import torch
import inspect
from torch import nn

def get_model_source(model, model_dict):
    if isinstance(model, nn.Module) and inspect.getsourcefile(model.__class__)!=inspect.getsourcefile(nn.Module):
#         print(model.__class__)
#         print(inspect.getsource(model.__class__))
#         print(inspect.getsourcefile(model.__class__))
#         print(inspect.getsourcelines(model.__class__))
        model_dict[str(model.__class__)] = inspect.getsource(model.__class__)
    else: return
    for k, v in model.named_children():
        get_model_source(v, model_dict)

def get_source(model:nn.Module, target_file:str):
    """
    参数：
        model为类
    """
    model_dict = {}
    get_model_source(model, model_dict)
    if os.path.isfile(target_file):
        raise Exception(f'{target_file} 已存在!') 
    with open(target_file, 'a') as file:
        for model_source in model_dict.values():
            file.write(model_source)