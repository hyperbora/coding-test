"""
https://leetcode.com/problems/implement-trie-prefix-tree/
트라이(Trie)는 검색 트리의 일종으로 일반적으로 키가 문자열인,
동적 배열 또는 연관 배열을 저장하는 데 사용되는 정렬된 트리 자료구조이다.
"""
import collections


# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
