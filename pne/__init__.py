import warnings

from promptulate import beta
from promptulate.agents.assistant_agent.agent import AssistantAgent
from promptulate.agents.base import BaseAgent
from promptulate.agents.planner.planner import Planner
from promptulate.agents.tool_agent.agent import ToolAgent
from promptulate.agents.web_agent.agent import WebAgent
from promptulate.chat import AIChat, chat
from promptulate.llms.base import BaseLLM
from promptulate.llms.factory import LLMFactory
from promptulate.llms.openai.openai import ChatOpenAI
from promptulate.output_formatter import OutputFormatter
from promptulate.schema import (
    AssistantMessage,
    BaseMessage,
    MessageSet,
    SystemMessage,
    UserMessage,
)
from promptulate.tools.base import BaseTool, Tool, ToolTypes, define_tool
from promptulate.utils.logger import enable_log
from promptulate.utils.string_template import StringTemplate

_util_fields = [
    "enable_log",
    "OutputFormatter",
    "StringTemplate",
]

_schema_fields = [
    "AssistantMessage",
    "SystemMessage",
    "UserMessage",
    "BaseMessage",
    "MessageSet",
]

_llm_fields = ["chat", "AIChat", "BaseLLM", "ChatOpenAI", "LLMFactory"]

_tool_fields = [
    "Tool",
    "define_tool",
    "BaseTool",
    "ToolTypes",
]

_agent_fields = [
    "BaseAgent",
    "WebAgent",
    "ToolAgent",
    "AssistantAgent",
    "Planner",
]


__all__ = [
    *_util_fields,
    *_schema_fields,
    *_llm_fields,
    *_tool_fields,
    *_agent_fields,
    "beta",
]

warnings.filterwarnings("always", category=DeprecationWarning)
