import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import Tool

# 配置 LLM（建议使用 Claude 3.5 或 GPT-4o 以获得最佳代码解析效果）
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

# 封装成 CrewAI 工具
ast_tool = Tool(
    name="Code-AST-Parser",
    func=extract_function_metadata,
    description="Extracts precise function structures and metadata from legacy source code using Tree-sitter."
)

# 1. 代码考古学家：识别旧系统的业务逻辑
archaeologist = Agent(
    role='Legacy Code Archaeologist',
    goal='Precisely analyze legacy code structures using AST tools.',
    backstory="You are a meticulous engineer who uses AST parsing to avoid hallucinations.",
    tools=[ast_tool], # 给 Agent 配备专业工具
    verbose=True
)

# 2. API 架构师：生成 OpenAPI 和 FastAPI 实现
architect = Agent(
    role='Modern API Architect',
    goal='Translate legacy logic into modern RESTful API specifications and Python FastAPI implementations.',
    backstory="""You are a master of OpenAPI 3.1 and FastAPI. You take logic descriptions 
    and turn them into high-performance, well-documented, and secure code.""",
    verbose=True,
    allow_delegation=False
)