from dataclasses import dataclass
from typing import Callable, Dict, Any


@dataclass
class AgentResult:
    answer: str
    steps: list


class SimpleAgent:
    def __init__(self, tools: Dict[str, Callable[[str], Any]]):
        self.tools = tools

    def select_tool(self, tool_name: str):
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        return self.tools[tool_name]

    def execute(self, tool_name: str, query: str):
        tool = self.select_tool(tool_name)
        return tool(query)

    def synthesize(self, query: str, observations: list) -> AgentResult:
        return AgentResult(
            answer=f"Synthesized response for: {query}",
            steps=observations,
        )


def example_agent():
    tools = {
        "search": lambda query: f"Search results for: {query}",
        "database": lambda query: f"Database results for: {query}",
    }

    agent = SimpleAgent(tools)

    observations = []

    observations.append(
        agent.execute("search", "current technical information")
    )

    observations.append(
        agent.execute("database", "related internal information")
    )

    return agent.synthesize(
        "Combine external and internal information",
        observations,
    )


if __name__ == "__main__":
    result = example_agent()

    print(result.answer)

    for step in result.steps:
        print(step)
