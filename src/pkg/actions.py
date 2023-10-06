from m.github.actions import Action

from pkg.inputs import GithubInputs
from pkg.main import main_step

actions = Action(
    name='Square Number',
    description='Square the given number',
    file_path='action.yaml',
    inputs=GithubInputs,
    steps=[
        main_step(step_id='square', args=GithubInputs(num='inputs.num')),
    ]
)