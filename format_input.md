1. 对非负函数 $f$ ，如果 $\displaystyle\int f=0$ ，那么必定有 $f=0, a . e$.

   记 $A_\varepsilon := \{x \in E \big| f(x) > \varepsilon \}$, 于是对于 $\forall \varepsilon > 0, m(A_\varepsilon ) = 0$

   这是由于如果 $m(A_\varepsilon ) > 0 $, 那么考虑 $g(x) := \begin{cases}
   \varepsilon, x \in A_\varepsilon\\
   0, x \notin A_\varepsilon
   \end{cases}$ , 显然有 $g \le f$, 

   但是 $\displaystyle 0 < m(A_\varepsilon) \cdot \varepsilon = \int g \le \int f = 0 $ 矛盾! 

   注意到 $\{x \in E \big| f(x) > 0\} = \bigcup\limits_{n = 1}^\infty m(A_{\frac{1}{n}})$ 的测度为 $0$, 于是 $f = 0, a.e.$ 即证.



2. 对于可积函数 $f$ ，如果对于任意开集 $O$ 都有 $\int_O f=0$ ，那么 $f=0$ ，a．e．．

3. Chebychev 不等式如果 $f$ 可积，那么对任意 $\alpha>0$ 有 $\displaystyle m(\{x:|f(x)|>\alpha\}) \leq \frac{1}{\alpha} \int|f| .$

    记 $E:= \{x: |f(x)|>\alpha\}$, 考虑 $g(x) := \begin{cases}
   \alpha, x \in E\\
   0, x \notin E
   \end{cases}$, 显然 $|g| \le $


首先 `σA` 等 σ type 有如下好处 :  他们结构general适用于多种结构 ,如果

但某些程度上, 结构过于自由, 这意味条件非常弱, 难以支撑结论(比如如果不加任何限制条件时, `σ = {\bot}`完全合法). 于是我们需要对 `σ type` 加以限制, 于是有了这个class

其中 `coe_eq` 保证 每个f 的range在sB中.

3. Chebychev 不等式如果 $f$ 可积, 那么对任意 $\alpha>0$ 有 $\displaystyle m(\{x:|f(x)|>\alpha\}) \leq \frac{1}{\alpha} \int|f| .$