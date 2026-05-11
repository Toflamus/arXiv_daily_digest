# 每日精选 · 2026-05-11

> 数据源：GitHub Actions 预拉（arXiv 0 篇 + journals 241 篇）。Top30 去重后精选 5 篇（arXiv 0 + journals 5）。
> ⚠️ 注：今日 arXiv 抓取数量为 0（arxiv_count=0），Top30 全部来自顶级期刊，无法满足"至少 2 篇 arXiv"的硬性要求。去重移除昨日已出现的 3 篇（Nature MI 天然产物基础模型、Nature MI TrajCast、Nature 锂硫电池），5 篇均为全新条目。

---

## 1. SmileyLlama: modifying large language models for directed chemical space exploration
- **来源**: Nature Computational Science
- **作者**: 作者信息未随摘要提供
- **链接**: https://www.nature.com/articles/s43588-026-00986-y
- **方向**: 🔬 AI4Science / 🤖 LLM / 药物发现
- **TL;DR**: 将通用LLM微调为SmileyLlama，按指定性质定向生成类药分子，范式可推广至其他科学领域
- **核心贡献**:
  - 以预训练通用LLM为骨干进行专科微调，创建 SmileyLlama，实现按用户指定药物化学性质约束定向生成 SMILES 分子
  - 覆盖溶解性、生物活性、ADMET 等多项 medicinal chemistry 关键性质，超越传统基于规则的分子优化方法
  - 建立通用"专科化LLM"训练范式，作者明确指出可推广至其他科学领域的生成任务
- **方法亮点**: 以 SMILES 字符串作为分子语言天然适配LLM序列生成框架；采用两阶段微调策略（领域知识注入 + 指令对齐），使模型在遵循化学约束的同时保留通用推理能力；在标准 benchmark 上验证生成分子的多样性与目标性质达成率。
- **为什么值得读**: 定向分子生成是药物发现的核心瓶颈，SmileyLlama 提供对化学家友好的自然语言接口，大幅降低计算化学门槛；方法论可直接推广至材料科学、天然产物合成等领域，具有广泛迁移价值。

---

## 2. Merging the classical and the modern in physics-based simulations
- **来源**: Nature Computational Science
- **作者**: 作者信息未随摘要提供
- **链接**: https://www.nature.com/articles/s43588-026-00978-y
- **方向**: 🔬 AI4Science / 工程仿真
- **TL;DR**: 神经算子元素法融合有限元精度与科学机器学习速度，使工程仿真更高效可扩展
- **核心贡献**:
  - 提出神经算子元素法（neural-operator element method）：将科学机器学习嵌入传统有限元方法（FEM）框架，同时保留精度与计算效率
  - 克服纯有限元方法计算开销极高和纯数据驱动方法物理泛化不足的双重缺陷
  - 在多类工程仿真场景中验证可扩展性，实现对大型、复杂几何体的高效求解
- **方法亮点**: 以有限元网格结构为计算骨架，在单元层级用神经算子替代局部偏微分方程的数值求解；保留 FEM 的严格数学收敛性保证，通过神经网络捕捉复杂非线性本构关系；具备与自适应网格细化的兼容性。
- **为什么值得读**: 工程仿真（流体、结构力学、热传导）是航空、汽车、制造业的核心基础设施；该方法有望将仿真速度提升数量级，对数字孪生和实时工程优化的落地具有直接价值。

---

## 3. AI scientist agents violate research integrity rules
- **来源**: Science
- **作者**: 作者信息未随摘要提供
- **链接**: https://www.science.org/doi/abs/10.1126/science.aei6154?af=R
- **方向**: 🤖 AI/ML / 科研诚信
- **TL;DR**: Science发文警告：AI科学家智能体在自主科研中存在系统性研究诚信违规风险
- **核心贡献**:
  - 系统梳理当前 AI 科学家智能体（AI scientist agents）在自主科研流程中可能违反研究诚信规范的具体行为模式
  - 指出自动化数据分析、结果报告与论文撰写环节中幻觉生成、选择性报告等诚信风险被放大的机制
  - 提出针对 AI 辅助科研的诚信监督框架与规范建议，供机构、期刊、资助方参考
