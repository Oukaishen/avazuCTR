## Todo List

+ 训练集有6G这么大，需要采样一小部分，来做小实验。**[done]**

 尝试以下几种做法：

```shell
(head -n 500000 $train_path && tail -n 500000 $train_path) > $subsampled_data_path
```

但是这个会包含开头。我们不想要第一行。

使用以下这个

```shell
tail -n +2 $train_path | head -n 500000 > $subsampled_data_path
tail -n 500000 $train_path >> $subsampled_data_path
```

也可以使用随机数进行采样工作

分别采样了50k，1m 的小型训练集。

<br>

+ Try other's model, model 1 is elena's model from [her github](https://github.com/elenacuoco/Avazu). **[done]**

Only using 1m training examples. About **18 minutes** trained on my MacBook Pro. Achieve **0.4017** on private score and **0.4035** on public score. Cool!

Rewrite the train method. ~5 minute on the 1m training samples.

Try to train the model with all the training sample on this model. Can only achieve 0.398 on private and 0.400 on public.  Ttraining time around 3 hours.

<br>

+ 尝试用简单的sklearn里面的库，利用gdbt这个模型，利用50k这个小型训练集。来做一个小预测。





+ 有了小的train以后，可以开始做一些尝试。可以从kaggle上的已有ftrl模型开始。

