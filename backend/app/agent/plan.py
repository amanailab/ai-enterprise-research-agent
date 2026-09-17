from pydantic import BaseModel


class ResearchPlan(BaseModel):

    company: bool

    news: bool

    search: bool