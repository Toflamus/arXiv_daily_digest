# 每日精选 · 2026-06-18

> ⚠️ **数据说明**：`raw/papers_2026-06-18.json` 不存在（GitHub Actions 今日（UTC）未成功运行）。`raw/papers_2026-06-17.json` 存在（获取时间 2026-06-17T23:18 UTC），但对应的 `arxiv_daily_2026-06-17.md` 为空白失败记录（digest 在 raw 文件生成前运行）。本次 digest 使用 2026-06-17 数据补齐。
>
> 数据源：GitHub Actions 预拉（arXiv 323 篇 + journals 211 篇，去重后 530 篇）。Top30 去重（0 篇重复）后精选 **5** 篇（arXiv **5** + journals **0**）。
>
> 注：top30 全部为 arXiv 论文，顶刊论文未进入本次 top30 排名。

---

## 1. Environment-Grounded Automated Prompt Optimization for LLM Game Agents
- **来源**: arXiv (2606.17838)
- **作者**: Rean Clive Fernandes et al.
- **链接**: http://arxiv.org/abs/2606.17838v1
- **方向**: 🤖 LLM / Agent
- **TL;DR**: 自动化提示优化框架让 LLM 游戏 Agent 在 PutNext 任务上从 0% 跃升至 72.5% 成功率。
- **核心贡献**:
  - 将 observation→action 流水线拆解为目标条件描述 Agent 和动作选择 Agent，各自独立优化提示
  - 引入行为分析器追溯 episode 结果到具体提示组件，再由 mutator 提出定向修改并通过环境回滚验证
  - 无需更新模型权重，在 BALROG 基准的全部五个 BabyAI 任务上均稳定提升性能
- **方法亮点**: 采用 LLM 驱动的进化循环（evolutionary loop）以环境回报为导向迭代精化提示；通过环境实际执行而非人工判断来筛选提示变体，确保优化信号真实可靠。
- **为什么值得读**: 将 PutNext 成功率从 0% 提至 72.5% 证明提示优化本身即可弥补大量能力差距，无需微调；框架通用性强，可直接迁移至其他 LLM Agent 场景，对工业界"免训练"Agent 开发路径有直接参考价值。

---

## 2. WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning
- **来源**: arXiv (2606.18147)
- **作者**: Yuwei Zhang et al.
- **链接**: http://arxiv.org/abs/2606.18147v1
- **方向**: 🧪 AI+Health / 可穿戴设备
- **TL;DR**: 查询自适应 Agent 框架将 LLM 推理与专用可穿戴分析工具融合，准确率比 baseline 高 24%。
- **核心贡献**:
  - 提出 WEQA：LLM 控制器动态规划执行路径并路由至适配的传感器分析和预训练模型组合
  - 构建涵盖四个开源可穿戴数据集的 benchmark，横跨分析与预测任务及三个健康领域
  - 通过外部知识进行 grounded 响应审核，12 名医学专家盲测显示临床有效性显著提升
- **方法亮点**: 针对可穿戴数据高维连续、多模态传感器的特点，以查询意图驱动动态工具组合；相比固定工作流，自适应路由机制能兼容传感器类型差异与用户意图多样性。
- **为什么值得读**: 可穿戴设备已进入数十亿用户日常生活，但 LLM 尚无法直接理解其输出；WEQA 填补了 LLM 文本能力与连续时序健康数据之间的鸿沟，且经过医学专家验证，具备直接落地潜力。

---

## 3. Learning to Refine Hidden States for Reliable LLM Reasoning
- **来源**: arXiv (2606.17524)
- **作者**: Chia-Hsuan Hsu, Jui-Ming Yao
- **链接**: http://arxiv.org/abs/2606.17524v1
- **方向**: 🧠 AI/ML / LLM 推理
- **TL;DR**: ReLAR 在解码前迭代精化隐层表示，无需显式 CoT 即可提升多步推理稳定性。
- **核心贡献**:
  - 提出 ReLAR：保持紧凑隐层推理状态，通过学得的深度和动作控制器自适应决定精化步骤数和方向
  - 控制器以步级 likelihood 改进为策略梯度目标训练，实现依输入自适应的高效推理
  - 在医学、数学、多跳推理和开放生成 benchmark 上同时提升准确率、生成质量与推理稳定性
- **方法亮点**: 放弃显式 chain-of-thought，转而在模型内部对隐层状态进行强化学习引导的迭代精化；通过控制器网络实现计算自适应，比显式推理 baseline 推理开销显著更低。
- **为什么值得读**: 显式 CoT 会带来推理长度膨胀和延迟开销；ReLAR 提供了一条"内省式"替代路径，在推理质量与效率之间找到新平衡点，对 inference-time scaling 研究方向具有重要参考价值。

---

## 4. ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation
- **来源**: arXiv (2606.17937)
- **作者**: Tianyi Lu et al.
- **链接**: http://arxiv.org/abs/2606.17937v1
- **方向**: 🤖 Robotics / VLA
- **TL;DR**: 统一 Mixture-of-Transformers 架构交错文本与视觉推理，通过前向+逆向 CoT 大幅提升长视野机械臂操控性能。
- **核心贡献**:
  - 提出前向 CoT（识别子目标→预测下一视觉状态）与逆向 CoT（基于预测图像推断动作意图）的统一双链框架
  - 在单一自回归架构中交错生成文字和图像推理，实现端到端的操控规划
  - 在仿真和真实 benchmark 上全面超越 SOTA baseline，在长视野任务上提升幅度尤为突出
- **方法亮点**: 前向 CoT 生成预测目标状态图像，逆向 CoT 以该图像为 grounding 推理空间关系与动作意图；Mixture-of-Transformers 架构统一文本和视觉 token 的自回归生成，无需独立的视觉解码器。
- **为什么值得读**: 现有 VLA 模型直接映射观察到动作，缺乏规划深度；ThinkingVLA 将"想象下一个状态再反推动作"的认知范式引入机器人操控，为长视野任务提供了架构层面的解决方案，对机器人学习与具身智能社区具有重要示范意义。

---

## 5. Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure
- **来源**: arXiv (2606.18154)
- **作者**: Ziqi Zhou et al.
- **链接**: http://arxiv.org/abs/2606.18154v1
- **方向**: 🔬 AI4Science / 数字孪生
- **TL;DR**: LEADS 让 LLM Agent 在结构化动作空间中自主发现患者个性化的物理-神经混合心脏电生理模型。
- **核心贡献**:
  - 将心脏 EP 领域知识形式化为结构化动作空间，LLM Agent 通过推理-行动循环选择、组合、精化混合模型
  - Agent 负责架构发现，梯度下降负责参数拟合，两者分工明确
  - 在合成数据（三种真实反应模型）和真实心脏 EP 数据上均超越人工设计混合模型及其他 LLM 方法
- **方法亮点**: 区别于直接用 LLM 生成代码或充当模型本身，LEADS 将 LLM 定位为"架构搜索 Agent"，在物理约束的可解释空间内探索，保证数值稳定性；迭代推理环确保架构候选与领域先验一致。
- **为什么值得读**: 个性化心脏数字孪生是精准心脏病学的核心需求，但传统方法依赖专家手工设计架构，难以跨患者迁移；LEADS 将架构搜索自动化并保留物理可解释性，为 AI4Science 中"LLM 作为科学发现 Agent"提供了严格验证的新范式。

---

*完整归档：https://github.com/Toflamus/arXiv_daily_digest/tree/main/digests*
