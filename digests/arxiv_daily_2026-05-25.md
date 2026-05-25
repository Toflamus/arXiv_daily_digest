# 每日精选 · 2026-05-25

> 数据源：GitHub Actions 预拉（arXiv **0** 篇 ⚠️ + journals 158 篇）。Top30 去重后精选 5 篇（arXiv 0 + journals 5）。
>
> ⚠️ **注意**：今日 arXiv 抓取返回 0 篇（`arxiv_count: 0`，`arxiv_error: null`），原因未知（可能是 arXiv 周末/节假日停止发布、Actions 网络异常，或 arXiv 接口变动）。硬性要求"至少 2 篇 arXiv"无法满足，本期全部来自顶刊。请检查 Actions 日志确认根因。

---

## 1. SmileyLlama: modifying large language models for directed chemical space exploration
- **来源**: Nature Computational Science
- **作者**: (Authors not listed) et al.
- **链接**: https://www.nature.com/articles/s43588-026-00986-y
- **方向**: 🧪 AI4Science / 🤖 LLM
- **TL;DR**: 将通用 LLM 微调为 SmileyLlama，可按用户指定药化属性定向生成类药分子。
- **核心贡献**:
  - 证明通用 LLM 可通过专项训练转化为化学空间探索专用模型
  - 支持用户指定多种药物化学相关属性（如活性、ADMET 特征）
  - 提供可推广至其他科学领域的训练范式
- **方法亮点**: 以 SMILES 字符串为分子表示，对开源 LLM 进行指令微调，将用户指定的目标属性编码为提示条件，引导模型在化学空间中定向采样，而非随机生成。
- **为什么值得读**: 连接了 LLM 与药物发现，展示通用预训练模型经轻量微调即可进入高度专业化科学领域；该范式对材料设计、合成路线规划等任务同样适用，具有宽泛的 AI4Science 迁移价值。

---

## 2. Reward magnitude determines reinforcement learning efficiency
- **来源**: Science
- **作者**: (Authors not listed) et al.
- **链接**: https://www.science.org/doi/abs/10.1126/science.aeb0813?af=R
- **方向**: 🧠 AI/ML / 🔬 AI4Science（神经科学）
- **TL;DR**: 在神经系统中，奖励幅度直接决定强化学习的效率，而非仅仅影响选择偏好。
- **核心贡献**:
  - 揭示奖励量级对 RL 学习速率的因果性影响
  - 为生物 RL 与人工 RL 奖励设计之间建立实验桥梁
  - 提供关于多巴胺/神经调制如何编码奖励大小的新证据
- **方法亮点**: 通过行为实验与神经记录解耦奖励大小与选择倾向，量化不同量级奖励下的学习曲线，直接检验奖励幅度对突触可塑性速率的调控。
- **为什么值得读**: 对 RL 算法设计有直接启发意义——奖励缩放（reward shaping/normalization）不仅影响收敛稳定性，也可能从根本上改变学习效率，值得在神经网络训练策略中重新审视。

---

## 3. Dynamics of disordered quantum systems with two- and three-dimensional tensor networks
- **来源**: Science
- **作者**: (Authors not listed) et al.
- **链接**: https://www.science.org/doi/abs/10.1126/science.adx2728?af=R
- **方向**: 🔬 AI4Science（量子计算 / 计算物理）
- **TL;DR**: 用 2D/3D 张量网络模拟无序量子多体系统的动力学，突破了 1D 方法的局限。
- **核心贡献**:
  - 将张量网络方法从 1D 推广到 2D/3D 无序量子系统
  - 在多体局域化（MBL）等难题上取得可信数值结果
  - 为量子模拟提供经典计算基准
- **方法亮点**: 构建高维张量网络表示，利用结构化截断和随机平均技术处理无序性带来的纠缠复杂度，使大规模量子系统时间演化的经典模拟成为可能。
- **为什么值得读**: 张量网络与机器学习的深度交叉（TN 可视为特殊神经网络结构），该工作在量子多体领域的突破也将反哺张量网络在 ML 中的方法论；同时为量子计算机的经典基准验证提供工具。

---

## 4. Mucosal vaccination in mice provides protection from diverse respiratory threats
- **来源**: Science
- **作者**: (Authors not listed) et al.
- **链接**: https://www.science.org/doi/abs/10.1126/science.aea1260?af=R
- **方向**: 🔬 AI4Science（生物医学）
- **TL;DR**: 黏膜疫苗接种在小鼠中对多种呼吸道病原体提供广谱保护。
- **核心贡献**:
  - 证明黏膜给药途径可激活局部免疫，实现跨病原体广谱保护
  - 为通用呼吸道疫苗策略提供概念验证
  - 揭示黏膜免疫在应对多样性病原威胁中的独特优势
- **方法亮点**: 通过鼻内/气道给药构建黏膜免疫模型，系统比较黏膜 vs. 注射疫苗接种后的组织驻留记忆 T 细胞（Trm）与 IgA 抗体分布，用多种病毒/细菌攻毒验证广谱性。
- **为什么值得读**: COVID-19 后黏膜疫苗成为研究热点，此研究在动物模型中给出了广谱有效性的有力证据，对下一代泛呼吸道疫苗和 AI 辅助抗原设计均有重要参考价值。

---

## 5. Abrupt stream acidification and metal mobilization from permafrost degradation
- **来源**: Science
- **作者**: (Authors not listed) et al.
- **链接**: https://www.science.org/doi/abs/10.1126/science.aea2898?af=R
- **方向**: 🔬 AI4Science（地球科学 / 气候）
- **TL;DR**: 永久冻土退化导致河流突发酸化和重金属释放，是被忽视的气候环境风险。
- **核心贡献**:
  - 记录永久冻土融化引发的河流突发性、高强度酸化事件
  - 量化金属（铁、铝、重金属）向水体的快速迁移规律
  - 揭示北极气候变化对淡水生态系统的级联威胁
- **方法亮点**: 结合野外实地监测、水化学时序分析和遥感数据，追踪多个永久冻土融区的水质突变事件，建立冻土退化→硫化物氧化→酸化→金属溶出的因果链。
- **为什么值得读**: 气候变化的非线性、突变式影响往往被线性模型低估；该研究为气候模型提供了新的正反馈机制证据，也对 AI 驱动的地球系统建模提出新需求——需要捕捉突变事件而非仅拟合平均趋势。

---
