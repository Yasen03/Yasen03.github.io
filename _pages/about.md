---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
# 💡 About Me
<span class='anchor' id='about-me'></span>
I am currently a master's student at Tsinghua Shenzhen International Graduate School (SIGS), Tsinghua University. My research interests mainly focus on <span class="paper-badge-text" style="background-color: #6B7A99;"><i class="fas fa-shield-alt" aria-hidden="true"></i>&nbsp;AI-Generated Audio/Video Detection (AIGC Safety)</span> and <span class="paper-badge-text" style="background-color: #4A7C8C;"><i class="fas fa-globe" aria-hidden="true"></i>&nbsp;World Models</span>. Welcome to collaborate on related projects.

Contact me at: [yueshenghuang@stu.gpnu.edu.cn](mailto:yueshenghuang@stu.gpnu.edu.cn) | <strong>English</strong> / <a href="/zh">中文</a>

# 🔥 News
<span class='anchor' id='-news'></span>
- *2026.01*: &nbsp;🚀 I released **Awesome Affective Computing** — A curated list of Affective Computing & Emotion AI: Papers, datasets, and toolkits for Multimodal Emotion Recognition, Emotional Reasoning, Multimodal Sentiment Analysis, and Empathetic LLMs/MLLMs. <a href="https://github.com/Yasen03/awesome-affective-computing" style="text-decoration: none;"> <i class="fab fa-fw fa-github" aria-hidden="true"></i> Awesome Affective Computing <img src="https://img.shields.io/github/stars/Yasen03/awesome-affective-computing?style=social" alt="Stars" style="vertical-align: middle;"></a>
- *2025.08*: &nbsp;🏆 I won **1st Place** in the **ACM MM 2025 MER Challenge (DES Track)** as team leader!
- *2025.08*: &nbsp;📄 My first-author paper was accepted by the **ACM MM 2025 Main Conference Grand Challenge Track**!
- *2024.12*: &nbsp;&nbsp;🎉 I was selected as the 2023 **Guangdong Provincial Person of the Year** (one of 10 winners), the **youngest winner** that year.
- *2024.05*: &nbsp;&nbsp;🎉 I was featured in the **People's Daily** as a representative of 100 undergraduate national scholarship winners, **only 4** of whom were from Guangdong Province. 
- *2023.12*: &nbsp;&nbsp;🎉 I was awarded the **National Scholarship**.

# 📝 Publications 
<span class='anchor publications-anchor' id='-publications'></span>
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2025</div><img src='{{ site.baseurl }}/images/affective.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">Affective-CoT: Decomposing Multimodal Emotion Reasoning through a Hierarchical Cognitive Workflow（🏆 MER2025-DES Champion）</div>
  
**Yuesheng Huang**, Jinming Liu, Jiajia Chen, Yihang Lin, Yanmei Chen<sup>*</sup>, Jianwei Dong

<div class="paper-meta">ACM MM 2025 Main Conference Grand Challenge Track（Oral）</div>
<div class="paper-links">
  <a class="paper-badge" href="https://dl.acm.org/doi/10.1145/3695952.3731175"><img src="https://img.shields.io/badge/Paper-ACM%20DL-0071C5" alt="ACM DL"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-acmmm2025', event)">Cite</button>
  <a class="paper-badge" href="https://scholar.google.com/citations?user=edyJPQQAAAAJ"><img id="citation-badge-affective-cot" src="https://img.shields.io/badge/Citations-3-blue?style=social&logo=google-scholar" class="paper_citations" data-paper-id="edyJPQQAAAAJ:Y0pCki6q_DkC" alt="Scholar Citations"></a>
