# 机器人研究每日摘要 · 2026-10-18

> 自动生成,共 54 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 2. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 3. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 4. What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning

- **arXiv**: [2610.21915v1](https://arxiv.org/abs/2610.21915v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21915v1)
- **作者**: Haitao Shen, Hanyu Liu, Yihan Lin et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions. Auxiliary objectives such as latent-action (LA) and future-vision (FV) prediction are often added to improve policy learning, yet they compete with action prediction for the same training budget. We a…

### 5. Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models

- **arXiv**: [2610.21522v1](https://arxiv.org/abs/2610.21522v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21522v1)
- **作者**: Lichao Ni, Yuhan Liu, Pengfei Li et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Specialized vision-language-action (VLA) policies acquire strong domain-specific skills, yet consolidating these skills into one shared policy remains challenging. On-policy distillation (OPD) transfers teacher knowledge on inputs induced by the student, addressing the distribution mismatch encountered during deployment. For flow-based VLAs, this mismatch a…

### 6. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 7. REKI: Registering Knowledge in VLAs

- **arXiv**: [2610.22178v1](https://arxiv.org/abs/2610.22178v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22178v1)
- **作者**: Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action e…

## 🌐 具身智能 / 机器人基础模型 (2 篇)

### 1. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

### 2. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

## 🦵 人形 / 足式机器人 (13 篇)

### 1. SOMA: Stack-of-Objects Manipulation using a Quadruped Robot

- **arXiv**: [2610.20968v1](https://arxiv.org/abs/2610.20968v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20968v1)
- **作者**: Stergios E. Bachoumas, Panagiotis Artemiadis
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Executing heavy-duty physical manipulation in unpredictable environments remains a major challenge for quadrupedal robots lacking dedicated manipulators. This paper presents SOMA, a hierarchical reinforcement learning framework for whole-body non-prehensile manipulation of multi-object stacks using a quadruped robot. Unlike traditional methods restricted to…

### 2. Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control

- **arXiv**: [2610.19393v1](https://arxiv.org/abs/2610.19393v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19393v1)
- **作者**: Lingfan Bao, Hanshang Zhu, Yan Pan et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessari…

### 3. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 4. Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

- **arXiv**: [2610.22342v1](https://arxiv.org/abs/2610.22342v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22342v1)
- **作者**: Tianxing Chen, Wenwei Lin, Chuqiao Lyu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, imag…

### 5. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 6. Whole-Body Dexterity

- **arXiv**: [2610.22184v1](https://arxiv.org/abs/2610.22184v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22184v1)
- **作者**: Conor Mc Gartoll, An Dang, Pranay Thangeda et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Current humanoid dexterous manipulation remains largely confined to end-effectors and simple grasps, falling short of humans' ability to engage the entire body by bracing and sliding bulky objects against the arms and torso. We introduce Whole-Body Dexterity (WBD), a general framework that uses the robot's body and appendages as contact surfaces to grasp an…

### 7. Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation

- **arXiv**: [2610.22119v1](https://arxiv.org/abs/2610.22119v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22119v1)
- **作者**: Venki Parsuram, Michelle Wang, Jin-Hyuk Hong et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: We propose Compliant GMT (C-GMT), a modular framework for full-body compliant responses in general motion tracking. As humanoid robots move into real world deployment, they not only need to perform any motion but also respond safely and robustly to interaction forces. Existing general motion tracking policies can imitate diverse motions but are trained to b…

### 8. Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation

- **arXiv**: [2610.22176v1](https://arxiv.org/abs/2610.22176v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22176v1)
- **作者**: James Foster, Beomyeong Park, Luigi Penco et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: The effective deployment of humanoid robots in practical tasks of interest will require a capability of sensing and adapting to variations in inertial parameters, as occurs during heavy tool use or when carrying significant payload. Such payloads constitute a significant proportion of the combined payload-robot system, the effects of which cannot be ignored…

### 9. TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion

- **arXiv**: [2610.21515v1](https://arxiv.org/abs/2610.21515v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21515v1)
- **作者**: Zejian Kang, Yifu Luo, Boyang Shen et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language. The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 hum…

### 10. Eye, Robot: Learning Expressive Gaze Dynamics via a VLM-Guided Transformer-VAE

- **arXiv**: [2610.19635v1](https://arxiv.org/abs/2610.19635v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19635v1)
- **作者**: Yuhang Hu, Junlin Lyu, Yuan Fang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Gaze coordinates attention in human interaction through coupled eye, head, and eyelid motion. A humanoid robot must choose where to look while generating a suitable movement toward that target; fixed tracking rules alone do not model the temporal structure of human gaze. We separate these tasks with an asynchronous vision-language model that selects a scene…

## 🦾 操控 / 灵巧手 / 抓取 (19 篇)

### 1. FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models

- **arXiv**: [2610.22146v1](https://arxiv.org/abs/2610.22146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22146v1)
- **作者**: Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention…

### 2. Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation

- **arXiv**: [2610.19753v1](https://arxiv.org/abs/2610.19753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19753v1)
- **作者**: Yiming Meng, Yanming Shao, Weijie Shen et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand inte…

### 3. Causal Analysis of Robot Foundation Models Enables Efficiency Gains

- **arXiv**: [2610.20750v1](https://arxiv.org/abs/2610.20750v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20750v1)
- **作者**: Aiden Swann, Mathilde Papillon, Mozes Jacobs et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question…

### 4. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 5. Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

- **arXiv**: [2610.22363v1](https://arxiv.org/abs/2610.22363v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22363v1)
- **作者**: Zirui Wu, Chen Guo, Tianjian Jiang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed…

### 6. Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation

- **arXiv**: [2610.21180v1](https://arxiv.org/abs/2610.21180v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21180v1)
- **作者**: Bing Cheng, Yiran Mao, Zewei Ye et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: General-purpose dexterous manipulation requires policies to transfer knowledge from related tasks to new tasks with only a few target demonstrations. Existing benchmarks often provide too many target demonstrations. They also leave the differences between source and target tasks uncontrolled. As a result, they cannot clearly distinguish knowledge transfer f…

### 7. EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos

- **arXiv**: [2610.20904v1](https://arxiv.org/abs/2610.20904v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20904v1)
- **作者**: Meng Cao, Can Zhao, Jinjie Wei et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand- crafted geometric mappings. However, such mappi…

### 8. TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation

- **arXiv**: [2610.20320v1](https://arxiv.org/abs/2610.20320v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20320v1)
- **作者**: Fucai Zhu, Xidong Zhang, Yichi Zhang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Large-scale robot learning increasingly relies on diverse human demonstrations, yet tactile manipulation data remain difficult to scale, and existing multimodal datasets often lack consistent quality control and structured supervision. We present TacClaw-Infinity, a large-scale structured Vision-Tactile-Language-Action (VTLA) dataset for contact-rich manipu…

### 9. VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

- **arXiv**: [2610.21985v1](https://arxiv.org/abs/2610.21985v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21985v1)
- **作者**: Xueli Sun, Yuxiang Lu, Yantong Liu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversi…

### 10. TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control

- **arXiv**: [2610.21922v1](https://arxiv.org/abs/2610.21922v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21922v1)
- **作者**: Menghao Yin, Jiaju Yin, Xiyue Dong et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states. These limitations hinder learning from action-free videos and can encourage overfitting to demonstration conditions, weakening generalization and robustness. We present TS-WAM, a lightweight Teacher-Student Wor…

## 🎓 模仿学习 / 强化学习 (5 篇)

### 1. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

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

### 4. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 5. Runtime Monitoring of Supermartingale Certificates

- **arXiv**: [2610.19701v1](https://arxiv.org/abs/2610.19701v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19701v1)
- **作者**: Mirco Giacobbe, Thomas A. Henzinger, Konstantin Kueffner et al.
- **发表**: 2026-10-14  ·  **类别**: cs.AI, eess.SY
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Supermartingale certificates formally guarantee temporal properties of discrete and continuous-time stochastic dynamical systems. However, these guarantees rely on a mathematical model of the world, leaving a sim-to-real gap that can invalidate them for the deployed system. We formulate the runtime monitoring problem for supermartingale certificates, in whi…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 2. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 3. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 4. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 5. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 6. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. SNOAR: Self-training with Noise filtering, Observation adding, and Remixing for Speech Denoising Without Clean References

- **arXiv**: [2610.20863v1](https://arxiv.org/abs/2610.20863v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20863v1)
- **作者**: Samuele Cornell, Matthew Maciejewski
- **发表**: 2026-10-14  ·  **类别**: eess.AS, cs.LG, cs.SD
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Unsupervised speech denoising methods such as MixIT and noisy-target training can be trained directly on noisy recordings, avoiding the sim-to-real gap of synthetic training data, but remain well below supervised performance. Teacher--student self-training, as in RemixIT, narrows this gap by remixing a teacher's estimates into new mixtures that supervise a…

## 📦 其他机器人相关 (1 篇)

### 1. ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning

- **arXiv**: [2609.19661v1](https://arxiv.org/abs/2609.19661v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19661v1)
- **作者**: Chiyoung Kim, Min Sung Choi, Jinho Ju et al.
- **发表**: 2026-09-17  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approac…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146v1) — score 16
2. [Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2610.19753v1) — score 15
3. [SOMA: Stack-of-Objects Manipulation using a Quadruped Robot](https://arxiv.org/abs/2610.20968v1) — score 15

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
