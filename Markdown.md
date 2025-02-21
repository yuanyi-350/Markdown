[TOC]

## Typora安装

https://djcgihkpzx.feishu.cn/docx/WtBodvJKooOfuVxVNuxc5aixn3f
非正版Typora的下载网址，亲测有效

## Markdown自动补全

[VIM+LaTeX 自动补全 - 简书](https://www.jianshu.com/p/720b369dd583)

[教程向: 在 VS Code 中用 Markdown 做「数字化」学习笔记 - 知乎](https://zhuanlan.zhihu.com/p/366596107)

下载 vscode , 并且 **开启** 在 markdown 下的 **自动补全提示**, 请使用 `Shift + Ctrl + P` 然后输入 `open settings json` 打开配置文件, 然后加入以下部分:

```json
"[markdown]": {
    "editor.quickSuggestions": true
},
```

**安装完成后**, 按下快捷键 `Ctrl + Shift + P`, 输入命令 `Open Snippets Directory`, 就可以打开一个文件夹. 在 **该文件夹** 新建一个文件 `markdown.hsnips`, 并将 [OrangeX4's hsnips](https://github.com/OrangeX4/OrangeX4-HyperSnips/blob/main/markdown.hsnips) 里面的内容输入进去, 保存, 就可以使用了.

hsnips 文件规则参照 [draivin/hsnips: HyperSnips: a powerful snippet engine for VS Code, inspired by vim's UltiSnips](https://github.com/draivin/hsnips)

先看个 **普通例子**:

```hsnips
snippet \R "R" iAm
\mathbb{R}
endsnippet
```

这是一个在数学环境中自动展开的 Snippet, 它有三个标示符 `iAm`, 分别代表 "在词语内部也会触发", "自动展开" 和 "数学环境".

这个例子会在数学环境内, 自动将 `\R` 展开成为 `\mathbb{R}`

相比于原来的 HyperSnips, 最大特点是, 它只会在数学环境 `$...$`, `$$...$$`, `\(...\)` 和 `\[...\]` 中自动展开!

##### 特别的注意点

原文件考前有一句`end global`不要忽略

` `` `中用`\\`展示`"\"` , 在`snippet`首行用`\`展示`"\"`

## [Markdown_Format](https://www.zhihu.com/question/276209281/answer/3045412944)

#####标题

打几个井号"#"#表示是第几级标题（h1~h6）



#####有序列表

使用数字接着一个英文句点" . "作为标记，序号跟内容之间要有空格



#####无序列表

使用星号" * "、加号" + "或是减号" - "作为列表标记," - " " + " " * " 跟内容之间都要有一个空格



#####单行代码

用一个反引号" ` "包起来

```markdown
这里有一句代码`代码内容`。
```

这里有一句代码`代码内容`



##### 代码块

用三个反引号" ` "包起来



##### 粗体<font : color = Red> (Ctrl + B)</font>

“ ** ” + 文本内容 + “ ** ” (星号) 

'' __ '' + 文本内容 + ' __ '   (下划线)

```markdown
这是一段普通文本
**这里是一段加粗文本**
__这也是一段加粗文本__
```

这是一段普通文本
**这里是一段加粗文本**
__这也是一段加粗文本__



##### 文本下划线<font : color = Red>(Ctrl + U)</font>

**`<u>`** + 文本内容 + **`</u>`**

```markdown
<u>这是一段加了下划线的文本</u>
```

<u>这是一段加了下划线的文本</u>



##### 斜体

“ * ” + 文本内容 + “ * ”  (星号)

'' _ '' + 文本内容 + ' _ '   (下划线)

```markdown
这是一段普通文本
*这里是一段斜体文本*
_这也是一段斜体文本_
```

这是一段普通文本

*这里是一段斜体文本*
_这也是一段斜体文本_



##### 文本删除线

**`~~`** + 文本内容 +**`~~`** (首尾各加两个 **~** 波浪号)

```markdown
~~这是一段加了删除线的文本~~
```

~~这是一段加了删除线的文本~~



##### 水平分割线

水平分割线由至少 **3** 个 `*` 或 `-` 组成

```markdown
---
```

***



##### 颜色

```html
<font color=Blue>蓝色</font>
```

<font color=Blue>蓝色</font>

```latex
$\color{blue} e^{i\pi}+1=0$ 
```

$\color{blue} e^{i\pi}+1=0$ 

```latex
$\text{\textcolor{blue}{蓝色}}$
```

$\text{\textcolor{blue}{蓝色}}$



##### 超链接

```markdown
[北大树洞](https://treehole.pku.edu.cn/web/)
```

[北大树洞](https://treehole.pku.edu.cn/web/)



##### 分页

```html
<div STYLE="page-break-after: always;"></div>
```

<div STYLE="page-break-after: always;"></div>

##Markdown_Sheet

```markdown
| Header 1 | Header 2 | Header 3 |
```

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
|          |          |          |

Ctrl + Enter 加行 



## Markdown_MathMode

##### 空格

```latex
$1\ 2$ $1\quad2$ $1\qquad2$
```

output : $1\ 2$

​	       $1\quad2$

​	       $1\qquad2$



##### 公式等号对齐

```latex
\begin{align*}
1 & = 2\\
& = 345\\
& = 6
\end{align*}
```

$$
\begin{align*}
1 & = 2\\
& = 345\\
& = 6
\end{align*}
$$



##### 公式等号对齐且居于左侧

(vscode编译器不支持)

```latex
\begin{flalign}
1 & = 2\\
& = 345\\
& = 6&
\end{flalign}
```

$$
\begin{flalign}
1 & = 2\\
& = 345\\
& = 6&
\end{flalign}
$$



##### 多重对齐

```latex
\begin{flalign}
&\text{We have}\\
&\begin{split}
1 & = 2\\
& = 345\\
& = 6
\end{split}\\
&\text{Therefore}&
\end{flalign}
```

$$
\begin{flalign}
&\text{We have}\\
&\begin{split}
1 & = 2\\
& = 345\\
& = 6
\end{split}\\
&\text{Therefore}&
\end{flalign}
$$



##### 文字

```latex
$\textsf{墨可}$墨可
```

$\textsf{墨可}$墨可



##### 注释

```latex
%%e^{i\pi}+1 = 0
e^{i\pi}+1 = 0
```

$$
%%e^{i\pi}+1 = 0
e^{i\pi}+1 = 0
$$



## Markdown_Latex

##### 左右括号

```latex
$\displaystyle\vert \frac{e^x+e^{-x}}2 \vert$
$\displaystyle\left\vert \frac{e^x+e^{-x}}2 \right\vert$
```

$\displaystyle\vert \frac{e^x+e^{-x}}2 \vert$	$\displaystyle\left\vert \frac{e^x+e^{-x}}2 \right\vert$



##### Big Operator下标

```latex
$\lim\limits_{x\rightarrow0}$
$\sum\limits_{i=1}^{n}$
$\frac12$
%% beter format :
$\displaystyle\sum_{i=1}^{n}$
$\displaystyle\int_a^b$
$\dfrac12$
```

$\lim\limits_{x\rightarrow0}$		$\sum\limits_{i=1}^{n}$		$\displaystyle\sum_{i=1}^{n}$		$\displaystyle\int_a^b$		$\dfrac12$



##### 数域

```latex
$\N$	$\Q$	$\R$	$\C$
$\mathcal{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
$\mathscr{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
```

$\N$	$\Q$	$\R$	$\C$ (并不需要用`\mathbb{N}`)

$\mathcal{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$

$\mathscr{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$



##### 矩阵

```latex
$$\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}$$
```

$$\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}$$

- 横省略号：`\cdots`
- 竖省略号：`\vdots`
- 斜省略号：`\ddots`
- `pmatrix`：小括号边框
- `bmatrix`：中括号边框
- `vmatrix`：单竖线边框



##### 方程组

```latex
$$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}$$
```

$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}$



##### 方框

```latex
$$\boxed{1}$$
```

$$\boxed{1}$$



##### 等号

```latex
$\overset{\text{容斥原理}}=$
$\xlongequal{\text{容斥原理}}$
```

$$\overset{\textbf{容斥原理}}=$$		$\xlongequal{\textbf{容斥原理}}$







## Markdown_Graph

##### 文本单箭头

```latex
$A \xrightarrow[\text{below}]{\text{above}} B$		$A \xRightarrow{\text{above}} B$		
$\overset{\sim}{\longmapsto}$		一致收敛 : $\rightrightarrows$
```

$A \xrightarrow[\text{below}]{\text{above}} B$			$A \xRightarrow{\text{above}} B$			$\overset{\sim}{\longmapsto}$			一致收敛 : $\rightrightarrows$



##### 斜向箭头

```Latex
$\nearrow$	$\searrow$	$\swarrow$	$\nwarrow$
```

$\nearrow$	$\searrow$	$\swarrow$	$\nwarrow$



##### [交换图表](Mamscd.pdf)

##### Baisc Rules

```latex
 @<<< leftarrow		 @>>> rightarrow
 @AAA uparrow 		 @= horizontalequals
 @VVV downarrow  	 @| verticalequals
 @. emptyarrow.
```

##### Examples

```latex
\begin{CD}
A @>a>> B\\
@VVbV @VVcV\\
C @>d>> D
\end{CD}
```

$$
\begin{CD}
A @>a>> B\\
@VVbV @VVcV\\
C @>d>> D
\end{CD}
$$

```latex
\begin{CD}
A@<<<B@>>>C\\
@. @| @AAA\\
@. D@= E
\end{CD}
```

$$
\begin{CD}
 A@<<<B@>>>C\\
 @. @| @AAA\\
 @. D@= E
 \end{CD}
$$





