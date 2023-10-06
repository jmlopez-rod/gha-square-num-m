from m.github.actions import InArg, KebabModel


class GithubInputs(KebabModel):
    """Inputs from the Github Action."""

    num: str = InArg(help='the number to square')
