from dotenv import load_dotenv
from pathlib import Path
import gentopia
print(gentopia.__path__)
from gentopia import chat
from gentopia.assembler.agent_assembler import AgentAssembler

load_dotenv();

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
file_url = BASE_DIR.as_posix() +'/example/config/react_template.yaml';
print('file_url:',file_url)
agent = AgentAssembler(file=file_url).get_agent()
chat(agent=agent)
# result = agent.run("hi")
# print("result:",result)