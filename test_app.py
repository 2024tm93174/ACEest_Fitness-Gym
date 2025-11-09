# test_app.py

import pytest
from unittest import mock
import ACEest_Fitness  # your main app file

@pytest.fixture
def tk_app():
    root = mock.MagicMock()
    app = ACEest_Fitness.FitnessTrackerApp(root)
    return app


def test_add_workout_success(tk_app):
    tk_app.workout_entry.get = mock.MagicMock(return_value="Pushups")
    tk_app.duration_entry.get = mock.MagicMock(return_value="30")

    with mock.patch("ACEest_Fitness.messagebox.showinfo") as mock_info:
        tk_app.add_workout()
        mock_info.assert_called_once_with("Success", "'Pushups' added successfully!")

    assert len(tk_app.workouts) == 1
    assert tk_app.workouts[0] == {"workout": "Pushups", "duration": 30}
