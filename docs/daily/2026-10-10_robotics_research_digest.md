# 机器人研究每日摘要 · 2026-10-10

> 自动生成,共 90 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models

- **arXiv**: [2610.12090v1](https://arxiv.org/abs/2610.12090v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12090v1)
- **作者**: Hongyu Shi, Sen Zhao, Zuyu Zhang et al.
- **发表**: 2026-10-08  ·  **类别**: cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation…

### 2. PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies

- **arXiv**: [2610.12285v1](https://arxiv.org/abs/2610.12285v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12285v1)
- **作者**: Yu Liu, Hetian Guo, Tianlv Huang et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and how it conditions action generation. We introduce PLaW-VLA, which models task-relevant future states in a pretrained prediction-oriented repre…

### 3. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 4. Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning

- **arXiv**: [2610.12231v1](https://arxiv.org/abs/2610.12231v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12231v1)
- **作者**: Yuchen Zhou, Jiacheng You, Weikang Wan et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Learning from demonstration has enabled impressive robot behaviors. A common choice for policy learning is to use diffusion or flow matching (Flow-Policies), which often outperforms direct action regression trained with mean squared error (MSE-Policies). This gap is commonly attributed to multimodal demonstrations. We revisit this gap from the perspective o…

### 5. NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

- **arXiv**: [2610.10787v1](https://arxiv.org/abs/2610.10787v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10787v1)
- **作者**: Gengze Zhou, Yicong Hong, Jiazhao Zhang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control…

## 🌐 具身智能 / 机器人基础模型 (8 篇)

### 1. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 2. RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment

- **arXiv**: [2610.09294v1](https://arxiv.org/abs/2610.09294v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09294v1)
- **作者**: Tianruo Rose Xu, Jiawei Ren, Yichi Yang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-t…

### 3. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

### 4. SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation

- **arXiv**: [2610.08941v1](https://arxiv.org/abs/2610.08941v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08941v1)
- **作者**: Yunheng Liu, Ziqi Cai, Siqi Yang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming…

### 5. Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage

- **arXiv**: [2610.08933v1](https://arxiv.org/abs/2610.08933v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08933v1)
- **作者**: Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI, cs.HC
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independe…

### 6. SpaTime: Streaming Vision-Language Models for Spatio-temporal Reasoning

- **arXiv**: [2610.08713v1](https://arxiv.org/abs/2610.08713v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08713v1)
- **作者**: Hairong Yin, Huangying Zhan, Shin-Fang Chng et al.
- **发表**: 2026-10-06  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents must reason about 3D space while the video is still arriving, answering questions as soon as they have observed enough of the scene. VLMs that incorporate 3D geometric priors achieve strong spatial reasoning, but they operate offline, i.e., the full video must be available before they produce an answer. Streaming VLMs process frames causally…

### 7. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- **arXiv**: [2610.00864v1](https://arxiv.org/abs/2610.00864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00864v1)
- **作者**: Jiawei Fan, Sifeng Wang, Yuqing Hou et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited…

### 8. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (28 篇)

### 1. BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation

- **arXiv**: [2610.07594v1](https://arxiv.org/abs/2610.07594v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07594v1)
- **作者**: Zexi Zhang, Zecheng Zhu, Zidong Chen et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchron…

### 2. A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control

- **arXiv**: [2610.12465v1](https://arxiv.org/abs/2610.12465v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12465v1)
- **作者**: Octi Zhang, Mateo Guaman Castro, Patrick Yin et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: General-purpose robots must perform a wide range of tasks from agile locomotion to dexterous manipulation. While sim-to-real reinforcement learning (RL) has proven to be a useful tool for this goal, current RL pipelines depend on engineering-heavy, per-task structural priors such as shaped rewards and demonstrations. Recent work has shown that diverse simul…

### 3. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

- **arXiv**: [2610.06850v1](https://arxiv.org/abs/2610.06850v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06850v1)
- **作者**: Yucheng Zhang, Sirui Xu, Jinhong Li et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.GR
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object i…

### 4. Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data

- **arXiv**: [2610.09117v1](https://arxiv.org/abs/2610.09117v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09117v1)
- **作者**: Songbo Hu, Qiayuan Liao, Yufeng Chi et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid robots still struggle to plan contact-rich whole-body manipulation from egocentric RGB and proprioception. Workhorse learns such manipulation from robot-free human demonstrations. A visual planner predicts five-link targets: the poses of the torso, both wrists, and both feet. A reinforcement-learning whole-body tracker follows them on the robot. Bo…

### 5. Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and Reward Gating

- **arXiv**: [2610.08320v1](https://arxiv.org/abs/2610.08320v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08320v1)
- **作者**: Haozhuo Zhang, Qiang Zhang, Jian Tang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Cluttered indoor environments, where large and heavy objects are scattered across diverse surfaces, require humanoid robots to sequentially navigate, grasp, transport, and accurately place each item at its target location within a single uninterrupted episode. This long-horizon, whole-body loco-manipulation task remains a significant challenge for current m…

### 6. Humanoid World Action Model With Joint State--Action Generation

- **arXiv**: [2610.12026v1](https://arxiv.org/abs/2610.12026v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12026v1)
- **作者**: Yan Yang, Jikun Rong, Minzhao Zhu et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output referen…

### 7. Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction

- **arXiv**: [2610.09291v1](https://arxiv.org/abs/2610.09291v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09291v1)
- **作者**: Jeonghwan Kim, Hyeonwoo Kim, Hanbyul Joo
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present…

### 8. LLA-MPPI: Rapidly Adaptive Whole-body Control of Legged Robots with GPU-Accelerated Parallel Simulations

- **arXiv**: [2610.10465v1](https://arxiv.org/abs/2610.10465v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10465v1)
- **作者**: Sebin Jung, Maitham F. AL-Sunni, Juan Alvarez-Padilla et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Real-time whole-body controllers for legged robots typically plan through a fixed nominal model and degrade when the deployed dynamics change. Adaptive methods typically require a model structure that contact dynamics do not provide, or they need offline training for each anticipated condition. We present Look-back and Look-ahead Adaptive Model Predictive P…

### 9. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 10. PhoneBot: A Low-Cost Open Humanoid Robot Platform Reusing Smartphones

- **arXiv**: [2610.08737v1](https://arxiv.org/abs/2610.08737v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08737v1)
- **作者**: Ruochen Hou, Quanyou Wang, Daniel Koh et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: The adoption of humanoid robots in education and research remains limited by high hardware costs, complex sensing systems, and substantial computational requirements. This paper presents PhoneBot, a low-cost, open-source humanoid robot platform that repurposes commodity smartphones as its primary sensing and computing unit. By using a smartphone's integrate…

## 🦾 操控 / 灵巧手 / 抓取 (29 篇)

### 1. Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration

- **arXiv**: [2610.12470v1](https://arxiv.org/abs/2610.12470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12470v1)
- **作者**: Jusuk Lee, Sungha Kim, Yeonsoo Park et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via…

### 2. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors

- **arXiv**: [2610.07681v1](https://arxiv.org/abs/2610.07681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07681v1)
- **作者**: Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation poses a challenging high-dimensional optimization problem, as useful behaviors require coordinated motion across many hand joints. In reinforcement learning (RL) and sampling-based trajectory optimization, exploration commonly relies on independent robot joint perturbations, making coordinated behaviors difficult to discover. Prior wo…

### 3. OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes

- **arXiv**: [2610.11194v1](https://arxiv.org/abs/2610.11194v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11194v1)
- **作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous grasping is the foundational primitive in embodied AI, demanding massive data to train robust models. As real-world data collection is expensive, simulation has become the mainstream paradigm. Yet, while cluttered scenes best reflect real-world applications, learning to grasp within them is bottlenecked by a critical scarcity of large-scale data.…

### 4. SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation

- **arXiv**: [2610.11248v1](https://arxiv.org/abs/2610.11248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11248v1)
- **作者**: Kyoungin Baik, Youngwoon Lee
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Large-scale, diverse datasets have driven the success of LLMs and VLMs. But VLAs for robotics remain limited by the cost and complexity of real-world data collection. While simulation offers a scalable alternative, its potential for sim-to-real VLA learning in mobile manipulation remains largely underexplored. We introduce SimVLA, an end-to-end framework th…

### 5. GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive

- **arXiv**: [2610.03861v1](https://arxiv.org/abs/2610.03861v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03861v1)
- **作者**: Yulin Liu, Lai Wei, Yen-Jen Wang et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Foundation models and large-scale human data provide rich sources of manipulation intent, but translating this intent into multi-fingered robot behavior remains difficult. Dexterous hands still lack a reusable low-level primitive that reliably establishes contact across tasks and embodiments. We propose GOTT, a reach-acquire-move framework built around a si…

### 6. PatternDex: Learning Interaction Patterns to Guide Reinforcement Learning of Bimanual Dexterous Manipulation of Articulated Objects

- **arXiv**: [2610.04765v1](https://arxiv.org/abs/2610.04765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04765v1)
- **作者**: David Minkwan Kim, Runfa Blark Li, Beckham Po-Ju Lee et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: In this paper, we develop a method that enables bimanual dexterous hands to manipulate articulated objects with a high success rate without suffering from an embodiment gap. We observe that the correlation between hand motions and object motions is dictated by the object rather than the hands and can be learned from human-object demonstrations. Based on thi…

### 7. SkillWeave: Weaving Heterogeneous Demonstrations into Long-Horizon Manipulation Skills

- **arXiv**: [2610.12046v1](https://arxiv.org/abs/2610.12046v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12046v1)
- **作者**: Ryosei Tamura, Xiaoxiang Dong, Uksang Yoo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation requires both large-scale task progression and precise contact-rich interaction, making it challenging to collect demonstrations that effectively support both regimes. We present SkillWeave, a heterogeneous demonstration framework for long-horizon dexterous manipulation that combines teleoperation for coarse reaching and transport wit…

### 8. VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

- **arXiv**: [2610.12451v1](https://arxiv.org/abs/2610.12451v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12451v1)
- **作者**: Boyao Han, Chen Shi, Jingjing Qian et al.
- **发表**: 2026-10-08  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set represen…

### 9. OmniHOI: Dexterous Hand-Object Interaction from Monocular Human Video

- **arXiv**: [2610.10855v1](https://arxiv.org/abs/2610.10855v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10855v1)
- **作者**: Ting Mao, Yanming Shao, Ziheng Wang et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Monocular videos of human manipulation provide abundant dexterous demonstrations, yet reconstructing hand-object interaction from a single view and transferring it to robot hands remain difficult, limiting their direct use for robot execution. Prior methods either require task-specific RL training, limiting scalability, or assume clean motion-capture trajec…

### 10. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

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
- **相关性评分**: 8  ·  **👀 watch**
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
2. [EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors](https://arxiv.org/abs/2610.07681v1) — score 20
3. [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
