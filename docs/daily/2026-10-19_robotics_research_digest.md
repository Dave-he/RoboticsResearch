# 机器人研究每日摘要 · 2026-10-19

> 自动生成,共 90 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (8 篇)

### 1. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 2. AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents

- **arXiv**: [2610.20474v1](https://arxiv.org/abs/2610.20474v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20474v1)
- **作者**: Peidong Wang, Ying Chang, Zhiming Ma et al.
- **发表**: 2026-10-14  ·  **类别**: cs.CL, cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the ex…

### 3. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

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

### 6. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 7. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 8. REKI: Registering Knowledge in VLAs

- **arXiv**: [2610.22178v1](https://arxiv.org/abs/2610.22178v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22178v1)
- **作者**: Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action e…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models

- **arXiv**: [2610.19108v1](https://arxiv.org/abs/2610.19108v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19108v1)
- **作者**: Mahdieh Mallahnezhad, Masoud Jafaripour, Mohamadali Tofigh et al.
- **发表**: 2026-10-13  ·  **类别**: cs.CV, cs.AI, cs.CL
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Multimodal Large Language Models (MLLMs) have been widely applied in embodied agents and robotics for vision tasks. However, MLLMs suffer from limitations in spatial reasoning and perception. Post-training techniques have shown promise for improving these capabilities; yet, there are limited data-driven surveys of such approaches. In this survey, we conside…

### 2. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 3. F2A-ObjectNav: An Adaptive Agentic Architecture for Object-Goal Navigation

- **arXiv**: [2610.19618v1](https://arxiv.org/abs/2610.19618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19618v1)
- **作者**: Seyed Ali Mirghasemi, Alireza Taheri
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Object-goal navigation requires an embodied agent to explore an unfamiliar environment, identify a target object, navigate toward candidate instances, and reliably determine whether the observed object satisfies the mission goal. This work investigates this problem through a two-stage development process. In Stage I, a fixed modular framework is used to exa…

### 4. From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents

- **arXiv**: [2610.19420v1](https://arxiv.org/abs/2610.19420v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19420v1)
- **作者**: Yue Zhang, Han Lin, Zun Wang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Simulated environments enable scalable training data generation for embodied agents, but more data does not necessarily provide what a particular agent needs to learn. Existing environment-generation pipelines largely optimize generic properties such as realism, diversity, or task coverage, while different pretrained policies can fail for different environm…

### 5. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

- **arXiv**: [2610.18617v1](https://arxiv.org/abs/2610.18617v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18617v1)
- **作者**: St John Grimbly, Nicolas Kuske, Evert A. Boonstra et al.
- **发表**: 2026-10-13  ·  **类别**: cs.AI, q-bio.NC
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask ho…

### 6. MemAct: Streaming Spatial Understanding with Memory and Active Exploration

- **arXiv**: [2610.17640v1](https://arxiv.org/abs/2610.17640v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17640v1)
- **作者**: Yuxi Wei, Wei Huang, Qirui Chen et al.
- **发表**: 2026-10-13  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Spatial understanding is essential for embodied agents navigating and interacting with the physical world. As observations arrive incrementally, agents must reason in a streaming manner. Yet streaming understanding must also be closed-loop: task-relevant evidence may require both recalling past observations and actively acquiring new views. Existing streami…

### 7. Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration

- **arXiv**: [2610.16895v1](https://arxiv.org/abs/2610.16895v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.16895v1)
- **作者**: Adrián Szlatincsán, Filippo Ziliotto, Bruno Lepri et al.
- **发表**: 2026-10-12  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: LLMs are used as high-level controllers for embodied agents, but it remains unclear whether they support collaborative reasoning, such as anticipating a collaborator's actions in real-time teamwork without dialogue. We ask if observing the partner's state, exchanging object knowledge, and predicting the partner's next action, shape task outcomes and coordin…

### 8. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 9. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

### 10. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

## 🦵 人形 / 足式机器人 (25 篇)

### 1. Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control

- **arXiv**: [2610.19393v1](https://arxiv.org/abs/2610.19393v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19393v1)
- **作者**: Lingfan Bao, Hanshang Zhu, Yan Pan et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessari…

### 2. SOMA: Stack-of-Objects Manipulation using a Quadruped Robot

- **arXiv**: [2610.20968v1](https://arxiv.org/abs/2610.20968v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20968v1)
- **作者**: Stergios E. Bachoumas, Panagiotis Artemiadis
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Executing heavy-duty physical manipulation in unpredictable environments remains a major challenge for quadrupedal robots lacking dedicated manipulators. This paper presents SOMA, a hierarchical reinforcement learning framework for whole-body non-prehensile manipulation of multi-object stacks using a quadruped robot. Unlike traditional methods restricted to…

### 3. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 4. CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation

- **arXiv**: [2610.21349v1](https://arxiv.org/abs/2610.21349v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21349v1)
- **作者**: Yanchen Ding, Jiayi Chen, Jianfeng Xu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable q…

### 5. Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

- **arXiv**: [2610.22342v1](https://arxiv.org/abs/2610.22342v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22342v1)
- **作者**: Tianxing Chen, Wenwei Lin, Chuqiao Lyu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, imag…

### 6. Whole-Body Dexterity

- **arXiv**: [2610.22184v1](https://arxiv.org/abs/2610.22184v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22184v1)
- **作者**: Conor Mc Gartoll, An Dang, Pranay Thangeda et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Current humanoid dexterous manipulation remains largely confined to end-effectors and simple grasps, falling short of humans' ability to engage the entire body by bracing and sliding bulky objects against the arms and torso. We introduce Whole-Body Dexterity (WBD), a general framework that uses the robot's body and appendages as contact surfaces to grasp an…

### 7. KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration

- **arXiv**: [2610.21152v1](https://arxiv.org/abs/2610.21152v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21152v1)
- **作者**: Zibo Zhou, Yueru Chen, Junsong Wu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that s…

### 8. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 9. KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation

- **arXiv**: [2610.20552v1](https://arxiv.org/abs/2610.20552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20552v1)
- **作者**: Qi Wu, Lulu Zhao, Sanghyun Hahn et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We present KinoGen, a framework that synthesizes customizable humanoid loco-manipulation references through kinematically grounded video generation. KinoGen conditions a pretrained video generator on calibrated renders of the target robot and object in a simulated task instance and recovers the reference by fitting the same models to the generated two-view…

### 10. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

- **arXiv**: [2610.18872v1](https://arxiv.org/abs/2610.18872v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18872v1)
- **作者**: Yunsong Zhou, Xuekun Jiang, Haiqi Shen et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce Ego…

## 🦾 操控 / 灵巧手 / 抓取 (28 篇)

### 1. HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning

- **arXiv**: [2610.19518v1](https://arxiv.org/abs/2610.19518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19518v1)
- **作者**: Linyi Huang, Guowei Huai, Weibin Liu et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: While multi-fingered dexterous robot hands have the potential to provide human-level dexterity, using them for functional manipulation remains difficult because task success depends on precise contact, coordinated arm-hand motion, and reactive recovery from execution errors. Precise contact depends on complex contact dynamics that are difficult to model acc…

### 2. OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes

- **arXiv**: [2610.11194v1](https://arxiv.org/abs/2610.11194v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11194v1)
- **作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous grasping is the foundational primitive in embodied AI, demanding massive data to train robust models. As real-world data collection is expensive, simulation has become the mainstream paradigm. Yet, while cluttered scenes best reflect real-world applications, learning to grasp within them is bottlenecked by a critical scarcity of large-scale data.…

### 3. FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models

- **arXiv**: [2610.22146v1](https://arxiv.org/abs/2610.22146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22146v1)
- **作者**: Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention…

### 4. DexMimic: A Generalist Dexterous Hand-Object Tracking Policy via Value-Guided Reset Allocation

- **arXiv**: [2610.19089v2](https://arxiv.org/abs/2610.19089v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19089v2)
- **作者**: Zhexi Luo, Zhixuan Xu, Rui Yang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Achieving human-like dexterous manipulation remains a central challenge in robotics. Learning from human hand-object interaction (HOI) datasets offers a promising pathway to diverse dexterous skills, yet existing physics-based approaches train specialist policies for individual trajectories, thereby limiting skill reuse at scale. We introduce DexMimic, a ge…

### 5. Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation

- **arXiv**: [2610.19753v1](https://arxiv.org/abs/2610.19753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19753v1)
- **作者**: Yiming Meng, Yanming Shao, Weijie Shen et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand inte…

### 6. EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization

- **arXiv**: [2610.17572v1](https://arxiv.org/abs/2610.17572v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17572v1)
- **作者**: Zhixin Sun, Kairui Shi, Tianao Ren et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: While expert demonstrations on real robots are difficult to collect, human ego-centric videos are easy to collect and abundant on the internet. However, learning dexterous manipulation policies from human videos remains challenging---one of the most important challenges being the difficulty of reconstructing physically grounded robot trajectories due to the…

### 7. Causal Analysis of Robot Foundation Models Enables Efficiency Gains

- **arXiv**: [2610.20750v1](https://arxiv.org/abs/2610.20750v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20750v1)
- **作者**: Aiden Swann, Mathilde Papillon, Mozes Jacobs et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

- **arXiv**: [2610.22363v1](https://arxiv.org/abs/2610.22363v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22363v1)
- **作者**: Zirui Wu, Chen Guo, Tianjian Jiang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed…

### 10. Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation

- **arXiv**: [2610.21180v1](https://arxiv.org/abs/2610.21180v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21180v1)
- **作者**: Bing Cheng, Yiran Mao, Zewei Ye et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: General-purpose dexterous manipulation requires policies to transfer knowledge from related tasks to new tasks with only a few target demonstrations. Existing benchmarks often provide too many target demonstrations. They also leave the differences between source and target tasks uncontrolled. As a result, they cannot clearly distinguish knowledge transfer f…

## 🎓 模仿学习 / 强化学习 (9 篇)

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

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (8 篇)

### 1. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 2. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 3. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 4. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 5. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 6. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 7. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 8. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

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
1. [HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning](https://arxiv.org/abs/2610.19518v1) — score 19
2. [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194v1) — score 17
3. [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146v1) — score 16

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
