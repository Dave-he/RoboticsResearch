# 机器人研究每日摘要 · 2026-06-18

> 自动生成,共 92 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (3 篇)

### 1. Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models

- **arXiv**: [2606.19297v1](https://arxiv.org/abs/2606.19297v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.19297v1)
- **作者**: Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin et al.
- **发表**: 2026-06-17  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and factual knowledge they retain after adaptation. Failures on knowledge-sensitive tasks are ambiguous, conflating missing knowledge with poor generalization of low-level control. We introduce…

### 2. Robots Need More than VLA and World Models

- **arXiv**: [2606.06556v1](https://arxiv.org/abs/2606.06556v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06556v1)
- **作者**: Elis Karcini, Faisal Mehrban, Quang Nguyen et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation. In this position paper, we argue that this framing is incomplete. The central bottleneck is not only policy learning, but the absence of mechanisms that convert the…

### 3. Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems

- **arXiv**: [2606.00090v1](https://arxiv.org/abs/2606.00090v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00090v1)
- **作者**: Barak Or
- **发表**: 2026-05-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Physical AI systems increasingly map multimodal observations, language instructions, and learned world representations into physically consequential actions. Robotics foundation models, vision-language-action models, and world-model-based autonomous systems can condition decisions that move vehicles, robots, drones, and industrial machines. This transition…

## 🌐 具身智能 / 机器人基础模型 (7 篇)

### 1. ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI

- **arXiv**: [2606.17639v2](https://arxiv.org/abs/2606.17639v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17639v2)
- **作者**: Hong Yang, Basura Fernando
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Generalist embodied agents require more than object recognition: they must reason about spatial relations, actions, procedures, human intentions, environmental constraints, and commonsense consequences from situated visual observations. Yet existing visual and embodied question answering benchmarks often provide limited control over the reasoning dependenci…

### 2. ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM

- **arXiv**: [2606.00307v1](https://arxiv.org/abs/2606.00307v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00307v1)
- **作者**: Yuhao Zhang, Yifu Tao, Frank Dellaert et al.
- **发表**: 2026-05-29  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Recent works have explored unifying SLAM with geometric foundation models (GFMs). However, directly using GFM predictions for tracking is highly sensitive to model capability and uncertainty, as geometric inaccuracies in the predictions can adversely affect pose estimation. To address this limitation, we present a decoupled framework that integrates classic…

### 3. MagicSim: A Unified Infrastructure for Executable Embodied Interaction

- **arXiv**: [2606.17511v1](https://arxiv.org/abs/2606.17511v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17511v1)
- **作者**: Haoran Lu, Songling Liu, Yue Chen et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot learning and embodied agents now require simulation to serve as a shared execution substrate linking control, skills, and planning, not only as a renderer, controller testbed, or fixed task environment. Existing pipelines split these layers with "magic" actions, disconnected training environments, or forward-only renders that cannot reproduce, evaluat…

### 4. WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

- **arXiv**: [2606.18847v1](https://arxiv.org/abs/2606.18847v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18847v1)
- **作者**: Yehang Zhang, Jianchong Su, Haojian Huang et al.
- **发表**: 2026-06-17  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while embodied benchmarks often focus on short-horizon task execution without testing long-term memory use in dynamic e…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation

- **arXiv**: [2606.18235v1](https://arxiv.org/abs/2606.18235v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18235v1)
- **作者**: Qi Chai, Wenhao Shen, Nanjie Yao et al.
- **发表**: 2026-06-16  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Zero-Shot Object-Goal Navigation (ZS-OGN) requires embodied agents to explore and locate target objects without any prior training. To this end, recent methods leverage foundation models. But they typically rely on static priors and lack adaptation, which leads to repeated errors and costly trial and error. In this paper, we propose a self-evolving ZS-OGN f…

### 7. From Ad Hoc Pilots to Repeatable Patterns: Structuring Drone Collaboration in Emergency Services with DroneLets

- **arXiv**: [2606.17839v1](https://arxiv.org/abs/2606.17839v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17839v1)
- **作者**: Dzmitry Katsiuba, Samuel Brander, Mateusz Dolata et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.HC
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Drones hold promise for supporting emergency services, but their integration into workflows remains ad hoc and coordination-intensive. This paper addresses two research questions: how emergency teams want to collaborate with drones, and how to formalize these collaborations into repeatable processes. Based on four field trials and 95 interviews, we derive 4…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

- **arXiv**: [2606.17011v1](https://arxiv.org/abs/2606.17011v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17011v1)
- **作者**: Wei Xiao, Weiliang Tang, Yuying Ge et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human interventions provide crucial corrective signals for post-training Vision-Language-Action (VLA) models. However, enabling seamless humanoid interventions is a formidable systems challenge due to complex whole-body kinematics and dexterous-hand control. Consequently, the collected intervention trajectories are often suboptimal, and methods that rely on…

### 2. Energy-Efficient Arm Reaching for a Humanoid Robot via Deep Reinforcement Learning with Identified Power Models

- **arXiv**: [2606.15918v1](https://arxiv.org/abs/2606.15918v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15918v1)
- **作者**: Nestor N. Deniz, Simon Parsons, Fernando Auat Cheein
- **发表**: 2026-06-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid r…

### 3. HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations

- **arXiv**: [2606.18772v1](https://arxiv.org/abs/2606.18772v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18772v1)
- **作者**: Zehui Zhao, Yuxuan Zhao, Gaojing Zhang et al.
- **发表**: 2026-06-17  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Human demonstrations, which can be collected at scale and naturally capture active hand-eye coordination, are a promising data source for learning humanoid loco-manipulation. However, directly transferring human demonstrations to humanoids requires a precise world-frame tracking controller, which is often brittle under Out-of-Distribution(OOD) targets, whil…

### 4. Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots

- **arXiv**: [2606.19067v1](https://arxiv.org/abs/2606.19067v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.19067v1)
- **作者**: Roberto Corlito, Fabian Schmidt, Nils Seibert et al.
- **发表**: 2026-06-17  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Autonomous navigation of quadrupedal robots in diverse environments fundamentally relies on resilient Simultaneous Localization and Mapping (SLAM). While visual-inertial SLAM has matured across wheeled, handheld, and aerial platforms, a critical evaluation gap remains regarding how hardware-level sensor configurations affect performance under the aggressive…

### 5. WaveSync: Constrained Wavefront Optimization for Synchronized Co-Speech Gestures in Humanoid Robots

- **arXiv**: [2606.16600v1](https://arxiv.org/abs/2606.16600v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16600v1)
- **作者**: Thang Tran Viet, Thanh Nguyen Canh, Gia Huy Uong et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Expressive co-speech gestures are crucial for natural human-robot interaction, but generating them on physical humanoid robots is difficult because gesture strokes must align with speech emphasis while satisfying strict kinematic and dynamic constraints. Unlike virtual avatars, humanoid robots cannot freely execute rapid or overlapping motions, making word-…

### 6. DragMesh-2: Physically Plausible Dexterous Hand-Object Interaction with Articulated Objects

- **arXiv**: [2606.15133v1](https://arxiv.org/abs/2606.15133v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15133v1)
- **作者**: Tianshan Zhang, Yijia Duan, Yanjun Li et al.
- **发表**: 2026-06-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Dexterous interaction with articulated objects is important for household, assistive, and humanoid manipulation, where multi-finger hands can provide compliant contact patterns beyond parallel-jaw grasping. However, articulated-object manipulation differs from static-object manipulation: the target part cannot be directly actuated, and its motion must emerg…

### 7. M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking

- **arXiv**: [2606.04829v1](https://arxiv.org/abs/2606.04829v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.04829v1)
- **作者**: Zuxing Lu, Ziang Zheng, Yao Lyu et al.
- **发表**: 2026-06-03  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on distinct motion reference modalities: locomotion primarily depends on coordinated robot joint trajectories, whereas manipulation…

### 8. SRL: Combining SLIP Model and Reinforcement Learning for Agile Robotic Jumping

- **arXiv**: [2606.18625v1](https://arxiv.org/abs/2606.18625v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18625v1)
- **作者**: Xiaowen Hu, Linqi Ye, Yudi Zhu et al.
- **发表**: 2026-06-17  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Robotic jumping is pivotal in applications such as search and rescue and logistics, where crossing obstacles and enhancing mobility efficiency are critical. The Spring-Loaded Inverted Pendulum (SLIP) model leverages simplified spring-mass dynamics that naturally encode biologically plausible hopping motions, yet its performance degrades on irregular terrain…

### 9. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

- **arXiv**: [2606.06493v3](https://arxiv.org/abs/2606.06493v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06493v3)
- **作者**: Lizhi Yang, Junheng Li, Nehar Poddar et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface tha…

### 10. Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs

- **arXiv**: [2606.18747v1](https://arxiv.org/abs/2606.18747v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18747v1)
- **作者**: Chris Lee, Flora Salim, Benjamin Tag et al.
- **发表**: 2026-06-17  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Expressive gestures are essential for natural and effective communication, complementing speech when verbal cues alone are insufficient (e.g., pointing). For social robots such as the humanoid Pepper, producing natural and expressive movements is critical for improving human-robot interaction (HRI) and long-term acceptance. However, generating gestures rema…

## 🦾 操控 / 灵巧手 / 抓取 (40 篇)

### 1. T-Rex: Tactile-Reactive Dexterous Manipulation

- **arXiv**: [2606.17055v1](https://arxiv.org/abs/2606.17055v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17055v1)
- **作者**: Dantong Niu, Zhuoyang Liu, Zekai Wang et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO
- **相关性评分**: 23  ·  **🔥 read_now**
- **摘要**: The ability to react dynamically to tactile signals has long been considered crucial to agile human-level dexterity. Yet contemporary learning-based Vision-Language-Action (VLA) models for robotic manipulation generally either overlook the tactile modality or are limited to encoders with static cues, due in part to the scarcity of diverse training data and…

### 2. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

- **arXiv**: [2606.17598v1](https://arxiv.org/abs/2606.17598v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17598v1)
- **作者**: Xingyuming Liu, Ruichun Ma, Heyu Guo et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present…

### 3. WireCraft: A Simulation Benchmark for Industrial DLO Manipulation

- **arXiv**: [2606.18097v1](https://arxiv.org/abs/2606.18097v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18097v1)
- **作者**: Chongyu Zhu, Ramy ElMallah, Hyegang Kim et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Deformable Linear Objects (DLOs), such as wires and cables, are central to industrial assembly. Unlike rigid objects, whose state is captured by a 6-DoF pose, DLOs have an infinite-dimensional configuration space and deform continuously under contact with grippers, fixtures, and the workspace, making them a demanding benchmark for general dexterous manipula…

### 4. Transferring Contact, Not Just Motion: Compliant Grasping Across Dexterous Hands

- **arXiv**: [2606.15516v1](https://arxiv.org/abs/2606.15516v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15516v1)
- **作者**: Soofiyan Atar, Yao-Ting Huang, Michael Yip
- **发表**: 2026-06-14  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous grasping depends on contact regulation, not motion alone. Stable manipulation requires fingers to maintain appropriate object loading as contacts slip, deform, or become visually occluded. Existing cross-embodiment dexterous policies unify motion through retargeted hand poses or latent actions, but force feedback remains tied to each hand's sensin…

### 5. V2P-Manip: Learning Dexterous Manipulation from Monocular Human Videos

- **arXiv**: [2606.16436v1](https://arxiv.org/abs/2606.16436v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16436v1)
- **作者**: Kaihan Chen, Yanming Shao, Haifeng Ji et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Achieving autonomous robotic dexterous manipulation requires precise, human-like action sequences at scale. As a scalable supplement to costly teleoperation data, extracting trajectories with both visual fidelity and physical plausibility from monocular videos represents a promising frontier in embodied AI. To this end, we introduce V2P-Manip, an efficient…

### 6. Zero-Shot Long-Horizon Dexterous Manipulation via Multi-View 3D-Grounded VLM Reasoning

- **arXiv**: [2606.19340v1](https://arxiv.org/abs/2606.19340v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.19340v1)
- **作者**: Jisoo Kim, Sangwon Baik, Taeksoo Kim et al.
- **发表**: 2026-06-17  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: We present a zero-shot framework for long-horizon dexterous manipulation that grounds language instructions into executable 3D task plans from calibrated multi-view RGB images. Rather than training an end-to-end policy, our system uses a vision-language model (VLM) to produce reference-frame task grounding and primitive-level 2D keypoints, then lifts them i…

### 7. Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

- **arXiv**: [2606.18953v1](https://arxiv.org/abs/2606.18953v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18953v1)
- **作者**: Kinam Kim, Namiko Saito, Heecheol Kim et al.
- **发表**: 2026-06-17  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models can generalize across diverse manipulation tasks, but their imitation-learning-based policies remain brittle in precise physical interactions due to compounding execution errors; Can a reinforcement learning policy trained purely in simulation improve the robustness of real-world VLAs zero-shot? Residual RL, which learns…

### 8. R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

- **arXiv**: [2606.17040v1](https://arxiv.org/abs/2606.17040v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17040v1)
- **作者**: Xiuwei Xu, Haowen Sun, Angyuan Ma et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Spatial generalization is critical for imitation-learned manipulation policies, but achieving it typically requires scaling demonstrations across diverse object poses, robot configurations, and camera viewpoints. Data augmentation from a few source demonstrations offers a practical alternative to costly real-world collection. Simulation-based augmentation c…

### 9. Steering Autoregressive Vision-Language-Action Policies via Action Token Intervention

- **arXiv**: [2606.15021v1](https://arxiv.org/abs/2606.15021v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15021v1)
- **作者**: Jason Chan, Jonathan C. Kao
- **发表**: 2026-06-12  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We present Token Steering (TS), a method for dynamically steering trajectories generated by an autoregressive vision-language-action (VLA) model through direct intervention in the action-token space. TS injects low-dimensional user inputs into the model's native action-token representation, allowing users to influence trajectory generation without modifying…

### 10. A Bilateral Teleoperation Framework for Dexterous Manipulation

- **arXiv**: [2606.15434v1](https://arxiv.org/abs/2606.15434v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15434v1)
- **作者**: Stefano Dalla Gasperina, Dong Ho Kang, Haiyun Zhang et al.
- **发表**: 2026-06-13  ·  **类别**: cs.RO, cs.HC, eess.SY
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Dexterous teleoperation requires precise arm-hand coordination, low-latency feedback, and robust interaction in real-world contact-rich environments. This paper presents a modular bilateral teleoperation framework that integrates operator-side input interfaces with a robot-side dexterous hand and compliant robotic arm in a unified control architecture. The…

## 🎓 模仿学习 / 强化学习 (9 篇)

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

### 3. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 4. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 5. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 6. Dual Pose-Graph Semantic Localization for Vision-Based Autonomous Drone Racing

- **arXiv**: [2604.15168v1](https://arxiv.org/abs/2604.15168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.15168v1)
- **作者**: David Perez-Saura, Miguel Fernandez-Cortizas, Alvaro J. Gaona et al.
- **发表**: 2026-04-16  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Autonomous drone racing demands robust real-time localization under extreme conditions: high-speed flight, aggressive maneuvers, and payload-constrained platforms that often rely on a single camera for perception. Existing visual SLAM systems, while effective in general scenarios, struggle with motion blur and feature instability inherent to racing dynamics…

### 7. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 8. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

### 9. NeRF and Gaussian Splatting SLAM in the Wild

- **arXiv**: [2412.03263v1](https://arxiv.org/abs/2412.03263v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.03263v1)
- **作者**: Fabian Schmidt, Markus Enzweiler, Abhinav Valada
- **发表**: 2024-12-04  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Navigating outdoor environments with visual Simultaneous Localization and Mapping (SLAM) systems poses significant challenges due to dynamic scenes, lighting variations, and seasonal changes, requiring robust solutions. While traditional SLAM methods struggle with adaptability, deep learning-based approaches and emerging neural radiance fields as well as Ga…

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
- **相关性评分**: 8  ·  **👀 watch**
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
1. [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055v1) — score 23
2. [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](https://arxiv.org/abs/2606.17598v1) — score 21
3. [WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](https://arxiv.org/abs/2606.18097v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
