from interpret_manager import AgentManager

if __name__ == '__main__':
    agent_manager = AgentManager()
    files_to_analyze = ['interpret_manager.py', 'interpret_agentgpt.py']  # Replace with actual file names
    agent_manager.analyze_files(files_to_analyze)
    agent_manager.update_programming()