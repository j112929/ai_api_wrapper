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