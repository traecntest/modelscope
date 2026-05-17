# ModelScope 主模块
# 作用: 提供AI模型开发、训练、推理的一站式平台
# 主要接口/类:
#   - Exporter, TfModelExporter, TorchModelExporter: 模型导出器
#   - HubApi: ModelScope Hub API接口
#   - snapshot_download, dataset_snapshot_download, model_file_download, dataset_file_download: 模型/数据集下载
#   - check_local_model_is_latest, check_model_is_id, push_to_hub, push_to_hub_async: 模型管理
#   - Metric, AccuracyMetric, AudioNoiseMetric, BleuMetric, ImageColorEnhanceMetric, ImageColorizationMetric, ImageDenoiseMetric, ImageInpaintingMetric, ImageInstanceSegmentationCOCOMEMetric, ImagePortraitEnhancementMetric, ImageQualityAssessmentDegradationMetric, ImageQualityAssessmentMosMetric, LossMetric, MovieSceneSegmentationMetric, OCRRecognitionMetric, PplMetric, ReferringVideoObjectSegmentationMetric, SequenceClassificationMetric, TextGenerationMetric, TextRankingMetric, TokenClassificationMetric, TranslationEvaluationMetric, VideoFrameInterpolationMetric, VideoStabilizationMetric, VideoSummarizationMetric, VideoSuperResolutionMetric, task_default_metrics: 各类评估指标
#   - Model, TorchModel: 模型基类
#   - MsDataset: 数据集类
#   - Pipeline, pipeline: 推理流水线
#   - Preprocessor: 数据预处理器基类
#   - EpochBasedTrainer, TrainingArgs, Hook, Priority, build_dataset_from_file: 训练器及训练参数
#   - Tasks: 任务类型常量
#   - get_logger: 日志工具
#   - __release_datetime__, __version__: 版本信息
