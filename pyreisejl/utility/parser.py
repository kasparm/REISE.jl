import argparse

from pyreisejl.utility.launchers import get_available_solvers


def parse_call_args():
    parser = argparse.ArgumentParser(description="Run REISE.jl simulation.")

    # Arguments needed to run REISE.jl
    parser.add_argument(
        "-s",
        "--start-date",
        help="The start date for the simulation in format 'YYYY-MM-DD', 'YYYY-MM-DD HH', "
        "'YYYY-MM-DD HH:MM', or 'YYYY-MM-DD HH:MM:SS'.",
    )
    parser.add_argument(
        "-e",
        "--end-date",
        help="The end date for the simulation in format 'YYYY-MM-DD', 'YYYY-MM-DD HH', "
        "'YYYY-MM-DD HH:MM', or 'YYYY-MM-DD HH:MM:SS'. If only the date is specified "
        "(without any hours), the entire end-date will be included in the simulation.",
    )
    parser.add_argument(
        "-int", "--interval", help="The length of each interval in hours.", type=int
    )
    parser.add_argument(
        "-i",
        "--input-dir",
        help="The directory containing the input data files. "
        "Required files are 'grid.pkl', 'demand.csv', "
        "'hydro.csv', 'solar.csv', and 'wind.csv'.",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        help="The number of threads to run the simulation with. "
        "This is optional and defaults to Auto.",
    )
    parser.add_argument(
        "-d",
        "--extract-data",
        action="store_true",
        help="If this flag is used, the data generated by the simulation after the engine "
        "has finished running will be automatically extracted into .pkl files, "
        "and the result.mat files will be deleted. "
        "The extraction process can be memory intensive. "
        "This is optional and defaults to False if the flag is omitted.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        help="The directory to store the extracted data. This is optional and defaults "
        "to a folder in the input directory. This flag is only used if the extract-data flag is set.",
    )
    parser.add_argument(
        "-k",
        "--keep-matlab",
        action="store_true",
        help="The result.mat files found in the execute directory will be kept "
        "instead of deleted after extraction. "
        "This flag is only used if the extract-data flag is set.",
    )

    solvers = ",".join(get_available_solvers())
    parser.add_argument(
        "--solver",
        help="Specify the solver to run the optimization. Will default to gurobi. "
        f"Current solvers available are {solvers}.",
    )
    parser.add_argument(
        "-j",
        "--julia-env",
        help="The path to the julia environment within which to run REISE.jl. "
        "This is optional and defaults to the default julia environment.",
    )

    # For backwards compatability with PowerSimData
    parser.add_argument(
        "scenario_id",
        nargs="?",
        default=None,
        help="Scenario ID only if using PowerSimData. ",
    )
    return parser.parse_args()


def parse_extract_args():
    parser = argparse.ArgumentParser(
        description="Extract data from the results of the REISE.jl simulation."
    )

    # Arguments needed to run REISE.jl
    parser.add_argument(
        "-s",
        "--start-date",
        help="The start date as provided to run the simulation. Supported formats are"
        " 'YYYY-MM-DD', 'YYYY-MM-DD HH', 'YYYY-MM-DD HH:MM', or 'YYYY-MM-DD HH:MM:SS'.",
    )
    parser.add_argument(
        "-e",
        "--end-date",
        help="The end date as provided to run the simulation. Supported formats are"
        " 'YYYY-MM-DD', 'YYYY-MM-DD HH', 'YYYY-MM-DD HH:MM', or 'YYYY-MM-DD HH:MM:SS'.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        nargs="?",
        default=None,
        help="The directory to store the results. This is optional and defaults "
        "to a folder in the input directory.",
    )
    parser.add_argument(
        "-f",
        "--frequency",
        nargs="?",
        default="H",
        help="The frequency of data points in the original profile csvs as a "
        "Pandas frequency string. "
        "This is optional and defaults to an hour.",
    )
    parser.add_argument(
        "-k",
        "--keep-matlab",
        action="store_true",
        help="If this flag is used, the result.mat files found in the "
        "execute directory will be kept instead of deleted.",
    )

    # For backwards compatability with PowerSimData
    parser.add_argument(
        "scenario_id",
        nargs="?",
        default=None,
        help="Scenario ID only if using PowerSimData.",
    )
    return parser.parse_args()
