"""Main CLI launcher
"""

import argparse
import time
from .commands.traj2pdb_cli import traj2pdb_cli
from .commands.pdb2csv_cli import pdb2csv_cli  
from .commands.trajmap_cli import trajmap_cli
from .commands.csv2shift_cli import shift_cli
from .commands.shift2graph_cli import shift2graph_cli
from .commands.hotspot_cli import detect_shift_cli
from .commands.hotspot_cli import create_submatrices_cli
from .commands.hotspot_cli import slice_shifts_cli
from .commands.hotspot_cli import run_hotspot_cli
from .commands.diff2graph_cli import diff_map_cli
from .commands.average_trajmap_cli import avg_trajmap_cli
from colorama import init, Fore, Style
init(convert=False)


"""Time counter"""
def print_final_message(total):
    print(
        Fore.GREEN +
        "\nTrajMapQuick analysis complete. \n" +
        Fore.CYAN +
        "\nAll tasks completed successfully.\n"+
        Style.RESET_ALL
    )
    print(f"Total computation time: {total:.2f} seconds \n" +
        Fore.MAGENTA +
        "\nThank you for using TrajMapQuick 1.0 — ResLaR Labs, Afe Babalola University, Ado-Ekiti Nigeria.\n" +
        Style.RESET_ALL)
    

