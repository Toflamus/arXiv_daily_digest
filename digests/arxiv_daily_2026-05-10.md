# arXiv 每日精选 · 2026-05-10

> 数据源：GitHub Mirror（Tavish9/awesome-daily-AI-arxiv，2026-05-09 批次）
> 说明：arXiv API / RSS / HuggingFace 均因网络限制（HTTP 403）无法直接访问，降级使用每日同步 GitHub 镜像仓库作为数据源。
> 今日候选 186 篇（2605.XXXXX，去重后），精选 5 篇

---

## 1. LATTE: Language Agent Teams for Task Evolution
- **作者/机构**: Elizabeth Mieczkowski, Alexander Ku, Tiwalayo Eisape, Dilip Arumugam, Katherine M. Collins et al.
- **arXiv**: https://arxiv.org/abs/2605.06320
- **方向**: 🤖 LLM / Multi-Agent
- **TL;DR**: 分布式系统启发的多智能体 LLM 协调框架，用共享自适应任务图替代固定流水线，大幅降低 token 消耗与协调失败。
- **核心贡献**:
  - 提出 LATTE 框架：多 LLM 智能体协同维护一个共享、持续演化的协调图，编码子任务依赖、分配与进度状态
  - 支持局部可见性与通信约束下的动态工作分配和新任务发现，无需预先固定角色或分工
  - 在多个协作任务和多种基础模型上，以相当或更高准确率显著降低 token 使用量、挂钟时间、文件冲突和重复输出
- **方法亮点**: 将分布式系统（处理器间部分可见性 + 通信约束）的设计哲学迁移到 LLM 团队协调；协调图在运行时自适应演化，与 MetaGPT、Leader-Worker 层级等静态方案有本质区别。
- **为什么值得读**: 直接解决了多 LLM 智能体部署中的实际瓶颈（token 浪费、任务冲突），提供了可落地的工程蓝图；在所有主流协调范式（MetaGPT、去中心化团队、静态分解）上均优于现有方案，影响力覆盖软件工程智能体、科研助手等多场景。

---

## 2. RVPO: Risk-Sensitive Alignment via Variance Regularization
- **作者/机构**: Ivan Montero, Tomasz Jurczyk, Bhuwan Dhingra (CMU)
- **arXiv**: https://arxiv.org/abs/2605.05750
- **方向**: 🤖 LLM / RLHF & Alignment
- **TL;DR**: 用方差正则化取代奖励算术平均，解决多目标 RLHF 中"高分目标掩盖关键约束"的系统性缺陷。
- **核心贡献**:
  - 识别并形式化"约束遗漏"（constraint neglect）问题：现有 critic-less RLHF 对多目标奖励取均值，高权重目标的高分可合法掩盖安全/格式等低分约束
  - 提出 RVPO：在优势聚合阶段惩罚跨奖励方差，目标从"最大化总和"转为"最大化一致性"
  - 通过 Taylor 展开证明 LogSumExp（SoftMin）算子恰好是平滑方差惩罚；在 17 个并发 LLM 评判奖励信号下验证：HealthBench 上 0.261 vs GDPO 0.215（p<0.001），GPQA-Diamond 无后期退化
- **方法亮点**: 数学推导严谨（Taylor 展开揭示 SoftMin 即方差惩罚），在医疗推理和工具调用两类场景均有验证；无需额外 critic 模型，即插即用。
- **为什么值得读**: 安全关键领域（医疗、科学推理）对"不遗漏任何一条约束"有刚性需求，RVPO 直接解决这一缺陷；方法优雅且理论有保证，很可能成为多目标 RLHF 的新基线。

---

## 3. Earth-o1: A Grid-free Observation-native Atmospheric World Model
- **作者/机构**: Junchao Gong, Kaiyi Xu, Wangxu Wei, Siwei Tu, Jingyi Xu, Zili Liu et al.
- **arXiv**: https://arxiv.org/abs/2605.06337
- **方向**: 🔬 AI4Science / 气候与地球系统
- **TL;DR**: 首个直接从非网格化多源传感器数据学习连续三维大气动力学的世界模型，后报技巧比肩 ECMWF IFS。
- **核心贡献**:
  - 提出"观测原生"（observation-native）范式：彻底放弃传统数值天气预报的网格化假设，直接将异构多模态传感器输入统一到连续无网格动力场
  - 模型自主推进时空大气状态，无需显式数值求解器或传统数据同化流程
  - 后报评估中地表预报技巧与欧洲中期天气预报中心（ECMWF）IFS 业务系统相当，且支持实时预报和跨传感器推断
