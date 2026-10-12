# 机器人研究每日摘要 · 2026-10-13

> 自动生成,共 89 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (4 篇)

### 1. Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving

- **arXiv**: [2610.13453v1](https://arxiv.org/abs/2610.13453v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13453v1)
- **作者**: Yuechen Luo, He Chong, Fang Li et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reinforcement Learning (RL) substantially improves planning performance in autonomous-driving Vision-Language-Action (VLA) models. However, existing RL methods rely on scalar trajectory rewards that measure overall quality but fail to identify specific planning errors or provide actionable correction signals. In long-tail scenarios, errors in scene understa…

### 2. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 3. Forward Dynamics Models

- **arXiv**: [2610.13117v1](https://arxiv.org/abs/2610.13117v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13117v1)
- **作者**: Zipei Ma, Junzhe Jiang, Jiahui Zhang et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively. Yet VLAs learn without explicit supervision from future world states, while WAMs that condition actions on predicted futures incur extra inference c…

### 4. NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

- **arXiv**: [2610.10787v1](https://arxiv.org/abs/2610.10787v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10787v1)
- **作者**: Gengze Zhou, Yicong Hong, Jiazhao Zhang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures

- **arXiv**: [2610.13534v1](https://arxiv.org/abs/2610.13534v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13534v1)
- **作者**: Loan Bernat, Matthieu Grard, Ariane Herbulot et al.
- **发表**: 2026-10-09  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt their decisions as execution unfolds. Existing benchmarks investigate dynamic task execution and embodied multi-agent coordination, but provide limited evaluation of their intersection. We introduce MAGMA-Bench, an architecture-agnostic benchmark…

### 2. EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents

- **arXiv**: [2610.13021v1](https://arxiv.org/abs/2610.13021v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13021v1)
- **作者**: Jie Huang, Yanan Chen, Ruixun Liu et al.
- **发表**: 2026-10-09  ·  **类别**: cs.AI, cs.CL, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCLBench, the first benchmark in embodied simulation for evalu…

### 3. JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents

- **arXiv**: [2610.12957v1](https://arxiv.org/abs/2610.12957v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12957v1)
- **作者**: Gangyi Li, LuYao Wang, Jingfu Sun et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Embodied agents must translate multimodal observations and user requests into executable actions while adapting to product constraints, changing goals, and execution feedback. We present JoyInside-VLM-Agent, a ReAct-style multimodal agent developed through product-conditioned trajectory construction and staged policy learning for robotic platforms and smart…

### 4. What Should Embodied Agents Remember? Benchmarking and Evaluating Memory Modality for Embodied Agents

- **arXiv**: [2610.12561v1](https://arxiv.org/abs/2610.12561v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12561v1)
- **作者**: Junxiang Wang, Yuchen Liu, Yi Wu et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Memory allows large language model (LLM) agents to use past experience, often stored as textual records, when responding to requests. For embodied agents that control robots, visual and spatial observations introduce a broader choice of memory modalities, affecting both the information available for subsequent tasks and the model inference costs of construc…

### 5. TAME-Nav: Temporal Asymmetric Mixture-of-Experts Distillation for Agile and Versatile Robot Navigation

- **arXiv**: [2610.12877v1](https://arxiv.org/abs/2610.12877v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12877v1)
- **作者**: Lingjie Zhang, Jun Xue, Shanze Wang et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Agile and reliable navigation is a core capability for embodied robots navigating complex spatial constraints and dynamic interactions. However, a single policy often struggles to accommodate the distinct decision-making demands of diverse scenarios. We present TAME-Nav, an asymmetric Teacher-Student navigation framework built around a temporal soft mixture…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

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

## 🦵 人形 / 足式机器人 (26 篇)

### 1. Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads

- **arXiv**: [2610.12972v1](https://arxiv.org/abs/2610.12972v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12972v1)
- **作者**: Manh Cuong Nguyen, Duc Cuong Vu, Viet Anh Vu et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads. However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predict…

### 2. A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control

- **arXiv**: [2610.12465v1](https://arxiv.org/abs/2610.12465v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12465v1)
- **作者**: Octi Zhang, Mateo Guaman Castro, Patrick Yin et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: General-purpose robots must perform a wide range of tasks from agile locomotion to dexterous manipulation. While sim-to-real reinforcement learning (RL) has proven to be a useful tool for this goal, current RL pipelines depend on engineering-heavy, per-task structural priors such as shaped rewards and demonstrations. Recent work has shown that diverse simul…

### 3. PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface

- **arXiv**: [2610.12558v1](https://arxiv.org/abs/2610.12558v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12558v1)
- **作者**: Xiaomeng Xu, Han Zhang, Zhian Ruan et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body su…

### 4. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

- **arXiv**: [2610.06850v1](https://arxiv.org/abs/2610.06850v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06850v1)
- **作者**: Yucheng Zhang, Sirui Xu, Jinhong Li et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.GR
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object i…

### 5. LLA-MPPI: Rapidly Adaptive Whole-body Control of Legged Robots with GPU-Accelerated Parallel Simulations

- **arXiv**: [2610.10465v1](https://arxiv.org/abs/2610.10465v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10465v1)
- **作者**: Sebin Jung, Maitham F. AL-Sunni, Juan Alvarez-Padilla et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Real-time whole-body controllers for legged robots typically plan through a fixed nominal model and degrade when the deployed dynamics change. Adaptive methods typically require a model structure that contact dynamics do not provide, or they need offline training for each anticipated condition. We present Look-back and Look-ahead Adaptive Model Predictive P…

### 6. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 7. Humanoid World Action Model With Joint State--Action Generation

- **arXiv**: [2610.12026v1](https://arxiv.org/abs/2610.12026v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12026v1)
- **作者**: Yan Yang, Jikun Rong, Minzhao Zhu et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output referen…

### 8. Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction

- **arXiv**: [2610.09291v1](https://arxiv.org/abs/2610.09291v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09291v1)
- **作者**: Jeonghwan Kim, Hyeonwoo Kim, Hanbyul Joo
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present…

### 9. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 10. Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation

- **arXiv**: [2610.13087v1](https://arxiv.org/abs/2610.13087v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13087v1)
- **作者**: Chen Yu, Sudarshan S Harithas, Juan Borbon et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop, c…

## 🦾 操控 / 灵巧手 / 抓取 (30 篇)

### 1. Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration

- **arXiv**: [2610.12470v1](https://arxiv.org/abs/2610.12470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12470v1)
- **作者**: Jusuk Lee, Sungha Kim, Yeonsoo Park et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via…

### 2. OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes

- **arXiv**: [2610.11194v1](https://arxiv.org/abs/2610.11194v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11194v1)
- **作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous grasping is the foundational primitive in embodied AI, demanding massive data to train robust models. As real-world data collection is expensive, simulation has become the mainstream paradigm. Yet, while cluttered scenes best reflect real-world applications, learning to grasp within them is bottlenecked by a critical scarcity of large-scale data.…

### 3. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors

- **arXiv**: [2610.07681v1](https://arxiv.org/abs/2610.07681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07681v1)
- **作者**: Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation poses a challenging high-dimensional optimization problem, as useful behaviors require coordinated motion across many hand joints. In reinforcement learning (RL) and sampling-based trajectory optimization, exploration commonly relies on independent robot joint perturbations, making coordinated behaviors difficult to discover. Prior wo…

### 4. AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories

- **arXiv**: [2610.13643v1](https://arxiv.org/abs/2610.13643v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13643v1)
- **作者**: Xuanye Wu, Yue Shi, Yongcan Yang et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Automating biological laboratories requires robots to perform dexterous tool interactions under realistic visual conditions while handling dynamic experimental phenomena, presenting significant challenges for robotic manipulation. To enable systematic evaluation under these conditions, we introduce AutoBio+, a simulation benchmark and framework for dexterou…

### 5. JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation

- **arXiv**: [2610.13628v1](https://arxiv.org/abs/2610.13628v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13628v1)
- **作者**: Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO, cs.HC, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people. Remedies are evaluated on different streams, delays and metrics. JitterVLA replays identical commands and arrival traces through alternative controllers, isol…

### 6. RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation

- **arXiv**: [2610.13578v1](https://arxiv.org/abs/2610.13578v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13578v1)
- **作者**: Xuhui Kang, Sung-Wook Lee, Yan Zhuang et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learne…

### 7. SkillWeave: Weaving Heterogeneous Demonstrations into Long-Horizon Manipulation Skills

- **arXiv**: [2610.12046v1](https://arxiv.org/abs/2610.12046v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12046v1)
- **作者**: Ryosei Tamura, Xiaoxiang Dong, Uksang Yoo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation requires both large-scale task progression and precise contact-rich interaction, making it challenging to collect demonstrations that effectively support both regimes. We present SkillWeave, a heterogeneous demonstration framework for long-horizon dexterous manipulation that combines teleoperation for coarse reaching and transport wit…

### 8. OmniHOI: Dexterous Hand-Object Interaction from Monocular Human Video

- **arXiv**: [2610.10855v1](https://arxiv.org/abs/2610.10855v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10855v1)
- **作者**: Ting Mao, Yanming Shao, Ziheng Wang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Monocular videos of human manipulation provide abundant dexterous demonstrations, yet reconstructing hand-object interaction from a single view and transferring it to robot hands remain difficult, limiting their direct use for robot execution. Prior methods either require task-specific RL training, limiting scalability, or assume clean motion-capture trajec…

### 9. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

### 10. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314v1](https://arxiv.org/abs/2609.28314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314v1)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

## 🎓 模仿学习 / 强化学习 (13 篇)

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

### 4. Sim-to-Real RL for ASVs using SysID

- **arXiv**: [2610.12202v1](https://arxiv.org/abs/2610.12202v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12202v1)
- **作者**: Cody Sheltraw, Tsimafei Lazouski, Maani Ghaffari et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Autonomous Surface Vehicles (ASVs) operating in dynamic marine environments require robust control policies for tasks such as path following and station keeping, making reinforcement learning (RL) a promising alternative to classical controllers. However, existing ASV simulators rarely support parallel environments for RL training. Such existing simulators…

### 5. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

- **arXiv**: [2609.20589v1](https://arxiv.org/abs/2609.20589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.20589v1)
- **作者**: Marina Orozco González, Luis Merino
- **发表**: 2026-09-17  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. RiCo: Neural Simulation of Rigid-Body Interactions via Local Contact Reasoning

- **arXiv**: [2610.12333v1](https://arxiv.org/abs/2610.12333v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12333v1)
- **作者**: Ruixiang Ouyang, Guanren Qiao, Fansen Meng et al.
- **发表**: 2026-10-08  ·  **类别**: cs.CV, cs.AI, cs.GR
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Accurate simulation of rigid-body interactions is essential for predictive physical world models. Despite recent progress in modeling object dynamics, capturing how local contacts between surfaces shape object motion remains challenging. While end-to-end world models predict interactions across entire scenes or objects, in practice, rigid-body contact is in…

### 8. CRISP: Fixing Flying Pixels in Latent LiDAR Generation via Diffusion Decoding

- **arXiv**: [2610.11376v1](https://arxiv.org/abs/2610.11376v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11376v1)
- **作者**: Andrea Ceron, Michael Schmidt, Alvaro Marcos-Ramiro et al.
- **发表**: 2026-10-08  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Latent LiDAR pipelines suffer from flying pixels: convolutional VAEs blur sharp radial depth discontinuities, yielding edge depths that back-project to points floating between surfaces. We identify this as a major, directly correctable decoder bottleneck and introduce CRISP: a pixel-space diffusion decoder with a backbone-agnostic latent adapter, DiT-based…

### 9. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 10. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

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
1. [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration](https://arxiv.org/abs/2610.12470v1) — score 20
2. [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194v1) — score 19
3. [EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors](https://arxiv.org/abs/2610.07681v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
