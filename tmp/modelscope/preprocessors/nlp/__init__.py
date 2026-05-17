# NLP数据预处理子模块
# 作用: 提供自然语言处理领域的数据预处理功能
# 主要接口/类:
#   - WordAlignmentPreprocessor: 词对齐预处理器
#   - TextErrorCorrectionPreprocessor: 文本纠错预处理器
#   - TextGenerationJiebaPreprocessor: 文本生成Jieba预处理器
#   - Tokenize: 分词预处理器
#   - DocumentSegmentationTransformersPreprocessor: 文档分割预处理器
#   - FaqQuestionAnsweringTransformersPreprocessor: FAQ问答预处理器
#   - FillMaskPoNetPreprocessor: 掩码填充PoNet预处理器
#   - FillMaskTransformersPreprocessor: 掩码填充Transformers预处理器
#   - TextRankingTransformersPreprocessor: 文本排序预处理器
#   - RelationExtractionTransformersPreprocessor: 关系抽取预处理器
#   - SentenceEmbeddingTransformersPreprocessor: 句子嵌入预处理器
#   - TextClassificationTransformersPreprocessor: 文本分类预处理器
#   - TextGenerationTransformersPreprocessor: 文本生成预处理器
#   - TextGenerationT5Preprocessor: 文本生成T5预处理器
#   - TextGenerationSentencePiecePreprocessor: 文本生成SentencePiece预处理器
#   - SentencePiecePreprocessor: SentencePiece预处理器
#   - TokenClassificationTransformersPreprocessor: Token分类预处理器
#   - WordSegmentationBlankSetToLabelPreprocessor: 分词空白标签预处理器
#   - WordSegmentationPreprocessorThai: 泰语分词预处理器
#   - NERPreprocessorThai: 泰语NER预处理器
#   - NERPreprocessorViet: 越南语NER预处理器
#   - ZeroShotClassificationTransformersPreprocessor: 零样本分类预处理器
#   - DialogIntentPredictionPreprocessor: 对话意图预测预处理器
#   - DialogModelingPreprocessor: 对话建模预处理器
#   - DialogStateTrackingPreprocessor: 对话状态跟踪预处理器
#   - InputFeatures: 输入特征
#   - MultiWOZBPETextField: MultiWOZ BPE文本域
#   - IntentBPETextField: 意图BPE文本域
#   - ConversationalTextToSqlPreprocessor: 对话文本转SQL预处理器
#   - TableQuestionAnsweringPreprocessor: 表格问答预处理器
#   - MGLMSummarizationPreprocessor: MGLM摘要预处理器
#   - TranslationEvaluationTransformersPreprocessor: 翻译评估预处理器
#   - CanmtTranslationPreprocessor: Canmt翻译预处理器
#   - DialogueClassificationUsePreprocessor: 对话分类预处理器
#   - SiameseUiePreprocessor: Siamese UIE预处理器
#   - DocumentGroundedDialogGeneratePreprocessor: 文档对话生成预处理器
#   - DocumentGroundedDialogRetrievalPreprocessor: 文档对话检索预处理器
#   - DocumentGroundedDialogRerankPreprocessor: 文档对话重排序预处理器
#   - MachineReadingComprehensionForNERPreprocessor: 机器阅读理解NER预处理器
