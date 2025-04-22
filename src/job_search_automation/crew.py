from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from job_search_automation.tools.custom_tool import read_from_markdown, save_to_markdown

@CrewBase
class JobSearchAutomation():
    """JobSearchAutomation crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def job_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['job_search_agent'],
            tools=[save_to_markdown],
            verbose=True
        )

    @agent
    def resume_tailor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_tailor_agent'],
            tools=[read_from_markdown, save_to_markdown],
            verbose=True
        )

    @agent
    def cover_letter_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['cover_letter_writer_agent'],
            tools=[read_from_markdown, save_to_markdown],
            verbose=True
        )

    @agent
    def interview_prep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_prep_agent'],
            tools=[read_from_markdown, save_to_markdown],
            verbose=True
        )

    @task
    def job_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_search_task']
        )

    @task
    def resume_tailor_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_tailor_task'],
            output_file='report.md'
        )

    @task
    def cover_letter_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['cover_letter_writer_task'],
        )

    @task
    def interview_prep_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_prep_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the JobSearchAutomation crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
