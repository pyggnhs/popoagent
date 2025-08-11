import os
import json
import subprocess
from pathlib import Path
from sqlite3 import connect
from typing import List , Optional
from dataclasses import dataclass
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from typing import Any



@dataclass
class RepoInfo:
    """项目仓库信息结构体"""
    currentDirectory: str
    rootPath: str
    repoUrl: str
    repoPath: str
    Branch: str
    status: str
    recentCommit: str
    directoryStructure:str
    hasReadme: bool
    hasMakefile: bool
    totalFiles: int
    totalDirectories: int

def get_project_structure() -> Optional[RepoInfo]:
    """获取项目仓库信息并返回RepoInfo实例"""
    try:
        # 基础路径信息
        current_dir = os.getcwd()
        root_path = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()


        #远程仓库URL
        remote_info = subprocess.check_output(
            ['git', 'remote',  '-v'],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
        repo_url = "git@github.com:pyggnhs/popoagent.git"
        for line in remote_info.split('\n'):
            if line.startswith('origin') and 'fetch' in line:
                repo_url = line.split()[1]
                break

        #分支信息
        branch_output = subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
        current_branch = branch_output

        #状态信息
        status_info = subprocess.check_output(
            ['git', 'status'],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()

        #最近commit信息
        commit_output = subprocess.check_output(
            ['git', 'log','-1','--pretty=format:%H%n%an%n%ae%n%ad%n%s'],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
        recent_commit = commit_output.split('\n')

        #目录结构及统计（同时计算文件和目录数量）
        ignore_dirs = {'.git','__pycache__','.idea','.vscode','node_modules'}
        total_files = 0
        total_dirs = 0

        def build_markdown_tree(path: Path,prefix: str = "", is_last: bool = True) -> str:
            """递归构建Markdown树形结构字符串"""
            nonlocal total_files, total_dirs

            #忽略制定目录
            if path.name in ignore_dirs:
                return ""

            #统计目录
            if path.is_dir():
                total_dirs += 1
                item_str = f"{path.name}/"
            else:
                total_dirs += 1
                item_str = path.name

            #确定当前行的前缀符号
            if prefix == "":  #根节点
                line = f"-{item_str}\n"
            else:
                connector = "└── " if is_last else "├── "
                line = f"{prefix}{connector}{item_str}\n"













