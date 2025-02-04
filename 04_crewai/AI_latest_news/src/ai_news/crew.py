from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class AiNews():
	"""AiNews crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def retrieve_news(self) -> Agent:                    ##this agent will do google search and retrieve news websites
		return Agent(
			config=self.agents_config['retrieve_news'],
			tools=[SerperDevTool()],                      ## the Search Engine Results Page Development Tool
			verbose=True
		)

	@agent
	def website_scraper(self) -> Agent:                  ##this will extract data from the websites
		return Agent(
			config=self.agents_config['website_scraper'],
			tools=[ScrapeWebsiteTool()],
			verbose=True
		)
	
	@agent
	def ai_news_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_news_writer'],         ##will write a concise summary of the collected data from each website
			tools=[],
			verbose=True
		)
	
	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],        ##writes collected content in a file the content will contain a heading and a summary form each of the 10 website that it will scrape
			tools=[FileWriterTool()],
			verbose=True
		)

	@task
	def retrieve_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_news_task'],
		)

	@task
	def website_scrape_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_scrape_task'],
		)
	
	@task
	def ai_news_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_news_write_task'],
		)
	
	@task
	def file_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_write_task'],
		)

	@crew                            ##registers def(crew) funtion as a special crew function 
	def crew(self) -> Crew:           
		"""Creates the AiNews crew"""
		return Crew(                 ###these are argument assignment not a function call
			agents=self.agents, # Automatically looks for every function with @agent decorator on it and will know that,that function is going to be an agent and therefore it will return the function as an agent 
			tasks=self.tasks, # Automatically looks for every function with @task decorator
			process=Process.sequential,    ##runs tasks one after the another
			verbose=True,              ##to show execution details 
		)