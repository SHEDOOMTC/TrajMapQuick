from setuptools import setup, find_packages

setup(
    name="tmq",
    version="1.0",
    description = "Trajectory map analysis toolkit",
    authors = "Wande M. Oluyemi (PhD), Adeniyi Adewumi (PhD), Shadrach Eze @ ResLaR Labs, Afe Babalola University, Nigeria",
    readme = "README.md",
    python_requires = ">=3.9",
    packages=find_packages(include=["tmq", "tmq.*"]),
    include_package_data=True,
    extras_require={"md": ["mdtraj"],},
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "tqdm",
        "biopython",
        "scipy",
        "netcdf4",
        "colorama"

    ],
    entry_points={
        "console_scripts": [
            "tmq=tmq.cli:main",
        ]
    },
)
