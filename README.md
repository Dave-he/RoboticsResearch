# RoboticsResearch

> 一个面向"通用机器人技术(机械臂 / 移动机器人 / 操控 / 导航 / SLAM / 具身智能)"的持续研究知识库。
> 采用 Living Systematic Review 模式:每日自动抓取 arXiv / GitHub / 官方博客 → 筛选 → 研读报告 → 全局索引 → 产业链/应用/成本观察。

## 🎯 项目目标

在机器人技术快速演进的时代,把分散的学术论文、开源项目、行业动态、产业链信息沉淀为一个**可审计、可搜索、可推理**的活知识库,实现:

- **横通**:把机械臂、移动机器人、SLAM、VLA 模型、灵巧手、人形机器人等子领域拉通对比
- **纵深**:对单篇论文做到"理论 + 公式 + 复现线索 + 行业落地"四层研读
- **前瞻**:跟踪 Figure / Tesla Optimus / 1X / Unitree / Physical Intelligence 等前沿玩家,推演技术拐点
- **务实**:每个研读报告都要回答「应用方向 / 行业 / 成本 / 替代方案」

## 📁 仓库结构

```
RoboticsResearch/
├── README.md                       本文件
├── AGENTS.md                       AI Agent / Skill 协作规范
├── docs/
│   ├── 机器人研究协议.md            Living Review 协议(范围/关键词/数据源/筛选规则)
│   ├── 机器人_深度研读报告.md        全局索引(每篇研读报告的精简版)
│   ├── 机器人行业格局与产业链.md     厂商 / 玩家 / 成本拆解(长期维护)
│   ├── daily/                      每日自动生成的研读摘要
│   ├── reports/                    单篇论文 / 单个项目的深度研读报告
│   ├── research/                   综述、月度合成、跨子领域对照
│   └── guides/                     使用指南
├── papers/daily/                   原始抓取数据(机器可读 JSON)
├── analysis/
│   └── repo_watchlist/             GitHub / HuggingFace 仓库观察
├── scripts/                        数据抓取与处理脚本
│   ├── daily_robotics_research.py  主入口:每日抓取 + 生成摘要
│   └── ...
├── configs/                        关键词、优先级、源配置
└── skills/
    └── living-field-robotics-researcher/   可复用的"机器人领域研究"Skill
```

## 🚀 快速开始

### 一次性手动运行

```bash
cd /Users/hyx/workspace/RoboticsResearch
python3 scripts/daily_robotics_research.py \
    --max-arxiv 80 \
    --github-per-query 12 \
    --output-root .
```

输出:
- `papers/daily/YYYY-MM-DD_robotics_research.json` (机器可读原始数据)
- `docs/daily/YYYY-MM-DD_robotics_research_digest.md` (人类可读摘要)
- `analysis/repo_watchlist/YYYY-MM-DD_robotics_repos.md` (仓库观察)
- 自动追加到 `docs/机器人_深度研读报告.md` 全局索引

### 启用每日定时任务

参见 [docs/guides/每日自动化任务.md](docs/guides/每日自动化任务.md)。

### 在其他 AI 工具中调用本项目 Skill

```bash
npx skills add ./skills/living-field-robotics-researcher
```

## 📚 子领域覆盖

- **机械臂与工业自动化**:运动学 / 动力学 / 力控 / 抓取
- **移动机器人与自动驾驶**:SLAM / 路径规划 / 多传感器融合
- **人形机器人**:运动控制 / 全身协调 / 步态
- **灵巧手与操控**:dexterous manipulation / 触觉感知
- **具身智能 / VLA**:RT-2 / π0 / OpenVLA / 视觉-语言-动作模型
- **仿真与数字孪生**:Isaac Sim / MuJoCo / SAPIEN
- **数据集与 Benchmark**:RT-X / DROID / Bridge
- **行业与产业链**:核心玩家、供应链、量产成本

## 🔗 关联项目

- [LNN](https://github.com/Dave-he/LNN) —— 液态神经网络的同模式研究库,本项目的范式参考
- `skills/living-field-robotics-researcher` 来自 LNN 项目的 `skills/living-field-researcher`,已重写为机器人领域版本

## 📝 维护原则

- 每一个引用都必须有可点击的来源(URL / arXiv ID / 本地 PDF)
- 每一个结论都必须区分"论文自述"、"我们的推断"、"未验证"
- 研读报告必须包含:核心问题 / 方法 / 公式 / 成果 / 局限 / 复现线索 / **应用与行业映射**
- 不做内容农场式的表面摘要,坚持"融汇贯通 + 深刻推理"
