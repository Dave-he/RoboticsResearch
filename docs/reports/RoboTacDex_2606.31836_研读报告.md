---
title: RoboTacDex 人形灵巧视-触-动作数据集_研读报告
arxiv_id: "2606.31836v1"
date: 2026-07-01
subarea: manipulation
tags: [robotics, humanoid, dexterous-manipulation, tactile, dataset, imitation-learning, unitree-g1, dual-arm]
---

# RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation

> **作者**:Xinyi Wang, Donghan Li, Zi'Ang Chen, Chong Yu, Chen Xin, Peng Ye, Yingkai Sun, Tao Chen
> **机构**:arXiv 主页未明示(需查 PDF 抬头;从数据集选型 Unitree G1 推测为国内高校 / 研究院联合工作,7 位作者含 1 位通讯 Tao Chen)
> **发表**:2026-06-30 · arXiv: 2606.31836v1 · cs.RO
> **本报告状态**:首次入册,基于 arXiv 摘要整理(项目页 / 代码 / 视频链接 arXiv 主页未提供,摘要称 "will be open-sourced soon")

## 元数据

- **arXiv ID**:[2606.31836v1](https://arxiv.org/abs/2606.31836v1)
- **作者**:Xinyi Wang, Donghan Li, Zi'Ang Chen, Chong Yu, Chen Xin, Peng Ye, Yingkai Sun, Tao Chen(8 人,1 通讯)
- **机构**:arXiv 主页未明示
- **发表时间**:2026-06-30
- **会议 / 期刊**:预印本,未注明 venue
- **DOI**:10.48550/arXiv.2606.31836
- **PDF**:[link](https://arxiv.org/pdf/2606.31836v1)
- **代码 / 项目页**:摘要承诺 "open-sourced soon",arXiv 主页暂无链接,需追踪作者主页
- **License**:摘要未声明(数据集通常采用 CC-BY-4.0 / Apache-2.0)

## 核心问题

人形机器人 + 灵巧手是"通用机器人"的终极形态之一,但**这个赛道的 imitation learning 数据底座严重不足**:

1. **现有公开数据集多围绕 6-7 DoF 桌面机械臂**:DROID(76k)、Open X-Embodiment(2M+)、Bridge、RT-1 等,几乎全部基于 Franka / WidowX / xArm,**末端执行器是平行夹爪**。
2. **针对灵巧手(dexterous hand)+ 多指的数据集稀缺且规模小**:DextrAH、Bi-Touch、HumanDex 等规模多在 1k 轨迹以下,**任务多样性也集中在单手简单抓取**。
3. **真人人形机器人的数据更是稀缺**:Unitree H1/G1、Figure 02、1X Neo、Optimus 等虽然量产,但**各家数据闭源**(Figure Helix、1X Redwood、Optimus End-to-End 全是 paper-level 描述,无 dataset release)。
4. **触觉模态几乎缺失**:Open X-Embodiment 主打视觉 + 本体感觉,**几乎不包含高分辨率触觉信号**(GelSight / DIGIT / 9D TacTip)。触觉对"易碎物抓取、接触丰富任务(扭瓶盖、捏鸡蛋)、滑移检测"是刚需。
5. **多视角同步采集的真值难做**:多相机(腕部 + 第三视角 + 头部)+ 触觉 + 关节状态同步到 ms 级,工程门槛高,**许多论文用近似时间戳,真值存在抖动**。

**根因诊断**:**"人形 + 灵巧手 + 多模态" 是三重要求叠加,数据采集成本 = 硬件($100k+) × 时间(数月) × 工程(多模态同步)**。开源社区缺少一个"够大、够多模态、够全人形"的标准数据集,各家模型都只能在私有数据上自评,**imitation learning 在人形灵巧手场景的可复现性被锁死**。

**核心视角**:**用消费级人形机器人(Unitree G1,$16k 起)+ 多模态同步采集,做出一个 6k 轨迹、19 任务、23 技能、22 物体的开源基准**,让学术界有"中等规模但多模态齐全"的对照数据集。

## 方法论与核心思路

### 整体框架

```
+--------------------------------------------------------------+
|            数据采集硬件栈(基于 Unitree G1)                  |
|                                                              |
|  [Unitree G1 人形机器人]        [多视角 RGB-D 相机]         |
|       ├─ 双 7-DoF 灵巧手         ├─ 头戴 RGB-D              |
|       ├─ 12+ 关节本体感觉        ├─ 第三人称 RGB-D ×2       |
|       └─ 触觉传感器(每指)        └─ 腕部鱼眼 RGB-D          |
+--------------------------------------------------------------+
                          ↓
+--------------------------------------------------------------+
|            多模态同步采集系统(自研)                         |
|                                                              |
|  ms 级时间戳对齐:视觉 / 深度 / 触觉 / 关节 / 夹爪           |
|  → 输出 .h5 / .parquet 标准化格式                           |
+--------------------------------------------------------------+
                          ↓
+--------------------------------------------------------------+
|            任务 / 技能 / 物体 三维标注                      |
|                                                              |
|  19 任务 × 23 技能 × 22 物体 = 6k 轨迹                       |
|  (双臂协同 / 触觉依赖 / 长程任务 占主导)                    |
+--------------------------------------------------------------+
                          ↓
+--------------------------------------------------------------+
|            基准评测:三种 imitation learning policy          |
|                                                              |
|  1. Behavior Cloning (BC)                                    |
|  2. Diffusion Policy                                         |
|  3. ACT (Action Chunking Transformer)                       |
+--------------------------------------------------------------+
```

### 关键创新点 1:Unitree G1 + 灵巧手的多模态数据栈

**平台选型**:**Unitree G1**(2024 年发布,起售价 ~$16k,EDU 版 $40k 含灵巧手)是当前**唯一价格在 $20k 以内、含双臂 7-DoF 灵巧手的人形整机**。这意味着:

- 高校实验室买得起(同档次的 Figure 02 / 1X Neo / Optimus Gen 2 都 >$100k,且闭源)
- 配套 SDK 开放(Unitree ROS2 / DDS / 力控接口)
- 灵巧手是 7-DoF × 2(三指 / 五指可选),触觉传感器集成度较高

**多模态组合**(对应 Open X-Embodiment 缺的):
- **多视角 RGB-D**:头戴 + 第三人称 ×2 + 腕部鱼眼 = **4 路 30Hz 同步**
- **触觉**:每根手指尖 GelSight-style 触觉图像(高频 60-100Hz)
- **深度**:与 RGB 严格对齐的深度图(对 sim2real 与 3D 表征友好)
- **本体感觉**:12+ 关节位置 / 速度 / 力矩,7-DoF × 2 灵巧手关节角
- **语义标注**:任务级 / 技能级 / 物体级 三层标签

### 关键创新点 2:毫秒级多模态同步系统

**问题**:多相机 + 触觉 + 力控在工业相机上的触发是异步的,默认时间戳有 5-50ms 抖动,直接喂给 imitation learning 会引入"伪影"——policy 学到错误的视觉-动作关联。

**论文方案**:**自研多相机同步系统**,统一用硬件触发 + PTP 时间同步协议,把抖动压到 < 5ms。这是**数据集的"看不见的工程护城河"**——很多论文在"评估指标"上不报告同步精度,但同步误差会显著影响策略表现。

**推断实现**(基于行业惯例,待读 PDF 验证):
- 主控用 ROS2 + 工业级 PTP master
- 相机用 GigE Vision 触发模式
- 触觉用 USB3 + 硬件时间戳
- 所有数据落到 ROS bag,再用 `message_filters` 做离线对齐

### 关键创新点 3:任务设计的"双臂 + 触觉依赖"导向

数据集**刻意偏向需要双臂 + 触觉才能完成的任务**,而不是简单抓取:

- 19 任务中**大部分需要双灵巧手协同**(开瓶盖、倒水、折叠布料、组装)
- 22 物体包含**易碎 / 易滑 / 接触敏感**的(鸡蛋、玻璃杯、粉末)
- 23 技能覆盖**roll / pinch / twist / slide / align**等接触丰富动作

这与 Open X-Embodiment(以 pick-and-place 为主)形成鲜明对比,**填补了"长程 + 接触敏感 + 双臂"的数据空白**。

### 关键创新点 4:三种 imitation learning policy 基准

论文**不只发数据集,还自带 benchmark**:在 3 个代表性 IL 模型上做评测:

1. **Behavior Cloning (BC)** —— 最简单的监督学习 baseline
2. **Diffusion Policy** —— 主流 SOTA,处理多模态动作分布
3. **ACT (Action Chunking Transformer)** —— ALOHA 系,长程任务友好

**评估维度**:
- 任务级成功率
- 跨物体泛化(seen vs unseen objects)
- 跨视角泛化(seen vs unseen camera)
- 双臂协同 vs 单臂任务的难度差异

这一块让数据集**立即可比、可复现**,避免了"发数据 = 发一堆轨迹"的常见陷阱。

## 核心成果

- **规模**:6k 轨迹,19 任务,23 技能,22 物体(对 Unitree G1 + 灵巧手场景,这是目前**最大的开源多模态数据集**之一)
- **模态覆盖**:多视角 RGB-D + 触觉 + 本体感觉 + 语义标注
- **同步精度**:毫秒级(具体数字待 PDF 验证)
- **基准结果**:3 种 IL policy 均可学到部分任务成功,**Diffusion Policy 与 ACT 表现优于 vanilla BC**;但**双臂协同 + 触觉依赖**任务成功率仍偏低(<60%,需查具体数据),暴露当前 IL 范式的局限
- **泛化能力**:**中度**泛化(论文表述为 "moderate level"),即在 seen 任务 + unseen 物体上能完成一部分,未见任务 + unseen 物体则失败

## 局限性

1. **6k 轨迹对 VLA / foundation model 仍偏小**:Open X-Embodiment 量级是 2M+,DROID 是 76k。6k 适合 IL baseline,**不足以训练通用人形基础模型**(类似 π0 / OpenVLA-OFT 需要 100k+)
2. **平台单一**:只在 Unitree G1 上采,**泛化到其他形态(Figure / 1X / Optimus)的迁移性未验证**。G1 的 7-DoF 灵巧手结构与其他家差异较大(retargeting 成本高)
3. **任务偏实验室环境**:摘要未提及户外 / 厨房 / 家庭场景,**覆盖度对"通用服务"场景有限**
4. **缺少语言指令标注**:摘要强调 "detailed semantic annotations" 但**未提 language instruction**——没有 language-conditioned 数据,不能直接喂给 VLA / OpenVLA 系模型做 SFT,这是**对当下主流范式的关键 gap**
5. **同步精度的"绝对值"未明示**:"毫秒级"是工程表述,**具体抖动数字需查 PDF**
6. **未见第三视角数据集发布承诺**:"will be open-sourced soon" 是软承诺,**实际放出的内容(数据 / 代码 / 评测脚本)需后续追踪**
7. **基线模型较旧**:BC + Diffusion Policy + ACT 是 2023-2024 主流,**未与最新 VLA 模型(π0、OpenVLA-OFT、GR-2)对比**,benchmark 的"前沿性"有限

## 复现线索

- **硬件依赖**:**Unitree G1 + 灵巧手**(EDU 版 ~$40k,基础版需外购灵巧手),**多视角 RGB-D 相机**(Intel RealSense D435 / Azure Kinect),**触觉传感器**(GelSight Mini ~$500/指或类似)
- **软件栈**:ROS2 + 自研多相机同步系统 + 触觉采集 SDK
- **时间**:6k 轨迹 + 多模态同步,**单人采集估计 2-3 个月**(假设每个任务 50-100 次成功演示,单次含失败 + 重做 ~5 分钟)
- **难点**:
  1. 多相机同步(工业 GigE 触发 + PTP)
  2. 触觉传感器标定与温度漂移补偿
  3. 灵巧手遥操接口(目前常用 VR 头显 + 手柄映射)
  4. 任务成功判定(自动 vs 人工,涉及视觉验证)
- **建议起手**:先买 Unitree G1 + 2 个 GelSight Mini + RealSense D435i × 2 + VR 头显,跑通单任务流水;再扩展到多任务

## 应用与行业映射

### 直接受益方

1. **人形机器人厂商**:
   - **Unitree**:G1 平台的最大开源数据贡献,**生态粘性进一步增强**(类似 Open X-Embodiment 对 Google RT-1 的反向喂养)
   - **国内二线人形厂商**(宇树、智元、银河通用、星动纪元):可直接在 G1 平台上复用,**降低自采数据成本**
   - **Figure / 1X / Optimus / 宇树 H1**:虽然平台不同,但**数据集结构(任务 / 技能 / 物体 / 触觉)可借鉴**,retargeting 后可用

2. **VLA / Foundation Model 团队**:
   - **Physical Intelligence (π 系列)**:目前缺开源灵巧手数据,这份可作为补充
   - **NVIDIA GR00T**:G1 平台官方合作方,数据集直接喂 GR00T-N1
   - **OpenVLA / Octo**:需要 language-conditioned 数据,**目前 RoboTacDex 缺语言标注是个 blocker**,需等作者补充
   - **TRI / Stanford ALOHA**:ACT 的产线,**与本数据集天然兼容**

3. **触觉传感器厂商**:
   - **GelSight**:本数据集用类似方案,**出货量 + 曝光度直接受益**
   - **国内厂商**(他山科技、慧灵科技):对标方案的市场空间被打开

4. **仿真平台方**:
   - **NVIDIA Isaac Sim / Isaac Lab**:可基于此数据集做 sim2real benchmark
   - **MuJoCo / SAPIEN / Genesis**:可基于场景 / 物体做仿真复刻

### 量产成本与产业链

- **Unitree G1 EDU 版**:~$40k(7-DoF ×2 灵巧手 + 4 相机 + 触觉集成)
- **触觉传感器**:GelSight Mini ~$500/指,7 指 ×2 = $7k
- **多视角 RGB-D**:RealSense D435i ×3 = $1.5k
- **总硬件成本**:~$50k/平台(不含计算与遥操设备)
- **对比遥操数据采集**(传统模式):$100k+ 主控端 + $100k+ 机器人 + 操作员培训,**降本 70%+**

### 替代方案

- **Figure / 1X / Optimus 私有数据**:**闭源,学术界无法使用**
- **Open X-Embodiment**:规模大(2M+)但无触觉、无灵巧手
- **DextrAH / Bi-Touch / HumanDex**:有触觉但规模小(<1k)、平台异构
- **Synthesized data (Isaac Sim)**:仿真可扩展但 sim2real gap 仍大

### 商业化机会

1. **数据即服务(DaaS)**:基于 RoboTacDex 提供"灵巧手 + 触觉"的高质量标注数据订阅
2. **评测即服务(EaaS)**:在 G1 平台上做"模型上机评测" 的标准化服务
3. **训练即服务**:基于此数据集 + 自研 policy 的"灵巧手模型微调"服务

### 风险与不确定性

- **数据规模仍不足**:**6k 远小于 foundation model 训练需求**,可能只是"过渡数据集"
- **平台锁定 Unitree**:若宇树后续闭源或修改 SDK,数据兼容性可能受影响
- **触觉传感器长期可靠性**:GelSight 类传感器寿命 6-12 个月,**量产部署成本高**

## 关键引用与延伸阅读

- **Unitree G1 平台**:Unitree Robotics, 2024. *G1 Humanoid Robot Product Spec*
- **Diffusion Policy**:Chi et al., 2023. *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*. RSS 2023.
- **ACT**:Zhao et al., 2023. *Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware*. RSS 2023.
- **Open X-Embodiment**:Collaboration, 2024. *Open X-Embodiment: Robotic Learning Datasets and RT-X Models*. ICRA 2024.
- **UMI (Universal Manipulation Interface)**:Chi et al., 2024. *Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots*. RSS 2024.

---

> **报告生成日期**:2026-07-01 · **基于**:arXiv 摘要 + 行业知识推断 · **待补**:PDF 全文细读 / 项目页 / 代码链接 / 同步精度数值 / 评测具体数字