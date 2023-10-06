import pytest
from m.github.actions import Action
from m.testing import ActionStepTestCase as TCase
from m.testing import run_action_test_case
from pytest_mock import MockerFixture

from pkg.actions import actions


@pytest.mark.parametrize(
    'tcase',
    [
        TCase(
            name='square_number',
            py_file=f'src/pkg/main.py',
            inputs={'INPUT_NUM': '4'},
            expected_stdout='Squaring the number\n',
            outputs=['squared-num=16'],
        ),
    ],
    ids=lambda tcase: tcase.name,
)
def test_m_gh_actions_api(tcase: TCase, mocker: MockerFixture) -> None:
    run_action_test_case(mocker, tcase)


def test_actions_instance() -> None:
    assert isinstance(actions, Action)
    assert actions.name == 'Square Number'
