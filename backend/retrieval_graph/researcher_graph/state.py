"""State management for the researcher graph.

This module defines the state structures used in the researcher graph.
"""

from dataclasses import dataclass, field
from typing import Annotated

from langchain_core.documents import Document

from backend.utils import reduce_docs


@dataclass(kw_only=True)
class QueryState:
    """Private state for the retrieve_documents node in the researcher graph."""

    query: str


@dataclass(kw_only=True)
class ResearcherState:
    """State of the researcher graph / agent."""

    question: str
    """A step in the research plan generated by the retriever agent."""
    queries: list[str] = field(default_factory=list)
    """A list of search queries based on the question that the researcher generates."""
    documents: Annotated[list[Document], reduce_docs] = field(default_factory=list)
    """Populated by the retriever. This is a list of documents that the agent can reference."""
