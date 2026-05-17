# ModelScope 主模块
# 作用: 提供AI模型开发、训练、推理的一站式平台
# 主要接口/类:
#   - Exporter, TfModelExporter, TorchModelExporter: 模型导出器
#   - HubApi: ModelScope Hub API接口
#   - snapshot_download, dataset_snapshot_download: 模型/数据集下载
#   - Metric, AccuracyMetric, BleuMetric等: 各类评估指标
#   - Model, TorchModel: 模型基类
#   - MsDataset: 数据集类
#   - Pipeline, pipeline: 推理流水线
#   - Preprocessor: 数据预处理器基类
#   - EpochBasedTrainer, TrainingArgs: 训练器及训练参数
#   - Tasks: 任务类型常量
#   - get_logger: 日志工具
#   - __version__: 版本信息
