import dotenv
from pathlib import Path
from gentopia import chat
from gentopia.assembler.agent_assembler import AgentAssembler

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.load_dotenv(".env")  # load environmental keys
file_url = BASE_DIR.as_posix() +'/yml_file_agent/react_template.yaml';
print('file_url:',file_url)
agent = AgentAssembler(file=file_url).get_agent()

chat(agent) 