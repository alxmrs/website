# Notes on Robust ML

An article (talk?) in the making. 


## Undifferentiated ML Eng Tips

- use [DI](https://en.wikipedia.org/wiki/Dependency_inversion_principle) for model configuration, e.g. [gin](https://github.com/google/gin-config)

- [active learning](https://humanloop.com/blog/why-you-should-be-using-active-learning/) 

- [interpretability techniques](https://christophm.github.io/interpretable-ml-book/)
  
  - [anchors](https://github.com/marcotcr/anchor)
  
  - [shap](https://github.com/slundberg/shap)
    
  - confusion mx to find what to interpret
    
  - find out why you’re model is wrong, what it’s bounds are
    
- structure the output of the model to have a robust “don’t know class”
  - currency detector (most images it will see are not currency)
  - [squad 2.0](https://rajpurkar.github.io/SQuAD-explorer/)
    - e.g. [Colorless green ideas sleep furiously](https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously) --> "I don't know"
    
- pre train your model on synthetic data you can cheaply create. fine tune the model on in house data

- TODO(alxr): research: curriculum learning

- [metamorphic testing](https://www.hillelwayne.com/post/metamorphic-testing/)

- version control data + models

  - [dvc](https://dvc.org/) vs [hub](https://github.com/activeloopai/Hub) vs git-lfs vs [roll your own](https://github.com/alxrsngrtn/Electron-Diffraction-CNN)

- the shape of your program should be commensurate to the size of your data

  - fits in memory: jupyter notebook
  
  - fits on your computer: library w/ scripts
  
  - fits on the data center: [beam](https://beam.apache.org/), [spark](https://spark.apache.org/)

- when you write code to answer data science questions, package it into an API

- cicd
  
  - [cml](https://cml.dev/)

## Principles at Play

- [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)

- [Techniques for software correctness](https://www.hillelwayne.com/uncle-bob/)
