from pandas.testing import assert_frame_equal

import main
import solution


if __name__ == '__main__':
    student_df = main.load_data('Data source\dataset.csv')
    reference_df = solution.load_data('Data source\dataset.csv')
    assert_frame_equal(student_df, reference_df)
    student_df = main.remove_columns(student_df)
    reference_df = solution.remove_columns(reference_df)
    assert_frame_equal(student_df, reference_df)
    student_df = main.filter_data(student_df)
    reference_df = solution.filter_data(reference_df)
    assert_frame_equal(student_df, reference_df)
    student_df = main.group_data(student_df)
    reference_df = solution.group_data(reference_df)
    assert_frame_equal(student_df, reference_df)
