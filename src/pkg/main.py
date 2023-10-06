from m.core import Good, Res
from m.github.actions import KebabModel, OutArg, RunStep, run_action

from .inputs import GithubInputs


class Outputs(KebabModel):
    """Outputs from the Github Action."""

    squared_num: str = OutArg(help='the squared number', export=True)


def main(inputs: GithubInputs) -> Res[Outputs]:
    """Square the given number.
    
    Args:
        inputs: The inputs to the step.

    Returns:
        The outputs of the step or an issue.
    """
    print('Squaring the number')
    num = int(inputs.num)
    result = num * num
    return Good(Outputs(squared_num=str(result)))


def main_step(
    step_id: str,
    args: GithubInputs
) -> RunStep[GithubInputs, Outputs]:
    """Create a step to square the given number.
    
    Args:
        step_id: The id of the step.
        inputs: The inputs to the step.

    Returns:
        A step to use in the action.
    """
    return RunStep[GithubInputs, Outputs](id=step_id, run=main, args=args)

if __name__ == '__main__':
    run_action(main)
