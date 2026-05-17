# 训练钩子子模块
# 作用: 提供训练过程中的各类钩子，用于扩展训练功能
# 主要接口/类:
#   - Hook: 钩子基类
#   - Priority: 钩子优先级
#   - get_priority: 获取优先级函数
#   - build_hook: 构建钩子的工厂函数
#   - HOOKS: 钩子注册表
#   - EarlyStopHook: 早停钩子
#   - SparsityHook: 稀疏化钩子
#   - EvaluationHook: 评估钩子
#   - IterTimerHook: 迭代计时钩子
#   - TensorBoardHook: TensorBoard日志钩子
#   - TextLoggerHook: 文本日志钩子
#   - LrSchedulerHook: 学习率调度钩子
#   - ApexAMPOptimizerHook, NoneOptimizerHook, OptimizerHook, TorchAMPOptimizerHook: 优化器钩子
#   - CheckpointHook, LoadCheckpointHook, BestCkptSaverHook: 检查点钩子
#   - DDPHook: DDP分布式钩子
#   - DeepspeedHook: Deepspeed分布式钩子
#   - MegatronHook: Megatron分布式钩子
#   - SwiftHook: Swift高效微调钩子
