import json
from app.services.parser.splitter import DocumentSplitter

# 1. 模拟一段从 PDF 转换来的 Markdown (包含 LaTeX)
dummy_markdown = r"""
# Introduction
This paper discusses advanced optimization.

## Theorem 3.1
Let $f$ be an L-smooth function. Then for any step size $\eta < 1/L$:
$$ f(x_{k+1}) \le f(x_k) - \frac{\eta}{2} ||\nabla f(x_k)||^2 $$

### Proof
Using the Taylor expansion with Lagrange remainder:
$$ f(y) \le f(x) + \nabla f(x)^T(y-x) + \frac{L}{2}||y-x||^2 $$
Setting $y = x - \eta \nabla f(x)$, we get the result immediately.
Q.E.D.

## Lemma 3.2 (Boundedness)
The sequence $\{x_k\}$ remains in a compact set $C$.

**Proof**
This follows from the coercivity of function $f$.
"""

# 2. 运行解析器
if __name__ == "__main__":
    splitter = DocumentSplitter()
    result = splitter.parse(dummy_markdown)
    
    # 3. 打印结果
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 4. 简单的自动化断言
    assert len(result) == 2, "应该识别出 2 个块"
    assert result[0]["id"] == "theorem_3.1"
    assert "Taylor expansion" in result[0]["proof"], "Proof 内容应该被正确提取"
    assert "Taylor expansion" not in result[0]["statement"], "Proof 不应该混入 Statement"
    print("\n✅ 测试通过！核心逻辑工作正常。")
