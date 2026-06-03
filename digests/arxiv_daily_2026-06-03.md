# 每日精选 · 2026-06-03

> ⚠️ **数据说明**：`raw/papers_2026-06-03.json` 不存在（今日 Actions 尚未运行或失败）。改用 `raw/papers_2026-06-02.json`（2026-06-02T23:29:17 UTC 拉取，因该时刻之前的 2026-06-02 digest 已使用 papers_2026-06-01.json，本批数据为**首次**被精选）。
>
> 数据源：GitHub Actions 预拉（arXiv **422** 篇 + journals **228** 篇，top30 全部来自 arXiv）。Top30 去重（过去 7 日 arXiv 论文均为 0 篇，移除 **0** 篇重复）后精选 **5** 篇（arXiv: 5 + journals: 0）。

---

## 1. Multi-Agent Computer Use
- **来源**: arXiv (2606.01533v1)
- **作者**: Jing Yu Koh et al.
- **链接**: http://arxiv.org/abs/2606.01533v1
- **方向**: 🤖 Multi-Agent / 自动化任务
- **TL;DR**: 用 DAG 编排并行子智能体完成电脑操作任务，效果远超单智能体基线
- **核心贡献**:
  - 提出 MACU（Multi-Agent Computer Use）范式：主管模型将任务分解为 DAG，并行调度多个 CUA 子智能体
  - 在 OSWorld、Online-Mind2Web、WebTailBench、Odysseys 四个 benchmark 上超越单智能体基线 3.4–25.5%
  - 设计 DAG 动态修订机制，支持基于子智能体反馈实时增、删、改任务节点；同时保留"无法重复观察"的信息向后传递
- **方法亮点**: 主管模型将任务表达为有向无环图（DAG），并发派遣多个子 CUA 执行 ready 节点；完成后持续修订 DAG 并聚合结果。Odysseys 上平均任务完成时间提速约 1.5×，同时在 test-time scaling 曲线上优于单智能体。
- **为什么值得读**: 单智能体 CUA 在长程任务上频繁卡死，MACU 通过任务分解与并行执行同时解决了时延和成功率两个瓶颈。代码与可视化全部开源，是未来计算机自动化基础架构的重要参考。

---

## 2. POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems
- **来源**: arXiv (2606.02282v1)
- **作者**: Iñaki Dellibarda Varela et al.
- **链接**: http://arxiv.org/abs/2606.02282v1
- **方向**: 🛡️ AI Safety / 多智能体可靠性
- **TL;DR**: 让系统自身的智能体互相审查，无需外部评判者即可检测故障与幻觉
- **核心贡献**:
  - 提出 POIROT 协议：将多智能体系统内已有智能体复用为诊断层，利用其认知多样性检测故障
  - 在 OR=1.60（p=0.008）的统计显著性下超越单 LLM 评判者基线，且增益随问题复杂度、智能体数量和故障维度增加而扩大
  - 开源 POIROT 库及 BLAME 安全关键系统故障归因 benchmark
- **方法亮点**: 不依赖集中式裁判（单点失效、需要领域专家），而是让执行该角色的智能体集合互问互答完成自审；复合故障场景下性能依然稳定。
- **为什么值得读**: AI 监管法规要求多智能体系统具备可解释安全机制，POIROT 给出了一个无需额外专家模型、可直接内嵌于现有 MAS 架构的解决方案，对生产部署极具参考价值。

---

