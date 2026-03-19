import os
import sys

from google.adk.agents import LlmAgent
from utils.file_loader import load_instructions_file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..")))


requirements_writer_agent = LlmAgent(
    name="requirements_writer_agent",
    model="gemini-flash-latest",
    instruction=load_instructions_file("agents/requirements_writer/instructions.txt"),
    description=load_instructions_file("agents/requirements_writer/description.txt"),
    output_key="Requirements_Writer_Output"
)