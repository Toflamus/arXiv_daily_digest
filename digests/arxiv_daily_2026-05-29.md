# 每日精选 · 2026-05-29

> ❌ **数据缺失**：`raw/papers_2026-05-29.json` 不存在。GitHub Actions 未能在今日（UTC 2026-05-29）成功抓取论文数据。最新可用数据为 `raw/papers_2026-05-28.json`（昨日，已在 2026-05-28 digest 中处理）。
>
> 本日 digest 为空，无法生成精选论文。请检查 GitHub Actions 工作流日志以排查问题。

**可能原因**：
- arXiv API 连续遭遇 HTTP 429 限速（2026-05-28 已记录此问题）
- GitHub Actions 工作流未在 UTC 2026-05-29 触发
- 网络代理或 cron 任务配置问题

**建议操作**：
- 前往 https://github.com/Toflamus/arXiv_daily_digest/actions 查看最近的 workflow 运行状态
- 如需补运行，可手动触发 workflow（workflow_dispatch）
- 若 arXiv 持续 429，考虑在 Actions 中加入 retry 逻辑或降低请求频率
