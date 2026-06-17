# 机器人研究每日摘要 · 2026-06-17

> 自动生成,共 82 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (3 篇)

### 1. PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space

- **arXiv**: [2606.17924v1](https://arxiv.org/abs/2606.17924v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17924v1)
- **作者**: Bochen Yang, Lianlei Shan
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial…

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

## 🌐 具身智能 / 机器人基础模型 (8 篇)

### 1. ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI

- **arXiv**: [2606.17639v1](https://arxiv.org/abs/2606.17639v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17639v1)
- **作者**: Hong Yang, Basura Fernando
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Generalist embodied agents require more than object recognition: they must reason about spatial relations, actions, procedures, human intentions, environmental constraints, and commonsense consequences from situated visual observations. Yet existing visual and embodied question answering benchmarks often provide limited control over the reasoning dependenci…

### 2. Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents

- **arXiv**: [2606.13097v1](https://arxiv.org/abs/2606.13097v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.13097v1)
- **作者**: Saehun Chun, Wonje Choi, Sera Choi et al.
- **发表**: 2026-06-11  ·  **类别**: cs.PL, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Code-writing large language models (CodeLLMs) generate executable code policies for embodied agents by translating natural language goals and environmental constraints into structured control programs. However, policy generation in open-domain embodied environments suffers from two fundamental limitations: (i) delayed decoding caused by repetitive prefill c…

### 3. ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM

- **arXiv**: [2606.00307v1](https://arxiv.org/abs/2606.00307v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00307v1)
- **作者**: Yuhao Zhang, Yifu Tao, Frank Dellaert et al.
- **发表**: 2026-05-29  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Recent works have explored unifying SLAM with geometric foundation models (GFMs). However, directly using GFM predictions for tracking is highly sensitive to model capability and uncertainty, as geometric inaccuracies in the predictions can adversely affect pose estimation. To address this limitation, we present a decoupled framework that integrates classic…

### 4. MagicSim: A Unified Infrastructure for Executable Embodied Interaction

- **arXiv**: [2606.17511v1](https://arxiv.org/abs/2606.17511v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17511v1)
- **作者**: Haoran Lu, Songling Liu, Yue Chen et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot learning and embodied agents now require simulation to serve as a shared execution substrate linking control, skills, and planning, not only as a renderer, controller testbed, or fixed task environment. Existing pipelines split these layers with "magic" actions, disconnected training environments, or forward-only renders that cannot reproduce, evaluat…

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

### 8. Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization

- **arXiv**: [2606.16898v1](https://arxiv.org/abs/2606.16898v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16898v1)
- **作者**: Dongbin Na, Chanwoo Kim, Giyun Choi et al.
- **发表**: 2026-06-15  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Detecting unanswerable user queries remains essential for the reliable deployment of real-world embodied agents. However, modern vision-language models (VLMs) often generate overly confident answers even when the available visual memory cannot support the query. Such overconfidence poses various task-dependent risks. The agent may provide misleading informa…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation

- **arXiv**: [2604.21541v1](https://arxiv.org/abs/2604.21541v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.21541v1)
- **作者**: Yan Ning, Xingzhou Chen, Delong Li et al.
- **发表**: 2026-04-23  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Wheel-legged robots combine the efficiency of wheeled locomotion with the versatility of legged systems, enabling rapid traversal over both continuous and discrete terrains. However, conventional designs typically employ fixed wheels as feet and limited degrees of freedom (DoFs) at the hips, resulting in reduced stability and mobility during legged locomoti…

### 2. PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots

- **arXiv**: [2605.17681v1](https://arxiv.org/abs/2605.17681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.17681v1)
- **作者**: Jiarong Kang, Kunzhao Ren, Tao Pang et al.
- **发表**: 2026-05-17  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Humanoid and legged robots interact with the environment through intermittent contacts, making accurate motion estimation fundamentally dependent on reasoning about contact dynamics. However, standard sensing pipelines-whether based on onboard proprioception with Extended Kalman Filters (EKFs) or external motion capture systems-recover only kinematics, whil…

### 3. ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

- **arXiv**: [2606.17011v1](https://arxiv.org/abs/2606.17011v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17011v1)
- **作者**: Wei Xiao, Weiliang Tang, Yuying Ge et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human interventions provide crucial corrective signals for post-training Vision-Language-Action (VLA) models. However, enabling seamless humanoid interventions is a formidable systems challenge due to complex whole-body kinematics and dexterous-hand control. Consequently, the collected intervention trajectories are often suboptimal, and methods that rely on…

### 4. Energy-Efficient Arm Reaching for a Humanoid Robot via Deep Reinforcement Learning with Identified Power Models

- **arXiv**: [2606.15918v1](https://arxiv.org/abs/2606.15918v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15918v1)
- **作者**: Nestor N. Deniz, Simon Parsons, Fernando Auat Cheein
- **发表**: 2026-06-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid r…

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

### 8. GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training

- **arXiv**: [2606.12995v1](https://arxiv.org/abs/2606.12995v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12995v1)
- **作者**: Zhihai Bi, Qiang Zhang, Guoyang Zhao et al.
- **发表**: 2026-06-11  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to the tight coupling between dynamic balance and stable interaction with diverse objects. Existing methods often require time-consuming task-specific policy training or rely on rigid trajectory replay, which limits their ability to accommodate…

### 9. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

- **arXiv**: [2606.06493v3](https://arxiv.org/abs/2606.06493v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06493v3)
- **作者**: Lizhi Yang, Junheng Li, Nehar Poddar et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface tha…

### 10. Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms

- **arXiv**: [2606.14617v1](https://arxiv.org/abs/2606.14617v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.14617v1)
- **作者**: Yongyan Cao
- **发表**: 2026-06-12  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Floating-base robots must balance under rigid contact constraints while interacting safely with humans. Existing whole-body control~(WBC) frameworks allocate the full joint space to locomotion or rely on fixed-gain impedance feedback that accumulates steady-state error under sustained physical human--robot interaction~(pHRI) forces. This paper extends the a…

## 🦾 操控 / 灵巧手 / 抓取 (25 篇)

### 1. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

- **arXiv**: [2606.17598v1](https://arxiv.org/abs/2606.17598v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17598v1)
- **作者**: Xingyuming Liu, Ruichun Ma, Heyu Guo et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present…

### 2. Transferring Contact, Not Just Motion: Compliant Grasping Across Dexterous Hands

- **arXiv**: [2606.15516v1](https://arxiv.org/abs/2606.15516v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15516v1)
- **作者**: Soofiyan Atar, Yao-Ting Huang, Michael Yip
- **发表**: 2026-06-14  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous grasping depends on contact regulation, not motion alone. Stable manipulation requires fingers to maintain appropriate object loading as contacts slip, deform, or become visually occluded. Existing cross-embodiment dexterous policies unify motion through retargeted hand poses or latent actions, but force feedback remains tied to each hand's sensin…

### 3. WireCraft: A Simulation Benchmark for Industrial DLO Manipulation

- **arXiv**: [2606.18097v1](https://arxiv.org/abs/2606.18097v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18097v1)
- **作者**: Chongyu Zhu, Ramy ElMallah, Hyegang Kim et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Deformable Linear Objects (DLOs), such as wires and cables, are central to industrial assembly. Unlike rigid objects, whose state is captured by a 6-DoF pose, DLOs have an infinite-dimensional configuration space and deform continuously under contact with grippers, fixtures, and the workspace, making them a demanding benchmark for general dexterous manipula…

### 4. V2P-Manip: Learning Dexterous Manipulation from Monocular Human Videos

- **arXiv**: [2606.16436v1](https://arxiv.org/abs/2606.16436v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16436v1)
- **作者**: Kaihan Chen, Yanming Shao, Haifeng Ji et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Achieving autonomous robotic dexterous manipulation requires precise, human-like action sequences at scale. As a scalable supplement to costly teleoperation data, extracting trajectories with both visual fidelity and physical plausibility from monocular videos represents a promising frontier in embodied AI. To this end, we introduce V2P-Manip, an efficient…

### 5. Mana: Dexterous Manipulation of Articulated Tools

- **arXiv**: [2606.13677v1](https://arxiv.org/abs/2606.13677v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.13677v1)
- **作者**: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel et al.
- **发表**: 2026-06-11  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Articulated tool manipulation remains a major challenge in dexterous robotics due to the need to coordinate internal degrees of freedom and contact-rich interactions. While prior work has largely focused on rigid objects, articulated tool use remains underexplored because of its physical complexity and the difficulty of learning functional grasping and mani…

### 6. R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

- **arXiv**: [2606.17040v1](https://arxiv.org/abs/2606.17040v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.17040v1)
- **作者**: Xiuwei Xu, Haowen Sun, Angyuan Ma et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Spatial generalization is critical for imitation-learned manipulation policies, but achieving it typically requires scaling demonstrations across diverse object poses, robot configurations, and camera viewpoints. Data augmentation from a few source demonstrations offers a practical alternative to costly real-world collection. Simulation-based augmentation c…

### 7. Steering Autoregressive Vision-Language-Action Policies via Action Token Intervention

- **arXiv**: [2606.15021v1](https://arxiv.org/abs/2606.15021v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15021v1)
- **作者**: Jason Chan, Jonathan C. Kao
- **发表**: 2026-06-12  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We present Token Steering (TS), a method for dynamically steering trajectories generated by an autoregressive vision-language-action (VLA) model through direct intervention in the action-token space. TS injects low-dimensional user inputs into the model's native action-token representation, allowing users to influence trajectory generation without modifying…

### 8. SimWeaver: Zero-Shot RGB Sim-to-Real for Deformable Manipulation

- **arXiv**: [2606.15338v1](https://arxiv.org/abs/2606.15338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15338v1)
- **作者**: Wenkang Hu, Haoran Wang, Yitong Li et al.
- **发表**: 2026-06-13  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: RGB sim-to-real for deformable manipulation has remained largely unsolved without real-world fine-tuning. We present SimWeaver, which trains zero-shot RGB VLA policies on 200 simulated demonstrations per task, reaching above 80% per-task and 91% average real-world success across 5 diverse deformable tasks including plastic-bag manipulation, without teleoper…

### 9. A Bilateral Teleoperation Framework for Dexterous Manipulation

- **arXiv**: [2606.15434v1](https://arxiv.org/abs/2606.15434v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15434v1)
- **作者**: Stefano Dalla Gasperina, Dong Ho Kang, Haiyun Zhang et al.
- **发表**: 2026-06-13  ·  **类别**: cs.RO, cs.HC, eess.SY
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Dexterous teleoperation requires precise arm-hand coordination, low-latency feedback, and robust interaction in real-world contact-rich environments. This paper presents a modular bilateral teleoperation framework that integrates operator-side input interfaces with a robot-side dexterous hand and compliant robotic arm in a unified control architecture. The…

### 10. Uncertainty Quantification for Flow-Based Vision-Language-Action Models

- **arXiv**: [2606.18043v1](https://arxiv.org/abs/2606.18043v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.18043v1)
- **作者**: Ralf Römer, Maximilian Seeliger, Saida Liu et al.
- **发表**: 2026-06-16  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action models (VLAs) combine vision-language backbones with expressive generative action heads trained via flow matching on large-scale robotic datasets. Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms to quantify confidence in their predictions and to detect when their actions may be unreliable. This…

## 🎓 模仿学习 / 强化学习 (11 篇)

### 1. Agile Fall Recovery for Quadrotors with Bidirectional Thrust via Reinforcement Learning

- **arXiv**: [2606.16513v1](https://arxiv.org/abs/2606.16513v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16513v1)
- **作者**: Anke Zhao, Yuhang Zhong, Kenghou Hoi et al.
- **发表**: 2026-06-15  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous fall recovery is a critical capability for quadrotors operating in real-world environments, where collisions or failures may leave the vehicle resting on the ground in an arbitrary attitude. This problem is challenging because recovery must be achieved under limited onboard sensing, in constrained free space, with ground contact, and in the prese…

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

### 5. RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos

- **arXiv**: [2606.16278v1](https://arxiv.org/abs/2606.16278v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16278v1)
- **作者**: Zhenhua Wu, Yun Pang, Mingkun Chang et al.
- **发表**: 2026-06-15  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Long-tail hazardous scenarios are essential for safety-oriented autonomous driving, yet they are difficult to collect and reproduce at scale. Editable 3D Gaussian Splatting (3DGS) simulation offers a promising alternative by reconstructing real driving scenes and supporting controllable scene editing. However, edited 3DGS-rendered videos still suffer from a…

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

### 8. Dual Pose-Graph Semantic Localization for Vision-Based Autonomous Drone Racing

- **arXiv**: [2604.15168v1](https://arxiv.org/abs/2604.15168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.15168v1)
- **作者**: David Perez-Saura, Miguel Fernandez-Cortizas, Alvaro J. Gaona et al.
- **发表**: 2026-04-16  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Autonomous drone racing demands robust real-time localization under extreme conditions: high-speed flight, aggressive maneuvers, and payload-constrained platforms that often rely on a single camera for perception. Existing visual SLAM systems, while effective in general scenarios, struggle with motion blur and feature instability inherent to racing dynamics…

### 9. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 10. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

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

## 🧪 仿真 / Sim2Real (2 篇)

### 1. PhysGuard: Fisher-Guided Gradient Projection for Sim-to-Real Neural PDE Surrogates

- **arXiv**: [2606.16602v1](https://arxiv.org/abs/2606.16602v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.16602v1)
- **作者**: Changjian Zhou, Junfeng Fang, Negin Yousefpour et al.
- **发表**: 2026-06-15  ·  **类别**: cs.LG, math.NA, physics.comp-ph
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Neural operator models trained on simulation data often lose accuracy when applied to experimental measurements due to the sim-to-real gap. Standard fine-tuning with limited real data can reduce this gap, but it may also damage the core physics-relevant representations learned during pretraining. Although knowledge-preserving adaptation has been widely inve…

### 2. Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances

- **arXiv**: [2606.13842v1](https://arxiv.org/abs/2606.13842v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.13842v1)
- **作者**: Hongyu Zhou, Mingtian Tan, Vasileios Tzoumas
- **发表**: 2026-06-11  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We present an algorithm for efficient domain-adaptive policy learning via kernel representations. Learning domain-adaptive policies is challenging since it requires an environment representation that is both sufficiently expressive to model complex sim-to-real gaps during offline training, and computationally efficient enough to support rapid online adaptat…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](https://arxiv.org/abs/2606.17598v1) — score 22
2. [X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation](https://arxiv.org/abs/2604.21541v1) — score 20
3. [Transferring Contact, Not Just Motion: Compliant Grasping Across Dexterous Hands](https://arxiv.org/abs/2606.15516v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
