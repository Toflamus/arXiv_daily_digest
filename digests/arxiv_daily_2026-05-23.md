# 每日精选 · 2026-05-23

> 数据源：GitHub Actions 预拉（arXiv 0 篇 + journals 241 篇，共 30 篇进入 top30）。
> ⚠️ **今日 arXiv 抓取返回 0 篇**（`arxiv_count: 0`，`arxiv_error: null`），top30 全为期刊论文。硬性要求"至少 2 篇 arXiv"无法满足，已在此说明原因。
> Top30 去重后（移除 1 篇已推送论文）精选 **5 篇**（arXiv: 0 + journals: 5）。

---

## 1. Accelerating Scientific Discovery with Co-Scientist
- **来源**: Nature（2026-05-19）
- **作者**: Authors not available
- **链接**: https://www.nature.com/articles/s41586-026-10644-y
- **方向**: 🤖 LLM / 🧪 自动化实验室
- **TL;DR**: Google Co-Scientist AI 系统大幅加速科学发现全流程
- **核心贡献**:
  - 提出 Co-Scientist 系统，将 AI 融入科学假设生成、文献综合和实验规划全流程
  - 系统在多个真实科学领域（含医学、生物）实现可验证的发现加速
  - 标志着 AI 从"辅助工具"升级为"主动参与者"的范式转变
- **方法亮点**: Co-Scientist 整合大语言模型与领域知识库，通过迭代的假设生成—验证—精炼循环，在受控实验条件下系统性推进科学探索。
- **为什么值得读**: 这是继 AlphaFold 之后又一个在 Nature 正刊发表的 AI 大规模推进科学前沿的里程碑，对计算生物、药物发现和基础研究的工作流程将产生深远影响。AI 科学家时代的具体实现细节在此首次公开。

---

## 2. SmileyLlama: Modifying Large Language Models for Directed Chemical Space Exploration
- **来源**: Nature Computational Science（2026-05-11）
- **作者**: Authors not available
- **链接**: https://www.nature.com/articles/s43588-026-00986-y
- **方向**: 🤖 LLM / 🔬 AI4Science
- **TL;DR**: 微调通用 LLM 生成具有用户指定性质的类药分子
- **核心贡献**:
  - 将通用 Llama 模型专用化，使其能在 SMILES 化学空间中按需生成类药分子
  - 支持用户指定药物化学相关性质（如 ADMET、靶点选择性）进行定向探索
  - 展示了将通用 LLM 迁移到垂直科学领域的可推广框架
- **方法亮点**: 通过指令微调和 SMILES 格式训练，将 Llama 的自然语言能力对齐到分子生成任务，结合性质约束解码实现条件生成，无需从头训练专用模型。
- **为什么值得读**: 为药物发现提供了一条低成本路径——研究者可直接利用开源 LLM 进行定向化学空间探索，降低了 AI 辅助分子设计的门槛，方法框架可迁移至其他科学领域。

---

## 3. De Novo Design of Miniproteins Targeting GPCRs
- **来源**: Nature（2026-05-21）
- **作者**: Authors not available
- **链接**: https://www.nature.com/articles/s41586-026-10656-8
- **方向**: 🔬 AI4Science / 🧠 AI/ML
- **TL;DR**: 计算从头设计可靶向 GPCR 的迷你蛋白，开辟新型治疗平台
- **核心贡献**:
  - 利用 AI 驱动的蛋白质设计工具从头构建能选择性结合 GPCR 的迷你蛋白
  - 验证设计的迷你蛋白具备功能活性，可作为激动剂或拮抗剂
  - 将计算蛋白设计扩展至人类最重要的药物靶点家族（~34% FDA 批准药物靶向 GPCR）
- **方法亮点**: 结合 RFdiffusion/ProteinMPNN 等 AI 蛋白设计工具与 GPCR 结构信息，迭代设计并实验验证迷你蛋白的结合亲和力与选择性。
- **为什么值得读**: GPCR 靶向药物市场规模巨大，传统小分子和抗体各有局限；迷你蛋白填补了两者之间的空缺，此工作直接展示了 AI 蛋白设计在制药领域的转化价值。

---

## 4. De Novo Design of Quasisymmetric Two-Component Protein Cages
- **来源**: Nature（2026-05-20）
- **作者**: Authors not available
- **链接**: https://www.nature.com/articles/s41586-026-10464-0
- **方向**: 🔬 AI4Science / 🧠 AI/ML
- **TL;DR**: 计算设计准对称双组分蛋白笼，实现可调纳米载体
- **核心贡献**:
  - 提出几何受挫（geometric frustration）策略，设计出准对称双组分蛋白笼
  - 笼结构形貌可调，适用于载药、细胞摄取和蛋白质胞内定位研究
  - 扩展了类病毒颗粒（VLP）的设计空间，为精准药物递送提供新平台
- **方法亮点**: 通过打破完美对称引入几何受挫，使两种蛋白亚基以非传统方式共组装成稳定的笼状纳米结构，组装行为通过计算模型预测并经实验验证。
- **为什么值得读**: 蛋白质纳米笼是 mRNA 疫苗递送、基因治疗和成像的重要平台；准对称设计打开了新的结构多样性，有望用于下一代药物递送系统。

---

## 5. Genetic Analysis of Circulating Metabolic Traits in 619,372 Individuals
- **来源**: Nature（2026-05-20）
- **作者**: Authors not available
- **链接**: https://www.nature.com/articles/s41586-026-10532-5
- **方向**: 🔬 AI4Science
- **TL;DR**: 迄今最大规模代谢 GWAS 揭示代谢性状与疾病的因果遗传关联
- **核心贡献**:
  - 整合爱沙尼亚生物库与 UK Biobank 共 61.9 万人数据，开展代谢性状全基因组关联研究
  - 鉴定大量常见及低频变异与代谢性状的关联位点，涵盖脂质、氨基酸、有机酸等
  - 通过孟德尔随机化推断代谢性状与疾病结局之间的推定因果关系
- **方法亮点**: 多队列 meta 分析结合高分辨率代谢组学，利用低频变异的更大效应量提升功效，同时通过大样本量保证统计可信度，并整合功能注释辅助解读因果位点。
- **为什么值得读**: 为精准医学提供了覆盖数百种代谢性状的遗传蓝图，对心血管病、糖尿病等代谢综合征的早期风险预测和药物靶点识别具有直接应用价值。

---

> **去重说明**：今日 top30 中"A multi-agent system for automating scientific discovery"（s41586-026-10652-y）已在过去 7 日内推送，已跳过。
>
> **⚠️ arXiv 说明**：今日 Actions 拉取 arXiv 返回 0 篇（`arxiv_count: 0`），top30 全为期刊论文，无法满足"至少 2 篇 arXiv"的硬性要求。
