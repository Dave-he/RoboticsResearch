# 机器人研究每日摘要 · 2026-10-09

> 自动生成,共 89 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models

- **arXiv**: [2610.10526v1](https://arxiv.org/abs/2610.10526v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10526v1)
- **作者**: Mikey Watts, Yuchen Cui
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.CL, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ ch…

### 2. Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization

- **arXiv**: [2610.09943v1](https://arxiv.org/abs/2610.09943v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09943v1)
- **作者**: Haoru Li, Jinmei Liu, Zhiyong Wang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts,…

### 3. Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding

- **arXiv**: [2610.10178v1](https://arxiv.org/abs/2610.10178v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10178v1)
- **作者**: Theodor Wulff, Angelo Cangelosi
- **发表**: 2026-10-07  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical f…

### 4. Juno: Taming Predictive Latents for Vision-Language-Action Models

- **arXiv**: [2610.09940v1](https://arxiv.org/abs/2610.09940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09940v1)
- **作者**: Yuchen Zhu, Chenyi Xu, Yulin Zhang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific cont…

### 5. Q-Learning with Scalar Adjoint Matching

- **arXiv**: [2610.10437v1](https://arxiv.org/abs/2610.10437v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10437v1)
- **作者**: Yonghoon Dong, Minsung Yoon, Jaehyuk Kim et al.
- **发表**: 2026-10-07  ·  **类别**: cs.LG, cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest. However, fine-tuning a flow policy against a learned value function is not trivial, because the policy generates its action over many flow steps. Adjoint matching offers a principled way to upd…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents

- **arXiv**: [2610.07785v1](https://arxiv.org/abs/2610.07785v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07785v1)
- **作者**: Gyusik Seo, Jaehong Yoon
- **发表**: 2026-10-06  ·  **类别**: cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon tas…

### 2. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 3. RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment

- **arXiv**: [2610.09294v1](https://arxiv.org/abs/2610.09294v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09294v1)
- **作者**: Tianruo Rose Xu, Jiawei Ren, Yichi Yang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-t…

### 4. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

### 5. SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation

- **arXiv**: [2610.08941v1](https://arxiv.org/abs/2610.08941v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08941v1)
- **作者**: Yunheng Liu, Ziqi Cai, Siqi Yang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming…

### 6. Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage

- **arXiv**: [2610.08933v1](https://arxiv.org/abs/2610.08933v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08933v1)
- **作者**: Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI, cs.HC
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independe…

### 7. SpaTime: Streaming Vision-Language Models for Spatio-temporal Reasoning

- **arXiv**: [2610.08713v1](https://arxiv.org/abs/2610.08713v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08713v1)
- **作者**: Hairong Yin, Huangying Zhan, Shin-Fang Chng et al.
- **发表**: 2026-10-06  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents must reason about 3D space while the video is still arriving, answering questions as soon as they have observed enough of the scene. VLMs that incorporate 3D geometric priors achieve strong spatial reasoning, but they operate offline, i.e., the full video must be available before they produce an answer. Streaming VLMs process frames causally…

### 8. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- **arXiv**: [2610.00864v1](https://arxiv.org/abs/2610.00864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00864v1)
- **作者**: Jiawei Fan, Sifeng Wang, Yuqing Hou et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (27 篇)

### 1. BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation

- **arXiv**: [2610.07594v1](https://arxiv.org/abs/2610.07594v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07594v1)
- **作者**: Zexi Zhang, Zecheng Zhu, Zidong Chen et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchron…

### 2. MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation

- **arXiv**: [2610.07511v1](https://arxiv.org/abs/2610.07511v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07511v1)
- **作者**: Suzannah Wistreich, Stephen Tian, Isabella Huang et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Mobile manipulators such as humanoid robots are increasingly deployed in dynamic, unstructured environments to perform dexterous manipulation tasks. However, end-to-end manipulation policies trained to imitate demonstration data collected from a single robot pose are brittle: even centimeter-scale deviations in robot pose at deployment can drive ego-centric…

### 3. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

- **arXiv**: [2610.06850v1](https://arxiv.org/abs/2610.06850v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06850v1)
- **作者**: Yucheng Zhang, Sirui Xu, Jinhong Li et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.GR
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object i…

### 4. Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data

- **arXiv**: [2610.09117v1](https://arxiv.org/abs/2610.09117v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09117v1)
- **作者**: Songbo Hu, Qiayuan Liao, Yufeng Chi et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid robots still struggle to plan contact-rich whole-body manipulation from egocentric RGB and proprioception. Workhorse learns such manipulation from robot-free human demonstrations. A visual planner predicts five-link targets: the poses of the torso, both wrists, and both feet. A reinforcement-learning whole-body tracker follows them on the robot. Bo…

### 5. Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and Reward Gating

- **arXiv**: [2610.08320v1](https://arxiv.org/abs/2610.08320v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08320v1)
- **作者**: Haozhuo Zhang, Qiang Zhang, Jian Tang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Cluttered indoor environments, where large and heavy objects are scattered across diverse surfaces, require humanoid robots to sequentially navigate, grasp, transport, and accurately place each item at its target location within a single uninterrupted episode. This long-horizon, whole-body loco-manipulation task remains a significant challenge for current m…

### 6. Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction

- **arXiv**: [2610.09291v1](https://arxiv.org/abs/2610.09291v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09291v1)
- **作者**: Jeonghwan Kim, Hyeonwoo Kim, Hanbyul Joo
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present…

### 7. LLA-MPPI: Rapidly Adaptive Whole-body Control of Legged Robots with GPU-Accelerated Parallel Simulations

- **arXiv**: [2610.10465v1](https://arxiv.org/abs/2610.10465v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10465v1)
- **作者**: Sebin Jung, Maitham F. AL-Sunni, Juan Alvarez-Padilla et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Real-time whole-body controllers for legged robots typically plan through a fixed nominal model and degrade when the deployed dynamics change. Adaptive methods typically require a model structure that contact dynamics do not provide, or they need offline training for each anticipated condition. We present Look-back and Look-ahead Adaptive Model Predictive P…

### 8. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 9. PhoneBot: A Low-Cost Open Humanoid Robot Platform Reusing Smartphones

- **arXiv**: [2610.08737v1](https://arxiv.org/abs/2610.08737v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08737v1)
- **作者**: Ruochen Hou, Quanyou Wang, Daniel Koh et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: The adoption of humanoid robots in education and research remains limited by high hardware costs, complex sensing systems, and substantial computational requirements. This paper presents PhoneBot, a low-cost, open-source humanoid robot platform that repurposes commodity smartphones as its primary sensing and computing unit. By using a smartphone's integrate…

### 10. Magnet-Aware Control of Legged Robots

- **arXiv**: [2610.08653v1](https://arxiv.org/abs/2610.08653v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08653v1)
- **作者**: J. Playan Garai, S. B. Djuve, C. McGreavy et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Autonomous robots can increase uptime and reduce human exposure in Big Science facilities, but strong magnetic fields needed for their operation corrupt sensors and induce pose-dependent mechanical wrenches that destabilize robots and challenge conventional reactive controllers. This paper presents a control framework for modeling, estimating, and dynamical…

## 🦾 操控 / 灵巧手 / 抓取 (30 篇)

### 1. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors

- **arXiv**: [2610.07681v1](https://arxiv.org/abs/2610.07681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07681v1)
- **作者**: Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation poses a challenging high-dimensional optimization problem, as useful behaviors require coordinated motion across many hand joints. In reinforcement learning (RL) and sampling-based trajectory optimization, exploration commonly relies on independent robot joint perturbations, making coordinated behaviors difficult to discover. Prior wo…

### 2. GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive

- **arXiv**: [2610.03861v1](https://arxiv.org/abs/2610.03861v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03861v1)
- **作者**: Yulin Liu, Lai Wei, Yen-Jen Wang et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Foundation models and large-scale human data provide rich sources of manipulation intent, but translating this intent into multi-fingered robot behavior remains difficult. Dexterous hands still lack a reusable low-level primitive that reliably establishes contact across tasks and embodiments. We propose GOTT, a reach-acquire-move framework built around a si…

### 3. Now You Feel It, Now You See Me: Digital-Twin-based Teleoperation Interface for Dexterous Manipulation

- **arXiv**: [2610.05081v1](https://arxiv.org/abs/2610.05081v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05081v1)
- **作者**: Youngchan Shim, Kyutae Lee, JooYun Kim et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Teleoperation is becoming increasingly important for collecting high-quality demonstrations to teach robots dexterous manipulation skills. For dexterous manipulation, bare-hand tracking provides a practical way to control robotic hands and demonstrate coordinated finger movements without gloves or exoskeletons. However, this type of teleoperation faces two…

### 4. DITTO-X: Forward and Reverse Teleoperation for Dexterous Manipulation and Human Intervention

- **arXiv**: [2610.00781v2](https://arxiv.org/abs/2610.00781v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00781v2)
- **作者**: Zhanpeng He, Joaquin Palacios, Zhangyu Wang et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Teleoperated demonstrations are a primary source of data for robot manipulation, and teleoperated interventions are a primary mechanism for correcting policies at deployment. Yet most teleoperation systems close the loop through vision alone and are built around parallel-jaw grippers, limiting both what the robot can execute and what the operator can expres…

### 5. PatternDex: Learning Interaction Patterns to Guide Reinforcement Learning of Bimanual Dexterous Manipulation of Articulated Objects

- **arXiv**: [2610.04765v1](https://arxiv.org/abs/2610.04765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04765v1)
- **作者**: David Minkwan Kim, Runfa Blark Li, Beckham Po-Ju Lee et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: In this paper, we develop a method that enables bimanual dexterous hands to manipulate articulated objects with a high success rate without suffering from an embodiment gap. We observe that the correlation between hand motions and object motions is dictated by the object rather than the hands and can be learned from human-object demonstrations. Based on thi…

### 6. DexJoCo-X: Benchmarking Action Representations for Multi-Hand Dexterous Manipulation

- **arXiv**: [2610.03278v1](https://arxiv.org/abs/2610.03278v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03278v1)
- **作者**: Xiangwei Jiang, Yao Mu, Lixin Duan et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: As dexterous hands proliferate, collecting data and training policies separately for every morphology becomes increasingly impractical. Scalable cross-embodiment learning therefore requires a unified representation that captures shared manipulation structure while preserving morphology-specific control. Differences in hands, tasks, datasets, and control int…

### 7. RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer

- **arXiv**: [2610.09254v1](https://arxiv.org/abs/2610.09254v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09254v1)
- **作者**: Huang Huang, Wensi Ai, Ziyu Chen et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Simulation enables large-scale, low-cost robot data generation, but policies trained in simulation often fail to transfer to the real world due to the sim-to-real visual discrepancies. Existing approaches often rely on intermediate representations, which can discard rich semantic information or require additional perception modules at deployment. We address…

### 8. ReDex: Repairing Sim-to-Real Dexterous Policies by Finger-Level Compliant Interaction

- **arXiv**: [2610.07525v1](https://arxiv.org/abs/2610.07525v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07525v1)
- **作者**: Jinzhou Li, Hadi Tabatabaee, Kelin Yu et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation policies trained in simulation often fail to transfer to the real world because of errors in contact timing and force regulation. Yet these policies can retain useful multi-finger coordination for task progression. We propose ReDex, a framework for adapting a simulation-trained base policy to the real world by correcting local contact…

### 9. VICON: Visual-Inertial-Contact based Hand-Object Tracking for Manipulation Datasets

- **arXiv**: [2610.05180v1](https://arxiv.org/abs/2610.05180v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05180v1)
- **作者**: Yubin Jeon, Uiseong Shin, Hwanchul La et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation benefits from human demonstration datasets that capture diverse and natural hand-object interactions. In particular, contact points and forces provide supervision on where and how strongly to interact, which cannot be fully captured by motion trajectories alone. However, methods for jointly capturing hand and object motion, c…

### 10. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

## 🎓 模仿学习 / 强化学习 (10 篇)

### 1. HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

- **arXiv**: [2609.17168v1](https://arxiv.org/abs/2609.17168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17168v1)
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei et al.
- **发表**: 2026-09-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place…

### 2. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 3. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 4. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

- **arXiv**: [2609.20589v1](https://arxiv.org/abs/2609.20589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.20589v1)
- **作者**: Marina Orozco González, Luis Merino
- **发表**: 2026-09-17  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure…

### 5. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 6. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 7. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 8. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 9. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

### 10. NeRF and Gaussian Splatting SLAM in the Wild

- **arXiv**: [2412.03263v1](https://arxiv.org/abs/2412.03263v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.03263v1)
- **作者**: Fabian Schmidt, Markus Enzweiler, Abhinav Valada
- **发表**: 2024-12-04  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Navigating outdoor environments with visual Simultaneous Localization and Mapping (SLAM) systems poses significant challenges due to dynamic scenes, lighting variations, and seasonal changes, requiring robust solutions. While traditional SLAM methods struggle with adaptability, deep learning-based approaches and emerging neural radiance fields as well as Ga…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 2. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 3. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

### 4. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 5. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 6. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Micro Neural Policies for Safe Real-Time Robotic Control

- **arXiv**: [2610.08541v1](https://arxiv.org/abs/2610.08541v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08541v1)
- **作者**: Hongpeng Cao, Riccardo Curcio, Daniele Ottaviano et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In this paper, we investigate the synthesis of Micro Neural Policies (MNP) to enable safe and robust real-time robotic control on computationally constrained embedded devices. We demonstrate that integrating Evolution Strategy (ES) and Statistical Model Checking (SMC)-based verification for policy search can drastically reduce neural network size without co…

## 📦 其他机器人相关 (1 篇)

### 1. ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning

- **arXiv**: [2609.19661v1](https://arxiv.org/abs/2609.19661v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19661v1)
- **作者**: Chiyoung Kim, Min Sung Choi, Jinho Ju et al.
- **发表**: 2026-09-17  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approac…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors](https://arxiv.org/abs/2610.07681v1) — score 21
2. [GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive](https://arxiv.org/abs/2610.03861v1) — score 19
3. [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](https://arxiv.org/abs/2610.07594v1) — score 18

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
