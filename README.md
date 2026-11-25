# data-qd-219 · 基因变异规范化与等价归组

核对变异参考等位基因，删除冗余上下文并在重复序列中左对齐插入缺失，最终按规范位置/ref/alt 聚合等价来源。

Python 3.11+；运行只用标准库，构建固定 setuptools 80.9.0 与 wheel 0.45.1。

    uv venv --python 3.12 .venv
    uv pip install --python .venv/bin/python --offline -r requirements-build.lock
    uv pip install --python .venv/bin/python --offline --no-build-isolation -e .
    .venv/bin/python -m unittest discover -s tests -v
    .venv/bin/python examples/run_sample.py

样例完全合成，不含患者数据。本仓不做临床解释、基因注释、分型或 VCF 全格式解析。
