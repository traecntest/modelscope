# 模型训练模块
# 作用: 提供模型训练、评估、微调的完整训练框架
# 主要接口/类:
#   - EpochBasedTrainer: 基于轮次的训练器基类
#   - TrainingArgs: 训练参数配置
#   - build_trainer: 构建训练器的工厂函数
#   - Hook, Priority: 训练钩子机制
#   - build_dataset_from_file: 从文件构建数据集
#   - 支持NLP、CV、音频、多模态领域的训练器
