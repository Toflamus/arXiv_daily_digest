# 每日精选 · 2026-05-22

> 数据源：GitHub Actions 预拉（arXiv 416 篇 + journals 225 篇）。Top30 去重后（去除 1 篇重复 Nature 论文）精选 5 篇（arXiv: 5 + journals: 0）。

## 1. Efficient Agentic Reasoning Through Self-Regulated Simulative Planning
- **来源**: arXiv
- **作者**: Mingkai Deng et al.
- **链接**: http://arxiv.org/abs/2605.22138v1
- **方向**: 🤖 LLM / Agent
- **TL;DR**: 三系统框架让 8B 模型媲美 355B，推理 token 减少 95%
- **核心贡献**:
  - 提出 SR²AM，将 agent 决策分解为三层系统：System I（反应式执行）、System II（模拟推理/世界模型）、System III（自我调控/何时规划）
  - 通过 SFT + RL 联合训练，RL 阶段使规划深度提升 22.8%，但规划频率仅增 2%
  - v0.1-8B / v1.0-30B 在数学、科学、网页检索任务上分别媲美 120-355B 和 685B-1T 参数系统
- **方法亮点**: 以 LLM 自身作为世界模型实现模拟推理，configurator 通过学习决定何时以及规划多深——绕开了逐 domain 工程化的瓶颈，同时在 chain-of-thought 内嵌入结构化规划阶段。
- **为什么值得读**: 从"token 越多越好"转向"按需规划"的范式转移，直接证明效率与精度不必二选一；System III 的自我调控思路对未来 agent 设计（包括学习与适应的自我治理）有广泛启发。

---

## 2. Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning
- **来源**: arXiv
- **作者**: Ismail Geles et al.
- **链接**: http://arxiv.org/abs/2605.22748v1
- **方向**: 🧠 AI/ML · 🤖 机器人
- **TL;DR**: 多智能体 RL 让四旋翼无人机以 22m/s 速度在真实赛道击败人类冠军且碰撞率降 50%
- **核心贡献**:
  - 首次在多机真实高速赛车场景中用 MARL 实现超人性能，同时大幅降低碰撞率
  - 联赛自我对弈（league-based self-play）让 agent 涌现出主动避障、超车、应对气动下洗等复杂预期行为
  - 在多样化人工 agent 下训练后，可零样本迁移至与真实人类的安全交互
- **方法亮点**: 训练时引入可变数量的参赛者和联赛制度，让 agent 学会在稠密气动干扰下进行战略性机动；不使用单独安全约束层，而是把安全需求内化为多智能体博弈的自然产物。
- **为什么值得读**: 将物理机器人中"与人共存"问题的解法从单智能体+安全约束，推进到多智能体博弈学习；对自动驾驶、无人机协作等领域有直接参考价值，且实验在真实硬件上验证。

---

## 3. ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling
- **来源**: arXiv
- **作者**: Woomin Song et al.
- **链接**: http://arxiv.org/abs/2605.22102v1
- **方向**: 🤖 LLM / Agent
- **TL;DR**: 多 agent 并行推理中途互相审计事实冲突，错误传播率显著下降
- **核心贡献**:
  - 观察到并行 agent 推理中大多数中间错误会产生可检测的跨 agent 事实冲突
  - 引入周期性审计 + 工具验证循环，以"软信念更新"（追加验证信息而非覆盖）修正错误，同时通过轨迹多样化模块避免通信导致的同质化
  - 在 AIME 2024/2025 和 GAIA 上平均超越最强基线 5.0-5.7%
- **方法亮点**: 利用 agentic 工作流的迭代结构，在工具调用等待期做跨 agent 一致性检查；不改变任何模型权重，是纯推理时干预方案，适配 Gemini-2.5-Flash-Lite 和 Qwen3.5-4B 等多种 backbone。
- **为什么值得读**: 解决了 test-time scaling 中被忽视的"错误传播"瓶颈，且提供了成本-性能最优的 trade-off；轨迹多样化与误差修正并存的设计思路对工业级多 agent 系统落地有实际指导意义。

---

## 4. LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation
- **来源**: arXiv
- **作者**: Zhuo Chen et al.
- **链接**: http://arxiv.org/abs/2605.22054v1
- **方向**: 🔬 AI4Science
- **TL;DR**: 用廉价 LLM 评估宽泛探索搜索空间，把真实实验预算留给高不确定区域
- **核心贡献**:
  - 提出门控准则动态平衡"依赖 LLM 预测"与"做真实实验"的比例
  - 在统一 BO 循环中整合 LLM 廉价预测与真实观测，提供有理论保证的累计遗憾界
  - 在多个科学任务上在相同实验预算下持续超越现有方法
- **方法亮点**: 关键洞察是 LLM 评估成本远低于真实实验——LABO 用 LLM 大范围探索，保留昂贵实验仅用于不确定性高的区域；门控机制有理论分析支撑而非纯启发式。
- **为什么值得读**: 为科学自动化提供了一条经济实用的路线：无需大量真实实验即可缩小搜索空间；对材料、药物、化学等数据稀缺领域的高通量筛选有直接应用价值。

---

## 5. LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems
- **来源**: arXiv
- **作者**: Sadia Asif et al.
- **链接**: http://arxiv.org/abs/2605.22786v1
- **方向**: 🤖 LLM / Agent · 🛡️ AI 安全
- **TL;DR**: KV cache 跨 agent 传递时泄露隐私，LCGuard 用对抗训练在表示层阻断信息泄漏
- **核心贡献**:
  - 形式化定义"KV cache 中隐私信息通过表示层传播"的威胁模型：若对抗解码器能重建敏感输入则判定为不安全
  - 提出对抗训练框架：解码器学习重建隐私，LCGuard 学习在保留任务语义的同时降低可重建性
  - 在多个模型族和多 agent benchmark 上一致降低重建泄漏率和攻击成功率，任务性能基本不损失
- **方法亮点**: 将 KV cache 视为"潜在工作记忆"而非透明通道，在传输前做表示级变换；无需修改模型权重或通信协议，是插拔式安全层。
- **为什么值得读**: 随着 KV 共享在多 agent 系统中提升效率，这一隐私风险将日益突出；本文是目前为数不多正面处理 latent communication 安全的工作，对构建可信多 agent 系统具有重要参考价值。

---
