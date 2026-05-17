# 学习率调度子模块
# 作用: 提供各类学习率调度策略
# 主要接口/类:
#   - LR_SCHEDULER: 学习率调度器注册表
#   - build_lr_scheduler: 构建学习率调度器的工厂函数
#   - BaseWarmup: Warmup基类
#   - ConstantWarmup, ExponentialWarmup, LinearWarmup: 各类Warmup策略
