# 每日精选 · 2026-06-19

> 数据源：GitHub Actions 预拉（arXiv 341 篇 + journals 217 篇，去重后 558 篇）。Top30 去重（0 篇重复，近 7 天 digest 均为 arXiv 2606.17xxx/18xxx 段，未与今日 2606.19xxx/20xxx 段重叠）后精选 **5** 篇（arXiv **5** + journals **0**）。
>
> 注：今日 top30 全部为 arXiv 论文（均提交于 2026-06-18），顶刊论文未进入本次 top30 排名。

---

## 1. Multi-Agent Transactive Memory
- **来源**: arXiv (2606.19911)
- **作者**: To Eun Kim et al.
- **链接**: http://arxiv.org/abs/2606.19911v1
- **方向**: 🤖 Multi-Agent / 知识共享基础设施
- **TL;DR**: MATM 让 Agent 种群共享过去轨迹记忆，无需协调或联合训练即可提升任务性能并减少交互步数。
- **核心贡献**:
  - 提出种群级轨迹存储与检索框架（MATM），生产者 Agent 贡献轨迹，消费者 Agent 按需检索复用
  - 将检索增强生成（RAG）从人类文档扩展至 Agent 生成的程序性知识，填补多 Agent 生态的基础设施空白
  - 在 ALFWorld 和 WebArena 交互式环境上验证：轨迹检索提升下游任务成功率并减少平均交互步数
- **方法亮点**: 借鉴认知科学的"交互记忆"概念，将 Agent 轨迹（含动作序列和环境反馈）编码入共享检索库；消费者 Agent 以任务描述为查询检索相关轨迹作为少样本上下文，无需修改 Agent 内部参数或进行协调训练。
- **为什么值得读**: 随着 Agent 部署规模扩大，个体重复试错造成巨大计算浪费；MATM 提出了一种轻量级"集体记忆"基础设施设计模式，对工业部署多 Agent 系统（如 AI Coding、流程自动化）具有直接参考价值，有望成为 Agent 生态的通用范式。

---

## 2. LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems（NRT-Bench）
- **来源**: arXiv (2606.20408)
- **作者**: Hanwool Lee et al.
- **链接**: http://arxiv.org/abs/2606.20408v1
- **方向**: 🔒 AI 安全 / LLM Agent 对抗鲁棒性
- **TL;DR**: NRT-Bench 在核电站控制室场景下压力测试 LLM Agent 团队，8.7–12.1% 的自适应攻击使电厂丢失安全功能。
- **核心贡献**:
  - 构建首个以工业级安全关键系统（核电站）为场景的多轮 LLM Agent 红队评测 benchmark
  - 定义 6 个关键安全功能（CSF）作为客观终止信号，完全脱离 LLM 主观判断，实现可重现的危害量化
  - 揭示四个前沿模型的漏洞几乎不重叠，相同防护措施对不同模型效果相反——提示"模型多样性"不等同于安全冗余
- **方法亮点**: 五角色 Operator 团队由可配置 LLM 驱动，对手通过四个通信信道注入有界多轮攻击；采用"固定攻击配对回放协议"确保实验可复现；CSF 丢失即终止计分，排除人类评判主观性。
- **为什么值得读**: LLM Agent 快速进入工业控制等高风险场景，但现有红队测试几乎局限于文本生成；本研究将风险具体化为"电厂停堆"等可量化后果，为安全关键 AI 部署提供了首个端到端评测框架，对监管标准制定和工程实践均有重要参考。

---

## 3. Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning
- **来源**: arXiv (2606.20002)
- **作者**: Yanxi Chen et al.
- **链接**: http://arxiv.org/abs/2606.20002v1
- **方向**: 🤖 LLM Agent 训练 / 终身学习
- **TL;DR**: CoD 框架用端到端 RL 训练 LLM 在长周期部署中边解题边更新上下文，实现跨域迁移的元能力。
- **核心贡献**:
  - 提出"Connect the Dots"（CoD）元能力：Agent 在环境中完成连续任务序列，同时持续学习并自更新对环境的理解
  - 设计交错"解任务 + 更新上下文"的长 rollout RL 算法（GRPO 变体），含细粒度信用分配机制
  - 实证验证域内、跨域及 CoD→RALPH 循环的泛化：训练习得的元能力不局限于特定领域