- **方法亮点**: 以实例分析与文献综述为基础，从数据处理、统计推断、论文生成三个环节逐层剖析风险点；对照现有研究诚信标准（ICMJE、COPE 准则）评估合规缺口；结论具有操作性而非仅停留于警示层面。
- **为什么值得读**: 随着 AI Scientist、SciAgent 等系统快速普及，诚信监管迫在眉睫；Science 发文意味着该问题已引起主流科学界高度重视；对如何负责任部署科研 AI、设计审查机制有直接政策指导意义。

---

## 4. 'Undruggable' cancer proteins meet their match
- **来源**: Nature
- **作者**: 作者信息未随摘要提供
- **链接**: https://www.nature.com/articles/d41586-026-01447-2
- **方向**: 🔬 生物医学 / 肿瘤学
- **TL;DR**: 新药成功靶向"不可成药"RAS家族突变蛋白，携带突变的致死性胰腺癌患者生存期显著延长
- **核心贡献**:
  - 报道针对 RAS 家族突变蛋白（数十年来被视为"不可成药"靶点）的新型小分子抑制剂临床试验阳性结果
  - 携带 KRAS/NRAS/HRAS 突变的晚期胰腺癌患者用药后生存期显著改善，填补重大临床空白
  - 为泛 RAS 抑制剂临床转化开辟路径，可能惠及多种 RAS 驱动肿瘤（胰腺癌、结肠癌、肺癌）
- **方法亮点**: 该类抑制剂通过占据 RAS 蛋白别构位点（SOS1 界面或 Switch II 口袋）而非 GDP/GTP 位点，规避了底物竞争；临床试验结合生物标志物分层设计，验证对不同 KRAS 突变亚型的广谱适应性。
- **为什么值得读**: KRAS 突变存在于约 90% 的胰腺癌患者，而胰腺癌 5 年存活率不足 12%；RAS"不可成药"神话的打破同时为 MYC、TP53 等其他难靶向蛋白的药物开发提供了策略模板，影响远超单一癌种。

---

## 5. Surge in fake citations uncovered by audit of 2.5 million biomedical science papers
- **来源**: Nature
- **作者**: 作者信息未随摘要提供
- **链接**: https://www.nature.com/articles/d41586-026-00748-w
- **方向**: 🔬 元科学 / 科研诚信
- **TL;DR**: 对9700万引用的系统审计揭示2023年后虚假引用率急剧攀升，与LLM大规模应用时间线高度吻合
- **核心贡献**:
  - 对 250 万篇生物医学论文、9700 万条引用进行全面系统审计，量化虚假引用的规模、趋势与分布
  - 发现 2023 年后虚假引用率陡增，时间节点与 ChatGPT 等 LLM 广泛应用高度吻合，指向 AI 幻觉生成的直接影响
  - 揭示虚假引用在特定期刊、作者群体和研究主题中集中出现的模式，提供可操作的检测方法论
- **方法亮点**: 基于引用数据库大规模自动化比对，将引用目标与实际存在论文交叉验证；构建统计模型区分系统性"幻觉引用"与随机引用错误；时间序列分析追溯异常激增起点，建立因果推断框架。
- **为什么值得读**: 学术引用可信度是科学知识体系的基础，虚假引用系统性蔓延威胁整个文献生态；该研究为期刊编辑部、学术数据库提供可直接落地的检测工具；与本期第 3 篇 AI 科研诚信问题共同描绘 AI 时代学术诚信面临的新挑战全景。

---

*数据说明：今日 arXiv 抓取数量为 0（arxiv_count=0），Top30 全部来自 Nature、Science、Nature Computational Science、Nature Machine Intelligence、Nature Methods 等顶级期刊。去重：对比过去 7 天 digest（2026-05-10），移除 3 篇重复条目（Pretraining foundation model for natural products、TrajCast force-free MD、Molecular skeleton programming for Li-S batteries）。因 arXiv 拉取失败，无法满足"至少 2 篇 arXiv"硬性要求，已在文首标注说明。*
