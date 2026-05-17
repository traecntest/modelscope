# 训练钩子子模块
# 作用: 提供训练过程中的各类钩子，用于扩展训练功能
# 主要接口/类:
#   - Hook: 钩子基类
#   - Priority: 钩子优先级
#   - build_hook: 构建钩子的工厂函数
#   - HOOKS: 钩子注册表
#   - CheckpointHook, LoadCheckpointHook, BestCkptSaverHook: 检查点钩子
#   - EvaluationHook: 评估钩子
#   - LrSchedulerHook: 学习率调度钩子
#   - OptimizerHook, ApexAMPOptimizerHook, TorchAMPOptimizerHook: 优化器钩子
#   - TensorboardHook, TextLoggerHook: 日志钩子
#   - IterTimerHook: 迭代计时钩子
#   - EarlyStopHook: 早停钩子
#   - SparsityHook: 稀疏化钩子
#   - DDPHook, DeepspeedHook, MegatronHook: 分布式训练钩子
#   - SwiftHook: Swift高效微调钩子
