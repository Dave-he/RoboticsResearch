# 机器人研究每日摘要 · 2026-09-16

> 自动生成,共 87 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (10 篇)

### 1. When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents

- **arXiv**: [2609.10873v1](https://arxiv.org/abs/2609.10873v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.10873v1)
- **作者**: Qinzhen Ma, Ruihai Wu
- **发表**: 2026-09-09  ·  **类别**: cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Independent evaluation can reject harmful policy updates yet also prevent useful continual learning. We argue that update admission must be assessed through both error control and retained learning opportunities at a stated interaction budget. We identify a concrete failure: a range-based confidence gate cannot certify unchanged old-task behavior within oth…

### 2. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

- **arXiv**: [2609.12641v1](https://arxiv.org/abs/2609.12641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12641v1)
- **作者**: Jianman Lin, Shailesh Shailesh, Zhongyi Luo et al.
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine g…

### 3. STAGE: Diagnosing Semantic Transfer at Grounded Execution in Embodied Agents

- **arXiv**: [2609.13458v1](https://arxiv.org/abs/2609.13458v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13458v1)
- **作者**: Baosheng Jin, Yushen Liang, Hua Shen
- **发表**: 2026-09-11  ·  **类别**: cs.RO, cs.CL
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Embodied language grounding requires more than identifying the referent of an instruction: recovered semantics must also control the action an agent exposes. We study this missing link as a semantic-action gap, where instruction semantics are recoverable but weakly expressed in native continuous actions. We introduce SAT-Bench, a fixed-observation counterfa…

### 4. GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving

- **arXiv**: [2609.15169v1](https://arxiv.org/abs/2609.15169v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.15169v1)
- **作者**: Xiao Liu, Haoyu Li, Jianghao Leng et al.
- **发表**: 2026-09-14  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior. We present GRAVA, a framework built around Grounded Reasoning-to-Action (GRA), which unifies grounding, reasoning, and action generation in a single…

### 5. Beyond Single-Axis Testing: Paired Evaluation of Compound Robustness in Vision-Language-Action Policies

- **arXiv**: [2609.15940v1](https://arxiv.org/abs/2609.15940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.15940v1)
- **作者**: Hiroki Sawada, Shunichi Kasahara
- **发表**: 2026-09-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-language-action policies are typically evaluated one perturbation at a time, providing a useful diagnosis of their sensitivity to individual distribution shifts. Real-world deployment, however, may involve several shifts simultaneously, and it remains unclear how these individual robustness measurements compose. We ask whether compound robustness can…

### 6. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

- **arXiv**: [2609.07470v1](https://arxiv.org/abs/2609.07470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07470v1)
- **作者**: Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible…

### 7. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 8. When Faster VLA Deployment Changes Closed-Loop Behavior: Task Success-Latency Analysis of SmolVLA Across PyTorch and ONNX Variants

- **arXiv**: [2609.14146v1](https://arxiv.org/abs/2609.14146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.14146v1)
- **作者**: Rafiqul Islam
- **发表**: 2026-09-12  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) deployment can reduce inference latency while changing closed-loop task behavior. We evaluate HuggingFaceVLA/smolvla_libero on an RTX 2060 (6 GB) in LIBERO Spatial and Object (MuJoCo 3.3.2, LeRobot 0.6.1, seed 42), comparing PyTorch+AMP with ONNX Runtime CUDA Execution Provider (CUDA EP). The main evaluation uses 100 episodes/su…

### 9. What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency

- **arXiv**: [2609.13984v1](https://arxiv.org/abs/2609.13984v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13984v1)
- **作者**: Luoyang Sun, Guoyang Xia, Fengfa Li et al.
- **发表**: 2026-09-12  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language-Action (VLA) models combine a pretrained vision encoder, a language backbone, and an action head, but their relative contribution has not been established under controlled, latency-paired conditions. We fix the backbone families (SigLIP2 and Qwen2.5) and the training pipeline, sweep action-head design and module scale, and pair each configur…

### 10. ReWeight: Leveraging Human Data for VLA Post-Training via Demonstration Retrieval and Sample Weighting

- **arXiv**: [2609.13851v1](https://arxiv.org/abs/2609.13851v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13851v1)
- **作者**: Chenwei Wang, Dianye Huang, Match W. L. Ko et al.
- **发表**: 2026-09-12  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Post-training vision-language-action (VLA) models for specific robots and tasks requires in-domain demonstrations, yet collecting diverse robot data is costly. Egocentric human demonstrations provide a scalable alternative, but directly mixing human and robot data can introduce cross-embodiment discrepancies and degrade policy performance. To address this c…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection

- **arXiv**: [2609.11225v1](https://arxiv.org/abs/2609.11225v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.11225v1)
- **作者**: Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie et al.
- **发表**: 2026-09-10  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through tas…

### 2. Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents

- **arXiv**: [2609.11660v1](https://arxiv.org/abs/2609.11660v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.11660v1)
- **作者**: Marica Notte, Ludovica Marinucci, Vieri Giuliano Santucci
- **发表**: 2026-09-10  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In recent years, artificial intelligence has made extraordinary progress thanks to large-scale models capable of generalization and the generation of complex outputs. However, transferring this potential into embodied agents reveals a significant limitation: the most advanced systems rely on pre-existing datasets and human feedback strategies that are power…

### 3. SmoothRL: Online Reinforcement Learning During Asynchronous Execution

- **arXiv**: [2608.29768v1](https://arxiv.org/abs/2608.29768v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29768v1)
- **作者**: Guang Gao, Yuxuan Nong, Baifu Huang et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learn…

### 4. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 5. Safe Task Planning with Long-Term Graph Memory for Embodied Agents

- **arXiv**: [2609.08444v1](https://arxiv.org/abs/2609.08444v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08444v1)
- **作者**: Siyuan Li, Taiyan Lang, Aoqi Yan et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Large language models (LLMs) and vision-language models (VLMs) have significantly advanced zero-shot task planning for embodied agents. However, most LLM- and VLM-driven methods struggle to generate safe high-level actions due to a lack of physical risk awareness, particularly under partial observability, where hazards lie outside the immediate field of vie…

### 6. GLAM: Training a latent world model over global spatiotemporal memory for active exploration and navigation

- **arXiv**: [2609.14561v1](https://arxiv.org/abs/2609.14561v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.14561v1)
- **作者**: I-Tak Ieong, Ruizhi Feng, Zhaoyang Lu et al.
- **发表**: 2026-09-13  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Active exploration and semantic navigation require an embodied agent to build memory from partial observations, predict how the evolution of observed spatial memory may support future motion, and convert that prediction into actionable plans. We present GLAM, a goal-conditioned latent world model trained over global spatiotemporal memory, and GLAM NAV, the…

### 7. Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction

- **arXiv**: [2609.13082v1](https://arxiv.org/abs/2609.13082v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13082v1)
- **作者**: Baoyang Jiang, Fengchun Zhang, Leyuan Wang et al.
- **发表**: 2026-09-11  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Agentic systems offer a promising way to automate embodied benchmark construction, but existing approaches typically cover isolated stages or remain specialized to predefined environments and task families. More importantly, multi-step construction produces dependent intermediate artifacts that are often passed downstream without artifact-specific verificat…

### 8. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 9. Monocular Depth Estimation from a Single Image: Progress and Opportunities

- **arXiv**: [2609.01172v1](https://arxiv.org/abs/2609.01172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01172v1)
- **作者**: Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al.
- **发表**: 2026-09-01  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing t…

## 🦵 人形 / 足式机器人 (23 篇)

### 1. A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots

- **arXiv**: [2609.01518v1](https://arxiv.org/abs/2609.01518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01518v1)
- **作者**: Duncan Calvert, Luigi Penco, Dexton Anderson et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: There is tremendous value in humanoid robots taking on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole-body motion, perception, contact, and operator supervision. We present a robot-local, runtime-editable behavior authoring and runtime system that ad…

### 2. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 3. Extending the Speed Limit of Quadrupedal Locomotion via Refined Actuator Modeling and Adaptive Command Scheduling

- **arXiv**: [2609.13289v1](https://arxiv.org/abs/2609.13289v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13289v1)
- **作者**: Yucheng Tao, Shaowen Cheng, Guorong Lan et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Achieving high-speed locomotion in quadrupedal robots remains highly challenging, as actuators operate near their physical limits and exhibit pronounced nonlinearities. However, many existing methods neglect actuator nonlinearities and physical constraints during training, leading to a significant sim-to-real gap under highly dynamic motions and limiting ac…

### 4. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 5. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 6. ViBe: Visual Behavior Adaptation for Perceptive Humanoid Whole-Body Control

- **arXiv**: [2609.09918v1](https://arxiv.org/abs/2609.09918v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09918v1)
- **作者**: Lokesh Krishna, Sarvesh Venkatesan, An Zhang et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Motion tracking provides a scalable recipe for humanoid whole-body control. By design, the resulting trackers lack exteroceptive feedback hence reacting to the environment remains the responsibility of a higher-level planner. Existing perceptive controllers train geometry-only encoders from scratch, trading semantics for sim-to-real ease, and typically rely…

### 7. TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

- **arXiv**: [2609.09158v1](https://arxiv.org/abs/2609.09158v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09158v1)
- **作者**: Anqi Li, Yuxin Chen, Zhaobo Li et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: We study the problem of navigating cluttered indoor environments with a humanoid robot. Unlike conventional methods that model navigation as a 2D path planning problem, humanoid traversal in cluttered environments requires continuous geometry-aware whole-body adaptation, including coordinated arm placement, torso adjustment, and gait modulation for collisio…

### 8. GLoRI: Closed-Loop Whole-Body Tracking with Global-Local Reference Interaction for Humanoid Loco-Manipulation

- **arXiv**: [2609.05994v1](https://arxiv.org/abs/2609.05994v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05994v1)
- **作者**: Qingyao Xu, Sheng Yin, Zibo Zhou et al.
- **发表**: 2026-09-05  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid loco-manipulation requires accurate whole-body motion tracking in the world frame for physical interaction. While local references preserve motion structure, they lack explicit constraints on absolute spatial placement, leading to accumulated global errors. Existing globally aware approaches augment teleoperation policies with global observations b…

### 9. FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation

- **arXiv**: [2609.03889v2](https://arxiv.org/abs/2609.03889v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.03889v2)
- **作者**: Yutian Zhang, Siyuan Ma, Liwen Yang et al.
- **发表**: 2026-09-03  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabiliz…

### 10. Skill Composition for Legged Robot Reinforcement Learning

- **arXiv**: [2609.14647v1](https://arxiv.org/abs/2609.14647v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.14647v1)
- **作者**: Daniel Gigliotti, Flavio Maiorana, Fabio Patrizi et al.
- **发表**: 2026-09-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Robots, and humanoid robots in particular, are increasingly competent at individual behaviors, each obtained by training a specialized controller. A specialized skill is quick to train, converges reliably because the problem it faces is narrow, and can be validated on its own, none of which is true of a single end-to-end policy asked to cover everything. Wh…

## 🦾 操控 / 灵巧手 / 抓取 (28 篇)

### 1. Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands

- **arXiv**: [2609.15726v1](https://arxiv.org/abs/2609.15726v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.15726v1)
- **作者**: Zhenjie Yang, Yideng Zhang, Dongjie Zhang et al.
- **发表**: 2026-09-14  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Tactile sensing provides contact information that can be difficult to infer from vision alone, but tactile hardware for dexterous hands has not converged to a common design. Dexterous hands differ in finger structure, contact surfaces, and sensor layouts, while simulated tactile signals still differ from measurements produced by physical sensors. These fact…

### 2. Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction

- **arXiv**: [2609.07747v2](https://arxiv.org/abs/2609.07747v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07747v2)
- **作者**: Ruoqu Chen, Feixiang Ruan, Liu Cao et al.
- **发表**: 2026-09-07  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection? We present DEX-X, a framewo…

### 3. Primitive-Informed Sampling-Based MPC for Multi-Fingered Dexterous Manipulation

- **arXiv**: [2609.14868v1](https://arxiv.org/abs/2609.14868v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.14868v1)
- **作者**: Emek Barış Küçüktabak, Karankumar Patel, Jinda Cui et al.
- **发表**: 2026-09-14  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: We present a primitive-informed sampling-based model predictive control (MPC) framework for multi-fingered dexterous manipulation. Sampling-based MPC avoids the need for gradients through complex contact dynamics, but direct exploration of the high-dimensional joint space is inefficient and makes performance strongly dependent on the sampling distribution.…

### 4. Real-World Reinforcement Learning with MPC Scaffolding for Dexterous Manipulation

- **arXiv**: [2609.14878v1](https://arxiv.org/abs/2609.14878v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.14878v1)
- **作者**: Emek Barış Küçüktabak, Karankumar Patel, Zhaodong Yang et al.
- **发表**: 2026-09-14  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Real-world reinforcement learning (RL) offers a promising route to dexterous manipulation policies that can adapt directly from physical interaction, but learning is hindered by inefficient early exploration and costly failures. We propose a framework that uses sampling-based model predictive control (MPC) as scaffolding for real-world dexterous RL, providi…

### 5. Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing

- **arXiv**: [2609.15921v1](https://arxiv.org/abs/2609.15921v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.15921v1)
- **作者**: Matteo Grimaldi, David Klee, Ziling Chen et al.
- **发表**: 2026-09-14  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation of deformable objects demands continuous fingertip-level regulation of pressure, friction, and incipient slip. We study one of the most challenging cases: dexterous cable tracing, feeding a cable through the hand with repeated pinch-and-curl motions of the thumb and index finger. We introduce Touch2Trace, a tactile-driven imitation-le…

### 6. IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

- **arXiv**: [2609.15005v1](https://arxiv.org/abs/2609.15005v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.15005v1)
- **作者**: Jinwoong Kim, Sangjin Park
- **发表**: 2026-09-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) policies perform robot manipulation tasks using multimodal inputs such as visual observations, proprioceptive states, and language instructions. However, it remains unclear at which execution stages each modality contributes to final task success and how input interventions propagate through subsequent states, observations, and…

### 7. Learning In-Hand Object Reaching to General 6D Poses

- **arXiv**: [2609.13761v1](https://arxiv.org/abs/2609.13761v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13761v1)
- **作者**: Junxiao Lin, Tianyue Wu, Jie Yin et al.
- **发表**: 2026-09-12  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: In-hand manipulation allows multi-fingered dexterous hands to reconfigure grasped objects without releasing and regrasping them. This improves manipulation efficiency by reducing repeated grasp acquisition and large arm motions. However, most learning-based methods focus on reorientation, continuous rotation, or translation, whereas many tasks require joint…

### 8. $τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885v1](https://arxiv.org/abs/2608.16885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16885v1)
- **作者**: Xiaowei Cai, Yunuo Cai, Bingao Chen et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_…

### 9. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 10. STAR: Sparse Tactile Representation Learning in Vision-Tactile-Language-Action Models for Dexterous Manipulation

- **arXiv**: [2609.12549v1](https://arxiv.org/abs/2609.12549v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12549v1)
- **作者**: Xiangcheng Liu, Tianhao Wu, Le Zheng et al.
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation requires coordinated multi-finger control and effective tactile feedback, yet learning these capabilities remains challenging due to the lack of large-scale real-world data and the difficulty of extracting effective representations from sparse tactile signals. We build a robot platform and teleoperation system to collect a 200-hour bi…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 2. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 3. Ostrich: Taking Large Strides Through Stiff Contact in Differentiable Dynamics

- **arXiv**: [2609.08800v1](https://arxiv.org/abs/2609.08800v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08800v1)
- **作者**: Aleš Kučera, Karel Zimmermann
- **发表**: 2026-09-08  ·  **类别**: cs.RO, cs.GR, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Three properties determine whether a differentiable simulator can drive gradient-based optimization through contact: simulation accuracy, gradient reliability, and per-iteration cost. Tape-based engines such as MJX and Newton Semi-Implicit require timesteps small enough to keep contacts numerically tractable, and their backpropagation memory grows linearly…

### 4. Praxist: From Experimental Artifacts to Solution Lineages

- **arXiv**: [2608.25955v1](https://arxiv.org/abs/2608.25955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25955v1)
- **作者**: Jin Li, Ahmed Murtadha, Zhiyu Wang et al.
- **发表**: 2026-08-26  ·  **类别**: cs.MA, cs.SE
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Autonomous R\&D agents now write, run, and improve executable artifacts under automated evaluation---but largely as laboratory instruments: shown on curated benchmarks, with gains that are hard to trace to a cause and costs well above what sustained engineering practice absorbs. The limitation is structural. Most systems treat each attempt as nearly self-co…

### 5. RIPE++: Reinforced Keypoint Learning from Positive Pairs Only

- **arXiv**: [2608.19693v1](https://arxiv.org/abs/2608.19693v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19693v1)
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **发表**: 2026-08-20  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. R…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 8. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 9. FPicker: Topology-Guided Evolution for Filament Tracing in Low-SNR Microscopy

- **arXiv**: [2609.08305v1](https://arxiv.org/abs/2609.08305v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08305v1)
- **作者**: Tingyin Zhao, Mingtao Huang, Yuan Shen
- **发表**: 2026-09-08  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Automating filament tracing in Cryo-Electron Microscopy (Cryo-EM) is essential for 3D helical reconstruction but challenged by intersecting topologies and extremely low Signal-to-Noise Ratios ($\text{SNR} = σ_s^2/σ_n^2$ < 0.1 or -10 dB). Existing paradigms fail: pixel-wise segmenters suffer from severe topological fracturing, box-based detectors face ghost…

### 10. Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions

- **arXiv**: [2608.30690v1](https://arxiv.org/abs/2608.30690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30690v1)
- **作者**: Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
- **发表**: 2026-08-31  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intend…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (4 篇)

### 1. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

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

### 4. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](https://arxiv.org/abs/2609.15726v1) — score 21
2. [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction](https://arxiv.org/abs/2609.07747v2) — score 20
3. [Primitive-Informed Sampling-Based MPC for Multi-Fingered Dexterous Manipulation](https://arxiv.org/abs/2609.14868v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