"""Display logo"""
def main():
    start_time = time.perf_counter()
    init()
    print(Fore.GREEN + r"""

     _______         _ __  __              ____  
    |__   __|       (_)  \/  |            / __ \ 
        | |_ __ __ _ _| \  / | __ _ _ __ | |  | |
        | | '__/ _` | | |\/| |/ _` | '_ \| |  | |
        | | | | (_| | | |  | | (_| | |_) | |__| |
        |_|_|  \__,_| |_|  |_|\__,_| .__/ \___\_\
                   _/ |            | |           
                  |__/             |_|           
          

          """ + Style.RESET_ALL)
    print("========== Welcome to TrajMapQuick 1.0 ==========")
    print("")
    print("Authors : " + Fore.BLUE + "Wande M. Oluyemi, Adeniyi T. Adewumi, Shadrach C. Eze & Stephen C. Nnemolisa @ ResLaR Labs, Afe Babalola University, Ado-Ekiti Nigeria" + Style.RESET_ALL)
    print("")
    print("")

    parser = argparse.ArgumentParser(
        prog="tmq",
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
    A command-line toolkit for MD trajectory map analysis:
    • matrix extraction
    • shift computation
    • visualization

    Built on the original work of Kožić & Bertoša, 2024,
    Trajectory maps: molecular dynamics visualization and analysis,
    https://doi.org/10.1093/nargab/lqad114

    TrajMapQuick is faster, improves batch processing, and allows
    automatic shift detection from trajectory maps.
    """
    )
    
    parser.add_argument(
    "-h", "--help",
    action="help",
    help="Show usage information")

    subparsers = parser.add_subparsers(
        title="Available subcommands",
        dest="command",
        metavar=""
    )

    """SHIFT SUBCOMMAND"""
    shift_parser = subparsers.add_parser(
        "shift",
        help="Extract matrices, compute residue-residue shifts and make plots: For more, use tmq shift --help",
        description=(
            "Converts your trajectory into pdb multimodel form and then to a CSV file, "
            "extracts a distance matrix from the CSV file and computes "
            "a shift value between a residue range over a specified frame.\n\n"
            "Example:\n"
            "  tmq shift --traj traj.pdb --top top.parmtop --str 1 --resr 1-300 --resrs 110-125 --cent backbone --plot --out shift_output\n\n"
            "This will compute the shift of the backbone atoms, for residues 110-125, across the trajectory of a protein with residues 1-300, and will generate plots automatically."),
        formatter_class=argparse.RawTextHelpFormatter
    )

    shift_parser.add_argument("-tr", "--traj", required=True,
                              help="Input trajectory, accepts pdb, nc, xtc xtr")
    shift_parser.add_argument("-to", "--top", required=True,
                              help="Topology file, accepts parmtop, pdb, gro")
    shift_parser.add_argument("-st", "--str", type=int, default=1,
                              help="Stride of the trajectory, (default: 1)")
    shift_parser.add_argument("-rr", "--resr", type=str, required=True,
                              help="Residue range of your protein in the form start-end (e.g., 1-300")
    shift_parser.add_argument("-rs", "--resrs", type=str, required=True,
                              help="Residue range for shift calculation, in the form start-end (e.g., 110-125")
    shift_parser.add_argument("-ce", "--cent", type=str, default="backbone", required=True,
                              help="Centre of calculations, either the backbone " \
                              "atoms or the ca atoms, (default: backbone)")
    shift_parser.add_argument("-ma", "--max", type=int, default=5, required=False,
                              help="Max shift value for color scaling, (default: 5)")
    shift_parser.add_argument("-o", "--out", type=str, required=True,
                              help="Basename for all outputs")
    

    """HOTSPOT SUBCOMMAND"""
    dehot_parser = subparsers.add_parser(
        "hotspot",
        help="Detect hotspots in residue shifts and create plots: For more, use tmq hotspot --help",
        description=(
            "Detect hotspots in residue shifts and creates publication-ready plot with trajectory map"
            "and hotspot regions annotated, and also generates shift graphs for detected hotspot regions.\n\n"
            "Example:\n"
            "  tmq hotspot --traj traj.pdb --top top.parmtop --str 1 --resr 1-300 --cent backbone --out hotspot_output\n\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    dehot_parser.add_argument("-tr", "--traj", required=True,
                              help="Input trajectory, accepts Pdb, nc, xtc xtr")
    dehot_parser.add_argument("-to", "--top", required=True,
                              help="Topology file, accepts .parmtop, pdb, gro")
    dehot_parser.add_argument("-st", "--str", type=int, default=1,
                              help="Stride of the trajectory, (default: 1)")
    dehot_parser.add_argument("-rr", "--resr", type=str, required=True,
                              help="Residue range of your protein in the form start-end (e.g., 1-300")
    dehot_parser.add_argument("-ce", "--cent", type=str, default="backbone", required=True,
                              help="Centre of calculations, either the backbone " \
                              "atoms or the ca atoms, (default: backbone)")
    dehot_parser.add_argument("-win", "--window", type=int, default=5, required=False,
                            help="Rolling window size for smoothing, (default: 5) (Not Required)")
    dehot_parser.add_argument("-md", "--mindist", type=int, default=3, required=False,
                               help="Minimum distance between peaks, (default: 3) (Not Required)")
    dehot_parser.add_argument("-hs", "--hot", type=int, default=10, required=False,
                          help="Number of top peaks to extract, (default: 10) (Not Required)")
    dehot_parser.add_argument("-ma", "--max", type=int, default=5, required=False,
                              help="Max shift value for color scaling, (default: 5) (Not Required)")
    dehot_parser.add_argument("-o", "--out", type=str, required=True,
                              help="Basename for outputs")
    

    """DIFFERENCE SUBCOMMAND"""
    dehot_parser = subparsers.add_parser(
        "diff",
        help="Computes difference between two matrices and creates the difference map: For more, use tmq diff --help",
        description=(
            "Computes difference between two matrices and creates publication-ready plot with difference map.\n\n"
            "The input matrices must be supplied by the names of the output of previous 'Shift' runs.\n\n"
            "A subsequent downstream processing after 'Shift' runs; thus, matrices must have equal lengths.\n\n"
            "Example:\n"
            "  tmq diff --mat1 apo --mat2 holo --resr 1-300 --max 8 --out my_diff\n\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    dehot_parser.add_argument("-m1", "--mat1", required=True,
                              help="First matrix, accepts only the name without extension")
    dehot_parser.add_argument("-m2", "--mat2", required=True,
                              help="Second matrix, accepts only the name without extension")
    dehot_parser.add_argument("-rr", "--resr", type=str, required=True,
                              help="Residue range of your protein in the form start-end (e.g., 1-300")
    dehot_parser.add_argument("-ma", "--max", type=int, default=5, required=True,
                              help="Max shift value for color scaling, (default: 5)")
    dehot_parser.add_argument("-o", "--out", type=str, required=True,
                              help="Basename for outputs")



    """DIFFERENCE SUBCOMMAND"""
    dehot_parser = subparsers.add_parser(
        "average",
        help="Computes average of n matrices and creates the average map: For more, use tmq average --help",
        description=(
            "Computes average of n matrices and creates publication-ready plot with average map. \n\n"
            "The input matrices must be supplied by the names of the output of previous 'Shift' runs as comma separated values.\n\n"
            "A subsequent downstream processing after 'Shift' runs; thus, matrices must have equal lengths.\n\n"
            "Example:\n"
            "  tmq average --mat apo,holo,bound --resr 1-300 --max 8 --out my_avg\n\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    dehot_parser.add_argument("-m", "--mat", required=True, type=str,
                              help="Comma-separated list of matrix names, accepts only the name without extension")
    dehot_parser.add_argument("-rr", "--resr", type=str, required=True,
                              help="Residue range of your protein in the form start-end (e.g., 1-300")
    dehot_parser.add_argument("-ma", "--max", type=int, default=5, required=True,
                              help="Max shift value for color scaling, (default: 5)")
    dehot_parser.add_argument("-o", "--out", type=str, required=True,
                              help="Basename for outputs")


    print("")
    args = parser.parse_args()

    if args.command == "shift":
        traj2pdb_cli(args)
        pdb2csv_cli(args)
        shift_cli(args)
        trajmap_cli(args)
        shift2graph_cli(args)
        end_time = time.perf_counter()
        total = end_time - start_time    
        print_final_message(total)
    elif args.command == "hotspot":
        traj2pdb_cli(args)
        pdb2csv_cli(args)
        trajmap_cli(args)
        detect_shift_cli(args)
        create_submatrices_cli(args)
        run_hotspot_cli(args)  
        slice_shifts_cli(args)
        run_hotspot_cli(args)
        end_time = time.perf_counter()
        total = end_time - start_time    
        print_final_message(total)

    elif args.command == "diff":
        diff_map_cli(args)
        end_time = time.perf_counter()
        total = end_time - start_time    
        print_final_message(total)

    elif args.command == "average":
        avg_trajmap_cli(args)
        end_time = time.perf_counter()
        total = end_time - start_time    
        print_final_message(total)        
        
    else:
        parser.print_help()
        print("")
        print("Cite this as: " + Fore.BLUE + "SHEDOOMTC. (2026). TrajMapQuick: Towards Fast Trajectory Map Analysis and Visualization (v1.0). Zenodo. https://doi.org/10.5281/zenodo.20681061" + Style.RESET_ALL)
        print("")
