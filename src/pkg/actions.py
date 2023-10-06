from m.github.actions import Action

from .inputs import GithubInputs
from .main import main_step

actions = Action(
    name='Square Number',
    description='Square the given number',
    file_path='action.yaml',
    inputs=GithubInputs,
    steps=[
        main_step(step_id='square', args=GithubInputs(num='inputs.num')),
    ]
)