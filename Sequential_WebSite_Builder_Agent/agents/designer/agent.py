import os
import sys

from google.adk.agents import LlmAgent
from utils.file_loader import load_instructions_file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..")))


designer_agent = LlmAgent(
    name="designer_agent",
    model="gemini-flash-latest",
    instruction=load_instructions_file("agents/designer/instructions.txt"),
    description=load_instructions_file("agents/designer/description.txt"),
    output_key="Designer_Output"
)