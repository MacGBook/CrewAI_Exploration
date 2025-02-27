from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from crewai_exploration_4.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CrewaiExploration4():
	"""CrewaiExploration4 crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def emergency_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['emergency_manager'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def civilian_mixed_opinion(self) -> Agent:
		return Agent(
			config=self.agents_config['civilian_mixed_opinion'],
			verbose=True
		)
	
	@agent
	def civilian_nay_opinion(self) -> Agent:
		return Agent(
			config=self.agents_config['civilian_nay_opinion'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task_mixed(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task_mixed'],
			output_file='report.md'
		)
	
	@task
	def reporting_task_nay(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task_nay'],
			output_file='report2.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiExploration4 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