- **方法亮点**: 关键创新在于将"学习如何学习"本身作为 RL 优化目标，而非只优化单次任务完成；长 rollout 序列强制模型在同一 episode 内体验知识积累的收益，形成内在激励去维护高质量的上下文更新。
- **为什么值得读**: 现有 Agent 多为"一次性部署"范式，无法从实际使用中持续积累经验；CoD 直指 Agent 真正长期有用所需的核心能力，与 AutoGPT/Devin 等系统的工程实践高度互补，对 AI Agent 通往 AGI 路径的学术探索和工业开发都具有战略意义。

---

## 4. Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users
- **来源**: arXiv (2606.20482)
- **作者**: Haw-Shiuan Chang et al.
- **链接**: http://arxiv.org/abs/2606.20482v1
- **方向**: 🧠 LLM 对齐 / 人机交互
- **TL;DR**: 用鼠标轨迹和眼动数据训练奖励模型，将文本 reward model 准确率从 55% 提升至 64%，DPO 后相对质量提升近 3 倍。
- **核心贡献**:
  - 构建 IFLLM 数据集：59 名众包工作者在回答 1336 个多轮问题时同步采集鼠标轨迹和眼动数据
  - 证明隐式行为信号（无需用户主动打分）可显著提升 reward model 预测准确率（55% → 64%）
  - 将隐式反馈引入 DPO 对齐流程，8 个 LLM 上相对响应质量提升约 3 倍，且数据收集成本远低于显式标注
- **方法亮点**: 利用用户阅读行为（滚动停留、扫视区域）和鼠标悬停位置作为偏好代理信号，建立多模态 reward 模型；该思路借鉴搜索引擎"点击行为"作为反馈的成熟范式，无缝集成到标准 RLHF/DPO 流程。
- **为什么值得读**: 高质量偏好标注是 RLHF 的核心瓶颈，价格昂贵且难以规模化；如果隐式信号能作为替代，每次用户与 LLM 的自然交互都将成为对齐信号的来源——这可能从根本上改变生产级 LLM 对齐数据的获取方式。

---

## 5. AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning
- **来源**: arXiv (2606.20373)
- **作者**: Zepeng Li et al.
- **链接**: http://arxiv.org/abs/2606.20373v1
- **方向**: 🔧 AI4Engineering / 编译器优化
- **TL;DR**: AutoPass 让 LLM Agent 查询编译器内部状态并分析 IR，在 x86-64 和 ARM64 上分别超越 -O3 基线 4.3% 和 11.7%。
- **核心贡献**:
  - 提出首个基于 LLM 多 Agent 框架的编译器性能自动调优系统，打破传统"编译器黑盒"假设
  - Agent 可主动查询编译器内部优化状态和中间表示（IR），以真实编译器反馈驱动决策
  - 训练无关（inference-only）设计，无需针对特定目标平台或 benchmark 进行微调，直接部署
- **方法亮点**: 与将编译器视为黑盒的经典 autotuner 不同，AutoPass 开放编译器内部 API 给 LLM，使其能够从中间表示层面理解性能瓶颈；迭代搜索循环以实际运行时反馈诊断回归并指导下一轮编辑，类比"代码审查+修复"工作流。
- **为什么值得读**: 编译器优化是高度依赖专家知识的领域，传统 autotuner 搜索空间巨大且效率低下；AutoPass 展示了 LLM 可从编译器内部信号"理解"程序行为而非盲目搜索，为 AI 驱动的系统软件优化提供了新范式，在 AI 芯片、嵌入式系统等对性能敏感领域有直接应用价值。

---

*完整归档：https://github.com/Toflamus/arXiv_daily_digest/tree/main/digests*
