![NeuralClassifier Logo](readme/logo.png)

# NeuralClassifierService: A Service for Multi-label Text Classification Toolkit

## Introduction

This service is for post use of the parent repository after trained with data sets, and if you want to use your model as some DeepLearning backend, fork this web wrapper repository.

## Notice

* I assume you have trained your model well and you are ready to use it for production.
* Production did not require GPU evniroment, and current repo config is using pytorch CPU opt by default
* Please use the config file while you are training instead of using my config file.
* I assume you are using GNU operating systems and using UTF-8 as encoding

## Requirement

* Python 3
* PyTorch 0.4+
* Numpy 1.14.3+
* Flask

## Usage

### Training

    python train.py conf/train.json

***Detail configurations and explanations see [Configuration](readme/Configuration.md).***

The training info will be outputted in standard output and log.logger\_file.

### Evaluation
    python eval.py conf/train.json

* if eval.is\_flat = false, hierarchical evaluation will be outputted.
* eval.model\_dir is the model to evaluate.
* data.test\_json\_files is the input text file to evaluate.

The evaluation info will be outputed in eval.dir.

### Prediction
    python predict.py conf/train.json data/predict.json

* predict.json should be of json format, while each instance has a dummy label like "其他" or any other label in label map.
* eval.model\_dir is the model to predict.
* eval.top\_k is the number of labels to output.
* eval.threshold is the probability threshold.

The predict info will be outputed in predict.txt.

## Input Data Format

    JSON example:

    {
        "doc_label": ["Computer--MachineLearning--DeepLearning", "Neuro--ComputationalNeuro"],
        "doc_token": ["I", "love", "deep", "learning"],
        "doc_keyword": ["deep learning"],
        "doc_topic": ["AI", "Machine learning"]
    }

    "doc_keyword" and "doc_topic" are optional.
## Start classification service

This service contains two module: a deep learning backend and a flask wrapper, they communicate via socket at port 4444. Above this is a shell wrapper to manipulate the two process: start them, keep them and kill them together when signal receieved.

>./start.sh #to start the whole service

the web page start at '0.0.0.0', port 55555 by default, or edit them in server.py.

The main page is to test if your config is valid, paste a post to the textarea,
`purge newline`, and click `Go` to get predict results, each post is splited by a newline which explains why you should purge new lines from a single post.



Also, headless json response is provided, send a json to `[host]:[port]/headless` and get a json with results

**send:**

{"posts":["blah","blah blah", "blah blah"]}

**and get:**

{"results" :["class of blah", "class of blah blah", "class of blah blah blah"]}

## Demo enviroment

* Training dataset : toutiao, 16 single labels, 280k posts, length 1536, eval precision 91%

* Infer server performance : CPU, no delay
