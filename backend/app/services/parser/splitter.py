import re
from typing import List, Dict, Any
import logging

# 配置简单的日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentSplitter:
    """
    核心解析器：负责将 Markdown 文本切分为语义块 (Theorems, Lemmas, Proofs)。
    """
    def __init__(self):
        # 1. 识别定理/引理的正则
        # 兼容: "## Theorem 3.1", "**Theorem 3.1**", "Theorem 3.1."
        self.block_pattern = re.compile(
            r"^(?:#{1,6}\s*|\*\*|__)?(Theorem|Lemma|Proposition|Corollary|Definition)\s+([\d\.]+)",
            re.IGNORECASE | re.MULTILINE
        )
        
        # 2. 识别证明开始的正则
        # 兼容: "### Proof", "**Proof**", "Proof."
        self.proof_pattern = re.compile(
            r"^(?:#{1,6}\s*|\*\*|__|_)Proof",
            re.IGNORECASE | re.MULTILINE
        )

    def parse(self, text: str) -> List[Dict[str, Any]]:
        lines = text.split('\n')
        blocks = []
        
        current_block = None
        capturing_proof = False  # 状态标志：当前是否正在抓取 Proof 内容

        for line in lines:
            stripped_line = line.strip()
            if not stripped_line: 
                continue # 跳过空行

            # --- A. 检测是否是新的定理/引理开始 ---
            block_match = self.block_pattern.search(stripped_line)
            if block_match:
                # 如果之前有一个正在处理的块，先保存它
                if current_block:
                    self._finalize_block(current_block)
                    blocks.append(current_block)

                # 初始化新块
                block_type = block_match.group(1) # e.g. "Theorem"
                block_id = block_match.group(2)   # e.g. "3.1"
                
                current_block = {
                    "id": f"{block_type.lower()}_{block_id}",
                    "type": block_type.lower(),
                    "title": stripped_line.replace("#", "").replace("*", "").strip(),
                    "statement": "",
                    "proof": "",  # 这里是关键：一定要把 proof 分离出来
                }
                capturing_proof = False # 重置状态，因为新定理刚开始，肯定还没到证明
                continue

            # --- B. 检测是否是 Proof 开始 ---
            # 只有当前已经在某个定理块内，遇到 Proof 才算数
            if current_block and self.proof_pattern.search(stripped_line):
                capturing_proof = True
                continue # 跳过 "Proof" 这一行本身

            # --- C. 内容填充 ---
            if current_block:
                if capturing_proof:
                    current_block['proof'] += line + "\n"
                else:
                    current_block['statement'] += line + "\n"

        # 循环结束，别忘了保存最后一个块
        if current_block:
            self._finalize_block(current_block)
            blocks.append(current_block)

        logger.info(f"Successfully parsed {len(blocks)} blocks.")
        return blocks

    def _finalize_block(self, block):
        """清理数据，比如去除首尾空格"""
        block['statement'] = block['statement'].strip()
        block['proof'] = block['proof'].strip()