- **方法亮点**: 将 o1 风格"先思考再预报"的推理模式嵌入地球系统建模；无网格连续场表示（隐式神经场 / token 化观测）使模型可以直接利用卫星、雷达、地面站等异构观测数据，无空间对齐代价。
- **为什么值得读**: 气候 AI 从"以网格为中心"到"以观测为中心"的范式转变，可能彻底改变数值天气预报工作流；对极端天气预警和气候下行缩放均有巨大实用价值。

---

## 4. SMolLM: Small Language Models Learn Small Molecular Grammar
- **作者/机构**: Akhil Jindal, Harang Ju
- **arXiv**: https://arxiv.org/abs/2605.06322
- **方向**: 🔬 AI4Science / 药物发现 & 分子设计
- **TL;DR**: 53K 参数权重共享 Transformer 以 95% 有效率生成药物分子，超越参数量大 10 倍的标准 GPT，并揭示其可解释分子语法机制。
- **核心贡献**:
  - 训练 SMolLM（53K 参数，权重共享 Transformer），在 ZINC-250K 药物分子基准上生成 95% 有效 SMILES，远超同等标准 GPT（参数量大 10 倍）
  - 通过误差分类、线性探测和稀疏自编码器揭示：同一个 block 按固定顺序（括号 → 环 → 化合价）分别在不同 pass 中解决不同约束
  - 精准定位：第一个括号匹配步骤完全依赖于单个 attention head，提供了对分子生成的细粒度可解释性
- **方法亮点**: 权重共享 + 多 pass 迭代计算 ≈ 用固定参数隐式扩展计算深度；结果反驳了"分子设计需要大模型"的默认假设，为在资源受限场景（实验室端侧部署）提供了全新思路。
- **为什么值得读**: 揭示分子语言模型的可解释机制是药物设计可信赖 AI 的关键一步；53K 参数的极端压缩性能暗示化学语法具有高度结构化规律，对蛋白质序列等类似领域的小模型设计有直接启发。

---

## 5. BALAR: A Bayesian Agentic Loop for Active Reasoning
- **作者/机构**: Aymen Echarghaoui, Dongxia Wu, Emily B. Fox (Stanford)
- **arXiv**: https://arxiv.org/abs/2605.05386
- **方向**: 🧠 AI/ML / 主动学习 & Agentic AI
- **TL;DR**: 无需微调的贝叶斯主动推理循环，通过最大化期望互信息引导 LLM 智能体选择下一个最优问题，显著超越交互式基线。
- **核心贡献**:
  - 提出 BALAR：任务无关的外部循环算法，让 LLM 智能体在与用户的多轮交互中维护对潜在状态的结构化贝叶斯信念
  - 以最大化期望互信息（EMI）为准则选择澄清问题；当信念空间不足时动态扩展状态表示
  - 在三类多样基准（侦探推理 AR-Bench-DC、思维谜题 AR-Bench-SP、临床诊断 iCraft-MD）上显著优于所有基线，无需任何额外微调
- **方法亮点**: 将经典贝叶斯实验设计（主动信息采集）无缝嵌入 LLM 对话循环；信念的动态扩展机制解决了预先枚举假设空间的局限性，使系统具备真正的开放域适应能力。
- **为什么值得读**: 与自动化实验室的"闭环优化"高度同构——贝叶斯实验设计 + 主动信息获取正是 self-driving lab 的核心逻辑；Emily Fox（Stanford）团队的工作在 Bayesian ML 领域具有高影响力；临床诊断的验证结果也证明了实际落地潜力。

---

*数据获取说明：本次 arXiv API（export.arxiv.org）、RSS（rss.arxiv.org）、HuggingFace Daily Papers 三大源均因运行环境网络限制（HTTP 403 / Host not in allowlist）无法直接访问。改用 GitHub API 拉取每日同步 arXiv 镜像仓库 Tavish9/awesome-daily-AI-arxiv（2026-05-09 批次），候选论文均为 arXiv ID 2605.XXXXX（2026 年 5 月提交），在 48h 时效窗口内。*
