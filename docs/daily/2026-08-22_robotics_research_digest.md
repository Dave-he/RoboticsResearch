# 机器人研究每日摘要 · 2026-08-22

> 自动生成,共 86 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms

- **arXiv**: [2608.20111v1](https://arxiv.org/abs/2608.20111v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20111v1)
- **作者**: Yanchen Guan, Xingcheng Liu, Bin Rao et al.
- **发表**: 2026-08-20  ·  **类别**: cs.RO, cs.ET
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols. This survey reviews this transition across behavior cloning, conditional imitation learning, privileged distillation, BEV and vectorized p…

### 2. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 3. OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation

- **arXiv**: [2608.19589v1](https://arxiv.org/abs/2608.19589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19589v1)
- **作者**: Jiaqi Wang, Zhou Fang, Qiongfeng Shi et al.
- **发表**: 2026-08-20  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Pretrained Vision-Language-Action models provide a strong foundation for robot learning, but sequentially adapting them to diverse skills can perturb the representations and velocity mappings used by previous skills, leading to catastrophic forgetting. Architecture-based approaches improve retention by isolating skills but lead to increased inference footpr…

### 4. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 5. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (8 篇)

### 1. SafeBranch: Branch-Pair Safety Alignment for Embodied Agents

- **arXiv**: [2608.19729v1](https://arxiv.org/abs/2608.19729v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19729v1)
- **作者**: Hyunse Lee, Jiwoo Jeong, Haneul Lee et al.
- **发表**: 2026-08-20  ·  **类别**: cs.AI, cs.CV, cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a traj…

### 2. If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation

- **arXiv**: [2608.17318v1](https://arxiv.org/abs/2608.17318v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.17318v1)
- **作者**: Seoyoung Lee, Neel P. Bhatt, Pranay Samineni et al.
- **发表**: 2026-08-18  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Vision-language navigation agents are often evaluated on their ability to follow route-like instructions toward a fixed goal. Yet, real navigation instructions often depend on observed states of the environment: if a condition holds, then follow one path, otherwise take another. Such instructions require an agent to evaluate scene evidence, select the corre…

### 3. Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation

- **arXiv**: [2608.16843v1](https://arxiv.org/abs/2608.16843v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16843v1)
- **作者**: Jiawei Liu, Jiacheng Guo, Tian Zhang et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Foundation models are increasingly used for perception, reasoning, planning, and action generation in embodied agents, creating security risks that can propagate from digital inputs to physical behavior. Existing surveys often organize threats by mechanisms such as jailbreaks, prompt injection, backdoors, poisoning, or adversarial examples, but these catego…

### 4. Neurosymbolic Embodied Agents

- **arXiv**: [2608.16794v2](https://arxiv.org/abs/2608.16794v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16794v2)
- **作者**: Mohammad Albinhassan, Yuming Feng, Alessandra Russo et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Language and vision-language models generate plausible embodied plans but do not guarantee executability, as their outputs can violate environment dynamics or act on incorrectly grounded entities. We present a neurosymbolic agent that factors long-horizon household tasks into task-directed visual exploration and constrained symbolic planning. In the first p…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 7. GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting

- **arXiv**: [2608.17535v1](https://arxiv.org/abs/2608.17535v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.17535v1)
- **作者**: Qijian Tian, Zimeng Wu, Xuhong Wang et al.
- **发表**: 2026-08-18  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Simultaneously reconstructing and understanding 3D environments is essential for embodied agents. Toward this goal, feed-forward semantic 3D Gaussian Splatting (3DGS) efficiently constructs semantic scene representations from sparse multi-view observations. However, existing methods lack explicit instance discrimination and mainly support category- or phras…

### 8. Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence

- **arXiv**: [2608.16590v1](https://arxiv.org/abs/2608.16590v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16590v1)
- **作者**: Xin Ding, Liang Mi, Mingzhe Huang et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents are increasingly used to close the gap left by end-to-end policy models. Yet the agentic path has not realized closed-loop learning in physical execution: existing harnesses remain largely open-loop, following fixed skills during rollout and reflecting only after an episode completes. Such post-hoc reflection cannot govern execution as it un…

## 🦵 人形 / 足式机器人 (27 篇)

### 1. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 2. Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking

- **arXiv**: [2608.20087v1](https://arxiv.org/abs/2608.20087v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20087v1)
- **作者**: Tao Huang, Ruofei Liu, Xuchen Tang et al.
- **发表**: 2026-08-20  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from bro…

### 3. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 4. Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning

- **arXiv**: [2608.17320v1](https://arxiv.org/abs/2608.17320v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.17320v1)
- **作者**: Ayumu Iwata, Kento Kawaharazuka, Keita Yoneda et al.
- **发表**: 2026-08-18  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Brachiation is a form of locomotion in which primates move primarily using their arms, enabling traversal in environments without footholds. However, this motion requires highly coordinated whole-body movement and precise timing control for bar grasping and release. As a result, achieving robust behavior on life-sized robotic platforms remains challenging.…

### 5. HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL

- **arXiv**: [2608.16837v1](https://arxiv.org/abs/2608.16837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16837v1)
- **作者**: Langzhe Gu, Chengkai Hou, Meng Li et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to…

### 6. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2608.03387v2](https://arxiv.org/abs/2608.03387v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03387v2)
- **作者**: Shuliang He, Shuai Wang, Bo Yue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual…

### 7. Throwing a Tight Spiral American Football by a Humanoid Robot

- **arXiv**: [2608.16642v1](https://arxiv.org/abs/2608.16642v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16642v1)
- **作者**: Zaid Mahboob, Bowen Weng
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Accurate throwing of the American football requires precise regulation of release conditions, where coupled linear and angular momentum determine flight stability and targeting accuracy. While prior work on robotic object throwing has largely focused on generating dynamically feasible release velocities using open-gripper paradigms, explicit control of spin…

### 8. DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation

- **arXiv**: [2608.20114v1](https://arxiv.org/abs/2608.20114v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20114v1)
- **作者**: Siyuan Ma, Boshi Zhang, Yutian Zhang et al.
- **发表**: 2026-08-20  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Mobile manipulation requires a robot to predict how locomotion and arm motion jointly alter future observations and control. Existing world-action models, developed largely for fixed-base platforms, do not explicitly distinguish camera ego-motion from base and arm actions. Here we introduce DECOWAM, a whole-body world-action model that separates these facto…

### 9. Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control

- **arXiv**: [2608.19443v1](https://arxiv.org/abs/2608.19443v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19443v1)
- **作者**: Chaoyi Pan, Zeji Yi, John Zhang et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Thanks to its parallelizability and flexibility, sampling-based Model Predictive Control (MPC) has become widely popular for controlling real-world robotic systems. However, for high-dimensional and open-loop unstable dynamical systems, the required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor s…

### 10. FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences

- **arXiv**: [2608.17027v1](https://arxiv.org/abs/2608.17027v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.17027v1)
- **作者**: Omar Rayyan, Zhi Li, Max Argus et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring tha…

## 🦾 操控 / 灵巧手 / 抓取 (28 篇)

### 1. LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories

- **arXiv**: [2608.18618v1](https://arxiv.org/abs/2608.18618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18618v1)
- **作者**: Zhipeng Tang, Sihang Chen, Sha Zhang et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Autonomous laboratories hold great promise for accelerating scientific discovery. To achieve this vision, robots are supposed to dexterously manipulate diverse labware and instruments and execute long-horizon, state-dependent experimental procedures. Yet existing benchmarks do not jointly capture dexterous hand use, real-world laboratory interactions, and m…

### 2. AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning

- **arXiv**: [2608.14028v1](https://arxiv.org/abs/2608.14028v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.14028v1)
- **作者**: Zhiyue Zhao, Jingyi Wu, Hairuo Liu et al.
- **发表**: 2026-08-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation is a fundamental capability for embodied intelligence, but scaling it remains difficult because robot demonstrations are expensive to collect and action spaces vary across embodiments. Policies trained on heterogeneous data can also entangle task-relevant visual cues with embodiment-specific appearance, limiting cross-embodiment gener…

### 3. $τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885v1](https://arxiv.org/abs/2608.16885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16885v1)
- **作者**: Xiaowei Cai, Yunuo Cai, Bingao Chen et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_…

### 4. ReForce: Learning Force-aware Retargeting for Dexterous Manipulation

- **arXiv**: [2608.15560v1](https://arxiv.org/abs/2608.15560v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.15560v1)
- **作者**: Yuhang Wu, Lingqi Zeng, Changwei Jing et al.
- **发表**: 2026-08-16  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Human demonstrations offer a scalable data source for dexterous manipulation, but transferring them to robot actions remains challenging due to the embodiment gap. Today's retargeting is mostly kinematic, yet manipulation is decided by force, which governs how the hand interacts with the object and how the object moves. In this paper, we present ReForce, a…

### 5. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 6. ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning

- **arXiv**: [2608.16572v1](https://arxiv.org/abs/2608.16572v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16572v1)
- **作者**: Fucai Zhu, Yanhou Lai, Paul Maestre et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Learning from demonstration is a promising approach for dexterous manipulation, but collecting high-quality contact-critical demonstrations remains difficult with low-cost teleoperation hardware. We present ViHaTeleop, a lightweight (0.7 kg), low-cost (\$550) visual-haptic teleoperation system with SLAM-based wrist tracking, camera-based hand tracking, and…

### 7. C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video

- **arXiv**: [2608.07045v1](https://arxiv.org/abs/2608.07045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.07045v1)
- **作者**: Jie Ren, Zhehao Jiang, Yinhong Yang et al.
- **发表**: 2026-08-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: High-quality demonstrations for dexterous robot manipulation are costly and difficult to collect, whereas monocular human videos provide a scalable source of diverse manipulation behaviors. However, transferring such demonstrations to dexterous robots remains challenging: monocular hand-object interaction (HOI) reconstruction often produces temporally unsta…

### 8. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 9. PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents

- **arXiv**: [2608.17129v1](https://arxiv.org/abs/2608.17129v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.17129v1)
- **作者**: Vineet Bhat, Siyi Chen, Alex Zook et al.
- **发表**: 2026-08-17  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-language Models (VLMs) excel at 2D grounding, spatial reasoning and agentic tool-based planning in static scenes. However, consider asking a home robot "Is my medication still in the cabinet?" The answer may be physically hidden behind a row of containers that must first be moved aside. Answering such questions in real-world cluttered environments re…

### 10. Breaking Planner Integrity Boundary: Enviroment State-Text Injection Attack on LLM-Driven Embodied Agents

- **arXiv**: [2608.16806v2](https://arxiv.org/abs/2608.16806v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16806v2)
- **作者**: Jiawei Liu, Jiacheng Guo, Tian Zhang et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Large language model (LLM)-driven embodied agents rely on environment states to interpret scenes, generate high-level plans, and drive physical execution, making planner-visible state representations a critical security boundary. Existing attacks primarily manipulate user instructions, prompt contexts, model behavior, or perceptual inputs, while paying limi…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation

- **arXiv**: [2608.19425v1](https://arxiv.org/abs/2608.19425v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19425v1)
- **作者**: Dijie Zhu, Seunghun Oh, Ruopeng Huang et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Reliable performance evaluation is a central bottleneck for deploying robot-learning policies in real-world conditions. Real-world testing is faithful but costly and difficult to scale, whereas simulation-based testing scales easily but is inevitably biased by the sim-to-real gap. Existing simulation-augmented methods combine limited real-world rollouts wit…

### 2. RIPE++: Reinforced Keypoint Learning from Positive Pairs Only

- **arXiv**: [2608.19693v1](https://arxiv.org/abs/2608.19693v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19693v1)
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **发表**: 2026-08-20  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. R…

### 3. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 4. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 5. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

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

### 10. Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

- **arXiv**: [2607.06464v1](https://arxiv.org/abs/2607.06464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06464v1)
- **作者**: Samuele Centanni, Yuhao Zhang, Yifu Tao et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (5 篇)

### 1. Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

- **arXiv**: [2607.11099v1](https://arxiv.org/abs/2607.11099v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11099v1)
- **作者**: Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 2. DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

- **arXiv**: [2607.17058v1](https://arxiv.org/abs/2607.17058v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17058v1)
- **作者**: Yuxuan Chen, Brook Du
- **发表**: 2026-07-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 3. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that a…

### 4. PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments

- **arXiv**: [2607.07374v1](https://arxiv.org/abs/2607.07374v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07374v1)
- **作者**: Seunghun Lee, Jihun Nam, Dong-Uk Seo et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliabili…

### 5. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618v1) — score 20
2. [AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning](https://arxiv.org/abs/2608.14028v1) — score 17
3. [Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds](https://arxiv.org/abs/2607.18135v1) — score 17

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
