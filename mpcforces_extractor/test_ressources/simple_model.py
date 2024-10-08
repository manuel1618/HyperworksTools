from typing import List


def get_simple_model_fem() -> List:
    """
    This method returns a simple model with MPC and CQUAD4 elements
    """

    lines = [
        "$$\n",
        "GRID           4        43.8828813.6511210.0    \n",
        "GRID           5        43.8828813.6511226.5871 \n",
        "GRID           6        51.5091413.6511217.62625\n",
        "GRID        6091        243.882913.6511210.0    \n",
        "GRID        6092        243.883413.65107-10.0   \n",
        "GRID        6093        0.0     -10.0   -10.0   \n",
        "GRID        6094        0.0     -10.0   0.0     \n",
        "GRID        6095        0.0     -10.0   10.0    \n",
        "GRID        6096        0.0     0.0     10.0    \n",
        "GRID        6097        0.0     10.0    10.0    \n",
        "GRID        6098        0.0     10.0    0.0     \n",
        "GRID        6099        0.0     10.0    -10.0   \n",
        "GRID        6100        0.0     0.0     -10.0   \n",
        "GRID        6101        0.0     0.0     0.0     \n",
        "GRID        6102        8.871956-10.0   -10.0   \n",
        "GRID        6103        8.871956-10.0   0.0     \n",
        "GRID        6104        8.871956-10.0   10.0    \n",
        "GRID        6105        8.8719560.0     10.0    \n",
        "GRID        6106        8.87195610.0    10.0    \n",
        "GRID        6107        8.87195610.0    0.0     \n",
        "GRID        6108        8.87195610.0    -10.0   \n",
        "GRID        6109        8.8719560.0     -10.0   \n",
        "GRID        6110        8.8719560.0     0.0     \n",
        "GRID        6111        4.435978-5.0    -6.66667\n",
        "$$\n",
        "$$ RBE2 Elements - Multiple dependent nodes\n",
        "$$\n",
        "$HMCOMP ID                     1       1       4\n",
        "RBE2           9    6111  123456    6093    6094    6100    6102    6109\n",
        "+           6110     0.0\n",
        "$\n",
        "$$\n",
        "$$  CQUAD4 Elements\n",
        "$$\n",
        "$HMCOMP ID                     1       1       4\n",
        "CQUAD4         1       1    6097    6098    6101    6096\n",
        "CQUAD4         2       1    6096    6101    6094    6095\n",
        "CQUAD4         3       1    6098    6099    6100    6101\n",
        "CQUAD4         4       1    6101    6100    6093    6094\n",
        "CQUAD4         5       1    6106    6107    6110    6105\n",
        "CQUAD4         6       1    6105    6110    6103    6104\n",
        "CQUAD4         7       1    6107    6108    6109    6110\n",
        "CQUAD4         8       1    6110    6109    6102    6103\n",
        "$\n",
        "$$\n",
        "$$  SPC Data\n",
        "$$\n",
        "SPC            1    6106  123456     0.0\n",
        "$$\n",
        "$$  FORCE Data\n",
        "$$\n",
        "FORCE          2    6097       01.0     0.0     0.0     1\n",
    ]
    return lines


def get_simple_model_mpc() -> List:
    """
    This method returns a simple model with MPC forces which is the output of Optistruct
    for the simple model fem above
    """
    lines = [
        "OPTISTRUCT RESULT 2023.1\n",
        " \n",
        "$ITERATION            0\n",
        " \n",
        "$SUBCASE              1  \n",
        "$TIME       0.10000000E+01\n",
        " \n",
        "$MPC FORCE [REAL]\n",
        "--------+-----------------------------------------------------------------------------\n",
        "  GRID #   X-FORCE      Y-FORCE      Z-FORCE      X-MOMENT     Y-MOMENT     Z-MOMENT\n",
        "--------+-----------------------------------------------------------------------------\n",
        "    6093              -2.65537E-02 -2.44183E-01  4.36841E-02\n",
        "    6094               7.00173E-01  4.53330E-01 -6.34804E-01\n",
        "    6100              -6.73619E-01 -1.20915E+00 -3.15689E-01\n",
        "    6102 -1.93745E-01  7.63245E-02 -2.52271E-01 -1.96810E-02 -8.38505E-01  1.92525E-01\n",
        "    6109 -1.09135E-01  5.39527E-01  3.23144E-01  1.70904E-01 -3.49756E-01  1.11075E+00\n",
        "    6110  3.02880E-01 -6.15851E-01  9.29127E-01  1.16756E+00  7.03142E+00  6.34173E-01\n",
        "    6111  0.00000E-00  0.00000E-00  0.00000E-00  0.00000E-00  0.00000E-00  0.00000E-00\n",
        "--------+-----------------------------------------------------------------------------\n",
    ]
    return lines
