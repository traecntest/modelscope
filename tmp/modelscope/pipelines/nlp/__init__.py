# NLP流水线子模块
# 作用: 提供自然语言处理领域的各类推理流水线
# 主要接口/类:
#   - AutomaticPostEditingPipeline: 自动后编辑流水线
#   - ConversationalTextToSqlPipeline: 对话式文本转SQL流水线
#   - TableQuestionAnsweringPipeline: 表格问答流水线
#   - DialogIntentPredictionPipeline: 对话意图预测流水线
#   - DialogModelingPipeline: 对话建模流水线
#   - DialogStateTrackingPipeline: 对话状态跟踪流水线
#   - DocumentSegmentationPipeline: 文档分割流水线
#   - ExtractiveSummarizationPipeline: 抽取式摘要流水线
#   - PolyLMTextGenerationPipeline: PolyLM文本生成流水线
#   - FasttextSequenceClassificationPipeline: FastText序列分类流水线
#   - FaqQuestionAnsweringPipeline: FAQ问答流水线
#   - FeatureExtractionPipeline: 特征提取流水线
#   - FillMaskPipeline: 掩码填充流水线
#   - InformationExtractionPipeline: 信息抽取流水线
#   - InteractiveTranslationPipeline: 交互式翻译流水线
#   - NamedEntityRecognitionPipeline: 命名实体识别流水线
#   - TextRankingPipeline: 文本排序流水线
#   - SentenceEmbeddingPipeline: 句子向量流水线
#   - TextClassificationPipeline: 文本分类流水线
#   - SummarizationPipeline: 摘要流水线
#   - TranslationQualityEstimationPipeline: 翻译质量评估流水线
#   - TextErrorCorrectionPipeline: 文本纠错流水线
#   - WordAlignmentPipeline: 词对齐流水线
#   - TextGenerationPipeline, TextGenerationT5Pipeline, SeqGPTPipeline, ChatGLM6bTextGenerationPipeline, ChatGLM6bV2TextGenerationPipeline, QWenChatPipeline, QWenTextGenerationPipeline, Llama2TaskPipeline: 文本生成流水线
#   - FidDialoguePipeline: FiD对话流水线
#   - TokenClassificationPipeline: Token分类流水线
#   - TranslationPipeline: 翻译流水线
#   - CanmtTranslationPipeline: Canmt翻译流水线
#   - WordSegmentationPipeline, WordSegmentationThaiPipeline: 分词流水线
#   - ZeroShotClassificationPipeline: 零样本分类流水线
#   - MGLMTextSummarizationPipeline: MGLM文本摘要流水线
#   - CodeGeeXCodeTranslationPipeline: CodeGeeX代码翻译流水线
#   - CodeGeeXCodeGenerationPipeline: CodeGeeX代码生成流水线
#   - GLM130bTextGenerationPipeline: GLM130b文本生成流水线
#   - TranslationEvaluationPipeline: 翻译评估流水线
#   - UserSatisfactionEstimationPipeline: 用户满意度评估流水线
#   - SiameseUiePipeline: Siamese UIE流水线
#   - DocumentGroundedDialogGeneratePipeline: 文档对话生成流水线
#   - DocumentGroundedDialogRetrievalPipeline: 文档对话检索流水线
#   - DocumentGroundedDialogRerankPipeline: 文档对话重排序流水线
#   - LanguageIdentificationPipeline: 语言识别流水线
#   - MachineReadingComprehensionForNERPipeline: 机器阅读理解NER流水线
#   - LLMPipeline: 大语言模型流水线
