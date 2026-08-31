# 机器人研究每日摘要 · 2026-08-31

> 自动生成,共 93 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models

- **arXiv**: [2608.21247v1](https://arxiv.org/abs/2608.21247v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.21247v1)
- **作者**: Zhuoyuan Li, Rui Zhao, Jin Wang et al.
- **发表**: 2026-08-21  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Token compression has become a key technique for reducing the inference cost of large foundation models, with approaches such as token pruning and KV-cache reuse widely adopted in vision-language models and recently explored for embodied agents. In embodied agents, tokens not only support perception and semantic understanding but also directly affect latenc…

### 2. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 3. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 4. Decoupling Planning and Control for Instructable Agents

- **arXiv**: [2608.26788v1](https://arxiv.org/abs/2608.26788v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.26788v1)
- **作者**: Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste et al.
- **发表**: 2026-08-27  ·  **类别**: cs.AI, cs.CL, cs.MA
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but…

### 5. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. Resilience Matters for Embodied Agents System: New Metrics, Systematic Evaluation, and Optimization

- **arXiv**: [2608.23839v1](https://arxiv.org/abs/2608.23839v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.23839v1)
- **作者**: Yapeng Liu, Yuanzhao Zhai, Xudong Gong et al.
- **发表**: 2026-08-24  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied Agents System (EAS) are increasingly deployed in open-world physical domains, where reliability directly dictates deployment quality and human-agent trust. However, existing evaluations rely on outcome-centric metrics as success rate or safety scores that collapse diverse execution trajectories into coarse scores, obscuring the dynamic processes un…

### 2. GenCoord: Skill-Path Commitments under Private Information

- **arXiv**: [2608.22055v2](https://arxiv.org/abs/2608.22055v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.22055v2)
- **作者**: Peng He, Junning Zhu, Haohan Yuan et al.
- **发表**: 2026-08-22  ·  **类别**: cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Suppose one embodied agent knows what must be built, while its teammate alone knows which transformation its workcell can perform. Neither local view determines who should act, what should be handed off, or how the joint task should continue. We introduce GenCoord, which turns the task consequence of such private facts into an executable skill-path commitme…

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 5. Embodied Scene Rearrangement Planning

- **arXiv**: [2608.27371v1](https://arxiv.org/abs/2608.27371v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.27371v1)
- **作者**: Canzhi Chen, Zan Wang, Siqi Zhu et al.
- **发表**: 2026-08-27  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: This paper introduces Embodied Scene Rearrangement Planning (ESRP), a novel task requiring embodied agents to rearrange furniture in 3D scenes to match a target configuration using only egocentric observations and a top-down target layout. Unlike prior rearrangement tasks, ESRP precludes global state access and introduces mutual object occlusions, reflectin…

### 6. 4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation

- **arXiv**: [2608.26947v1](https://arxiv.org/abs/2608.26947v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.26947v1)
- **作者**: Zehao Qi, Haochen Luo, Jia-Wang Bian et al.
- **发表**: 2026-08-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents need environments that are visually diverse, physically interactive, and changing over time. Procedural simulators can generate large interactive scene collections, and recent 4D generators produce compelling visual dynamics. Combining these properties in one environment, however, still demands extensive manual effort, and the result is rare…

### 7. 4DStreamCtrl: Interactive Video Generation with Online 4D Control

- **arXiv**: [2608.25479v2](https://arxiv.org/abs/2608.25479v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25479v2)
- **作者**: Shiqian Li, Chenguo Lin, Zhiguang Liu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the ima…

### 8. Meta-Ctrl: Guaranteed Plan Generation by Decoupling Syntactic and Semantic Constraints

- **arXiv**: [2608.22149v2](https://arxiv.org/abs/2608.22149v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.22149v2)
- **作者**: Gwen Yidou-Weng, Edward Sun, Tianyi Ma et al.
- **发表**: 2026-08-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: LLMs generate fluent plans for robots but routinely violate the syntactic and se8mantic constraints they must satisfy to execute, and existing remedies trade formal guarantees against plan quality: soft methods (affordance scoring, grounded decoding) give no guarantee, while symbolic planners (LLM+P) discard the LM's commonsense. We propose \textbf{Meta-Ctr…

### 9. ViSMoE: Visual-Aware Sparse Mixture-of-Experts for Embodied Referring Expression Grounding

- **arXiv**: [2608.21878v1](https://arxiv.org/abs/2608.21878v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.21878v1)
- **作者**: Shuo Feng, Piji Li
- **发表**: 2026-08-22  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Embodied Referring Expression Grounding is the task of enabling an agent to navigate in real environments and to localize a remote object based on natural language instructions. In this scenario, the agent needs to select one view for navigation at each step and identify a specific object among all candidate objects at the destination. However, most of the…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 2. LAC: Linear and Angular Compliance for Humanoid Whole-body Control

- **arXiv**: [2608.25405v1](https://arxiv.org/abs/2608.25405v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25405v1)
- **作者**: Yang Liu, Zhongkai Gu, Wei Zhu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches ap…

### 3. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 4. DELTA: Deformable Elevation-Based Local Terrain Attention Encoder for Sparse-Terrain Quadrupedal Locomotion

- **arXiv**: [2608.22033v1](https://arxiv.org/abs/2608.22033v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.22033v1)
- **作者**: Sanghyun Park, Moonkyu Jung, Jemin Hwangbo
- **发表**: 2026-08-22  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Stable quadrupedal locomotion on sparse terrain requires selecting state-relevant terrain evidence for precise foot placement. Model-based foothold planners provide precise foothold selection but rely heavily on explicit model assumptions. Recent attention-based map encoding (AME) studies show that end-to-end reinforcement learning (RL) can learn implicit f…

### 5. Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking

- **arXiv**: [2608.20087v1](https://arxiv.org/abs/2608.20087v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20087v1)
- **作者**: Tao Huang, Ruofei Liu, Xuchen Tang et al.
- **发表**: 2026-08-20  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from bro…

### 6. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2608.03387v2](https://arxiv.org/abs/2608.03387v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03387v2)
- **作者**: Shuliang He, Shuai Wang, Bo Yue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual…

### 7. CARO: Contact-Agnostic Residual Observation for Zero-Shot Robust Quadruped Locomotion

- **arXiv**: [2608.24217v1](https://arxiv.org/abs/2608.24217v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.24217v1)
- **作者**: Zihan Yang, Shixuan Han, Kexin Guo et al.
- **发表**: 2026-08-25  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We propose CARO, a contact-agnostic residual observation framework for policy adaptation. CARO embeds a fixed-base Euler--Lagrange model into the reinforcement learning control loop and constructs a torque-level residual observation without requiring torque sensors, explicit contact estimation, or vision-based measurements of the floating-base position and…

### 8. HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL

- **arXiv**: [2608.16837v1](https://arxiv.org/abs/2608.16837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16837v1)
- **作者**: Langzhe Gu, Chengkai Hou, Meng Li et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to…

### 9. EgoNav: Bridging Learned Waypoints and Geometry-Aware Local Control for Robust Indoor Navigation

- **arXiv**: [2608.25642v1](https://arxiv.org/abs/2608.25642v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25642v1)
- **作者**: Jing Wang, Shiqi Zhao, Hairong Qu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Image-goal navigation using lightweight topological maps is a practical paradigm for indoor robot deployment: the map requires only geotagged images, and localization relies on visual matching rather than precise pose estimation. However, learned waypoint predictors can produce targets that violate geometric constraints or deviate from the global path. Exec…

### 10. Humanoid Musical Robots as Experimental Interfaces for Music-Evoked Emotion

- **arXiv**: [2608.20433v1](https://arxiv.org/abs/2608.20433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20433v1)
- **作者**: Vincent K. M. Cheung, Jia-Yeu Lin
- **发表**: 2026-08-20  ·  **类别**: cs.RO, cs.HC, cs.MM
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Advances in technology have led to increasingly sophisticated musical humanoid robots. However, their use has largely been limited to performance and related research in human-robot interaction. In this position paper, we propose a novel perspective: musical humanoid robots as experimental interfaces for investigating music-evoked emotions. We argue that cu…

## 🦾 操控 / 灵巧手 / 抓取 (34 篇)

### 1. LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories

- **arXiv**: [2608.18618v1](https://arxiv.org/abs/2608.18618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18618v1)
- **作者**: Zhipeng Tang, Sihang Chen, Sha Zhang et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Autonomous laboratories hold great promise for accelerating scientific discovery. To achieve this vision, robots are supposed to dexterously manipulate diverse labware and instruments and execute long-horizon, state-dependent experimental procedures. Yet existing benchmarks do not jointly capture dexterous hand use, real-world laboratory interactions, and m…

### 2. A Tendon-Driven Five-Fingered Hand with Distributed Tactile Perception for Dexterous Manipulation

- **arXiv**: [2608.25547v1](https://arxiv.org/abs/2608.25547v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25547v1)
- **作者**: Huayang Chen, Longhui Qin
- **发表**: 2026-08-26  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: To apply the techniques of embodied artificial intelligence to human-oid robots for complex manipulations, dexterous robotic hands are indispensable, which are restricted by the dexterity and tactile perception capability. In this work, we proposed a novel design of tendon-driven five-fingered hand with dis-tributed tactile perception. With a soft-rigid-hyb…

### 3. GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation

- **arXiv**: [2608.27079v1](https://arxiv.org/abs/2608.27079v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.27079v1)
- **作者**: Yibo Qiu, Haoliang Ye, Shu'ang Sun et al.
- **发表**: 2026-08-27  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Pretrained vision-language-action (VLA) policies provide strong priors for robot manipulation, yet adapting them online to fine-grained biomedical tasks remains challenging. Task success often hinges on subtle, view-dependent visual cues, while task-level rewards provide little guidance about which regions matter, making it difficult to learn task-relevant…

### 4. StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models

- **arXiv**: [2608.26067v1](https://arxiv.org/abs/2608.26067v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.26067v1)
- **作者**: Zhe Liu, Jinghua Hou, Yuxiang Lu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equi…

### 5. $τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885v1](https://arxiv.org/abs/2608.16885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16885v1)
- **作者**: Xiaowei Cai, Yunuo Cai, Bingao Chen et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_…

### 6. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 7. Fiber Optic Sensing Glove for High Performance Dexterous Manipulation Capture

- **arXiv**: [2608.24572v1](https://arxiv.org/abs/2608.24572v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.24572v1)
- **作者**: J. D. Peiffer, Taylor Niehues, Li Guan et al.
- **发表**: 2026-08-25  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Capturing hand pose during dexterous manipulation remains difficult: vision-based methods degrade under occlusion and challenging lighting, while sensorized gloves, though occlusion-free, are prone to drift and magnetic interference and rarely match motion-capture accuracy. We introduce a fiber optic sensing glove for full hand pose tracking that targets th…

### 8. GhostTac: Manipulating Tactile Sensors without Physical Contact

- **arXiv**: [2608.20817v2](https://arxiv.org/abs/2608.20817v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20817v2)
- **作者**: Kun Wang, Xuancun Lu, Ruochen Zhou et al.
- **发表**: 2026-08-21  ·  **类别**: cs.CR, cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Tactile sensors are integral components of modern robotic systems, enabling robots to perceive and interact with the physical environment through tactile feedback. Despite their importance, the physical-layer security of tactile sensors has received little attention in prior work. In this paper, we present GhostTac, to the best of our knowledge, the first c…

### 9. ReForce: Learning Force-aware Retargeting for Dexterous Manipulation

- **arXiv**: [2608.15560v1](https://arxiv.org/abs/2608.15560v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.15560v1)
- **作者**: Yuhang Wu, Lingqi Zeng, Changwei Jing et al.
- **发表**: 2026-08-16  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Human demonstrations offer a scalable data source for dexterous manipulation, but transferring them to robot actions remains challenging due to the embodiment gap. Today's retargeting is mostly kinematic, yet manipulation is decided by force, which governs how the hand interacts with the object and how the object moves. In this paper, we present ReForce, a…

### 10. C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video

- **arXiv**: [2608.07045v1](https://arxiv.org/abs/2608.07045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.07045v1)
- **作者**: Jie Ren, Zhehao Jiang, Yinhong Yang et al.
- **发表**: 2026-08-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: High-quality demonstrations for dexterous robot manipulation are costly and difficult to collect, whereas monocular human videos provide a scalable source of diverse manipulation behaviors. However, transferring such demonstrations to dexterous robots remains challenging: monocular hand-object interaction (HOI) reconstruction often produces temporally unsta…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. Advantage-Driven Explicit Memory for Social Navigation

- **arXiv**: [2608.25610v1](https://arxiv.org/abs/2608.25610v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25610v1)
- **作者**: Yeonsoo Park, Mattia Racca, Guillaume Bono et al.
- **发表**: 2026-08-26  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Robot policies are predominantly learned with classical parametric variants of imitation learning or RL, where training stores the agent's behavior exclusively in the policy's network parameters, putting a heavy burden on the representation learning algorithm. We propose a new navigation agent equipped with non-parametric memory which explicitly indexes pri…

### 2. Praxist: From Experimental Artifacts to Solution Lineages

- **arXiv**: [2608.25955v1](https://arxiv.org/abs/2608.25955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25955v1)
- **作者**: Jin Li, Ahmed Murtadha, Zhiyu Wang et al.
- **发表**: 2026-08-26  ·  **类别**: cs.MA, cs.SE
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous R\&D agents now write, run, and improve executable artifacts under automated evaluation---but largely as laboratory instruments: shown on curated benchmarks, with gains that are hard to trace to a cause and costs well above what sustained engineering practice absorbs. The limitation is structural. Most systems treat each attempt as nearly self-co…

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

### 5. RIPE++: Reinforced Keypoint Learning from Positive Pairs Only

- **arXiv**: [2608.19693v1](https://arxiv.org/abs/2608.19693v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19693v1)
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **发表**: 2026-08-20  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. R…

### 6. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

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

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Bridge Damage Detection from Low-Light UAV Imagery via Degradation-Aware Mixture-of-Experts Enhancement

- **arXiv**: [2608.23136v1](https://arxiv.org/abs/2608.23136v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.23136v1)
- **作者**: Hu Wang, Hongxu Pu, Zhiqi Hu et al.
- **发表**: 2026-08-24  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Poor illumination obscures small, low-contrast defects in UAV bridge imagery, reducing the reliability and operational flexibility of automated inspection. This paper investigates whether degradation-aware image restoration can improve bridge damage detection under low-light conditions and transfer from synthetic degradations to real inspection scenes. We p…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618v1) — score 18
2. [A Tendon-Driven Five-Fingered Hand with Distributed Tactile Perception for Dexterous Manipulation](https://arxiv.org/abs/2608.25547v1) — score 17
3. [Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds](https://arxiv.org/abs/2607.18135v1) — score 16

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
