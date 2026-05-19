# 每日精选 · 2026-05-19

> 数据源：GitHub Actions 预拉（arXiv 409 篇 + journals 245 篇，去重后 654 篇）。Top30 去重后精选 5 篇（arXiv 4 + journals 1），过去 7 天无重复。

## 1. Alignment Dynamics in LLM Fine-Tuning
- **来源**: arXiv
- **作者**: Yuhan Huang et al.
- **链接**: http://arxiv.org/abs/2605.18309v1
- **方向**: 🤖 LLM
- **TL;DR**: 推导 alignment score 的闭式更新方程，揭示 fine-tuning 破坏对齐的动力学机制
- **核心贡献**:
  - 提出可追踪的 alignment score 并给出 fine-tuning 过程中的闭式解析更新
  - 将 alignment 变化分解为"Rebound Force"（恢复力）与"Driving Force"（驱动力）两个对抗项
  - 预测并验证"Rehearsal Priming Effect"：先前对齐留下的潜在后验印记可加速再对齐
- **方法亮点**: 从参数空间学习动力学出发，推导函数空间 alignment 行为，给出统一理论框架；在安全对齐、情感 fine-tuning 等多场景验证，并证明后验分布窄化会放大 Rebound 强度。
- **为什么值得读**: 首次将 LLM 对齐脆弱性与再对齐加速纳入同一数学框架，为对齐保持策略提供理论依据；对 RLHF 后再 fine-tuning 的安全风险评估极具参考价值。

---

## 2. BLAgent: Agentic RAG for File-Level Bug Localization
- **来源**: arXiv
- **作者**: Md Afif Al Mamun et al.
- **链接**: http://arxiv.org/abs/2605.17965v1
- **方向**: 🤖 LLM
- **TL;DR**: 结合 AST 感知编码与两阶段 agentic reranking，在 SWE-bench Lite 达 86% Top-1 且成本降低 18 倍
- **核心贡献**:
  - 路径增强 AST 分块 + 双视角查询变换，捕获代码结构与行为双重信号
  - 两阶段 agentic reranking：符号检查 + 证据推理，在紧凑候选集上做有界推理
  - 接入自动化程序修复框架后端到端修复成功率提升 20%+
- **方法亮点**: 有别于图结构或多跳方案，BLAgent 在小候选集上做深度推理，平衡精度与成本；开源模型 Top-1 达 78%，闭源模型达 86%，超越最强基线的同时 token 成本降低 18 倍。
- **为什么值得读**: 文件级 bug 定位是 APR 管线的关键瓶颈，BLAgent 大幅降低了工业落地门槛，为 agentic RAG 在软件工程中的应用树立了新基准。

---

## 3. Multi-agent AI systems outperform human teams in creativity
- **来源**: arXiv
- **作者**: Tiancheng Hu et al.
- **链接**: http://arxiv.org/abs/2605.17885v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 多智能体 LLM 团队在 6 类创意任务中以 Cohen's d=1.50 的效果量显著超越人类团队
- **核心贡献**:
  - 对比 4541 条多智能体 LLM 创意与 341 条人类团队创意，全面评估创意质量
  - 发现创意优势来自新颖性而非实用性的提升
  - 用语义空间路径分析揭示 LLM 与人类团队创意生成机制的本质差异
- **方法亮点**: 将对话轨迹映射为语义空间中的路径，量化全局/局部一致性与语义扩散度；LLM 团队受益于高效的宽泛探索（短路径+高扩散），人类团队受益于平滑的话语衔接（高局部一致）。
- **为什么值得读**: 首次以大规模受控实验证明多智能体 AI 在创意层面超越人类；为 AI 辅助创新的系统设计（模型选择×讨论结构）提供可操作的量化杠杆。

---

## 4. A multi-agent system for automating scientific discovery
- **来源**: Nature
- **作者**: Authors not listed
- **链接**: https://www.nature.com/articles/s41586-026-10652-y
- **方向**: 🔬 AI4Science
- **TL;DR**: Nature 发文：多智能体系统实现端到端科学发现自动化
- **核心贡献**:
  - 构建多智能体框架，覆盖假设生成、实验设计、结果分析的完整科研闭环
  - 在自动化科学发现任务上展示系统级可行性
  - 为 AI 驱动科研流程提供 Nature 认可的实证基础
- **方法亮点**: 系统将不同专责智能体（假设生成、实验规划、分析验证）协同编排，实现跨步骤的科学推理与迭代改进。
- **为什么值得读**: Nature 主刊发表意味着方法论和结果通过了严格同行评审；对自动化实验室、AI4Science 研究者是重要基准参考，将深刻影响 AI 参与科研的范式讨论。

---

## 5. HydroAgent: Closing the Gap Between Frontier LLMs and Human Experts in Hydrologic Model Calibration via Simulator-Grounded RL
- **来源**: arXiv
- **作者**: Zhi Li et al.
- **链接**: http://arxiv.org/abs/2605.17792v1
- **方向**: 🔬 AI4Science
- **TL;DR**: 领域微调的 4B 模型通过 RLSF 超越所有前沿 LLM，完成水文模型自动标定
- **核心贡献**:
  - 在美国国家气象局业务水文模型 CREST 上系统基准测试 9 个前沿 LLM（含 Claude Opus/Sonnet、GPT-5、Gemini）
  - 揭示前沿模型能力天花板在 NSE≈0.75，仅 Opus-4.7 单次超越人类专家，其余均未达标
  - 提出 HYDROAGENT：SFT（2576 条专家轨迹）+ GRPO 在线 RLSF，Qwen3-4B 超越所有前沿模型
- **方法亮点**: 将 NSE（Nash-Sutcliffe Efficiency）作为可验证奖励信号，通过实时 CREST 仿真实现强化学习闭环；证明"领域落地问题"而非"参数规模问题"是制约 LLM 专业任务表现的根本瓶颈。
- **为什么值得读**: 结论极具普适性：在物理科学领域，小模型+仿真器在环的强化学习比扩大通用模型更高效；为 AI4Science 的落地路径（领域 RL vs 通用 scaling）提供清晰的实验证据。
