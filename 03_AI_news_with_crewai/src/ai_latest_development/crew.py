from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class AiLatestDevelopment():
    """AiLatestDevelopment crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    # Initialize GPT-3.5 Turbo
    gpt_llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.7  # Better to set this via environment variable
    )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            llm=self.gpt_llm
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
            llm=self.gpt_llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiLatestDevelopment crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )