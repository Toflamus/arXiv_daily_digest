# 每日精选 · 2026-05-13

> 数据源：GitHub Actions 预拉（arXiv 500 篇 + journals 207 篇）。Top30 去重后精选 5 篇（arXiv 5 + journals 0）。注：今日 top30 全部由 arXiv 论文构成，期刊论文未进入排名前列。

## 1. Coordinated Diffusion: Generating Multi-Agent Behavior Without Multi-Agent Demonstrations
- **来源**: arXiv
- **作者**: Lasse Peters et al.
- **链接**: http://arxiv.org/abs/2605.11485v1
- **方向**: 🤖 多智能体机器人
- **TL;DR**: 无需联合示范数据，用单智能体扩散策略组合出鲁棒的多臂协作行为
- **核心贡献**:
  - 提出 CoDi 框架，将独立训练的单智能体扩散策略通过代价函数耦合，无需多智能体协作示范
  - 推导新的扩散采样方案，将 score function 分解为单智能体基础策略 + 代价驱动引导项
  - 引导项支持免梯度估计，可适配黑盒、不可微代价函数，无需额外训练
- **方法亮点**: CoDi 在扩散逆向采样过程中引入多智能体联合引导，每步采样同时优化各智能体的单体轨迹与协作约束。理论分析了单体策略支撑覆盖与代价设计之间的互补关系，并在双臂真实硬件上验证。
- **为什么值得读**: 突破了多智能体模仿学习的数据瓶颈——联合状态空间指数爆炸导致协作示范极难收集，CoDi 将这一需求彻底解耦。对多机器人、自动驾驶车队等场景有直接落地意义。

---

## 2. Deep Reasoning in General Purpose Agents via Structured Meta-Cognition
- **来源**: arXiv
- **作者**: Dean Light et al.
- **链接**: http://arxiv.org/abs/2605.11388v1
- **方向**: 🧠 AI/ML Agent
- **TL;DR**: DOLORES 通过推理时构建任务专属 scaffold，在多跳推理等四类基准上平均超越最强基线 24.8%
- **核心贡献**:
  - 提出 Deep Reasoning：推理时用形式化元推理语言动态生成任务专属 scaffold，而非预先硬编码
  - 引入 DOLORES 智能体，将复杂任务分发到多个低负载推理线程，减少幻觉和提前终止
  - 8B 版本在同系列模型中超越超过一半的 32B 基线，展示了架构对规模的弥补能力
- **方法亮点**: Deep Reasoning 使用可执行分解语言将元推理表示为联想推断、形式计算和递归子问题求解的组合，分解原则以 in-context 示例编码，在测试时引导 scaffold 构建。
- **为什么值得读**: 当前主流 Agent scaffold 在任务结构与预设不符时表现脆弱，本文给出了一个运行时自适应方案，对构建通用 Agent 系统有重要参考价值。

---

## 3. AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration
- **来源**: arXiv
- **作者**: Taicheng Guo et al.
- **链接**: http://arxiv.org/abs/2605.11518v1
- **方向**: 🤖 自动化实验室 / AI for AI Research
- **TL;DR**: 模拟研究员"低保真实验学原则、高保真实验验证"的思路，自动化高成本 LLM 实验配置
- **核心贡献**:
  - 构建 LLMConfig-Gym：涵盖四类 LLM 实验任务、超过 100 万 GPU 小时可验证实验结果的多保真环境
  - 将配置搜索建模为长时域 MDP，通过跨保真外推激励 Agent 学习泛化原则
  - 在保留实验上超越多个强基线，展示了对未见过的架构/超参空间的泛化能力
- **方法亮点**: 框架的核心是跨保真推理：Agent 在廉价的低保真实验（小模型、短训练）中积累规律，再外推到昂贵的高保真配置（大模型完整训练），避免高成本试错。
- **为什么值得读**: 首个专门针对高成本 LLM 实验配置自动化的系统性工作，直接解决 AI 研究中大量依赖专家直觉的痛点，有潜力降低大模型研究的门槛和资源浪费。

---

## 4. UniVLR: Unifying Text and Vision in Visual Latent Reasoning for Multimodal LLMs
- **来源**: arXiv
- **作者**: Houcheng Jiang et al.
- **链接**: http://arxiv.org/abs/2605.11856v1
- **方向**: 🧠 多模态 AI
- **TL;DR**: 将文本 CoT 与辅助视觉证据统一压缩为视觉潜变量，推理时只用视觉 token 直接解码答案
- **核心贡献**:
  - 提出 UniVLR：把文本推理轨迹和辅助图像渲染为统一视觉工作空间，再压缩为紧凑视觉潜变量
  - 推理阶段完全通过视觉 latent token 进行，无需外部工具调用或冗长文本推理
  - 在感知与视觉推理任务上超越现有视觉潜推理方法，同时显著减少生成的推理 token 数量
- **方法亮点**: 现有方法将文本 CoT 与视觉 latent token 交错排列，UniVLR 将推理轨迹和辅助图像统一渲染后训练模型将其压缩，推理时仅依赖视觉 latent 通道，彻底打通两种模态的推理路径。
- **为什么值得读**: 统一视觉推理空间是 MLLM 效率与能力提升的关键方向，本文提供了一个简洁有效的实现范式，对部署受限（token 预算紧张）的多模态应用尤为实用。

---

## 5. Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning
- **来源**: arXiv
- **作者**: Hannes Büchi et al.
- **链接**: http://arxiv.org/abs/2605.12388v1
- **方向**: 🤖 多智能体强化学习
- **TL;DR**: 以"事件"为触发点的 MARL 框架，让智能体在正确时机切换角色，实现零样本泛化
- **核心贡献**:
  - 将智能体身份与行为解耦，引入连续行为流形，智能体根据事件动态实例化行为
  - 提出 Neural Manifold Diversity（NMD）：适用于瞬时、智能体无关行为的形式化多样性度量
  - 基于事件的超网络生成 LoRA 模块，对共享策略进行即时重配置，理论保证多样性不干扰奖励最大化
- **方法亮点**: 超网络以事件状态为条件生成低秩适配模块，注入到共享团队策略中。NMD 通过神经网络输出空间的几何距离衡量行为多样性，避免了传统度量在动态角色切换场景下的失效问题。
- **为什么值得读**: 现有 MARL 多样性方法将固定行为绑定到固定身份，无法处理需要在特定时刻切换角色的任务，本文是迄今唯一能解决序列行为再分配任务的方法，零样本泛化结果令人印象深刻。
