# 评估指标模块
# 作用: 提供各类AI任务的评估指标计算功能
# 主要接口/类:
#   - Metric: 评估指标基类
#   - build_metric: 构建评估指标的工厂函数
#   - task_default_metrics: 任务默认指标映射
#   - METRICS: 指标注册表
#   - AccuracyMetric: 准确率指标
#   - AudioNoiseMetric: 音频噪声指标
#   - BleuMetric: BLEU翻译质量指标
#   - ImageColorEnhanceMetric: 图像色彩增强指标
#   - ImageColorizationMetric: 图像着色指标
#   - ImageDenoiseMetric: 图像去噪指标
#   - ImageInpaintingMetric: 图像修复指标
#   - ImageInstanceSegmentationCOCOMEMetric: 图像实例分割COCO指标
#   - ImagePortraitEnhancementMetric: 图像人像增强指标
#   - ImageQualityAssessmentDegradationMetric: 图像质量评估退化指标
#   - ImageQualityAssessmentMosMetric: 图像质量评估MOS指标
#   - LossMetric: 损失指标
#   - MovieSceneSegmentationMetric: 电影场景分割指标
#   - OCRRecognitionMetric: OCR识别指标
#   - PplMetric: 困惑度指标
#   - ReferringVideoObjectSegmentationMetric: 视频对象分割指标
#   - SequenceClassificationMetric: 序列分类指标
#   - TextGenerationMetric: 文本生成指标
#   - TextRankingMetric: 文本排序指标
#   - TokenClassificationMetric: Token分类指标
#   - TranslationEvaluationMetric: 翻译评估指标
#   - VideoFrameInterpolationMetric: 视频帧插值指标
#   - VideoStabilizationMetric: 视频稳像指标
#   - VideoSummarizationMetric: 视频摘要指标
#   - VideoSuperResolutionMetric: 视频超分辨率指标
