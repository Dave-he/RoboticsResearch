# 机器人研究每日摘要 · 2026-09-29

> 自动生成,共 56 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (2 篇)

### 1. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

- **arXiv**: [2609.12641v1](https://arxiv.org/abs/2609.12641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12641v1)
- **作者**: Jianman Lin, Shailesh Shailesh, Zhongyi Luo et al.
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine g…

### 2. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

- **arXiv**: [2609.07470v1](https://arxiv.org/abs/2609.07470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07470v1)
- **作者**: Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. AquaWAM: A Dynamics-aware World Action Model for Underwater Embodied Agents

- **arXiv**: [2609.33299v1](https://arxiv.org/abs/2609.33299v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.33299v1)
- **作者**: Cunhao Zhu, Yifeng Wang, Dongliang Xu et al.
- **发表**: 2026-09-27  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: World Action Models (WAMs) are becoming increasingly important and useful for embodied intelligence, as they enable robots to anticipate the consequences of candidate actions before interacting with the physical environment. However, underwater robots are usually subject to passive dynamics, such as inertia, buoyancy, hydrodynamic drag, and persistent drift…

### 2. Nutri-ATLAS: Embodied Agent for Tabulated Lookup and Assistance for Smarter nutrition

- **arXiv**: [2609.32803v1](https://arxiv.org/abs/2609.32803v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.32803v1)
- **作者**: Uttej Kallakuri, Boxun Hu, Ankur A. Butala et al.
- **发表**: 2026-09-26  ·  **类别**: cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Generative and Agentic IoT systems offer a promising foundation for digital healthcare applications that combine sensing, personalized reasoning, and autonomous interaction in real-world environments. Nutrition assistance is a natural use case, but existing Large Language Model (LLM)-based systems are often limited to passive text interaction and static con…

### 3. RAO-Nav: Probing Omni-Language Models for Zero-shot Semantic Audio-Visual Navigation

- **arXiv**: [2609.32224v1](https://arxiv.org/abs/2609.32224v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.32224v1)
- **作者**: Qilang Ye, Meng Liu, Yu Zhou
- **发表**: 2026-09-26  ·  **类别**: cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We explore whether Omni-Language Models (OLMs) can be directly applied to zero-shot Semantic Audio-Visual Navigation (SAVN). Recent work demonstrates that even state-of-the-art specialized models still struggle to achieve generalist multimodal navigation, despite extensive task-specific training. In this paper, we introduce RAO-Nav, short for Reasoning All-…

### 4. RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents

- **arXiv**: [2609.32862v1](https://arxiv.org/abs/2609.32862v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.32862v1)
- **作者**: Jingsong Liang, Shuhao Liao, Shizhe Zhang et al.
- **发表**: 2026-09-26  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: A foundation model should not act in isolation as an embodied agent. Yet, existing methods often optimize individual components of the agent stack, such as memory, context, skills, or action interfaces, rather than treating the supporting system itself as a unified policy. Moreover, interaction alone does not yield self-improvement unless execution experien…

### 5. PlanGuard: A Guardrail for Multi-Step Plan Safety in Embodied Agents

- **arXiv**: [2609.32801v1](https://arxiv.org/abs/2609.32801v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.32801v1)
- **作者**: Junchi Chen, Changtao Miao, Yuxiao Xiang et al.
- **发表**: 2026-09-26  ·  **类别**: cs.AI, cs.CR, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied task planners may produce multi-step plans whose subtask dependencies and interactions with the environment create physical risks during execution. Yet existing safeguards overlook such compositional risks, as general-purpose guardrails focus on semantic harm and embodied safety detectors assess subtasks in isolation. To address this gap, we introd…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. Beyond Tasks: A Vision for Reproducing an Animal-like Behavioral Substrate Using Modern Robot Learning Techniques

- **arXiv**: [2609.33165v1](https://arxiv.org/abs/2609.33165v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.33165v1)
- **作者**: Samiyuru Menik, Hemadri Jayalath
- **发表**: 2026-09-27  ·  **类别**: cs.RO, cs.AI, cs.HC
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Recent advances in robot learning have produced increasingly capable embodied agents. Yet comparatively less attention has been given to a more basic form of competence that animals exhibit continuously: the ability to remain situated, responsive, and behaviorally coherent as physical, environmental, and social demands change over time. We propose the ethol…

### 8. MemTransfer: Benchmarking Memory Beyond Matched Experience in Embodied Decision-Making

- **arXiv**: [2609.32313v1](https://arxiv.org/abs/2609.32313v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.32313v1)
- **作者**: Haiming Tang, Xianjie Dai, Gujie Shao et al.
- **发表**: 2026-09-26  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Memory lets an embodied agent reuse past experience, yet retaining useful information does not ensure that the agent can apply it when conditions change. We present MemTransfer, a benchmark comparing six memory representations, a working-memory baseline and five representations of past experience, under a shared frozen vision-language-model policy. It compr…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control

- **arXiv**: [2609.30521v1](https://arxiv.org/abs/2609.30521v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30521v1)
- **作者**: Yuanzhu Zhan, Yufei Jiang, Zemu Zhang et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Aerial manipulation in outdoor environments remains challenging due to the simultaneous requirements of reliable state estimation, stable aerial motion, and precise manipulation under external disturbances. In this work, we present a real-world outdoor aerial manipulation framework that integrates imitation learning, onboard LiDAR-inertial state estimation,…

### 2. Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

- **arXiv**: [2609.23968v1](https://arxiv.org/abs/2609.23968v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23968v1)
- **作者**: Fukang Liu, Yipu Chen, Jaehwi Jang et al.
- **发表**: 2026-09-21  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rel…

### 3. The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers

- **arXiv**: [2609.25696v1](https://arxiv.org/abs/2609.25696v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.25696v1)
- **作者**: Boxi Xia, Bokuan Li, Ryan Shin et al.
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Robotic manipulation has increasingly pursued human-like dexterous hands with many articulated degrees of freedom, offering rich manipulation capabilities at the cost of mechanical and control complexity. At the other extreme, parallel grippers are simple and robust, but provide little ability to manipulate an object after grasping it. Operating articulated…

### 4. Smoothness as a Constraint for Stable Humanoid Locomotion

- **arXiv**: [2609.24552v1](https://arxiv.org/abs/2609.24552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.24552v1)
- **作者**: Utsav Panchal, Denis Kleyko, Unal Artan et al.
- **发表**: 2026-09-21  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Embodied AI systems, particularly humanoid robots deployed in real world scenarios require whole-body control policies that are both task-responsive and physically smooth. However, smoothness is not uniform across the body: lower body must remain sufficiently reactive, while the upper body must be tightly regulated to preserve stability. Existing reinforcem…

### 5. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 6. A Comprehensive Review of Generative Physical Artificial Intelligence

- **arXiv**: [2609.18111v1](https://arxiv.org/abs/2609.18111v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.18111v1)
- **作者**: Satyam Gaba, Krutiksinh Rana, Siva Sai et al.
- **发表**: 2026-09-16  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: The integration of large-scale foundation models with physical embodiments has led to significant advancements in robotics known as Generative Physical Artificial Intelligence (GPAI). These agentic AI systems autonomously perceive, reason, and act in complex real-world situations. This survey comprehensively analyzes GPAI systems, focusing on their architec…

### 7. FRAMES: Failure Recovery And Monitoring of Embodied Skills for Humanoid Loco-Manipulation

- **arXiv**: [2609.22538v1](https://arxiv.org/abs/2609.22538v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.22538v1)
- **作者**: Ajay Vikram Periasami, Xinyuan Luo, Haoyu Li et al.
- **发表**: 2026-09-18  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Large language model (LLM) planners can decompose natural-language instructions and select reusable robot skills, but choosing the correct skill does not guarantee successful physical execution. This gap is especially important in humanoid loco-manipulation, where errors during approach, grasping, transport, or placement can invalidate the remainder of a lo…

### 8. Humanoids for Robot-Assisted Surgery: Bimanual Base Placement and Tool-Mount Optimization via Capability Maps

- **arXiv**: [2609.33096v1](https://arxiv.org/abs/2609.33096v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.33096v1)
- **作者**: Peihan Zhang, Zekai Liang, Florian Richter et al.
- **发表**: 2026-09-27  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Rapid advances in humanoid robotics have motivated growing interest in the application of humanoids for healthcare and clinical tasks. However, it remains unclear how close contemporary humanoids are to meeting the kinematic demands of robot-assisted laparoscopic surgery. In this work, we address the question of optimal robot positioning through a quantitat…

### 9. Humanoid Badminton: Learning Dynamic Racket Skills from Limited Human Motion Data

- **arXiv**: [2609.31840v1](https://arxiv.org/abs/2609.31840v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.31840v1)
- **作者**: Jingzhi Cui, Zhexiong Wang, Bangjie Xu et al.
- **发表**: 2026-09-25  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: High-speed racket sports provide a demanding testbed for humanoid robots, requiring time-critical decisions, precise striking, and dynamic whole-body coordination. In badminton, fast-changing shuttle trajectories require timely contact decisions, while successful returns demand precise racket pose and velocity within a brief contact window and across a broa…

### 10. Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory

- **arXiv**: [2609.28960v1](https://arxiv.org/abs/2609.28960v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28960v1)
- **作者**: Ming-Ju Lee, Zizhuo Wang, Shaoting Zhu et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: While recent advances in perceptive locomotion have enabled humanoid robots to traverse structured terrains, agile parkour in highly discontinuous environments remains an open challenge. In particular, crossing sparse footholds and narrow support regions requires precise foothold selection, effective use of visual observations, and consistent alternating fo…

## 🦾 操控 / 灵巧手 / 抓取 (13 篇)

### 1. VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation

- **arXiv**: [2609.25785v1](https://arxiv.org/abs/2609.25785v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.25785v1)
- **作者**: Jung-Woo Lee, Soo-Chul Lim
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have emerged as general-purpose robotic manipulation policies. However, in dexterous hand manipulation, contact forces are typically provided as separate states or force-specific representations, making it difficult to explicitly represent the spatial correspondence between force and their corresponding visual locations.…

### 2. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314v1](https://arxiv.org/abs/2609.28314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314v1)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

### 3. EgoWild2Dex: Learning Dexterous Robotic Manipulation from In-the-Wild Human Experience

- **arXiv**: [2609.23755v1](https://arxiv.org/abs/2609.23755v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23755v1)
- **作者**: Kunyang Lin, Xutao Wen, Jingxi Lin et al.
- **发表**: 2026-09-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Egocentric human data provide a principled source of supervision for learning dexterous robot manipulation. Unlike prior approaches that often collect such data in constrained or specially constructed environments, we collect in-the-wild egocentric demonstrations in real-world settings, including homes, factories, and pharmacies, etc., where people perform…

### 4. ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling

- **arXiv**: [2609.21449v2](https://arxiv.org/abs/2609.21449v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21449v2)
- **作者**: Xuancheng Zhang, Xuetao Liu, Qianying Tang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: World Action Models bring the predictive capabilities of video models into robot action generation, providing a rich foundation for modeling future visual states. Tactile sensing complements this foundation with direct measurements of physical interaction. Some existing methods use tactile features as conditioning inputs without jointly predicting future ta…

### 5. DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation

- **arXiv**: [2609.33882v1](https://arxiv.org/abs/2609.33882v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.33882v1)
- **作者**: Han Yang, Yian Wang, Yunlong Song et al.
- **发表**: 2026-09-27  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Glove-based motion capture is emerging as a scalable approach to collecting dexterous-hand demonstration data. However, due to the kinematic gap between the human and robot hand, the recorded human motions cannot be executed directly on the robot, especially for contact-rich tool-use tasks involving in-hand reorientation. Prior work bridges this gap in simu…

### 6. FINGR: Learning Dexterous Hand Control for Real-World Rubik's Cube Solving

- **arXiv**: [2609.33973v1](https://arxiv.org/abs/2609.33973v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.33973v1)
- **作者**: Yutong Liang, Quanquan Peng, Matthew Kim et al.
- **发表**: 2026-09-27  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Manipulating a Rubik's Cube with a single dexterous hand is a challenging test of sustained, contact-rich control: the hand must execute successive layer turns while keeping the cube secure. Each turn requires some fingers to support the cube while others push a moving layer, release contact, and reset for the next move. To learn this coordination, we intro…

### 7. SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents

- **arXiv**: [2609.30971v1](https://arxiv.org/abs/2609.30971v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30971v1)
- **作者**: Maokai Qin, Chuan Qin, Qi Zhang et al.
- **发表**: 2026-09-25  ·  **类别**: cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and systematic evaluation environments. Existing simulation-based laboratory benchmarks rely heavily on manual task engineering, making it challenging to systematically compile diverse scientific protocols into executab…

### 8. DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models

- **arXiv**: [2609.12316v1](https://arxiv.org/abs/2609.12316v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12316v1)
- **作者**: Samrat Sahoo, Yixuan Huang, Tom Silver
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Collecting high-quality robot data remains a fundamental challenge for training robot foundation models. Task and motion planning (TAMP) offers a scalable way to generate demonstrations, but our experiments show that raw TAMP trajectories provide surprisingly little benefit when used to fine-tune pretrained vision-language-action (VLA) models, despite succe…

### 9. HumynexSurg-1: A Curated Expert Liposuction Dataset

- **arXiv**: [2609.23885v1](https://arxiv.org/abs/2609.23885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23885v1)
- **作者**: Rhea Huang, David L. Matlock, Laurence Reich
- **发表**: 2026-09-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot foundation models learn manipulation from large demonstration corpora, but surgery is missing from those corpora: across the 780-hour Open-H surgical collection, one dataset carries synchronized force and none covers an aesthetic procedure. Liposuction is the hard case, because the instrument works under the skin and the surgeon operates by feel and b…

### 10. A Direct Rigid Transmission 2-DoF Wrist Extension for Tendon-Driven Hand

- **arXiv**: [2609.22681v1](https://arxiv.org/abs/2609.22681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.22681v1)
- **作者**: Yujie Pang, Sadman Sakib, Mohammad Abdullah Al Faruque
- **发表**: 2026-09-19  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Dexterous manipulation in confined spaces requires local control of hand orientation. Without a wrist, a dexterous hand must obtain this local orientation through coordinated motion of the robot arm, often involving several joints and a more complex end-effector path. We present CRAFT-Wrist, a concentric 2-DoF wrist extension that mounts between a robot arm…

## 🎓 模仿学习 / 强化学习 (5 篇)

### 1. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 2. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 3. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 4. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

### 5. NeRF and Gaussian Splatting SLAM in the Wild

- **arXiv**: [2412.03263v1](https://arxiv.org/abs/2412.03263v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.03263v1)
- **作者**: Fabian Schmidt, Markus Enzweiler, Abhinav Valada
- **发表**: 2024-12-04  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Navigating outdoor environments with visual Simultaneous Localization and Mapping (SLAM) systems poses significant challenges due to dynamic scenes, lighting variations, and seasonal changes, requiring robust solutions. While traditional SLAM methods struggle with adaptability, deep learning-based approaches and emerging neural radiance fields as well as Ga…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (1 篇)

### 1. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control](https://arxiv.org/abs/2609.30521v1) — score 19
2. [VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation](https://arxiv.org/abs/2609.25785v1) — score 19
3. [Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2609.23968v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
