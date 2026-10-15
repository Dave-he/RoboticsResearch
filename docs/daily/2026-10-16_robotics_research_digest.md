# 机器人研究每日摘要 · 2026-10-16

> 自动生成,共 89 篇命中论文。

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
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the ex…

### 3. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 4. What Matters for World Modeling in Vision-Language-Action Models?

- **arXiv**: [2610.19825v1](https://arxiv.org/abs/2610.19825v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19825v1)
- **作者**: Qisen Ma, Yixiang Chen, Yuan Xu et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping. However, existing approaches vary simultaneously in their world representations, integration paradigms, and policy backbones, making it difficult to determine…

### 5. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 6. SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving

- **arXiv**: [2610.20609v1](https://arxiv.org/abs/2610.20609v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20609v1)
- **作者**: Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue ins…

### 7. Towards Agentic Robots: Model, Data, Environment, and Harness

- **arXiv**: [2610.20442v1](https://arxiv.org/abs/2610.20442v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20442v1)
- **作者**: Chonghan Qin, Dongming Wu, Kaituo Feng et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic enviro…

### 8. Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand

- **arXiv**: [2610.20351v1](https://arxiv.org/abs/2610.20351v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20351v1)
- **作者**: Nagasrikanth Kallakuri
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Human demonstrations are today used largely for pretraining vision-language-action models, with little ability to use the same data for target-embodiment or task-oriented training, which scalable deployment of robots in industrial and general environments depends on. A human demonstration recorded on a simple and scalable device such as a mobile phone can s…

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

### 8. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 10. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads

- **arXiv**: [2610.12972v1](https://arxiv.org/abs/2610.12972v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12972v1)
- **作者**: Manh Cuong Nguyen, Duc Cuong Vu, Viet Anh Vu et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads. However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predict…

### 2. Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control

- **arXiv**: [2610.19393v1](https://arxiv.org/abs/2610.19393v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19393v1)
- **作者**: Lingfan Bao, Hanshang Zhu, Yan Pan et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessari…

### 3. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 4. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 5. Modeling and Control of a Rigid-soft Hybrid-link Humanoid Robot

- **arXiv**: [2610.15073v1](https://arxiv.org/abs/2610.15073v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15073v1)
- **作者**: Zewen He, Taiki Ishigaki, Ko Yamamoto
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Physical flexibility plays a significant role not only in human motions but also in robot motions. For example, a humanoid robot with passive and flexible elements, which can be regarded as a rigid--soft hybrid-link system, has the advantages of storing energy and mitigating impact in a dynamic motion. However, the motion design and control of a hybrid-link…

### 6. PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface

- **arXiv**: [2610.12558v1](https://arxiv.org/abs/2610.12558v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12558v1)
- **作者**: Xiaomeng Xu, Han Zhang, Zhian Ruan et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body su…

### 7. KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation

- **arXiv**: [2610.20552v1](https://arxiv.org/abs/2610.20552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20552v1)
- **作者**: Qi Wu, Lulu Zhao, Sanghyun Hahn et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We present KinoGen, a framework that synthesizes customizable humanoid loco-manipulation references through kinematically grounded video generation. KinoGen conditions a pretrained video generator on calibrated renders of the target robot and object in a simulated task instance and recovers the reference by fitting the same models to the generated two-view…

### 8. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

- **arXiv**: [2610.18872v1](https://arxiv.org/abs/2610.18872v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18872v1)
- **作者**: Yunsong Zhou, Xuekun Jiang, Haiqi Shen et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce Ego…

### 9. TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments

- **arXiv**: [2610.17999v1](https://arxiv.org/abs/2610.17999v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17999v1)
- **作者**: Qingyu Lan, Zhihao Tian, Zifan Wang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to t…

### 10. Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation

- **arXiv**: [2610.13087v1](https://arxiv.org/abs/2610.13087v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13087v1)
- **作者**: Chen Yu, Sudarshan S Harithas, Juan Borbon et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop, c…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning

- **arXiv**: [2610.19518v1](https://arxiv.org/abs/2610.19518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19518v1)
- **作者**: Linyi Huang, Guowei Huai, Weibin Liu et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: While multi-fingered dexterous robot hands have the potential to provide human-level dexterity, using them for functional manipulation remains difficult because task success depends on precise contact, coordinated arm-hand motion, and reactive recovery from execution errors. Precise contact depends on complex contact dynamics that are difficult to model acc…

### 2. DexMimic: A Generalist Dexterous Hand-Object Tracking Policy via Value-Guided Reset Allocation

- **arXiv**: [2610.19089v1](https://arxiv.org/abs/2610.19089v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19089v1)
- **作者**: Zhexi Luo, Zhixuan Xu, Rui Yang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Achieving human-like dexterous manipulation remains a central challenge in robotics. Learning from human hand-object interaction (HOI) datasets offers a promising pathway to diverse dexterous skills, yet existing physics-based approaches train specialist policies for individual trajectories, thereby limiting skill reuse at scale. We introduce DexMimic, a ge…

### 3. OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes

- **arXiv**: [2610.11194v1](https://arxiv.org/abs/2610.11194v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11194v1)
- **作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous grasping is the foundational primitive in embodied AI, demanding massive data to train robust models. As real-world data collection is expensive, simulation has become the mainstream paradigm. Yet, while cluttered scenes best reflect real-world applications, learning to grasp within them is bottlenecked by a critical scarcity of large-scale data.…

### 4. ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction

- **arXiv**: [2610.20223v1](https://arxiv.org/abs/2610.20223v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20223v1)
- **作者**: Huailiang Ma, Yuxuan Li, Ziyi Zhao et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions. However, most existing VLA models still operate on image-level visual representations inherited from pretrained vision-language backbones, while lacking fine-grained object…

### 5. EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization

- **arXiv**: [2610.17572v1](https://arxiv.org/abs/2610.17572v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17572v1)
- **作者**: Zhixin Sun, Kairui Shi, Tianao Ren et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: While expert demonstrations on real robots are difficult to collect, human ego-centric videos are easy to collect and abundant on the internet. However, learning dexterous manipulation policies from human videos remains challenging---one of the most important challenges being the difficulty of reconstructing physically grounded robot trajectories due to the…

### 6. Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation

- **arXiv**: [2610.19753v1](https://arxiv.org/abs/2610.19753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19753v1)
- **作者**: Yiming Meng, Yanming Shao, Weijie Shen et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand inte…

### 7. DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine

- **arXiv**: [2610.17208v1](https://arxiv.org/abs/2610.17208v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17208v1)
- **作者**: Haozhe Lou, Runyi Yang, Wanqi Zhong et al.
- **发表**: 2026-10-12  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Cutting a piece of food looks effortless in human hands. For a robot, however, every cut is a high-contact interaction with a deformable, elasto-plastic object whose behavior changes with pose, contact mode, and cutting stage. Collecting real-world data is expensive and wasteful: each trial typically contaminates or damages the food, so obtaining scalable r…

### 8. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

### 9. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 10. TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation

- **arXiv**: [2610.20320v1](https://arxiv.org/abs/2610.20320v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20320v1)
- **作者**: Fucai Zhu, Xidong Zhang, Yichi Zhang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Large-scale robot learning increasingly relies on diverse human demonstrations, yet tactile manipulation data remain difficult to scale, and existing multimodal datasets often lack consistent quality control and structured supervision. We present TacClaw-Infinity, a large-scale structured Vision-Tactile-Language-Action (VTLA) dataset for contact-rich manipu…

## 🎓 模仿学习 / 强化学习 (12 篇)

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

### 6. Runtime Monitoring of Supermartingale Certificates

- **arXiv**: [2610.19701v1](https://arxiv.org/abs/2610.19701v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19701v1)
- **作者**: Mirco Giacobbe, Thomas A. Henzinger, Konstantin Kueffner et al.
- **发表**: 2026-10-14  ·  **类别**: cs.AI, eess.SY
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Supermartingale certificates formally guarantee temporal properties of discrete and continuous-time stochastic dynamical systems. However, these guarantees rely on a mathematical model of the world, leaving a sim-to-real gap that can invalidate them for the deployed system. We formulate the runtime monitoring problem for supermartingale certificates, in whi…

### 7. WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

- **arXiv**: [2610.18846v1](https://arxiv.org/abs/2610.18846v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18846v1)
- **作者**: Mengchen Zhang, Yang Li, Chunshi Wang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RG…

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

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 2. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 3. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

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
1. [HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning](https://arxiv.org/abs/2610.19518v1) — score 20
2. [DexMimic: A Generalist Dexterous Hand-Object Tracking Policy via Value-Guided Reset Allocation](https://arxiv.org/abs/2610.19089v1) — score 17
3. [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194v1) — score 17

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
