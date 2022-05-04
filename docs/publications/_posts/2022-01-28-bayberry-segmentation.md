---
title: Bayberry segmentation in a complex environment based on a multi-module convolutional neural network
editor: leihuan
authors:
  - Huan Lei
  - Kai Huang
  - Zeyu Jiao
  - Yu Tang
  - Zhenyu Zhong
  - Yingjie Cai
by: Applied Soft Computing
tags:
  - SCI
doi: 10.1016/j.asoc.2022.108556
abstract: Automatic bayberry picking can substantially reduce labor costs and improve picking efficiency in an orchard management system. Nowadays, an automatic picking system mainly relies on machine vision to segment bayberry fruit from the background. Most existing methods are carried out in an environment where the light intensity is relatively fixed and the bayberries are unobstructed. However, due to the complexity of the growing environment, including variations in lighting and widespread occlusion, segmentation accuracy is quite limited, which affects the large-scale application of automatic picking systems. Aiming at these issues, in this study, a bayberry segmentation method based on a multi-module convolutional neural network is proposed. First, the bayberry images in a real scene were collected and preprocessed to form a dataset. Then, a convolutional neural network was constructed, with an image correction module to improve the network’s robustness to natural ambient lighting. Finally, a shape completion module with a puzzle algorithm was utilized to overcome the occlusion in the natural environment. The experimental results show that the average precision of the proposed method for semantic segmentation and instance segmentation of bayberry fruit can reach 0.913 and 0.755, respectively, which outperforms the existing methods and has important significance for automatic picking in orchards.
contributions:
  - A multi-module CNN is proposed for bayberry segmentation in complex environment.
  - An image correction module is adopted to make the model robust to lighting changes.
  - A puzzle algorithm is proposed to enhance the model’s robustness to occlusion.
  - Ablation experiments are implemented to analyze the effect of each module seriatim.
thumbnail_type: png
overview_image_type: png
---
目前果园自动采摘系统主要依靠机器视觉从背景中分割果实，但大多数现有的方法仅局限于光照强度固定且果实无遮挡的环境，对于光照变化大、重叠遮挡严重的杨梅生长环境仍难以推广应用。为此，提出了基于多模块卷积神经网络的复杂环境杨梅分割方法。通过构建基于图像校正的卷积神经网络和基于puzzle算法的形状补全模块，提高了模型对自然环境光照的鲁棒性并克服了果实重叠遮挡问题。通过实际环境数据验证，杨梅果实的语义分割和实例分割的平均精度分别达到0.913和0.755，对果园自动采摘具有重要意义。


## 数据增强示例
{: .text-center}

{: .text-center}
![Examples of the data augmentation](https://images.cdn.ergonomic.top{{ page.url }}/1.png){: .w-75}


## 算法总体方案
{: .text-center}

{: .text-center}
![Overall scheme of the proposed method](https://images.cdn.ergonomic.top{{ page.url }}/2.png){: .w-75}


## Puzzle算法流程
{: .text-center}

{: .text-center}
![The flow of the puzzle algorithm](https://images.cdn.ergonomic.top{{ page.url }}/3.png){: .w-75}


## 不同语义分割方法的效果展示
{: .text-center}

{: .text-center}
![Visual results of different semantic segmentation methods](https://images.cdn.ergonomic.top{{ page.url }}/4.png){: .w-75}


## 不同实例分割方法的效果展示
{: .text-center}

{: .text-center}
![Visual results of different instance segmentation methods](https://images.cdn.ergonomic.top{{ page.url }}/5.png){: .w-75}


## 不同现实复杂环境下的结果展示
{: .text-center}

{: .text-center}
![Segmentation results in different real-life environments](https://images.cdn.ergonomic.top{{ page.url }}/6.png){: .w-75}