</div>
<div id="citation-acmmm2025" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@inproceedings{huang2025affective, <br>      title={Affective-CoT: Decomposing Multimodal Emotion Reasoning through a Hierarchical Cognitive Workflow}, <br>      author={Huang, Yuesheng and Liu, Jinming and Chen, Jiajia and Lin, Yihang and Chen, Yanmei and Dong, Jianwei}, <br>      booktitle={Proceedings of the 33rd ACM International Conference on Multimedia}, <br>      pages={13848--13855}, <br>      year={2025} <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MRAC@ACM MM</div><img src='{{ site.baseurl }}/images/DARE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">DARE to Disagree: A Multi-Agent Adversarial Debate Framework for Open-Vocabulary Multimodal Emotion Recognition</div>
  
**Yuesheng Huang**, Meiqi Feng, Zhenming He, Yueyuan Peng, Jiawen Li<sup>*</sup>

<div class="paper-meta">ACM MM 2025 MRAC Workshop（Oral）</div>
<div class="paper-links">
  <a class="paper-badge" href="https://dl.acm.org/doi/10.1145/3706591.3706600"><img src="https://img.shields.io/badge/Paper-ACM%20DL-0071C5" alt="ACM DL"></a>
  <a class="paper-badge" href="https://github.com/GPNU-AIoT/DARE"><img src="https://img.shields.io/github/stars/GPNU-AIoT/DARE?style=social" alt="GitHub Stars"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-dare2025', event)">Cite</button>
  <a class="paper-badge" href="https://scholar.google.com/citations?user=edyJPQQAAAAJ"><img id="citation-badge-dare" src="https://img.shields.io/badge/Citations-1-blue?style=social&logo=google-scholar" class="paper_citations" data-paper-id="edyJPQQAAAAJ:Tyk-4Ss8FVUC" alt="Scholar Citations"></a>
</div>
<div id="citation-dare2025" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@inproceedings{huang2025dare, <br>      title={DARE to Disagree: A Multi-Agent Adversarial Debate Framework for Open-Vocabulary Multimodal Emotion Recognition}, <br>      author={Huang, Yuesheng and Feng, Meiqi and He, Zhenming and Peng, Yueyuan and Li, Jiawen}, <br>      booktitle={Proceedings of the 3rd International Workshop on Multimodal and Responsible Affective Computing}, <br>      pages={41--50}, <br>      year={2025} <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML NewInML</div><img src='{{ site.baseurl }}/images/fig1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">Synthetic Perception: Can Generated Images Unlock Latent Visual Prior for Text-Centric Reasoning?</div>
  
**Yuesheng Huang**<sup>*</sup>, Peng Zhang, Xiaoxin Wu, Riliang Liu, Jiaqi Liang

<div class="paper-meta">ICML 2025 NewInML Workshop（Poster）</div>
<div class="paper-links">
  <a class="paper-badge" href="https://arxiv.org/abs/2506.17623"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B" alt="arXiv"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-arxiv2025', event)">Cite</button>
  <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:W7OEmFMy1HYC"><img id="citation-badge-generated-images" src="https://img.shields.io/badge/Citations-loading-6c757d" class="paper_citations" data-paper-id="edyJPQQAAAAJ:W7OEmFMy1HYC" alt="Scholar Citations"></a>
</div>
<div id="citation-arxiv2025" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@misc{huang2025syntheticperception,<br>      title={Synthetic Perception: Can Generated Images Unlock Latent Visual Prior for Text-Centric Reasoning?}, <br>      author={Yuesheng Huang and Peng Zhang and Xiaoxin Wu and Riliang Liu and Jiaqi Liang},<br>      year={2025},<br>      eprint={2506.17623},<br>      archivePrefix={arXiv},<br>      primaryClass={cs.MM},<br>      url={https://arxiv.org/abs/2506.17623}, <br>}</div>
  </div>
</div>
</div>
</div>

- **Sentiment Analysis Using E-Commerce Review Keyword-Generated Image with a Hybrid Machine Learning-Based Model.** Jiawen Li, **Yuesheng Huang**, Yayi Lu, Leijun Wang\*, Yongqi Ren, Rongjun Chen. *Computers, Materials & Continua*, 2024. [[Paper](https://www.techscience.com/cmc/v80n1/57421)] <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:d1gkVwhDpl0C"><img class="paper_citations" data-paper-id="edyJPQQAAAAJ:d1gkVwhDpl0C" src="https://img.shields.io/badge/Citations-25-blue?style=social&logo=google-scholar" alt="Scholar Citations"></a>
- **An Improved Hybrid CNN-LSTM-Attention Model with Kepler Optimization Algorithm for Wind Speed Prediction.** **Yuesheng Huang**, Jiawen Li\*, Yushan Li, Routing Lin, Jingru Wu, Leijun Wang, Rongjun Chen. *Engineering Letters*, 2024. [[Paper](https://www.engineeringletters.com/issues_v32/issue_10/EL_32_10_14.pdf)] [[Code](https://github.com/Yasen03/KOA-CNN-LSTM-Attention)] <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:2osOgNQ5qMEC"><img class="paper_citations" data-paper-id="edyJPQQAAAAJ:2osOgNQ5qMEC" src="https://img.shields.io/badge/Citations-12-blue?style=social&logo=google-scholar" alt="Scholar Citations"></a>

# 🏆 Competition Awards
<span class='anchor' id='-honors-and-awards'></span>
- *2026.08* **Finalist** in the **Physical AI Hackathon 2026** (Hong Kong, China).
- *2025.08* **Champion (1st Place)** in the **ACM MM 2025 MER Challenge (DES Track)** as team leader.
- *2024.05* **Finalist Award** in the **COMAP Mathematical Contest in Modeling (MCM/ICM)**, Problem E (**Top 2%** worldwide).
- *2023.11* **First Prize** in the Guangdong Division of the China Undergraduate Mathematical Contest in Modeling.
- *2023.08* **First Prize** in the China College Student Computer Design Competition (Guangdong Division).
- *2021.12* **Silver Medal** in the Kaggle Lux AI Competition.

# 🎓 Educations
<span class='anchor' id='-educations'></span>
- *2026.09 - 2028.06*, Master's student, Tsinghua Shenzhen International Graduate School (SIGS), Tsinghua University.
- *2021.09 - 2025.06*, Bachelor of Engineering in Internet of Things Engineering(**ESI TOP 1%**), School of Computer Science, Guangdong Polytechnic Normal University, **Excellent Graduate**.(**GPA:92.1/100, Rank:1/111**)
- *2018.09 - 2021.06*, Ordinary high school, Shaoguan City Wengyuan middle School

# 📖 Research topics
<span class='anchor' id='-research-topics'></span>
- *2023.05-2024.05*, "Research and implementation of MIMO system detection algorithm based on Gaussian tree", Chinese college students Innovation and Entrepreneurship plan project, **Host**. (Project completed)
- *2024.01-2026-01*, "Research on fine-grained sentiment analysis of multi-modal data fusion based on deep learning", Guangdong Provincial Science and Technology Innovation Fund, 45,000CNY, **Host**. (Project completed)
- *2024.05-2025.05*, "Neurodetective: An interpretable multimodal contrastive learning Framework for the diagnosis of neurodegenerative diseases", Chinese college students Innovation and Entrepreneurship plan project, **Host**. (Project completed)
- *2024.05-2025.05*, "Aquaponics, Ecological co-prosperity: A general agricultural visual large model for digital aquaponics fish pond system called DASAM", Chinese college students Innovation and Entrepreneurship plan project, Participant.(Project completed)
