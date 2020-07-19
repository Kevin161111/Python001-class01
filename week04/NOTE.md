## W4 Notes

本周主要内容是数据清洗和预处理，主要通过 `pandas` 来实现。

#### pandas 的基本数据类型

* `Series` ，类似Excel 中的单独列。

* `DataFrame`，类似Excel中的多行多列。

`pandas`的底层是基于 python 的 数据处理库 `numpy`,很多的函数和数据结构可以相互转换。

#### 数据清洗和预处理

拿到数据后要先对数据进行清洗和预处理，主要是根据业务需求处理数据中的缺失值和重复值。

#### 数据的合并

- `merge`
- `concat`

数据合并接近 数据库表的操作，可以多了解数据库表操作的相关原理来处理数据。

#### 数据输出与绘制

- `matplotlib`
- `seaborn`

#### 语义分析库 `jieba`、`snownlp`

`jieba` 分词可以引入自己编辑的语义，对词进行划分。

- 提前定义
- 动态加载 `jieba.add_word('xxx')`
- 调整分词合并 `jieba.suggest_freq('xx',True)`

`snownlp` 情感倾向分析

