# 每日精选 · 2026-06-23

> 数据源：GitHub Actions 预拉（arXiv 368 篇 + journals 234 篇）。Top30 去重后精选 5 篇（arXiv 5 + journals 0）。
> 今日 Top30 全为 arXiv 论文，顶刊未进入本日前 30。

---

## 1. HOLMES: Evaluating Higher-Order Logical Reasoning in LLMs
- **来源**: arXiv
- **作者**: Yucheng Wu et al.
- **链接**: http://arxiv.org/abs/2606.23238v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 首个真实场景高阶逻辑推理 benchmark，当前最佳模型准确率仅 59.5%。
- **核心贡献**:
  - 构建 HOLMES：1379 个实例，覆盖法律与金融领域，配套 HOL 形式化、可验证推理轨迹与细粒度控制因子
  - 揭示"高准确率掩盖捷径推理"现象：在冲突解决场景中，模型在最终答案正确的同时存在推理捷径
  - 识别范围条件推理（scope-conditioned）和组合推理（compositional）是当前 LLM 的关键瓶颈
- **方法亮点**: 以高阶逻辑（HOL）为形式化基础，将自然语言问题与 HOL 公式配对，支持机器可验证的推理路径审计；同时引入可控推理难度因子，允许系统性剖析模型推理能力边界。
- **为什么值得读**: 现有 benchmark 几乎全部聚焦一阶逻辑；而法律、合规、科学推理等高价值场景天然需要高阶逻辑。本文为构建可靠、可验证 LLM 系统指明了下一个关键突破口。

---

## 2. Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?
- **来源**: arXiv
- **作者**: Anmol Goel et al.
- **链接**: http://arxiv.org/abs/2606.23189v1
- **方向**: 🤖 LLM / AI Safety
- **TL;DR**: 15 个主流 CUA 中 11 个在 50% 以上场景中泄露私人信息，平均泄露率 67.9%。
- **核心贡献**:
  - 提出 AgentCIBench：首个将"情境完整性"（Contextual Integrity）理论操作化为可执行、确定性评分场景的评测框架
  - 定义三类典型失效模式：视觉共存泄露、任务歧义过度分享、收件人错配
  - 在端到端完整执行环境中复现同样高失效率，排除"纯生成"场景的偶然性
- **方法亮点**: 将隐私风险转化为可确定性评分的测试用例，通过 UI 视觉共存、提示歧义、收件人错配三维度构建覆盖日常应用（邮件、日历、待办清单）的评测场景。
- **为什么值得读**: CUA 的跨应用访问能力正在快速普及，但本文用数据揭示绝大多数前沿 Agent 在隐私方面存在系统性盲区。AgentCIBench 作为预部署安全检查工具具有直接落地价值。

---

## 3. Field-level Weak Lensing Cosmology with <100 Simulations Using Multifidelity SBI
- **来源**: arXiv
- **作者**: Alex A. Saoulis et al.
- **链接**: http://arxiv.org/abs/2606.23346v1
- **方向**: 🔬 AI4Science
- **TL;DR**: 多保真度模拟推断将场级宇宙学分析所需高保真 N-body 模拟数量从千级降至 60–100。
- **核心贡献**:
  - 实现 KiDS-Legacy 级别真实场级弱引力透镜分析，高保真模拟需求降低约一个数量级
  - 在快速 log-normal GLASS 模拟上预训练神经推断模型，再以少量高保真模拟微调，成功迁移
  - 在 60–100 个高保真模拟下获得有信息量且校准良好的宇宙学后验分布
- **方法亮点**: 多保真度模拟推断（Multifidelity SBI）结合场级神经压缩与深度学习神经网络推断；通过低精度但海量的 log-normal 模拟做预训练以学习场级结构，再用极少量精确 N-body 模拟校准后验。
- **为什么值得读**: 场级宇宙学推断可提取功率谱之外的全部非高斯信息，但其对模拟精度与数量的双重需求构成主要障碍。本文将这一方法推向实用门槛，对下代巡天（Euclid、LSST）具有直接意义。

---

## 4. Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently
- **来源**: arXiv
- **作者**: Stanley Wei et al.
- **链接**: http://arxiv.org/abs/2606.22938v1
- **方向**: 🧠 AI/ML
- **TL;DR**: 理论证明 SFT 无法学会高效回退，而 RLVR 可以，两者推理计算量存在指数级差距。
- **核心贡献**:
  - 将 CoT 推理建模为图上路径查找问题，在此框架下严格比较 RLVR 与 SFT
  - 证明 SFT 在缺少负样本情况下无法学习高效回退（backtrack），导致指数级推理计算浪费
  - 证明 RLVR 模型可从死端高效回退，并能定位推理链中的困难决策点，从而优化推理时计算分配
- **方法亮点**: 构建图路径搜索的形式化模型，分析 SFT 在"只有最短金标路径"训练信号下的失败模式；通过 RLVR 的结果奖励信号证明其能学习等效于 BFS 的策略；最后证明 RLVR 轨迹可蒸馏回基础模型。
- **为什么值得读**: 这是业界广泛观察到"RLVR 训练效果优于 SFT"现象的首个严格理论解释，为大量工程实践提供了形式化基础，也指出了蒸馏路径。

---

## 5. GIF: Locally Sound Geometric Information Flow Control for LLMs
- **来源**: arXiv
- **作者**: Adam Storek et al.
- **链接**: http://arxiv.org/abs/2606.23277v1
- **方向**: 🤖 LLM / AI Security
- **TL;DR**: 用 Jacobian 上界香农互信息，实现 LLM 信息流控制，附 Lean 4 可机械验证的健全性证明。
- **核心贡献**:
  - 提出 GIF 框架：利用 LLM Jacobian 与局部输出几何对输入 token 到输出的信息流做有上界估计
  - 提供完整 Lean 4 机械化证明：在局部正则性假设下 GIF 上界满足局部几何健全性
  - 结合轻量 LLM 解密器，在多个提示注入与隐私泄露 benchmark 上以最高 81× 低 token 成本匹敌 GPT-5.5 xhigh 推理级别性能
- **方法亮点**: 通过自动微分与低秩近似在大模型上高效计算 Jacobian；小代理模型（最小可小 200×）检测的信息流可直接迁移到黑盒大模型，支持无需梯度访问的部署；彻底回避注意力归因启发式方法固有的污点爆炸问题。
- **为什么值得读**: 将形式化方法（定理证明）与生产级 LLM 安全结合，是该领域罕见的有可证明保证的工作。黑盒可迁移性和极低推理成本使其具备实际部署可行性。
