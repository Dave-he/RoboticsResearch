# 机器人研究每日摘要 · 2026-09-23

> 通过 arXiv OAI-PMH backfill 补回 (status=recovered_oai, candidates=981, relevant=164)。共 164 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (9 篇)

### 1. Embodied Snap: Octopus-Inspired Distributed Reach-and-Attach with a Speed-Limited Soft Arm

- **arXiv**: [2609.22926](https://arxiv.org/abs/2609.22926)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.22926)
- **作者**: Linxin Hou, Zhihang Qin, Heyang Zou et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reach-and-attach of soft robotic arms with passive suction requires accurate targeting and sufficient contact speed, yet geared actuators can impose a speed limit that improved trajectory tracking alone cannot overcome. This paper proposes an embodied snap controller that separates slow servo-driven preloading from rapid elastic release, enabling a complian…

### 2. Dissecting Advantage-Guided Post-Training for Vision-Language-Action Policies

- **arXiv**: [2609.28161](https://arxiv.org/abs/2609.28161)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28161)
- **作者**: Jiahang Cao, Hanye Zhao, Hang Lai et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Advantage-guided reinforcement learning provides a practical way to post-train vision-language-action (VLA) policies using limited robot data. However, its performance depends on several coupled choices, including how critic-derived advantages are constructed, calibrated, and used for policy training. Existing recipes often combine these choices into a sing…

### 3. HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models

- **arXiv**: [2604.12447](https://arxiv.org/abs/2604.12447)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.12447)
- **作者**: Zixing Chen, Yifeng Gao, Li Wang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language-Action (VLA) models inherit rich world knowledge from vision-language backbones and acquire executable skills from action demonstrations. Yet current evaluations primarily measure task completion, leaving the semantic safety of learned action policies underexplored. This gap creates a critical vulnerability: a policy may execute the intended…

### 4. Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy

- **arXiv**: [2609.28838](https://arxiv.org/abs/2609.28838)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28838)
- **作者**: Mehmet Turan Yardımcı, Yunus Emre Çoğurcu
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Online reinforcement learning fine-tuning of pretrained flow-matching vision-language-action (VLA) policies promises robots that keep learning after deployment, but continued updates often destroy competence on individual tasks while the aggregate still looks healthy. We study this failure mode, which we call task collapse, under a matched small-compute bud…

### 5. NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation

- **arXiv**: [2606.03159](https://arxiv.org/abs/2606.03159)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.03159)
- **作者**: Aarti Basant, Amlan Kar, Despoina Paschalidou et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck. In closed-loop simulation, the driving policy model actively interacts with the environment, where its actions dynamically update the simulator state and directly influence the next set of generated sensor observations. W…

### 6. What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency

- **arXiv**: [2609.13984](https://arxiv.org/abs/2609.13984)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13984)
- **作者**: Luoyang Sun, Guoyang Xia, Fengfa Li et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vision-Language-Action (VLA) models combine a pretrained vision encoder, a language backbone, and an action head, but their relative contribution has not been established under controlled, latency-paired conditions. We fix the backbone families (SigLIP2 and Qwen2.5) and the training pipeline, sweep action-head design and module scale, and pair each configur…

### 7. Less Language, More Latents: Annotation-Efficient VLAs for Driving

- **arXiv**: [2609.27747](https://arxiv.org/abs/2609.27747)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27747)
- **作者**: Alexey Zakharov, Kemal Oksuz, Puneet K. Dokania
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vision-language-action models (VLA) promise human-steerable autonomous driving, but their training is bottlenecked by the scarcity of frames paired with natural-language instructions: while camera streams and expert trajectories are logged at scale, language annotations (e.g., turn left at the intersection) remain scarce and expensive to acquire. To address…

### 8. Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control

- **arXiv**: [2609.28339](https://arxiv.org/abs/2609.28339)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28339)
- **作者**: Zanyi Wang, Yuheng Lei, Dengyang Jiang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Pretrained generative Diffusion Transformers (DiTs) capture rich pixel-level visual and language-conditioned structure through large-scale image and video generation training. A growing line of robot policies builds on this generative prior, but how it should be transferred to control remains unclear, and existing approaches commonly instantiate this transf…

### 9. Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction

- **arXiv**: [2609.28467](https://arxiv.org/abs/2609.28467)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28467)
- **作者**: Zilin Fang, Zishuo Wang, Gim Hee Lee et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Social navigation typically assumes a specified goal and focuses on reaching it while respecting social conventions, whereas robot group joining requires predicting where to join based on the group's real-time activity and formation. This is a highly semantic task, yet an important capability for applications such as robotic guide dogs and autonomous mobili…

## 🌐 具身智能 / 机器人基础模型 (16 篇)

### 1. OmniEcho: Audio-Visual Spatial Understanding for Omni-Modal Embodied Agents

- **arXiv**: [2609.23407](https://arxiv.org/abs/2609.23407)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23407)
- **作者**: Ruixun Liu, Yuxuan Wang, Jiacheng Xie et al.
- **发表**: 2026-09-23  ·  **类别**: cs.SD, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Humans can effortlessly localize the direction of a sound source and integrate it with visual cues for reasoning, yet this remains challenging for embodied agents. In particular, it is still unclear how to effectively evaluate and model spatial audio understanding in embodied settings. To address this gap, we introduce \textbf{OmniEchoBench}, a unified benc…

### 2. Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI

- **arXiv**: [2609.24815](https://arxiv.org/abs/2609.24815)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.24815)
- **作者**: Wenkang Qin, Yukun Zhou, Noah Shen et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Scalable simulation is essential for robot data generation, policy training, evaluation, and safe iteration, yet real-world interaction is costly and conventional simulators require labor-intensive construction. We present Uranus, a data-driven robot simulator built around a joint-trajectory-conditioned autoregressive diffusion model. Uranus offers three ke…

### 3. RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement

- **arXiv**: [2609.27612](https://arxiv.org/abs/2609.27612)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27612)
- **作者**: Kailin Wang, Haoxiang Jie, Yaoyuan Yan et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Long-horizon robot execution requires a clear distinction between a model's proposal, a controller's termination, and verified task completion. We present RegenHarness, an evidence-gated robot-agent harness connecting task planning to heterogeneous robot skills. Its execution architecture couples a model loop for context-conditioned proposals with an agent…

### 4. DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum

- **arXiv**: [2609.19801](https://arxiv.org/abs/2609.19801)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19801)
- **作者**: Haoqiang Kang, Yiming Zhang, Yiyang Guo et al.
- **发表**: 2026-09-23  ·  **类别**: cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Executable environments enable LLM agents to learn from the consequences of their actions. For embodied agents, those consequences extend beyond whether the current task succeeds: completing a delivery can consume the time, energy, or money needed for later work. Learning to plan therefore requires environments that preserve these dependencies and turn them…

### 5. EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks

- **arXiv**: [2609.28236](https://arxiv.org/abs/2609.28236)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28236)
- **作者**: Lizhou Liang, Xinyu Zhong, Miao Pan et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Long-horizon embodied interaction requires agents to retain and continually update information about the environment as they observe, act, and encounter change. Yet current agents struggle to maintain such memory reliably. Our analysis traces this limitation to four key deficiencies: weak fine-grained visual memory, unreliable dynamic world-state tracking,…

### 6. AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios

- **arXiv**: [2609.28366](https://arxiv.org/abs/2609.28366)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28366)
- **作者**: Zhipeng Bao, Wenjie Zhao, Tianle Zhu et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379…

### 7. Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration

- **arXiv**: [2609.09418](https://arxiv.org/abs/2609.09418)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09418)
- **作者**: Yiran Qiao, Feng Wang, Jing Ma
- **发表**: 2026-09-23  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: World Action Models (WAMs) couple predictive world modeling with action generation, allowing anticipated future states to guide agent behavior. Although WAMs are rapidly advancing embodied AI, general-purpose counterparts remain largely unexplored in games. Existing game-oriented approaches often combine action-conditioned world models with external policie…

### 8. NaviScale: Generating Large-Scale Semantic Map Datasets for Object Navigation

- **arXiv**: [2609.27218](https://arxiv.org/abs/2609.27218)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27218)
- **作者**: Chuanlin Lan, Yanwei Zheng, Weijian Liu et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Embodied navigation requires spatial representations that generalize across unseen environments, yet collecting large amounts of annotated data from real 3D environments is difficult. We propose NaviScale for semantic-map-based object navigation (ObjectNav), whose predictor can be trained on pairs of partial and complete semantic maps without reconstructing…

### 9. CoBranchMR: Supporting Parallel Design and Conflict Resolution in Mixed Reality

- **arXiv**: [2609.27235](https://arxiv.org/abs/2609.27235)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27235)
- **作者**: Niloofar Sayadi, Kaiyuan Tang, Yunhao Xing et al.
- **发表**: 2026-09-23  ·  **类别**: cs.HC
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: We present CoBranchMR, a mixed reality (MR) system that enables distributed collaborators to work in parallel from different locations on the same digital representation of a physical object. CoBranchMR lets users branch an object into editable virtual copies, customize them independently, and then merge their work back into a shared object. When merging co…

### 10. Geometry-Conditioned Visual Place Recognition in Natural Environments

- **arXiv**: [2609.27370](https://arxiv.org/abs/2609.27370)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27370)
- **作者**: Walter Nedov, Saimunur Rahman, Kavindie Katuwandeniya et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Visual Place Recognition (VPR) in natural environments remains challenging due to repetitive vegetation, sparse distinctive landmarks, and substantial appearance and viewpoint variation across traversals. While visual observations of the same place can change considerably, their underlying spatial structure is often more persistent. We exploit this compleme…

## 🦵 人形 / 足式机器人 (9 篇)

### 1. An Analysis of Streaming Deep Reinforcement Learning for Adaptive Continual Learning in Robotics

- **arXiv**: [2609.28807](https://arxiv.org/abs/2609.28807)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28807)
- **作者**: Teeratham Vitchutripop, Alyssa Quarles, Wenhe Zhang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Over the course of a lifetime, robots may encounter novel scenarios unaccounted for in its original training that result in performance degradation. One common approach to mitigating this issue is to further grow the offline training dataset in hopes of producing a policy robust to these changes. In contrast, biological learning occurs moment-to-moment via…

### 2. Banana Kick: Response-Informed Skill Evolution for Humanoid Soccer

- **arXiv**: [2609.27269](https://arxiv.org/abs/2609.27269)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27269)
- **作者**: Hao E. Zhang, Ruize Geng, Raihan Haque et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Humanoid kicking requires coordinated whole-body motion and precise contact, while a banana kick demands contact mechanics that generate ball spin and aerodynamic curvature. Motion imitation provides a reliable ordinary-kick prior, but reinforcement learning may improve shot speed and placement accuracy without changing the underlying kicking technique. Ada…

### 3. FleXray: Universal Clinical X-ray Segmentation

- **arXiv**: [2609.26756](https://arxiv.org/abs/2609.26756)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.26756)
- **作者**: Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing structures to overlap and anatomical boundaries to be ambiguous, even to experts. As a result, labeling X-ray databases for training general-purpose segmentatio…

### 4. FlyCNS: Connectome-Grounded Information Organization for Communication-Constrained Embodied Control

- **arXiv**: [2609.28816](https://arxiv.org/abs/2609.28816)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28816)
- **作者**: Jinchang Zhang, Jiakai Lin, Guoyu Lu
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Robotic bodies are inherently distributed in sensing and actuation, yet learning-based control still commonly relies on centralized information processing. This work studies the problem of information organization in communication-constrained embodied control: which computations should remain local, and which information is worth transmitting for whole-body…

### 5. Amplify: A Lightweight Library for Reproducible Nonlinear Programming Problems in Robotics

- **arXiv**: [2609.28377](https://arxiv.org/abs/2609.28377)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28377)
- **作者**: Nelson Rosa
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Optimization problems (OPs) are key to solving many challenging research problems in robotics. However, reproducibility still remains a major issue. In this paper, we present Amplify, a lightweight nonlinear programming library aimed at reproducible results of robotic-related trajectory optimization problems. The minimalistic requirements for the 537-line l…

### 6. ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control

- **arXiv**: [2609.28378](https://arxiv.org/abs/2609.28378)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28378)
- **作者**: Xukun Luan, Zhongxiang Lei, Chen Gong et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.CR, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Humanoid control, leveraging human demonstrations, has achieved diverse, agile, and natural locomotion behaviors through reinforcement learning (RL). While this paradigm has yielded remarkable performance in physical humanoid control, how to eliminate specific motions from learned policies remains insufficiently explored. Addressing this issue is motivated…

### 7. Omnidirectional Amphibious Locomotion via Internal Mass Actuation

- **arXiv**: [2609.27358](https://arxiv.org/abs/2609.27358)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27358)
- **作者**: Niko Weaver, Boxi Xia, Li-Yu Lo et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Field robots must traverse varied terrain and obstacles while remaining robust to water, debris, vegetation, and physical contact. We present MARBLE, a fully enclosed omnidirectional amphibious rolling robot driven entirely by internal mass redistribution. Three mutually orthogonal linear sliders shift internal masses to generate body rotation, while an ori…

### 8. DAVIS: A Depth-Only End-to-End Active-Vision Framework for Humanoid Soccer Skills

- **arXiv**: [2609.28175](https://arxiv.org/abs/2609.28175)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28175)
- **作者**: Jiakang Jin, Yixiao Huo, Pengyuan Wang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Humanoid soccer contact skills require more than producing high-impact foot-ball contacts: the robot must close the loop over perception, approach, alignment, impact, and recovery while its own motion induces substantial viewpoint changes, frequent loss of the ball from view, and uncertain contact outcomes. In this work, we ask a compact yet stricter questi…

### 9. When Search Becomes Memory: Accelerating Robot Design Discovery with Self-Evolving Skills

- **arXiv**: [2605.25832](https://arxiv.org/abs/2605.25832)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.25832)
- **作者**: Yunfei Wang, Xiaohao Xu, Yang Li et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Large language models (LLMs) are increasingly used as proposal generators for evolutionary robot design, yet most loops remain memoryless: simulator results shape the next population but are not preserved as reusable design knowledge. We present Auto-Robotist, a self-evolving LLM agent that distills morphology-search traces into an explicit natural-language…

## 🦾 操控 / 灵巧手 / 抓取 (53 篇)

### 1. A Quasi-Direct-Drive Underactuated Asymmetric Hand for Dexterous and Efficient Grasping and Manipulation

- **arXiv**: [2609.27240](https://arxiv.org/abs/2609.27240)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27240)
- **作者**: Benjamin Davis, Chase Kidder, Hannah S. Stuart
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: In this paper, we present the Berkeley QUAD (Quasi-direct-drive, Underactuated, Asymmetric Design) Hand, a four-finger anthropomorphic robotic hand with 11 degrees of freedom and 8 degrees of actuation. The design utilizes QDD actuation at the base of each finger, enabling high force transparency for dexterous, adaptive performance. However, the low torque…

### 2. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314](https://arxiv.org/abs/2609.28314)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

### 3. Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy

- **arXiv**: [2609.28660](https://arxiv.org/abs/2609.28660)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28660)
- **作者**: Tara Sadjadpour, Siming He, C. K. Wolfe et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Human hand-object interactions (HOIs) provide a rich source of demonstrations for dexterous manipulation, but learning directly from them presents challenges in bridging morphology gaps, ensuring dynamical feasibility, and sim-to-real deployment. We present Morphometric Imitation, a three-stage framework that transforms reconstructed HOIs into zero-shot sim…

### 4. LiMA: Bridging Long-term Imagination to Real-time Dexterous Manipulation via Asynchronous Diffusion

- **arXiv**: [2609.28431](https://arxiv.org/abs/2609.28431)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28431)
- **作者**: Ning Chen, Yankai Fu, Junkai Zhao et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation demands long-term foresight and rapid reactive control. Vision-Language-Action (VLA) models, while proficient in high-level reasoning, often lack a fine-grained understanding of physical dynamics and spatial perception. Conversely, World-Action Models (WAMs) typically suffer from high inference latency due to iterative generation. The…

### 5. DexWrist: A Robotic Wrist for Constrained and Dynamic Manipulation

- **arXiv**: [2507.01008](https://arxiv.org/abs/2507.01008)  ·  **PDF**: [link](https://arxiv.org/pdf/2507.01008)
- **作者**: Martin Peticco, Gabriella Ulloa, John Marangola et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Development of dexterous manipulation hardware has primarily focused on hands and grippers. However, these end-effectors are often paired with bulky and highly stiff wrists that limit performance in human environments. More recent designs have adopted backdrivable actuation, but are still difficult to model and control due to coupled kinematics or high mech…

### 6. Control Architecture for Safe Grasping of Fragile Objects Using a Coarse Position-Controlled Gripper

- **arXiv**: [2609.12737](https://arxiv.org/abs/2609.12737)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12737)
- **作者**: Marko Pavlic, Moritz Geier, Timo Markert et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Robots are increasingly used in unstructured environments. The need for them to safely grasp unknown objects without damaging them becomes crucial. Humans achieve this by sensing and quickly responding by adjusting their grasping force. Similarly, effective grasp acquisition in robots requires compliant interaction strategies that can adapt to uncertain obj…

### 7. Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies

- **arXiv**: [2609.21659](https://arxiv.org/abs/2609.21659)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21659)
- **作者**: Xingyu Lin, Zhuang Li, Zhongrun Wu et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) policies solve the same manipulation task through different action interfaces, but task success alone does not establish whether their physical executions agree. We study cross-policy end-effector geometry in 15,000 closed-loop LIBERO rollouts from four policies. The primary clean-condition analysis forms 3,600 configuration-mat…

### 8. Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR

- **arXiv**: [2609.27246](https://arxiv.org/abs/2609.27246)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27246)
- **作者**: Nathalia Gomez, Haig Shamlian, Omar Khan et al.
- **发表**: 2026-09-23  ·  **类别**: cs.HC, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: As embodied agents take on increasingly social and relational roles in VR, visual realism and embodiment alone may be insufficient; users must also perceive these agents as emotionally attuned, supportive, and humanlike. Prior work suggests that verbal attunement and nonverbal mimicry can each improve users' social evaluations of embodied agents. However, b…

### 9. BEE: Intervention-Adaptive Real-World Reinforcement Learning with Vision-Language-Action Models

- **arXiv**: [2609.27450](https://arxiv.org/abs/2609.27450)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27450)
- **作者**: Weihui Zhao, Xiaohan Yan, Zunian Wan et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models handle long-horizon manipulation, yet success hinges on a few precision-critical phases where millimeter-scale errors undo all prior progress. Online reinforcement learning (RL) can optimize exactly these actions, but free exploration is far too costly on real robots, which makes human corrections indispensable. However,…

### 10. MemBodied: Recurrent Associative Memory for Vision-Language-Action Models

- **arXiv**: [2609.28256](https://arxiv.org/abs/2609.28256)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28256)
- **作者**: Tej Deep Pala, Navonil Majumder, Bryce Goh et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level information beyond the current observation. This limitation is consequential in history-dependent manipulation tasks that depend on information available only in past observations. Retaining…

## 🎓 模仿学习 / 强化学习 (42 篇)

### 1. Spiking Neural Network Control of a Flapping-Wing Robot on Resource-Constrained Hardware

- **arXiv**: [2605.19430](https://arxiv.org/abs/2605.19430)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.19430)
- **作者**: Rim El Filali, Chenrui Feng, Chao Gao et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Flapping-Wing Micro Aerial Vehicles (FWMAVs) provide exceptional maneuverability and aerodynamic efficiency but pose significant challenges for onboard control due to nonlinear dynamics and stringent Size, Weight, and Power (SWaP) constraints, as exemplified by a butterfly-inspired robot less than 30 gram. To this end, we present a hierarchical neuromorphic…

### 2. SatUnreal: A High-Precision Synthetic Dataset for Satellite Stereo Matching via Unreal Engine

- **arXiv**: [2609.27442](https://arxiv.org/abs/2609.27442)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27442)
- **作者**: Han-Gyeol Kim, JaeWan Park, Junmin Park et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: 3D reconstruction from satellite imagery is essential for large-scale topographic analysis, yet the lack of high-fidelity training datasets with accurate occlusion labels remains a primary bottleneck. Existing benchmarks, such as US3D and WHU-Stereo, face inherent challenges in spatio-temporal mismatch -- environmental changes and shadow displacements betwe…

### 3. Learning a Speed-adaptive Hip Exoskeleton Control Policy Via Sim-to-real Reinforcement Learning

- **arXiv**: [2609.28027](https://arxiv.org/abs/2609.28027)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28027)
- **作者**: Bin Li, Zhimin Hou, Jiacheng Hou et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Providing personalized exoskeleton assistance across varying walking speeds remains challenging. Existing online optimization methods are sample-inefficient, requiring extensive human-in-the-loop (HIL) evaluations to optimize the entire assistive torque profile. Sim-to-real reinforcement learning (RL) offers a promising alternative but cannot directly accou…

### 4. A Scalable Multi-Robot Framework for Decentralized and Asynchronous Perception-Action-Communication Loops

- **arXiv**: [2309.10164](https://arxiv.org/abs/2309.10164)  ·  **PDF**: [link](https://arxiv.org/pdf/2309.10164)
- **作者**: Saurav Agarwal, Frederic Vatnsdal, Romina Garcia Camargo et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: We develop a decentralized Perception-Action-Communication (PAC) system for multi-robot teams that enables them to collaborate in large scale, outdoor environments. Our system natively supports deployments at any scale by leveraging a graph neural network (GNN) to diffuse information hop-by-hop across the fleet's network. This achieves global collaboration…

### 5. An Open Panoramic Aerial Robot: Airframe-Integrated Multi-Fisheye Sensing, Onboard ERP Formation, and Field Evaluation

- **arXiv**: [2609.02319](https://arxiv.org/abs/2609.02319)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02319)
- **作者**: Dun Dai, Ze Lu, Cheng He et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: We present an open panoramic aerial robot with four synchronized fisheye cameras integrated into a carbon-fiber airframe and an onboard NVIDIA Jetson Orin NX. The robot outputs calibrated raw views and an equirectangular panorama (ERP; 1280x640 in all experiments). The ERP pipeline uses overlap-specific projection radii, gated local alignment, seam control,…

### 6. VertexCBF: Improving Neural Control Barrier Functions via Vertex-Restricted Control Search

- **arXiv**: [2609.12831](https://arxiv.org/abs/2609.12831)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12831)
- **作者**: Bojan Derajić, Sebastian Bernhard, Wolfgang Hönig
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.LG, cs.SY
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: As the number of autonomous robots continues to grow, safety becomes increasingly important. Control barrier functions (CBFs) provide a theoretically grounded framework for ensuring safety, but existing design methods often face limitations in effectiveness, scalability, or interpretability, and may result in overly conservative safe sets. In this paper, we…

### 7. SyzHarness: Patch-Based Kernel Bug Reproduction with LLM-Synthesized Fuzzing Harnesses

- **arXiv**: [2609.23889](https://arxiv.org/abs/2609.23889)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23889)
- **作者**: Xingyu Li, Juefei Pu, Haonan Li et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CR, cs.AI
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Automated kernel vulnerability reproduction is essential for bug triage, patch validation, and regression testing, but still lacks an effective and efficient solution. The core challenge is twofold: a reproducer must first recover the trigger scaffold needed to reach the vulnerable state and determine the precise concrete values that actually trigger the bu…

### 8. BranchDrive: A Branch-Structured Dataset for Action-Conditioned Driving Prediction

- **arXiv**: [2609.27275](https://arxiv.org/abs/2609.27275)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27275)
- **作者**: Feeza Khan Khanzada, Sudarshan Sridhar, Jaerock Kwon
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Most autonomous-driving datasets record only the action executed by a behavior policy and the single future that followed, providing limited supervision for comparing alternative ego decisions. We introduce BranchDrive, a branch-structured CARLA dataset and benchmark that pairs one canonical pre-decision history with one nominal expert future and twelve phy…

### 9. Turning Safety into Competence: Minimally Exploitable Robot Policies via Safety-Filtered Reinforcement Learning

- **arXiv**: [2609.27312](https://arxiv.org/abs/2609.27312)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27312)
- **作者**: Ruihan Wu, Rui Yang, Donggeon David Oh et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Robots deployed for competitive tasks must outmaneuver their opponents without sacrificing safety. Existing approaches, including safe reinforcement learning (RL), train a single policy to achieve task success and avoid failures simultaneously. This coupling can complicate training and leave the learned policy exploitable by deliberate attacks. We propose S…

### 10. A Sample-Based Approach for Hierarchical Information-Theoretic Compression of Probabilistic Occupancy Grids

- **arXiv**: [2609.27330](https://arxiv.org/abs/2609.27330)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27330)
- **作者**: Zhenyu Jin, Daniel T. Larsson
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.IT, math.IT
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: We develop a sample-based framework for constructing information-driven hierarchical multi-resolution representations of probabilistic occupancy grids. Recent methods compute information-optimal abstractions via dynamic-programming-based exhaustive recursions, which become computationally prohibitive for large-scale grids and are ill-suited to robotics appl…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (1 篇)

### 1. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509](https://arxiv.org/abs/2609.27509)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

## 🧭 导航 / 路径规划 (10 篇)

### 1. DUGM-R: Uncertainty-Aware Dynamic Grid Mapping and Risk-Triggered Recovery for Learned Local Navigation

- **arXiv**: [2609.27338](https://arxiv.org/abs/2609.27338)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27338)
- **作者**: Haoyun Feng, Adrian Rubio-Solis, Zhaodong Guo et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Learned local navigation in crowded indoor environments is sensitive to how dynamic obstacle motion is represented, while collision-prone behaviour may persist after nominal policy training. We present a risk-aware reinforcement-learning framework that addresses these two issues through an uncertainty-aware Dynamic Uncertainty Grid Map (DUGM) and a modular…

### 2. Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP

- **arXiv**: [2609.27340](https://arxiv.org/abs/2609.27340)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27340)
- **作者**: Jungsoo Lee, Jaegyun Park, Wansoo Kim
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Large language models (LLMs) are increasingly used as natural-language interfaces for robotic systems, yet their integration with Robot Operating System (ROS)-based navigation remains limited by two gaps. First, navigation data such as occupancy grids are represented as raw geometric messages that are difficult for LLMs to use directly as spatial or semanti…

### 3. Optimal Trajectory Generation for Improved Magnetic Navigation

- **arXiv**: [2609.27553](https://arxiv.org/abs/2609.27553)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27553)
- **作者**: Justin Kang, Teddy Herrera, Liraz Mudrik et al.
- **发表**: 2026-09-23  ·  **类别**: eess.SY, cs.SY, math.OC
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Magnetic navigation has emerged as a promising alternative for navigation in Global Positioning System (GPS)-denied environments, leveraging geomagnetic field maps in conjunction with onboard magnetometer measurements. However, its performance is highly sensitive to trajectory-dependent observability, which limits its practical effectiveness under conventio…

### 4. Talk2Escape: Conversational Grounding for Vision-and-Language Navigation

- **arXiv**: [2609.28296](https://arxiv.org/abs/2609.28296)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28296)
- **作者**: Zerui Li, Sihao Lin, Yanyan Shao et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.HC
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: While Vision-and-Language Navigation (VLN) has demonstrated remarkable success, the prevailing single-turn paradigm exposes a fundamental vulnerability: agents operate in a strictly open-loop manner. In practice, factors such as perceptual aliasing, sensor noise, and odometry drift can cause minor deviations to accumulate over time, often leading to catastr…

### 5. Privacy-Preserving Semantic Segmentation from High-Resolution Depth and Ultra-Low-Resolution RGB

- **arXiv**: [2609.28360](https://arxiv.org/abs/2609.28360)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28360)
- **作者**: Xuying Huang, Swithinraj Moses Daniel, Sicong Pan et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: As mobile robots become increasingly integrated into everyday environments, privacy risks arising from onboard cameras have become a growing concern. Ultra-low-resolution (ULR) RGB can mitigate visual privacy exposure at the source, but ULR appearance alone substantially limits semantic and spatial understanding. We therefore introduce a privacy-preserving…

### 6. Multi-robot Graph Traversal with Support Coordination under Stochastically Moving Adversaries

- **arXiv**: [2603.14697](https://arxiv.org/abs/2603.14697)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.14697)
- **作者**: Manshi Limbu, Xuan Wang, Gregory J. Stein et al.
- **发表**: 2026-09-23  ·  **类别**: cs.MA
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Cooperative multi-robot missions require team of robots to traverse environments where adversaries or hazards with stochastic dynamics induce time-varying traversal risk. While support coordination--where robots assist teammates in traversing risky regions--can significantly reduce mission costs, its effectiveness depends on the team's ability to anticipate…

### 7. Automotive mmWave Spinning Radar Place Recognition with Spatially Gated Feature-Correlation Representation

- **arXiv**: [2609.27394](https://arxiv.org/abs/2609.27394)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27394)
- **作者**: Saimunur Rahman, Sagun Singh Shrestha, Abdelwahed Khamis et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Automotive spinning FMCW radar provides dense, $360^\circ$ sensing and remains reliable under poor illumination and adverse weather, making it well-suited to autonomous navigation. Place recognition uses these observations to identify previously visited locations for re-localization and long-term navigation. However, heading changes appear as circular shift…

### 8. Compressed delayed-information projection for six-degree-of-freedom underwater vehicle navigation under delayed acoustic positioning

- **arXiv**: [2609.27439](https://arxiv.org/abs/2609.27439)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27439)
- **作者**: Shuyue Li, Miguel López-Benítez, Eng Gee Lim et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Delayed acoustic positioning packets constrain historical navigation states, but a current-time update evaluates them against a mismatched state, whereas exact rewind/replay re-executes the intervening estimator history. This paper introduces compressed delayed-information projection (CDIP), a causal 15-state error-state Kalman filter (ESKF) treatment for d…

### 9. Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers

- **arXiv**: [2609.28247](https://arxiv.org/abs/2609.28247)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28247)
- **作者**: Frederic Vatnsdal, Roshan Gopal, Romina Garcia Camargo et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Large Language Models (LLMs) introduce an exciting new paradigm for planning and navigation in robotics, but fail on even simple multi-robot tasks as team sizes grow. We propose COMPASS, a scalable, decentralized multi-robot architecture for controlling large collectives of agentic robots with reasoning space feedback control. Feedback is generated locally…

### 10. BronchoTop: Bronchoscopy Navigation via RGB-Only Topological Localization

- **arXiv**: [2609.28328](https://arxiv.org/abs/2609.28328)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28328)
- **作者**: Clara Tomasini, Ana Cristina Murillo, Luis Riazuelo
- **发表**: 2026-09-23  ·  **类别**: cs.CV
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Accurate localization of the bronchoscope within the bronchial tree is essential for clinicians to be able to reach target lesions, perform biopsies and avoid misidentification of airway segments during diagnostic and therapeutic procedures. However, existing navigation systems typically rely on patient-specific CT scans or additional external sensors, incr…

## 🧪 仿真 / Sim2Real (7 篇)

### 1. Behavior-Aligned Action Tokenization for Robot Policy Learning

- **arXiv**: [2609.27513](https://arxiv.org/abs/2609.27513)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27513)
- **作者**: Junbo Dong, Ze Chen, Zhendong Xie et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Autoregressive robot policies learn continuous control by predicting discrete action tokens from observations. Different tasks often share local motions, yet behavioral correspondence across demonstrations receives limited explicit supervision in existing tokenizers. Motions with different timing can therefore lack a shared representation despite following…

### 2. Motoneuron-Inspired Sampling for Model Predictive Path Integral Control

- **arXiv**: [2609.28325](https://arxiv.org/abs/2609.28325)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28325)
- **作者**: Alexis Poignant, Jan Babič
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Model Predictive Path Integral (MPPI) control relies on stochastic trajectory sampling, and its performance under limited rollout budgets depends strongly on the structure of the proposal distribution. Standard implementations commonly perturb control sequences with Gaussian noise, despite growing evidence that temporally correlated and structured sampling…

### 3. Context-Continuous Preference Learning for Exoskeleton Personalization

- **arXiv**: [2609.28427](https://arxiv.org/abs/2609.28427)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28427)
- **作者**: Sunin Baek, Sungwoo Park, Daekyum Kim
- **发表**: 2026-09-23  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Personalizing exoskeleton assistance across operating conditions is constrained by the time and physical effort required to collect user feedback. We examined whether a user's preference landscape varies smoothly across operating conditions and when this continuity supports learning from limited feedback. We propose Context-Continuous Preference Learning (C…

### 4. OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight

- **arXiv**: [2609.28709](https://arxiv.org/abs/2609.28709)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28709)
- **作者**: Vittorio Palladino, Teaya Yang, Ruiqi Zhang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Autonomous UAV flight through cluttered and partially unknown environments requires reasoning not only about observed obstacles but also about occluded regions that the sensor cannot observe. We present OA-MPPI, an obstacle- and occlusion-aware extension of Model Predictive Path Integral (MPPI) control for quadrotor flight that accounts for potential moving…

### 5. Prescribed-Time Contracting-Boundary Control of a Tendon-Driven Flexible Arm

- **arXiv**: [2609.22963](https://arxiv.org/abs/2609.22963)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.22963)
- **作者**: Yi Lu, Chao Tang, Zhiji Han et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: This study develops a prescribed-time performance-shaping control method for curvature tracking of a single-segment flexible arm actuated by three antagonistic tendon pairs. A Cartesian curvature representation is introduced to avoid the undefined bending direction at the straight configuration and to establish an explicit six-tendon kinematic mapping. A cu…

### 6. Safety-Filtered Distributed Koopman-MPC

- **arXiv**: [2609.27463](https://arxiv.org/abs/2609.27463)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27463)
- **作者**: Shengjun Zhang, Wenhao Li, Zhenxin Lin et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.SY, eess.SY
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Distributed model predictive control (DMPC) often constructs both predictions and collision constraints from neighbor trajectories, so packet loss can remove both. We separate these roles: received trajectories drive Koopman-MPC, while local sensing and shelf geometry define a hard-constrained quadratic program (QP) that projects the applied input. Its radi…

### 7. CuACD: A Fully GPU-Resident Approximate Convex Decomposition

- **arXiv**: [2609.28731](https://arxiv.org/abs/2609.28731)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28731)
- **作者**: Ruoxi Shi, Xinyue Wei, Fanbo Xiang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CG, cs.GR
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Approximate convex decomposition (ACD) converts triangle meshes into small sets of convex parts and is a standard preprocessing step for physics simulation, collision detection, and large-scale robot learning. The majority of modern ACD methods produce high-quality decompositions through an expensive search over candidate cutting planes, with per-mesh runti…

## 🤏 软体机器人 / 柔性控制 (1 篇)

### 1. Collocated Shape Regulation for Soft Robots

- **arXiv**: [2609.27469](https://arxiv.org/abs/2609.27469)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27469)
- **作者**: Pietro Pustina, Ebrahim Shahabi, Daniel Feliu-Talegon et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.SY, eess.SY
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Controlling the shape of a continuum soft robot typically requires an accurate dynamic model and actuation of all degrees of freedom. We show that regulating only the actuated coordinates, through collocated shape control, achieves provably stable convergence of those coordinates and, under an explicit compatibility condition, of the entire robot shape. Whi…

## 📦 其他机器人相关 (16 篇)

### 1. Reproducible Dynamic Parameter Identification for a Low-Cost Robot Arm: A Positive-Definiteness Audit for Model Acceptance

- **arXiv**: [2605.15949](https://arxiv.org/abs/2605.15949)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.15949)
- **作者**: Junji Oaki, Koki Yamane, Koki Inami et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Dynamic parameter identification of low-cost robot arms is challenging because limited sensing and drivetrain nonidealities can yield models that predict measured torques well but are physically unsuitable for model-based control. This paper presents a reproducible dynamic parameter identification pipeline for CRANE-X7, a low-cost seven-degree-of-freedom ar…

### 2. Vision-Based Control of a Tether-Suspended Aerial Radiation Sensing Payload

- **arXiv**: [2609.27219](https://arxiv.org/abs/2609.27219)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27219)
- **作者**: Ian Snider, Brian J. Quiter, Emil Rofors et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Aerial radiation surveys achieve higher sensitivity when the radiation detector is held close to the ground. Detector sensitivity falls off roughly with the inverse square of the distance to the source, so a detector flown high is slower to reach a given minimum detectable activity. Flying the vehicle low puts the propellers near the ground, where downwash…

### 3. Distributed Stochastic Approximation Algorithms and Heavy-Tailed Age of Information

- **arXiv**: [2609.27499](https://arxiv.org/abs/2609.27499)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27499)
- **作者**: Adrian Redder, Arunselvan Ramaswamy, Holger Karl
- **发表**: 2026-09-23  ·  **类别**: math.OC, cs.DC, cs.MA
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Algorithms in multi-agent systems such as federated learning, mobile robotic swarming, and consensus control can be designed and analyzed as distributed stochastic approximation algorithms. Such algorithms involve information exchanges between agents for various computations. The freshness of the information can be quantified using the Age of Information (A…

### 4. Behaviora - A Conceptual Architecture for External and Internal Behavior of Robots and Agents

- **arXiv**: [2609.27536](https://arxiv.org/abs/2609.27536)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27536)
- **作者**: Gote Nyman
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Behaviora is a preliminary conceptual architecture for representing agent and robot behavior, external and internal alike, in an addressable form. A behaving robot or agent performs a Behavior Episode composed of episode components, which can be derived from behavior taxonomies (BTax) and assigned persistent identifiers. We denote these identifiers as IoB (…

### 5. GLASS: Architecture-Tuned, Composable, Device-Side Linear Algebra for Edge Robotics and Beyond

- **arXiv**: [2609.28179](https://arxiv.org/abs/2609.28179)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28179)
- **作者**: Brian Plancher
- **发表**: 2026-09-23  ·  **类别**: cs.RO, cs.DC, cs.MS
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: GPU robotics lacks the reusable numerical infrastructure of mature CPU stacks, instead relying on compiler frameworks that introduce overhead or repeatedly reimplementing numerical libraries. To address this, we introduce GLASS (GPU Linear Algebra Simple Subroutines), a header-only CUDA C++ library that provides thread-, warp-, block-, and NVIDIA-backed imp…

### 6. Reward-Rate Congestion Games and Replicator--Dinkelbach Dynamics

- **arXiv**: [2609.28240](https://arxiv.org/abs/2609.28240)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28240)
- **作者**: Hassan Abdelraouf, Vaibhav Srivastava, Vijay Gupta
- **发表**: 2026-09-23  ·  **类别**: eess.SY, cs.SY
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Reward rate is a key performance criterion in cyber-physical and robotic systems where time, workload, and coordination costs are limiting resources. We introduce reward-rate congestion games, where agents seek to maximize reward per unit execution time. The direct reward-rate game is generally not an exact potential game. We develop a Dinkelbach-based fram…

### 7. LLM-Powered Socially Assistive Robot-Delivered Cognitive Behavioral Therapy Exercises: an Exploratory Study with University Students

- **arXiv**: [2402.17937](https://arxiv.org/abs/2402.17937)  ·  **PDF**: [link](https://arxiv.org/pdf/2402.17937)
- **作者**: Mina Kian, Mingyu Zong, Katrin Fischer et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Mental health is a significant healthcare challenge, and cognitive behavioral therapy (CBT) is a widely used therapeutic method for treating anxiety and depression. However, traditional CBT often requires access to trained clinicians and can be cost-prohibitive or logistically difficult for many individuals. To address these barriers, we developed a low-cos…

### 8. Coverage Games

- **arXiv**: [2603.20398](https://arxiv.org/abs/2603.20398)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.20398)
- **作者**: Orna Kupferman, Noam Shenwald
- **发表**: 2026-09-23  ·  **类别**: cs.GT, cs.LO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: We introduce and study coverage games - a novel framework for multi-agent planning in settings in which a system operates several agents but does not have full control on them, or interacts with an environment that consists of several agents. The game is played between a coverer, who has a set of objectives, and a disruptor. The coverer operates several age…

### 9. MR.ScaleMaster: Scale-Consistent Collaborative Mapping from Crowd-Sourced Monocular Videos

- **arXiv**: [2604.11372](https://arxiv.org/abs/2604.11372)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.11372)
- **作者**: Hyoseok Ju, Giseop Kim
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: Crowd-sourced cooperative mapping combines monocular sessions from different front-ends, each an independently reconstructed keyframe sequence. Each session has its own local coordinate frame and may follow an incompatible scale convention. We present MR.ScaleMaster, a backend that accepts image, Sim(3) pose, and point-map packets without requiring a common…

### 10. MyoFlow: Anchor-Tied Rectified Flow for HD-sEMG Gesture Recognition Across Sessions and Subjects

- **arXiv**: [2609.17194](https://arxiv.org/abs/2609.17194)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17194)
- **作者**: Chenhao Wu, Dingjie Peng, Zhihe Zhang et al.
- **发表**: 2026-09-23  ·  **类别**: cs.LG
- **相关性评分**: 0  ·  **📌 info**
- **摘要**: High-density surface electromyography (HD-sEMG) gesture recognition supports prosthetic control, assistive robotics, and rehabilitation, but electrode re-donning and physiological variability cause distribution shifts that degrade accuracy across sessions and subjects. Generative HD-sEMG models primarily synthesize signals for augmentation; although diffusi…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [A Quasi-Direct-Drive Underactuated Asymmetric Hand for Dexterous and Efficient Grasping and Manipulation](https://arxiv.org/abs/2609.27240) — score 14
2. [TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](https://arxiv.org/abs/2609.28314) — score 13
3. [Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy](https://arxiv.org/abs/2609.28660) — score 13

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
