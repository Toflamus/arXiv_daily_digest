# 每日精选 · 2026-05-20

> 数据源：GitHub Actions 预拉（arXiv 369 篇 + journals 209 篇）。Top30 去重后剩 29 篇（1 篇 Nature 重复已跳过），精选 5 篇（arXiv: 5 + journals: 0）。

## 1. ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning
- **来源**: arXiv
- **作者**: Juncheng Wu et al.
- **链接**: http://arxiv.org/abs/2605.20176v1
- **方向**: 🏥 AI for Healthcare
- **TL;DR**: 从被动接受证据转向主动多模态证据检索的临床推理 Agent 框架
- **核心贡献**:
  - 提出 ClinSeekAgent，能自主查询医学知识库、导航原始 EHR 并调用医学影像工具
  - 构建 ClinSeek-Bench，对比固定证据输入 vs 自动化证据检索两种评估模式
  - 将 agentic 轨迹蒸馏成 ClinSeek-35B-A3B，在 AgentEHR-Bench 超越基线 +11.9 F1
- **方法亮点**: Agent 迭代假设精炼——先检索，再根据新信息修正假设，最终融合多模态证据作出临床决策；同时作为训练 pipeline 蒸馏高质量轨迹至开源小模型。
- **为什么值得读**: 将临床 AI 从"给定证据推理"推进到"自主获取证据再推理"，更贴近真实临床工作流；多模态任务上 Claude Opus 4.6 提升 +15.1 F1，证明框架对强模型也有显著增益。

---

## 2. Conflict-Resilient Multi-Agent Reasoning via Signed Graph Modeling
- **来源**: arXiv
- **作者**: Longgang He et al.
- **链接**: http://arxiv.org/abs/2605.19418v1
- **方向**: 🤖 LLM / Multi-Agent Systems
- **TL;DR**: 用有符号图显式建模 Agent 间信任/冲突关系，提升多 Agent 推理鲁棒性
- **核心贡献**:
  - 提出 SIGMA，在多 Agent 系统中引入带符号（正/负/中性）边的关系图
  - 冲突感知消息传递：强化可信 Agent 信息，抑制冲突信号
  - 在六个 benchmark 上一致超越 SOTA，覆盖多种 LLM 骨干和 Agent 配置
- **方法亮点**: 对每条查询先筛选相关多样的 Agent，再构造置信度加权有符号交互图；推理通过冲突感知消息传播完成，聚合时同时考虑结构特征和冲突信息，实现全局一致预测。
- **为什么值得读**: 现有图式 MAS 框架普遍忽略 Agent 间的对立关系，SIGMA 是首个将"信任/冲突/中立"纳入消息传递的框架，对构建生产级多 Agent 系统有直接指导意义。

---

## 3. STAR-PólyaMath: Multi-Agent Reasoning under Persistent Meta-Strategic Supervision
- **来源**: arXiv
- **作者**: Jiaao Wu et al.
- **链接**: http://arxiv.org/abs/2605.19338v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 持久元策略监督的多 Agent 框架，在 8 项顶级数学竞赛 benchmark 上达到 SOTA
- **核心贡献**:
  - 设计编排状态机 + 嵌套 challenge-step-replan 循环，将控制流与推理解耦
  - 引入持久 Meta-Strategist，跨尝试保留记忆并发出元级别战略指令，防止陷入无效循环
  - 在 AIME 2025–2026、IMO 2025、USAMO 2026、Putnam 2025 等获得满分或 SOTA
- **方法亮点**: Python 编排器（无 LLM）管理控制流，通过回溯与重规划界定错误传播范围；Meta-Strategist 记录历史失败模式，主动切换策略而非被动重试。
- **为什么值得读**: 在 Apex 2025 以 93.75% 对比最强基线 GPT-5.5 的 80.21%，消融实验证明增益来自框架编排而非模型多样性，为长链数学推理的可靠性提供了系统性解决思路。

---

## 4. From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models
- **来源**: arXiv
- **作者**: Juncheng Wu et al.
- **链接**: http://arxiv.org/abs/2605.20177v1
- **方向**: 🔬 AI4Science / Vision-Language
- **TL;DR**: 分阶段独立训练视觉感知与推理，VLM 性能更高且推理更简洁
- **核心贡献**:
  - 将 VLM 后训练分解为视觉感知、视觉推理、文本推理三个独立阶段
  - 证明感知能力需优先巩固，且 RL 训练比 caption SFT 更有效
  - 分阶段训练比混合训练提升 +5.2%（WeMath）和 +3.7%（RealWorldQA），推理链缩短 20.8%
- **方法亮点**: 分阶段课程提供了一个正交于"难度递增"的新维度；感知阶段用 RL 强化视觉定位精度，推理阶段才引入复杂 CoT，避免两者相互干扰。
- **为什么值得读**: 揭示了当前 VLM 性能瓶颈主要在感知而非推理，为多模态模型的训练配方提供了重要的实验依据，结论对后续模型设计有直接参考价值。

---

## 5. CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning
- **来源**: arXiv
- **作者**: Dachuan Shi et al.
- **链接**: http://arxiv.org/abs/2605.20075v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 先答后思 + 连续嵌入对比验证，无需训练提升 23% 准确率并节省 57% token
- **核心贡献**:
  - 逆转标准 CoT 顺序：先生成草稿答案，再条件化草稿做反思修正
  - 以连续嵌入 vs 离散 token 的反向 KL 估计器作为答案可靠性验证器
  - 第二个 KL 估计器动态控制草稿可见性，避免错误草稿误导后续思考
- **方法亮点**: 理论上证明该估计量等于潜在状态与答案 token 的互信息，因此捕获的是与答案相关的不确定性，而非任意潜在状态的不确定性；整个流程零训练成本。
- **为什么值得读**: 在数学、代码和 agentic 任务上免训练实现显著提升，token 效率提升尤其突出；对推理模型部署成本有直接降低作用，方法通用性强。
