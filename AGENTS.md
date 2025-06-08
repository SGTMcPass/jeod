# Agent Guidelines for the JEOD Repository

This file provides general instructions for any automated agent contributing to this repository.

## 1. Repository Purpose and License
- JEOD is released under the NASA Open Source Agreement 1.3. Any use must respect the waiver and indemnity clauses in the README and LICENSE files.
- Portions of the README describe the waiver of claims and the license terms. See README lines 39-54 for the indemnity clause and license reference.

## 2. Build Environment
- JEOD targets the Trick simulation environment. Version 19.7.3 or newer is recommended.
- Required environment variables include `JEOD_HOME`, `TRICK_HOME`, `TRICK_VER`, `TRICK_HOST_CPU`, `TRICK_CFLAGS`, and `TRICK_CXXFLAGS`. `TRICK_CFLAGS` and `TRICK_CXXFLAGS` must contain `-I${JEOD_HOME}/models`.
- JEOD 5.3 depends on `swig3` and `cmake3`.
- Simulations are built with the Trick `trick-CP` utility using `S_define` files.

## 3. Regression Tests
- Regression tests reside in `$JEOD_HOME/verif`, `$JEOD_HOME/sims`, and various model `verif` subdirectories.
- Reference test data is distributed as release assets to reduce repository size.
- Some verification tests intentionally fail ("fail" or "FAIL" in the run directory name).

## 4. Code Style
- All new code shall conform to the JEOD Coding Standards. Use `clang-format` with the repository `.clang-format` file.
- Prefer Doxygen style comments for C++ headers and source files.

## 5. Workflow for Automated Agents
1. **Create a new branch for each change.** Use descriptive branch names.
2. **Run `clang-format`** on any edited C++ files before committing.
3. **Build** using `cmake` and `make` where applicable. If the Trick environment is unavailable, document the limitation in the PR.
4. **Run available regression or unit tests** with `pytest` or Trick test harnesses when possible. Note that some tests require the Trick environment; skip with a note if not configured.
5. **Commit messages** should be concise: a one-line summary followed by optional details.
6. **Reference documentation** in PR summaries using file path citations.

