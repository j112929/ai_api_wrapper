import os
from crewai import Agent, Task, Crew, Process
from crewai.tools import Tool
# from crewai.agent import CacheHandler, RPMController
# from crewai.callbacks import ToolsHandler
# from crewai.runnables.config import RunnableConfig
# from typing import List, Any, Optional
# from tree_sitter import Language, Parser
from ast_extractor import extract_function_metadata

# 配置 LLM（建议使用 Claude 3.5 或 GPT-4o, Gemini 3 pro 以获得最佳代码解析效果）
# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE" # Security: Read from env instead
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY is not set in the environment.")

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

# 假设我们要解析的旧代码片段
legacy_code_snippet = """
double calc_v1(int a, char* b, float c) {
    // 2005年写的陈旧逻辑
    if (strcmp(b, "discount") == 0) return a * c * 0.8;
    return a * c;
}
"""

# 任务 1: 逻辑提取
task_analysis = Task(
    description=f"Analyze the following legacy code and list all inputs, outputs, and the core logic: {legacy_code_snippet}",
    expected_output="A structured report covering function names, parameters (types & meaning), and business rules.",
    agent=archaeologist
)

# 任务 2: 代码生成
task_generation = Task(
    description="Based on the archaeologist's report, generate a full Python FastAPI script and a corresponding openapi.yaml file.",
    expected_output="A complete FastAPI Python script that wraps the logic, including Pydantic models and API documentation.",
    agent=architect
)

# 启动 Crew
legacy_modernizer_crew = Crew(
    agents=[archaeologist, architect],
    tasks=[task_analysis, task_generation],
    process=Process.sequential # 顺序执行：先分析，后生成
)

result = legacy_modernizer_crew.kickoff()
print(result)