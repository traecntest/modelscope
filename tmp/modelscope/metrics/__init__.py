# 评估指标模块
# 作用: 提供各类AI任务的评估指标计算功能
# 主要接口/类:
#   - Metric: 评估指标基类
#   - build_metric: 构建评估指标的工厂函数
#   - task_default_metrics: 任务默认指标映射
#   - METRICS: 指标注册表
#   - AccuracyMetric: 准确率指标
#   - BleuMetric: BLEU翻译质量指标
#   - LossMetric: 损失指标
#   - SequenceClassificationMetric: 序列分类指标
#   - TokenClassificationMetric:  Token分类指标
#   - TextGenerationMetric: 文本生成指标
#   - ImageColorEnhanceMetric, ImageDenoiseMetric等: 图像质量指标
#   - VideoSuperResolutionMetric等: 视频质量指标
#   - AudioNoiseMetric: 音频噪声指标
