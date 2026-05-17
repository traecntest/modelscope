# 数据预处理模块
# 作用: 提供各类数据预处理功能，将原始数据转换为模型可接受的格式
# 主要接口/类:
#   - Preprocessor: 预处理器基类
#   - build_preprocessor: 构建预处理器的工厂函数
#   - PREPROCESSORS: 预处理器注册表
#   - Compose, ToTensor, Filter: 通用预处理操作
#   - 支持NLP、CV、音频、多模态领域的数据预处理
