# 机器人研究每日摘要 · 2026-07-15

> 自动生成,共 91 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence

- **arXiv**: [2607.11689v1](https://arxiv.org/abs/2607.11689v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11689v1)
- **作者**: Yuanzhi Liang, Xufeng Zhan, Haibin Huang et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models, vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fra…

### 2. Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference

- **arXiv**: [2607.12659v1](https://arxiv.org/abs/2607.12659v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12659v1)
- **作者**: Zebin Yang, Qi Wang, Yunhe Wang et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially m…

### 3. TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors

- **arXiv**: [2607.12571v1](https://arxiv.org/abs/2607.12571v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12571v1)
- **作者**: Pinhan Fu, Xianda Guo, Xuetao Li et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks li…

### 4. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 5. See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models

- **arXiv**: [2607.11498v1](https://arxiv.org/abs/2607.11498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11498v1)
- **作者**: Byungkun Lee, Dongyoon Hwang, Dongjin Kim et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models predict robot actions from visual observations and language instructions. These actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating a frame mismatch between where the scene is observed and where actions are defined. The mismatch is benign under a fixed…

### 6. ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory

- **arXiv**: [2607.10350v1](https://arxiv.org/abs/2607.10350v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10350v1)
- **作者**: Jiayi Tian, Shiao Liu, Yuting Xu et al.
- **发表**: 2026-07-11  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution. We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliber…

## 🌐 具身智能 / 机器人基础模型 (7 篇)

### 1. Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks

- **arXiv**: [2607.09330v1](https://arxiv.org/abs/2607.09330v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.09330v1)
- **作者**: Nuocheng Yang, Sihua Wang, Zihan Chen et al.
- **发表**: 2026-07-10  ·  **类别**: cs.AI, cs.MA
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Embodied agent teams powered by heterogeneous large language models (LLMs) are being widely deployed in physical artificial intelligence such as smart factories, warehouses, and service robotics. To enable collaboration among such an agent team, efficient coordination mechanisms that operate reliably under limited network resources are required. However, ex…

### 2. Instance-Enriched Semantic Maps for Visual Language Navigation

- **arXiv**: [2607.12630v1](https://arxiv.org/abs/2607.12630v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12630v1)
- **作者**: Jiho Hong, Eunae Kang, Sanghyun Kim et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Visual Language Navigation (VLN) aims to enable an embodied agent to navigate complex environments by following natural language instructions. Recent approaches build semantic spatial maps and leverage Large Language Models (LLMs) for reasoning and decision making. Despite these advances, existing systems lack instance-level object detail and robustness to…

### 3. Traj-VLN: Learning Pixel-Space Interaction via Autoregressive Trajectory Generation

- **arXiv**: [2607.10744v2](https://arxiv.org/abs/2607.10744v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10744v2)
- **作者**: Changfei Fu, Guangcheng Chen, Wenjun Xu et al.
- **发表**: 2026-07-12  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Benefiting from the powerful priors embedded in large-scale pre-training data and the emerging commonsense reasoning ability, large language models (LLMs) have shown unprecedented generalization capabilities in many research fields. Recently, projecting visual embeddings into the language space via vision-language models (VLMs) to achieve sim-toreal and cro…

### 4. Distributed Agent System: Fault-Tolerant Collaboration Among Embodied Agents

- **arXiv**: [2607.10811v1](https://arxiv.org/abs/2607.10811v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10811v1)
- **作者**: Kai Yu, Lu Chen, Hanqi Li
- **发表**: 2026-07-12  ·  **类别**: cs.MA, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: AI engineering is shifting from passive text generation by large language models (LLMs) to agent-driven task execution, creating new reliability challenges for long-horizon tasks under resource constraints and environmental uncertainty. Conventional error-elimination optimization strategies fail to address cumulative error propagation. This paper proposes D…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. Hy-Embodied-VLM-1.0: Efficient Physical-World Agents

- **arXiv**: [2607.12894v1](https://arxiv.org/abs/2607.12894v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12894v1)
- **作者**: Ziyi Wang, Xumin Yu, Yongming Rao et al.
- **发表**: 2026-07-14  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world. In this report, we introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model specifically designed for embodi…

### 7. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

- **arXiv**: [2607.06501v1](https://arxiv.org/abs/2607.06501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06501v1)
- **作者**: Anxing Xiao, Hanbo Zhang, Tianrun Hu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in huma…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation

- **arXiv**: [2607.10132v1](https://arxiv.org/abs/2607.10132v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10132v1)
- **作者**: Muqun Hu, Yuhao Zhou, Kabir Ray Malik et al.
- **发表**: 2026-07-11  ·  **类别**: cs.RO
- **相关性评分**: 24  ·  **🔥 read_now**
- **摘要**: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation, its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback…

### 2. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation

- **arXiv**: [2607.11874v1](https://arxiv.org/abs/2607.11874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11874v1)
- **作者**: Yunhai Feng, Natalie Leung, Jiaxuan Wang et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires…

### 3. PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings

- **arXiv**: [2607.11041v1](https://arxiv.org/abs/2607.11041v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11041v1)
- **作者**: Zhengmao He, Moonkyu Jung, Hyeongjun Kim et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Loco-manipulation has recently shown promising capabilities; however, achieving high-precision control, managing the high-dimensional action space induced by many degrees of freedom (DoFs), and fully exploiting the inherent redundancy of whole-body systems remain challenging. In this paper, we propose a novel whole-body control framework that effectively ad…

### 4. Immersive Social Interaction with VR and LLM-Assisted Humanoids

- **arXiv**: [2607.07430v1](https://arxiv.org/abs/2607.07430v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07430v1)
- **作者**: Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidi…

### 5. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 6. Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots

- **arXiv**: [2607.01574v1](https://arxiv.org/abs/2607.01574v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.01574v1)
- **作者**: Taizoon Chunawala, Jeeseop Kim, Kaveh Akbari Hamed
- **发表**: 2026-07-02  ·  **类别**: cs.RO, math.OC
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: This paper presents a novel layered planning and control framework based on multi-rate nonlinear model predictive control (MR-NMPC) that enables quadrupedal robots to perform hybrid bipedal locomotion with wall-assisted support in constrained environments. Real-time trajectory optimization for this locomotion presents significant challenges, as the controll…

### 7. GaitSpan: Growing Humanoid Locomotion from Walking to Running

- **arXiv**: [2607.12114v1](https://arxiv.org/abs/2607.12114v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12114v1)
- **作者**: Kwan-Yee Lin, Zilin Wang, Janelle J. Liu et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: A humanoid that can walk should not relearn locomotion from scratch to jog or run. Yet current approaches often obtain gait diversity by prescribing gait schedules, imitating motion clips, training experts to switch between or distilling skills into one policy. These strategies can produce impressive behaviors, but offer limited flexibility across continuou…

### 8. DA-Nav: Direction-Aware City-Scale Vision-Language Navigation

- **arXiv**: [2607.11638v2](https://arxiv.org/abs/2607.11638v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11638v2)
- **作者**: Ye Yuan, Kehan Chen, Xinqiang Yu et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: City-scale outdoor navigation is currently hindered by the heavy reliance on dense maps or costly navigation supervision. In this work, we introduce a novel paradigm for leveraging directional instructions from commercial navigation tools (e.g., Google Maps). To bridge the gap between commercial instructions and executable navigation actions, while mitigati…

### 9. Requirement-Driven Design of Whole-Body Social Tactile Sensing via Virtual Human-Robot Interaction

- **arXiv**: [2607.11690v1](https://arxiv.org/abs/2607.11690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11690v1)
- **作者**: Dakarai Crowder, Ruohan Zhang, Alexis E. Block et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.HC
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Tactile sensing for social-physical human-robot interaction (spHRI) is designed in a hardware-driven manner, where predefined sensor configurations constrain coverage, spatial resolution, and the range of recognizable gestures. We propose a requirement-driven framework that derives sensing requirements, specifically spatial resolution and placement, directl…

### 10. From Foundation to Application: Improving VLA Models in Practice

- **arXiv**: [2607.06403v1](https://arxiv.org/abs/2607.06403v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06403v1)
- **作者**: Wei Wu, Fangjing Wang, Fan Lu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Despite recent progress of VLA foundation models, the disparity between laboratory conditions and real-world applications continues to impede their practical implementation. To bridge this gap, we present LingBot-VLA 2.0, which advances LingBot-VLA through improvements in three functional domains. (1) Generalization across tasks and embodiments. Compared to…

## 🦾 操控 / 灵巧手 / 抓取 (33 篇)

### 1. DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

- **arXiv**: [2607.08751v1](https://arxiv.org/abs/2607.08751v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08751v1)
- **作者**: Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 24  ·  **🔥 read_now**
- **摘要**: Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering st…

### 2. LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation

- **arXiv**: [2607.06323v1](https://arxiv.org/abs/2607.06323v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06323v1)
- **作者**: Xinye Yang, Zhiyuan Ma, Hongze Yu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Real-world learning for dexterous hands remains brittle because high-dimensional hand actions amplify imitation errors and make reinforcement-learning exploration prone to contact-breaking motion. While combining imitation learning (IL) with online reinforcement learning (RL) can reduce manual supervision, unconstrained exploration in raw hand-action spaces…

### 3. Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation

- **arXiv**: [2607.04940v1](https://arxiv.org/abs/2607.04940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.04940v1)
- **作者**: Zhe Zhao, Zhibin Li, Yilin Ou et al.
- **发表**: 2026-07-06  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing t…

### 4. TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation

- **arXiv**: [2607.07287v2](https://arxiv.org/abs/2607.07287v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07287v2)
- **作者**: Jianyi Zhou, Feiyang Hong, Yunhao Li et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states su…

### 5. TS-Mask VLA: 2D Temporal-Spatial Masking for Vision-Language-Action Model with Effective Bridging

- **arXiv**: [2607.09818v1](https://arxiv.org/abs/2607.09818v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.09818v1)
- **作者**: Shengzhuo Yang, Ronghao Yu, Chuanjie Lv et al.
- **发表**: 2026-07-10  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models aim to understand natural-language instructions and visual observations, and to generate and execute corresponding actions as embodied agents. Recently, autoregressive token-based action generation has driven the development of many representative VLA models. However, this paradigm often reduces action generation to next-…

### 6. TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation

- **arXiv**: [2607.09190v1](https://arxiv.org/abs/2607.09190v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.09190v1)
- **作者**: Suting Ni, Hanbing Zhang, Zhenyu Wei et al.
- **发表**: 2026-07-10  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting in motion imitation without physically…

### 7. Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation

- **arXiv**: [2607.03529v1](https://arxiv.org/abs/2607.03529v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.03529v1)
- **作者**: Chenyang Ma, Yunchao Yao, Zhenyu Wei et al.
- **发表**: 2026-07-03  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Compliance is essential for dexterous manipulation, yet existing solutions often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands. We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states. Since motor current is closely relate…

### 8. ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning

- **arXiv**: [2607.12931v1](https://arxiv.org/abs/2607.12931v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12931v1)
- **作者**: Yilun Kong, Yunpeng Qing, Guozheng Ma et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frame…

### 9. VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation

- **arXiv**: [2607.12356v1](https://arxiv.org/abs/2607.12356v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12356v1)
- **作者**: Mohan Liu, Zhihao Gu, Xuanyu Chen et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts inc…

### 10. Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference

- **arXiv**: [2607.12287v1](https://arxiv.org/abs/2607.12287v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12287v1)
- **作者**: Yuzhou Wu, Yuxin Zheng, Muchun Niu et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines: repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies…

## 🎓 模仿学习 / 强化学习 (15 篇)

### 1. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

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

### 4. StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance

- **arXiv**: [2607.12370v1](https://arxiv.org/abs/2607.12370v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.12370v1)
- **作者**: Hung-Chieh Wu, Xiaopan Zhang, Kasra Sinaei et al.
- **发表**: 2026-07-14  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: This paper proposes StratMamba, a dual-stream Mamba-based temporal modeling architecture, to more efficiently capture long-horizon temporal dependencies required for robot navigation in complex and obstacle-rich environments. StratMamba leverages a combination of fast-decay and slow-decay memory architectures, where the fast-decay component processes high-f…

### 5. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 6. A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity

- **arXiv**: [2607.02005v1](https://arxiv.org/abs/2607.02005v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02005v1)
- **作者**: Sujan Kumar Dhali, Bhaskar Dasgupta
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper presents OCD SLAM, a dynamic stereo visual SLAM framework that extends ORB-SLAM2 by jointly addressing dynamic objects and dynamic features in the scene. Usual visual SLAM systems operating in dynamic environments often fail in the presence of moving objects, due to the static-world assumption used in pose estimation and mapping. To address this…

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
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (4 篇)

### 1. Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

- **arXiv**: [2607.11099v1](https://arxiv.org/abs/2607.11099v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11099v1)
- **作者**: Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 2. PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments

- **arXiv**: [2607.07374v1](https://arxiv.org/abs/2607.07374v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07374v1)
- **作者**: Seunghun Lee, Jihun Nam, Dong-Uk Seo et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliabili…

### 3. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 4. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation](https://arxiv.org/abs/2607.10132v1) — score 24
2. [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2607.08751v1) — score 24
3. [LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation](https://arxiv.org/abs/2607.06323v1) — score 20

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
