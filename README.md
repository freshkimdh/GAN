# GAN을 활용한 이미지 생성
한국인 얼굴 생성 프로젝트

## 1. GAN의 역사

* GAN (Generative Adversarial Network)

* CGAN (Conditional Generative Adversarial Network)

* DCGAN (Deep Convolutional Generative Adversarial Network)

* CoGAN (Coupled Generative Adversarial Networks)

* Pix2pix

* WGAN (Wasserstein Generative Adversarial Network)

* CycleGAN

* StackGAN (Stack Generative Adversarial Network)

* ProGAN (Progressive Growing of Generative Adversarial Network)

* SAGAN (Self-Attention Generative Adversarial Network)

* BigGAN (Big Generative Adversarial Network)

* StyleGAN (Style-based Generative Adversarial Network)


## 2. 프로젝트에 활용되는 GAN 알고리즘
GAN
DCGAN
CycleGAN
ProGAN
StyleGAN
StarGAN


#### GAN
기존의 디럽닝 기술에서 활용한 인공 신경망과는 다른 학습 방법을 활용하여 

사람이 보기에 진짜와 구분하기 힘들 정도로 정교한 가짜 이미지를 만들어 내는 기술

![그림1](https://user-images.githubusercontent.com/65889898/108954892-bc46a480-76b0-11eb-88cb-fafa53391872.png)


#### DCGAN

GAN의 불안정한 학습을 해결하고자 2016년 Google에서 DCGAN 발표하였으며,

GAN의 생성 신경말 구조에서 노이즈를 확장시키는데 있어서 미분이 불가능한 모든 층을 

모두 미분이 가능한 컨볼류션으로 대체 구성하여 학습의 안정성과 서능을 높이는 방법을 제시

예를 들어 아래 이미지처럼 안경을 쓴 남자의 이미지에서 안경을 쓰지 않은 남자의 이미지 정보를 제거하고

안견을 쓰지 않은 여자의 이미지 정보를 추가하면 안경을 쓴 여자의 이미지를 만들어 낼 수 있다는

이미지 연산이 가능함을 보여줬습니다.

![20210224150832](https://user-images.githubusercontent.com/65889898/108955854-2dd32280-76b2-11eb-86f6-e4990f2ee3fa.jpg)


#### ProGAN (Progressive growing)

GAN 에서 일반적으로 512 x 512 이상의 이미지에 대해서 고해상도라고 이야기 하고 있다.

ProGAN은 고해상도의 얼굴 이미지를 생성하기 위해 초저해상도(4x4)에서 부터 차근차근 이미지를 생성하는 방법을 학습하여

고해상도 이미지를 생성하는 방법이다.

DCGAN 에서 겨우 128x128 크기 해상도의 얼굴이밎 생성이 가능했는데, 최근 얼굴 이미지의 해상도가 1024 x 1024 로 크게 증가하였다.

![20210224154003](https://user-images.githubusercontent.com/65889898/108958642-97553000-76b6-11eb-9c64-289e8909967e.jpg)


#### StyleGAN

내용입력


#### StarGAN

한 개의 모델을 이용하여 내가 원하는 부분에 대해서만 이미지 변환을 수행 할 수 있게 된다.

사용자가 사람의 머리색 또는 피부색과 같이 단 한 개만 변화시키고 싶을 떄 사용할 수 있는 기술이다.

![20210224155841](https://user-images.githubusercontent.com/65889898/108960394-2f541900-76b9-11eb-810b-7bc0ac84ae36.jpg)


## 3. Train Dataset

한국 AI-HUB 한국인 이미지 활용

https://www.aihub.or.kr/


## 4. Skill Set
* GAN 알고리즘 활용
* Python
* Pytorch
* Activation Function


## 5. 구동방법
* VSCODE
* cuda
* Nvidia


참고문헌
https://engineer-mole.tistory.com/42 [매일 꾸준히, 더 깊이]
