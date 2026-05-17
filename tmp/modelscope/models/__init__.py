# 模型定义模块
# 作用: 提供各类AI模型的定义和实现
# 主要接口/类:
#   - Model: 模型基类
#   - TorchModel: PyTorch模型基类
#   - Head, TorchHead: 模型头部基类
#   - build_model: 构建模型的工厂函数
#   - MODELS, BACKBONES, HEADS: 模型注册表
#   - 支持NLP、CV、音频、多模态、科学计算领域的模型
