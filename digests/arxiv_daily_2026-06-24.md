# 每日精选 · 2026-06-24

> 数据源：GitHub Actions 预拉（arXiv 272 篇 + journals 100 篇）。Top30 去重后精选 5 篇（arXiv 5 + journals 0）。

## 1. Qwen-AgentWorld: Language World Models for General Agents
- **来源**: arXiv
- **作者**: Yuxin Zuo et al.
- **链接**: http://arxiv.org/abs/2606.24597v1
- **方向**: 🤖 LLM / AI Agents
- **TL;DR**: 首批语言世界模型（35B/397B），可跨 7 域仿真智能体环境并助力下游 agent RL 训练。
- **核心贡献**:
  - 发布 Qwen-AgentWorld-35B-A3B 和 397B-A17B，首个支持 7 类真实环境仿真的语言世界模型
  - 提出三阶段训练流程（CPT → SFT → RL）利用 10M+ 交互轨迹，引入混合 rubric+rule 奖励
  - 发布 AgentWorldBench 综合基准，并验证世界模型可显著提升下游 agentic 任务表现
- **方法亮点**: 通过长链思维推理预测环境状态转移；作为解耦模拟器为 agent RL 提供可扩展仿真，同时作为统一基础模型在 7 个 agentic 基准上提升性能。
- **为什么值得读**: 首次将语言模型定位为环境世界模型，开辟"语言驱动仿真环境"新范式；两种互补应用范式（解耦模拟器 vs 统一基础模型）对 agent 训练路线图有深远指导意义。

---

## 2. ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling
- **来源**: arXiv
- **作者**: Heng Ping et al.
- **链接**: http://arxiv.org/abs/2606.24437v1
- **方向**: 🤖 Multi-Agent / LLM Inference
- **TL;DR**: 跨层推理记忆机制让 Mixture-of-Agents 随深度增加持续涨分而不退化。
- **核心贡献**:
  - 提出 Ranked Reasoning Memory，跨层持久化存储并排名推理轨迹
  - 设计 Curated Diversified Memory Routing，使不同 agent 接触成功与失败轨迹的不同组合，保持多样性
  - 可选的多域 Reviewer 蒸馏流水线，通过前沿模型监督提升排名质量
- **方法亮点**: 将跨层记忆作为核心机制，区别于现有 MoA 方法中孤立的逐层传递；在数学、逻辑、代码、知识、常识 5 类推理基准上验证深度和宽度缩放均有效。
- **为什么值得读**: 识别并解决了 MoA 深度扩展的退化问题，为多 agent 推理时扩展（test-time compute）提供了原理性改进，有潜力成为大规模 inference 的标准组件。

---

## 3. OpenThoughts-Agent: Data Recipes for Agentic Models
- **来源**: arXiv
- **作者**: Negin Raoof et al.
- **链接**: http://arxiv.org/abs/2606.24855v1
- **方向**: 🤖 AI Agents / 开源社区
- **TL;DR**: 首个系统性开源 agentic 训练数据流水线，100K 样本微调 Qwen3-32B 跨 7 基准达到 SOTA。
- **核心贡献**:
  - 100+ 受控消融实验系统验证 agentic 训练数据管道各阶段关键因素
  - 构建 100K 样本训练集，Qwen3-32B 微调后在 7 个 agentic 基准上平均准确率 44.8%（超越最强开源模型 3.9 pp）
  - 完全开源：训练集、数据管道、实验数据、模型全部公开
- **方法亮点**: 聚焦任务来源与多样性作为主要变量，揭示跨基准泛化依赖数据多样性而非单一任务堆量；训练数据展现强扩展性，在各训练集大小上均优于替代数据集。
- **为什么值得读**: 填补了"如何为通用 agent 构建训练数据"的开放问题，全套开源资源对社区意义重大，扩展律结果对后续研究有直接指导价值。

---

## 4. SHERLOC: Structured Diagnostic Localization for Code Repair Agents
- **来源**: arXiv
- **作者**: Hovhannes Tamoyan et al.
- **链接**: http://arxiv.org/abs/2606.24820v1
- **方向**: 💻 Code AI / Agentic Software Engineering
- **TL;DR**: 无需微调的结构化故障定位框架，将代码修复 agent 解决率平均提升 5.95 pp 同时减少 23% token 消耗。
- **核心贡献**:
  - 提出 SHERLOC，训练免微调框架将推理 LLM 与紧凑仓库工具结合并具备自恢复能力
  - 在 SWE-Bench Lite 达到 84.33% accuracy@1，SWE-Bench Verified 达 81.27% recall@1，~30B 参数媲美更大模型
  - 注入 SHERLOC 诊断结果后修复 agent 在 SWE-Bench Verified 平均提升 5.95 pp，定位 token 减少 36.7%
- **方法亮点**: 将定位重新定义为"带诊断上下文的可操作输出"而非文件检索；配合自恢复机制和结构化假设驱动探索，无多 agent 协调开销。
- **为什么值得读**: 直接解决代码 agent 中定位占用 50% 预算的痛点，即插即用提升主流修复 agent 性能，且 token 效率显著改善，对生产级代码 AI 有立即可用价值。

---

## 5. RaDaR: A Specialized Reasoning LLM for Accelerating Rare Disease Diagnosis
- **来源**: arXiv
- **作者**: Haichao Chen et al.
- **链接**: http://arxiv.org/abs/2606.24510v1
- **方向**: 🔬 AI4Science / 医疗 AI
- **TL;DR**: 32B 开源稀有病诊断推理模型，随机对照试验证明辅助医生诊断准确率提升 21.44 pp。
- **核心贡献**:
  - RaDaR（32B）在公开基准上超越 671B DeepSeek-R1 等开源模型，通过 4 个外部验证中心验证
  - 在回顾性队列中 61.06% 病例诊断时间比临床记录早 1.87 个月
  - 随机医生辅助试验中相比单独网络搜索提升 21.44 pp 诊断准确率
- **方法亮点**: 利用 49,170 公开真实病例 + 104,666 合成病例进行推理增强训练；表型锚定叙事在长尾稀有病上提供有效训练信号，且具有单调扩展趋势。
- **为什么值得读**: 将随机对照试验引入医疗 AI 评估，提供严谨临床证据；开源 32B 模型且框架可复现，对医疗资源稀缺场景（稀有病专科医生匮乏）有真实落地价值。