## 3. Geometric Latent Reasoning Induces Shorter Generations in LLMs
- **来源**: arXiv (2606.02248v1)
- **作者**: Shashi Kumar et al.
- **链接**: http://arxiv.org/abs/2606.02248v1
- **方向**: 🧠 LLM 推理 / 方法创新
- **TL;DR**: 将 CoT 推理重新表述为嵌入空间中的几何路径逼近，意外涌现出更短的生成序列
- **核心贡献**:
  - 提出 GLR（Geometric Latent Reasoning）：用轻量级 transition head 在 token 嵌入空间内迭代预测方向更新，以连续轨迹近似离散推理路径
  - 以 CoT 文本链作为锚点训练，但允许连续偏离精确 token 嵌入，实现"软离散推理"
  - 在 Qwen3 系列数学推理 benchmark 上发现涌现现象：无需显式长度目标，连续潜在步骤自然替换早期显式推理，令总生成步数大幅缩减
- **方法亮点**: 将 chain-of-thought 的离散化瓶颈转化为嵌入空间中的几何优化问题，无需额外数据或强化学习；transition head 参数量极小，可即插即用于预训练模型。
- **为什么值得读**: 在推理成本日益成为瓶颈的背景下，GLR 揭示了连续潜在计算与输出长度之间的新权衡关系，为高效 inference 提供了全新角度；涌现更短生成这一现象本身也值得后续深入研究。

---

## 4. OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents
- **来源**: arXiv (2606.02031v1)
- **作者**: Rui Yang et al.
- **链接**: http://arxiv.org/abs/2606.02031v1
- **方向**: 🤖 Web Agent / 强化学习
- **TL;DR**: 开源在线 RL 框架训练视觉 Web 智能体，仅需少量数据即达到专有系统水平
- **核心贡献**:
  - 提出 OpenWebRL：完整的在线多轮 RL 训练流程，涵盖可扩展实时浏览器基础设施、监督初始化、多模态上下文管理、轨迹级成功判断和高效策略优化
  - OpenWebRL-4B 在 Online-Mind2Web 达 67.0%、DeepShop 达 64.0% 成功率，与 OpenAI CUA 和 Gemini CUA 持平
  - 仅用 0.4K 初始化轨迹和 2.2K 开放式 RL 任务，数据效率极高；训练数据、模型和代码全部开源
- **方法亮点**: 直接在真实网站上进行在线 RL，无需大规模人工标注演示；系统研究了影响视觉 Web 智能体的关键设计选择（上下文管理、reward shaping、多轮优化），并分析了 RL 如何改善智能体推理能力。
- **为什么值得读**: 最强的 Web 智能体至今仍以专有系统为主，OpenWebRL 提供了可复现、低成本的替代路线，且结果媲美商业系统，对开源社区价值极大。

---

## 5. AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design
- **来源**: arXiv (2606.02386v1)
- **作者**: Sahil Rahman, Maxx Richard Rahman
- **链接**: http://arxiv.org/abs/2606.02386v1
- **方向**: 🔬 AI4Science / 蛋白质设计
- **TL;DR**: 为蛋白质语言模型接入工具调用与在线纠错，从被动 oracle 变成主动设计智能体
- **核心贡献**:
  - 提出 RAD（Reasoning-Augmented Decoding）：在自回归生成过程中穿插 ESMFold、FoldX、AutoDock Vina 等生物物理工具调用，实时评估候选序列
  - 提出 CAPO（Contrastive Agent Policy Optimisation）：基于 DPO 的轨迹级策略优化，训练模型学习"何时工具反馈有价值"，而非单纯模仿高适应度序列
  - 在抗体优化 top-10% 命中率等多项 benchmark 上达到 SOTA，展示无显式回溯的在线错误纠正能力
- **方法亮点**: 将智能体框架（工具调用 + 策略学习）迁移至蛋白质序列设计领域，突破传统 PLM 单次前向推理的局限；工具 API 标准化、序列同一性分割等设计保证了 benchmark 可信度。
- **为什么值得读**: 蛋白质设计正从结构预测转向主动序列优化，AgentPLM 为"智能体 + 湿实验工具"的闭环设计范式树立了清晰的方法论模板，对药物开发和酶工程领域均有直接意义。

---

*完整归档：https://github.com/Toflamus/arXiv_daily_digest/tree/main/digests*
