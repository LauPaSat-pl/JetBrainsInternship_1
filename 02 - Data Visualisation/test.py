import unittest
import main
import solution
from matplotlib.testing.decorators import image_comparison
from pandas.testing import assert_frame_equal


@image_comparison(baseline_images=['final_plot_example'], extensions=['png'])
def test_plot():
    df = main.load_data('Data source\processed_data.csv')
    main.plot_data(df)


if __name__ == '__main__':
    assert_frame_equal(main.load_data('Data source\processed_data.csv'),
                       solution.load_data('Data source\processed_data.csv'))
    test_plot()
