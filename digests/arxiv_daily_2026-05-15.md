# 每日精选 · 2026-05-15

> 数据源：GitHub Actions 预拉（arXiv 431 篇 + journals 245 篇）。Top30 去重后精选 5 篇（arXiv 5 + journals 0）。

## 1. Orchard: An Open-Source Agentic Modeling Framework
- **来源**: arXiv 2605.15040v1
- **作者**: Baolin Peng et al.
- **链接**: http://arxiv.org/abs/2605.15040v1
- **方向**: 🤖 LLM / Agent 基础设施
- **TL;DR**: 开源智能体训练框架，Orchard-SWE 在 SWE-bench Verified 达到 67.5%（开源同规模 SOTA）
- **核心贡献**:
  - 轻量级环境服务 Orchard Env，提供跨任务域、跨流水线阶段的沙箱生命周期管理原语
  - Orchard-SWE 从 107K 蒸馏轨迹出发，结合信用分配 SFT + Balanced Adaptive Rollout RL，达到 SWE-bench Verified 67.5%
  - Orchard-GUI（仅 4B VLM）用 0.4K 蒸馏轨迹在 WebVoyager 达 74.1%；Orchard-Claw 个人助手以 0.2K 合成任务达 59.6% pass@3
- **方法亮点**: 核心是与 harness 解耦的轻量级环境层，同一套环境原语可跨编程、GUI、个人助手三类任务复用；SFT 阶段引入信用分配机制，从未解决的轨迹中提取有价值的片段而非整条丢弃，大幅提升数据效率。
- **为什么值得读**: 在多个主流基准上同时取得开源 SOTA，且训练代码和数据管道全部开放，是研究社区可直接用于复现和二次开发的重要基础设施。该框架证明"轻量环境层 + 领域无关训练配方"可复用性极高，有助于加速后续智能体研究的开放生态。

---

## 2. Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model
- **来源**: arXiv 2605.14723v1
- **作者**: Minghao Wu et al.
- **链接**: http://arxiv.org/abs/2605.14723v1
- **方向**: 🔬 AI4Science / 医疗 AI
- **TL;DR**: 将临床世界模型与 LLM 结合，为 ICU 脓毒症治疗提供更安全的用药决策
- **核心贡献**:
  - 临床世界模型（CWM）学习液体-血管加压素干预下的患者生理响应，为 LLM 提供候选方案的前向模拟
  - 提出"propose–simulate–refine"工作流：LLM 先提方案，CWM 模拟患者反应，再由 LLM 迭代精修处方
  - 三阶段课程训练（患者动力学 SFT → 行为克隆 → 世界模型强化学习），在 MIMIC-IV 脓毒症轨迹上超越全部 RL 和 LLM 基线，同时取得最优安全指标
- **方法亮点**: 将 LLM 的广泛临床知识与可学习的患者动力学模型结合，借助世界模型在提交处方前"虚拟试药"；进一步发现即使移除模拟器访问权限，智能体仍保留从交互中习得的患者演变规律，说明世界模型知识已内化到策略中。
- **为什么值得读**: 脓毒症是 ICU 死亡的主要原因之一，该框架将 LLM 从"知识检索"提升为"动态决策主体"，在安全性指标（指南遵从率、危险操作率）上有明确提升，具有真实临床落地价值，也为其他时序治疗决策场景提供了可借鉴范式。

---

## 3. MetaAgent-X: Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning
- **来源**: arXiv 2605.14212v1
- **作者**: Yaolun Zhang et al.
- **链接**: http://arxiv.org/abs/2605.14212v1
- **方向**: 🧠 AI/ML / 多智能体系统
- **TL;DR**: 端到端 RL 联合优化 MAS 的设计（designer）与执行（executor），突破"冻结执行器"瓶颈
- **核心贡献**:
  - 识别现有自动 MAS 方法的"冻结执行器天花板"：设计者与执行者分离优化导致系统上限受限
  - MetaAgent-X 支持脚本化 MAS 生成、执行轨迹采集以及设计者-执行者双路信用分配
  - 引入 Executor-Designer Hierarchical Rollout 和 Stagewise Co-evolution，在多个基准上较现有自动 MAS 基线最高提升 21.7%
- **方法亮点**: 将 MAS 编排脚本的生成与执行统一在一个 RL 循环中，通过阶段性共进化策略稳定训练；消融实验表明设计者和执行者在训练中均单独提升，验证了联合优化的必要性。
- **为什么值得读**: 端到端可训练的自动 MAS 是一个尚未充分探索的方向，该工作提供了清晰的问题定义和可行的训练框架，为构建"自设计-自执行"的智能体系统开辟了新路径，对工业级复杂任务自动化有直接意义。

---

## 4. Stateful Reasoning via Insight Replay
- **来源**: arXiv 2605.14457v1
- **作者**: Bin Lei et al.
- **链接**: http://arxiv.org/abs/2605.14457v1
- **方向**: 🧠 AI/ML / 推理与 CoT
- **TL;DR**: 周期性重放推理轨迹中的关键洞见，防止长 CoT 中注意力衰减导致的精度下降
- **核心贡献**:
  - 揭示 CoT 精度随链长先升后降的根本原因：早期关键洞见在注意力中逐渐被"淡忘"
  - InsightReplay 定期从推理轨迹中提取关键洞见并重放到当前生成前沿，以线性代价维持其可达性
  - 在 2×3×4 基准网格（8B/30B 模型 × Qwen3.5/R1-Distill/Gemma-4 × AIME/HMMT/GPQA/LiveCode）全部 24 个设置中一致提升，平均 +1.65 pp，单项最高 +9.2 pp
- **方法亮点**: 无需修改模型权重或架构，仅在推理阶段周期性插入提炼后的洞见 token；跨模型家族和规模均有效，说明注意力衰减是普遍现象而非特定模型缺陷。
- **为什么值得读**: 测试时计算扩展（test-time scaling）是当前热点，该工作指出扩展效果不只取决于"推理了多少"，更取决于"关键信息是否始终可及"，为更高效的长推理链设计提供了新视角，且实现轻量、可直接叠加到现有框架。

---

## 5. Lang2MLIP: End-to-End Language-to-Machine Learning Interatomic Potential Development with Autonomous Agentic Workflows
- **来源**: arXiv 2605.14527v1
- **作者**: Wenwen Li et al.
- **链接**: http://arxiv.org/abs/2605.14527v1
- **方向**: 🔬 AI4Science / 材料科学
- **TL;DR**: 用自然语言指令驱动多智能体框架，端到端自动化机器学习原子间势的开发流程
- **核心贡献**:
  - 将 MLIP 开发（涉及原子模拟、主动学习、工作流设计）形式化为序贯决策问题，由 LLM 多智能体求解
  - 决策智能体观察当前数据集、模型评估结果和执行日志，自动选取下一步动作，支持自我纠错回溯
  - 在固体电解质界面（SEI）多组分多界面体系（电池材料领域高难场景）上验证，无需领域专家介入
- **方法亮点**: 无预定义流水线，智能体根据当前状态灵活调整策略，遇到新失败可主动回溯到上游模块；这种自适应性对于最优主动学习课程尚不明确的异质材料体系尤为关键。
- **为什么值得读**: MLIP 开发历来需要原子模拟、机器学习和工作流设计三方面专业知识，是阻碍计算材料科学民主化的核心瓶颈。该工作展示了 LLM 智能体在真实科学计算流程中自主决策的可行性，对加速新材料（电池、催化剂等）研发具有实际价值。
