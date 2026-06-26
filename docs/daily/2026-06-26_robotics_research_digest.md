# 机器人研究每日摘要 · 2026-06-26

> 自动生成,共 88 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (4 篇)

### 1. ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models

- **arXiv**: [2606.27079v1](https://arxiv.org/abs/2606.27079v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27079v1)
- **作者**: Mingyang Lyu, Yinqian Sun, Yiyang Jia et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: In embodied intelligence, safety is a prerequisite for reliable robot deployment in the physical world. Current vision-language-action (VLA) models continue to advance toward general-purpose task capability, yet their embodied safety limits remain poorly understood. To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes saf…

### 2. Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)

- **arXiv**: [2606.27163v1](https://arxiv.org/abs/2606.27163v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27163v1)
- **作者**: Ilia Larchenko
- **发表**: 2026-06-25  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding. The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final. It improves a vision-language-action (VLA) policy with a reinforcement-learning loop. The policy is its own value function: the same network that predic…

### 3. RouterVLA: Turning Smoke Tests into Supervision for Heterogeneous VLA Selection

- **arXiv**: [2606.27355v1](https://arxiv.org/abs/2606.27355v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27355v1)
- **作者**: Xingyu Ren, Chugang Yi, Ge Ma et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We study whether pre-deployment evaluation rollouts can be reused to supervise policy selection. Robot teams routinely smoke test candidate vision-language-action (VLA) policies, then compress those trials into a global winner. RouterVLA evaluates this idea with outcome-disjoint cross-fitting: recorded probes build a profile for each frozen expert, and a se…

### 4. Robots Need More than VLA and World Models

- **arXiv**: [2606.06556v1](https://arxiv.org/abs/2606.06556v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06556v1)
- **作者**: Elis Karcini, Faisal Mehrban, Quang Nguyen et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation. In this position paper, we argue that this framing is incomplete. The central bottleneck is not only policy learning, but the absence of mechanisms that convert the…

## 🌐 具身智能 / 机器人基础模型 (7 篇)

### 1. ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM

- **arXiv**: [2606.00307v1](https://arxiv.org/abs/2606.00307v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00307v1)
- **作者**: Yuhao Zhang, Yifu Tao, Frank Dellaert et al.
- **发表**: 2026-05-29  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Recent works have explored unifying SLAM with geometric foundation models (GFMs). However, directly using GFM predictions for tracking is highly sensitive to model capability and uncertainty, as geometric inaccuracies in the predictions can adversely affect pose estimation. To address this limitation, we present a decoupled framework that integrates classic…

### 2. SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

- **arXiv**: [2606.25497v1](https://arxiv.org/abs/2606.25497v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.25497v1)
- **作者**: Hao Su, Yuehao Huang, Yukai Ma et al.
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Object-Goal Navigation (ObjNav) requires embodied agents to autonomously locate specified targets using only egocentric visual observations. Existing monolithic methods struggle with long-horizon reasoning and generalize poorly to novel environments. To address these limitations, we propose SAGE-Nav, a novel hierarchical framework that integrates the reason…

### 3. See-and-Reach: Precise Vision-Language Navigation for UAVs within the Field of View

- **arXiv**: [2606.20045v1](https://arxiv.org/abs/2606.20045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.20045v1)
- **作者**: Fanfu Xue, En Yu, Yantian Shen et al.
- **发表**: 2026-06-18  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: UAV Vision-Language Navigation (UAV-VLN) is typically formulated as a holistic search-and-reach problem, where long-range target discovery and final target approach are optimized and evaluated jointly. This formulation makes it difficult to assess a critical capability of aerial embodied agents, namely whether a UAV can accurately ground a visible target an…

### 4. Advancing DialNav through Automatic Embodied Dialog Augmentation

- **arXiv**: [2606.19948v1](https://arxiv.org/abs/2606.19948v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.19948v1)
- **作者**: Leekyeung Han, Sangwon Jung, Hyunji Min et al.
- **发表**: 2026-06-18  ·  **类别**: cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: For embodied agents capable of physical interaction, the capability to create and understand dialog is crucial to ensure both safety and effectiveness. While DialNav~\cite{han2025dialnav} provides a framework for holistic evaluation of the dialog--execution loop in photorealistic indoor navigation, its performance remains limited by a critical scarcity of t…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming

- **arXiv**: [2606.24245v2](https://arxiv.org/abs/2606.24245v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.24245v2)
- **作者**: Pingchuan Ma, Zhaoyu Wang, Zimo Ji et al.
- **发表**: 2026-06-23  ·  **类别**: cs.SE, cs.AI, cs.CR
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large language model (LLM) agents increasingly automate complex tasks by integrating language models with external tools and environments. However, their autonomy poses significant safety risks: agents may execute destructive commands, leak sensitive data, or violate domain constraints. Existing safety approaches face a fundamental tradeoff: hand-crafted ru…

### 7. IOI: Decoupling Kinematics and Physics for Interactive World Models

- **arXiv**: [2606.23296v1](https://arxiv.org/abs/2606.23296v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.23296v1)
- **作者**: Chengyu Bai, Peidong Jia, Tiecheng Guo et al.
- **发表**: 2026-06-22  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Developing generalist embodied agents requires interactive environments providing visually realistic feedback and accurate action-conditioned dynamics. Interactive world models address this by simulating such complex dynamics. However, purely data-driven methods struggle to ensure precise control alignment and physically plausible visual feedback due to a l…

## 🦵 人形 / 足式机器人 (24 篇)

### 1. A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots

- **arXiv**: [2606.26425v1](https://arxiv.org/abs/2606.26425v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26425v1)
- **作者**: Duncan William Calvert
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Humanoid robots could take on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole body motion, perception, contact, and operator supervision. This thesis presents a robot-local, runtime-editable behavior authoring and runtime system. Our system strives to…

### 2. CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation

- **arXiv**: [2606.23680v1](https://arxiv.org/abs/2606.23680v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.23680v1)
- **作者**: Sikai Li, Shuning Li, Zhenyu Wei et al.
- **发表**: 2026-06-22  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexter…

### 3. HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation

- **arXiv**: [2606.27239v1](https://arxiv.org/abs/2606.27239v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27239v1)
- **作者**: Hongwu Wang, Chenhao Yu, Youhao Hu et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors that require coordinated perception, locomotion, and manipulation. Existing data-collection methods largely rely on robot teleoperation, which is constrained by hardware accessibility, operator expertise, and limited efficiency. Inspired by t…

### 4. StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots

- **arXiv**: [2606.25765v1](https://arxiv.org/abs/2606.25765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.25765v1)
- **作者**: Xincheng Tang, Youhan Xie, Zhengjie Shu et al.
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a…

### 5. MPC-Injection: Biasing Off-Policy Locomotion RL Toward Controller-Induced Behavior Basins

- **arXiv**: [2606.26392v1](https://arxiv.org/abs/2606.26392v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26392v1)
- **作者**: Roy Xing, Seyoung Ree, Brian Plancher
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) for locomotion frequently converges to locally optimal but undeployable behaviors, such as vibrating limbs or scooting on the torso, that maximize return without producing a usable gait. We present MPC-Injection, a low-overhead method that steers RL toward a designer-preferred gait by inserting transitions into the replay buffer…

### 6. FT-WBC: Learning Fault-Tolerant Whole-Body Control for Legged Loco-Manipulation

- **arXiv**: [2606.24466v1](https://arxiv.org/abs/2606.24466v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.24466v1)
- **作者**: Yudong Zhong, Pengfei Mai, Sikai Guo et al.
- **发表**: 2026-06-23  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Legged manipulators combine the mobility of legged platforms with the manipulation capability of robotic arms. However, arm-induced Center-of-Mass shifts and dynamic disturbances make the system more prone to instability under actuator failures, potentially leading to falls, task failures, or safety risks. Existing fault-tolerant control methods mainly focu…

### 7. PressMimic: Pressure-Guided Motion Capture and Control for Humanoid Robot Imitation

- **arXiv**: [2606.26741v1](https://arxiv.org/abs/2606.26741v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26741v1)
- **作者**: Yi Lu, Shenghao Ren, Tianyu Xiong et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid motion imitation requires not only accurate perception of human kinematics but also faithful reproduction of physical interactions with the environment. However, existing pipelines rely primarily on vision-based motion capture and kinematic imitation, largely ignoring contact dynamics, leading to artifacts such as foot sliding, floor penetration, a…

### 8. Self Capacitive Tactile Sensor System designed for Companion Robots

- **arXiv**: [2606.25348v1](https://arxiv.org/abs/2606.25348v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.25348v1)
- **作者**: Mohsin Ali, Hidenobu Sumioka, Shuhei Ikemoto
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Tactile sensing is essential for humanoid robots to achieve safe physical interaction, dexterous manipulation, and truly human-like responsiveness. However, the design of such systems remains challenging. Conventional approaches often suffer from complex multilayer structures, intricate wiring, high cost, and poor scalability, making it difficult to realize…

### 9. DynaMOMA: Instantaneous Prediction of Grasp Poses for Mobile Manipulation of Dynamic Objects

- **arXiv**: [2606.25295v1](https://arxiv.org/abs/2606.25295v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.25295v1)
- **作者**: Zhinan Yu, Junyan Xu, Jiazhao Zhang et al.
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Mobile manipulation is a fundamental robotics task and has advanced rapidly in recent years, enabling robots to navigate, reach, and interact with objects in complex environments. However, mobile manipulation of dynamic objects remains highly challenging, as robots must coordinate the mobile base and arm while adapting to continuously evolving target poses.…

### 10. ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

- **arXiv**: [2606.17011v1](https://arxiv.org/abs/2606.17011v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17011v1)
- **作者**: Wei Xiao, Weiliang Tang, Yuying Ge et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Human interventions provide crucial corrective signals for post-training Vision-Language-Action (VLA) models. However, enabling seamless humanoid interventions is a formidable systems challenge due to complex whole-body kinematics and dexterous-hand control. Consequently, the collected intervention trajectories are often suboptimal, and methods that rely on…

## 🦾 操控 / 灵巧手 / 抓取 (34 篇)

### 1. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

- **arXiv**: [2606.17598v1](https://arxiv.org/abs/2606.17598v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17598v1)
- **作者**: Xingyuming Liu, Ruichun Ma, Heyu Guo et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present…

### 2. Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data

- **arXiv**: [2606.22136v2](https://arxiv.org/abs/2606.22136v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.22136v2)
- **作者**: Yangtao Chen, Zixuan Chen, Peiyang Wang et al.
- **发表**: 2026-06-20  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Scaling dexterous manipulation requires generalization across objects, scenes, and tasks, yet existing data sources face a trade-off between scale and scene/embodiment alignment: teleoperation data is well aligned with robot deployment but expensive to collect; simulation is scalable but limited by the sim-to-real gap; and real egocentric videos scale effec…

### 3. VibeAct: Vibration to Actions for Contact-Rich Reactive Robot Dexterity

- **arXiv**: [2606.27344v1](https://arxiv.org/abs/2606.27344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27344v1)
- **作者**: Yuemin Mao, Uksang Yoo, Jean Oh et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation depends on contact events that are fast, local, and often visually occluded. Piezoelectric microphones offer a compact and high-bandwidth way to sense these interactions, but the resulting vibro-acoustic signals are difficult to simulate faithfully enough for end-to-end sim-to-real policy learning on dexterous robot hands. We propose…

### 4. Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation

- **arXiv**: [2606.22471v1](https://arxiv.org/abs/2606.22471v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.22471v1)
- **作者**: Zechu Li, Yufeng Jin, Puze Liu et al.
- **发表**: 2026-06-21  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: A key bottleneck in training generalist policies for bimanual dexterous manipulation is the lack of large-scale, high-quality datasets. Synthetic data generation in simulation provides a scalable alternative to human video demonstrations by overcoming challenges such as morphology mismatch, missing physical interactions, and the generation of robot actions.…

### 5. Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?

- **arXiv**: [2606.26428v1](https://arxiv.org/abs/2606.26428v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26428v1)
- **作者**: Tyler Ga Wei Lum, Kushal Kedia, C. Karen Liu et al.
- **发表**: 2026-06-24  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Multi-fingered robots promise the speed and dexterity of human hands, yet challenging problems such as precise assembly have remained out of reach. These tasks are contact-rich, making data collection for imitation learning difficult, and sparse-reward, making direct exploration with reinforcement learning (RL) intractable. Consequently, prior work has made…

### 6. DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy

- **arXiv**: [2606.23431v1](https://arxiv.org/abs/2606.23431v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.23431v1)
- **作者**: Haichao Liu, Yuyao Jiang, Hyunsun Park et al.
- **发表**: 2026-06-22  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Fine-grained, bimanual dexterous manipulation remains a foundational challenge in robotics. Traditional teleoperation systems often fail in contact-rich tasks because embodiment gaps hinder accurate kinematic mapping, while tactile and force feedback remain absent. Consequently, data collection efficiency for high-precision tasks remains prohibitively low.…

### 7. PAMAE: Phase-Aware-MoE Action Experts Towards Reliable Flow-Matching Vision-Language-Action Policies

- **arXiv**: [2606.27144v1](https://arxiv.org/abs/2606.27144v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27144v1)
- **作者**: Jiayu Yang, Tao Yang, Xiang Chang et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Reliable action generation for multi-stage robotic manipulation remains challenging for Vision-Language-Action (VLA) models. While existing flow-matching VLA policies offer strong multimodal grounding and generalization, they typically employ a single shared action expert, limiting their ability to capture phase-specific control patterns across distinct exe…

### 8. Steering Autoregressive Vision-Language-Action Policies via Action Token Intervention

- **arXiv**: [2606.15021v1](https://arxiv.org/abs/2606.15021v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15021v1)
- **作者**: Jason Chan, Jonathan C. Kao
- **发表**: 2026-06-12  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We present Token Steering (TS), a method for dynamically steering trajectories generated by an autoregressive vision-language-action (VLA) model through direct intervention in the action-token space. TS injects low-dimensional user inputs into the model's native action-token representation, allowing users to influence trajectory generation without modifying…

### 9. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 10. LA4VLA: Learning to Act without Seeing via Language-Action Pretraining

- **arXiv**: [2606.27295v1](https://arxiv.org/abs/2606.27295v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27295v1)
- **作者**: Tao Lin, Yuxin Du, Yiran Mao et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models are commonly pretrained on robot demonstrations by jointly mapping visual observations and language instructions to actions. However, dense visual-action supervision can dominate the comparatively sparse language-action signal. As a result, policies may rely on visual shortcuts rather than learn how language conditions ac…

## 🎓 模仿学习 / 强化学习 (12 篇)

### 1. IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control

- **arXiv**: [2606.26575v1](https://arxiv.org/abs/2606.26575v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26575v1)
- **作者**: Chenlong Liu, Zhuohui Zhang, Xinyan Chen et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Complex multi-agent control tasks remain challenging for traditional rule-based and model-based approaches, motivating the adoption of learning-based methods. However, learning-based methods often struggle with sim-to-real transfer because they rely on accurate dynamics modeling or system identification and learn policies in low-level control spaces that ar…

### 2. MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM

- **arXiv**: [2606.19874v1](https://arxiv.org/abs/2606.19874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.19874v1)
- **作者**: Fan Zhu, Ziyu Chen, Peichen Liu et al.
- **发表**: 2026-06-18  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: 3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to in…

### 3. RobOralScan: Learning Active Intraoral Scanning for Robotic Dental Reconstruction

- **arXiv**: [2606.26955v1](https://arxiv.org/abs/2606.26955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26955v1)
- **作者**: Jinhyung Lee, Haeun Yun, Siwon Kim et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Intraoral scanning is widely used for digital optical impressions in prosthodontic, implant, and orthodontic treatment, but full-arch and long-span scanning remain labor-intensive tasks with limited automation. In the confined oral cavity, operators must continuously adjust scanner motion while accumulating narrow field-of-view observations, making reconstr…

### 4. Cross-View Variance Correlation in Path-Traced Stereo:A Hidden Shortcut in Synthetic Training Data

- **arXiv**: [2606.25483v1](https://arxiv.org/abs/2606.25483v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.25483v1)
- **作者**: Po-Ting Lin
- **发表**: 2026-06-24  ·  **类别**: cs.CV, cs.GR
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Path-traced synthetic stereo data underlie a large fraction of modern disparity-estimation training pipelines. We report a previously unrecognised property of such data: while the Monte Carlo (MC) noise streams of the two cameras are statistically independent, the underlying \emph{variance fields} -- deterministic per-pixel functions of the rendering integr…

### 5. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 6. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 7. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 8. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 9. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 10. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (7 篇)

### 1. Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study

- **arXiv**: [2605.03678v1](https://arxiv.org/abs/2605.03678v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.03678v1)
- **作者**: Prasoon Kumar, Akshay Deepak, Sandeep Kumar
- **发表**: 2026-05-05  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reliable localization in GPS-denied, visually degraded environments is critical for autonomous UAV opera- tions. This paper presents a systematic comparative evaluation of five V-SLAM systems ORB-SLAM3, DPVO, DROID-SLAM, DUSt3R, and MASt3R spanning classical, deep learning, recurrent, and Vision Transformer (ViT) paradigms. Experiments are conducted on cura…

### 2. FusionCore: A 23-State Unscented Kalman Filter for IMU, Wheel Encoder, GPS, and Visual SLAM Fusion in ROS 2

- **arXiv**: [2605.25239v1](https://arxiv.org/abs/2605.25239v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.25239v1)
- **作者**: Manan Kharwar
- **发表**: 2026-05-24  ·  **类别**: cs.RO, eess.SP
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: We present FusionCore, an open-source ROS 2 sensor fusion package that fuses IMU, wheel encoder odometry, GPS, and Visual SLAM pose into a single 100 Hz odometry stream using a 23-state Unscented Kalman Filter (UKF). The 23rd state is an online estimate of the wheel encoder's systematic yaw rate bias, identified through GPS heading cross-covariance and subt…

### 3. Passage-Aware Structural Mapping for RGB-D Visual SLAM

- **arXiv**: [2604.24707v1](https://arxiv.org/abs/2604.24707v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.24707v1)
- **作者**: Ali Tourani, Miguel Fernandez-Cortizas, Saad Ejaz et al.
- **发表**: 2026-04-27  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Doorways and passages are critical structural elements for indoor robot navigation, yet they remain underexplored in modern Visual SLAM (VSLAM) frameworks. This paper presents a passage-aware structural mapping approach for RGB-D VSLAM that detects doors and traversable openings by jointly fusing geometric, semantic, and topological cues. Doors are modeled…

### 4. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 5. WildPose: A Unified Framework for Robust Pose Estimation in the Wild

- **arXiv**: [2605.12774v1](https://arxiv.org/abs/2605.12774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.12774v1)
- **作者**: Jianhao Zheng, Liyuan Zhu, Zihan Zhu et al.
- **发表**: 2026-05-12  ·  **类别**: cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Estimating camera pose in dynamic environments is a critical challenge, as most visual SLAM and SfM methods assume static scenes. While recent dynamic-aware methods exist, they are often not unified: semantic-based approaches are brittle, per-sequence optimization methods fail on short sequences, and other learned models may degrade on static-only scenes. W…

### 6. Hardware-Aware Neural Feature Extraction for Resource-Constrained Devices

- **arXiv**: [2605.04282v2](https://arxiv.org/abs/2605.04282v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.04282v2)
- **作者**: Francesco Tosini, Simone Pedroni, Christian Veronesi et al.
- **发表**: 2026-05-05  ·  **类别**: cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Visual SLAM is a core component of spatial computing systems, yet deploying learned local feature extractors on microcontroller-class hardware remains challenging due to memory, bandwidth, and quantization constraints. While modern neural descriptors provide strong robustness, their practical adoption is often hindered by system-level bottlenecks that are n…

### 7. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots](https://arxiv.org/abs/2606.26425v1) — score 20
2. [CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.23680v1) — score 19
3. [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](https://arxiv.org/abs/2606.17598v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
