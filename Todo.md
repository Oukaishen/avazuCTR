## Todo List

+ 训练集有6G这么大，需要采样一小部分，来做小实验。

   尝试以下几种做法：

  ```shell
  (head -n 500000 $train_path && tail -n 500000 $train_path) > $subsampled_data_path
  ```

  但是这个会包含开头。我们不想要第一行。

  

  