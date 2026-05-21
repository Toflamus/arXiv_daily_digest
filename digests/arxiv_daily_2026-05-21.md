# 每日精选 · 2026-05-21

> 数据源：GitHub Actions 预拉（arXiv 366 篇 + journals 208 篇），共 574 篇去重后 Top30。过去 7 天已出现 1 篇（Nature s41586-026-10652-y），去重后精选 5 篇（arXiv 5 + journals 0）。

## 1. Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning
- **来源**: arXiv
- **作者**: Lukas Twist et al.
- **链接**: http://arxiv.org/abs/2605.21127v1
- **方向**: 🤖 LLM
- **TL;DR**: 标准 SFT 可静默摧毁推理模型的链式推理能力，而最终答案准确率几乎不变
- **核心贡献**:
  - 定义"推理迹崩塌"现象：微调后模型保持答题能力但丧失有效推理结构
  - 提出结构性评估框架，将推理迹有效性与答案正确率解耦
  - 证明简单 loss-masking 策略可大幅缓解崩塌，无需教师推理数据
- **方法亮点**: 对四个开源推理模型进行标准 SFT，在训练过程中分别统计推理迹有效率、空迹率、截断率及条件任务准确率，发现推理迹有效率快速跌至接近零而答题准确率维持稳定，两者出现严重解耦。
- **为什么值得读**: 推理模型（o1/QwQ 类）已被大量企业下游微调，本文揭示了这一过程中隐藏的能力退化风险，直接影响推理模型评估标准的制定。loss-masking 的简洁修复方案立即可用于工程实践。

---

## 2. Multi-agent Collaboration with State Management (STORM)
- **来源**: arXiv
- **作者**: Mengyang Liu et al.
- **链接**: http://arxiv.org/abs/2605.20563v1
- **方向**: 🤖 LLM
- **TL;DR**: 在写入时实时检测冲突的状态管理层，比 git-worktree 方案在 Commit0 上高出 18.7 分
- **核心贡献**:
  - 提出 STORM：通过统一共享工作区状态中介，在写入时而非合并时解决冲突
  - 在 Commit0-Lite 上相对 git-worktree 基线提升 +18.7，在 PaperBench 提升 +1.4
  - 框架无缝插入任意多智能体系统，无需修改底层 LLM
- **方法亮点**: STORM 将共享代码库的每次写操作路由到状态管理器，维护全局一致视图，冲突在提交时立即标记并协商解决；避免了隔离工作树方案中代价高昂的后期合并。结合单智能体运行，Commit0 达到 87.6 分的新高。
- **为什么值得读**: 多智能体代码协作是 SWE-Agent 等系统的核心瓶颈之一，本文给出了比 fork-and-merge 更高效的工程解，对构建大规模软件工程 Agent pipeline 有直接参考价值。

---

## 3. Tracing the Ongoing Emergence of Human-like Reasoning in Large Language Models
- **来源**: arXiv
- **作者**: Paolo Morosi et al.
- **链接**: http://arxiv.org/abs/2605.21299v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 跨四语言测试 25 个 LLM 发现：模型是精准语义算子，但系统性缺失人类的语用推理能力
- **核心贡献**:
  - 人口匹配实验设计：25 个 LLM 与每种语言等量人类受试者直接对比
  - 覆盖英、法、德、意四种类型各异的语言，条件推理任务横向比较
  - 揭示 LLM 准确率与开/闭源状态、训练方向、架构类型均无显著相关性
- **方法亮点**: 以真值表一致性（逻辑语义）与语用推断接受率两个独立维度分析模型行为，发现部分模型完美符合逻辑真值表却拒绝语用推断，另一些模型则反之；语用推理是当前模型的系统性短板而非个体差异。
- **为什么值得读**: 语用理解直接关系到指令跟随、对话理解等核心应用，本文为 LLM 认知能力边界提供了严格的跨语言证据，对评估基准设计和认知模型研究均有参考意义。

---

## 4. Federated LoRA Fine-Tuning for LLMs via Collaborative Alignment (CLAIR)
- **来源**: arXiv
- **作者**: Shuaida He et al.
- **链接**: http://arxiv.org/abs/2605.21217v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 联邦 LoRA 框架在存在恶意客户端时精确恢复共享子空间并识别污染方
- **核心贡献**:
  - 提出 CLAIR：将联邦 LoRA 合并建模为低秩加块稀疏分解，天然分离共享子空间与局部污染
  - 严格证明无噪声时共享 LoRA 子空间的精确恢复及污染客户端的一致识别
  - 适用范围广：从线性回归到神经网络/LLM 模块，只要更新可表示为矩阵更新即可
- **方法亮点**: CLAIR 不依赖特定服务器端验证数据，仅基于本地初步估计器；通过跨客户端平均降低非子空间估计误差，同时在共享子空间内保留客户端特异性变化，理论量化了相对于本地微调的提升上限。
- **为什么值得读**: 医疗、金融等高度隐私场景对联邦 LLM 微调需求迫切，CLAIR 在高度异构且含恶意参与者的现实条件下仍提供可证明保障，直接推动联邦 LLM 的安全部署。

---

## 5. COAgents: Multi-Agent Framework to Learn and Navigate Routing Problems Search Space
- **来源**: arXiv
- **作者**: Oleksandr Yakovenko et al.
- **链接**: http://arxiv.org/abs/2605.20618v1
- **方向**: 🔬 AI4Science
- **TL;DR**: 将 VRP 求解建模为图上搜索，协作多智能体在 VRPTW 上将与最优解的差距缩小 44%
- **核心贡献**:
  - 提出 Partial Search Graph（PSG）动态表示搜索过程，统一强化和多样化操作
  - 训练三类专用智能体：节点选择、局部移动选择、跳跃触发，分工明确
  - VRPTW N=50 时相对最强神经求解器 POMO 缩小 gap 44%，N=100 缩小 14%
- **方法亮点**: COAgents 将问题无关的搜索控制与紧凑的领域编码清晰分离，节点选择和跳跃智能体分别负责精化（intensification）与多样化（diversification），通过 PSG 的历史信息避免盲目搜索。
- **为什么值得读**: 车辆路径规划是物流、供应链的核心 NP 难问题，本文展示了多智能体学习在组合优化中的系统性突破，框架设计对 TSP、调度等其他 CO 问题也具有迁移价值。
