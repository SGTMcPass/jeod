# Changelog

## [0.1.7] - Coverage workflow
- Added coverage reporting via pytest-cov with 100% threshold.
- Workflow now uploads coverage.xml as an artifact.
- Bumped version to 0.1.7.

## [0.1.6] - Testing and CI
- Added unit tests and GitHub Actions workflow to run pytest.
- Bumped version to 0.1.6.


## [0.1.5] - CLI interface
- Added a CLI with `generate` and `version` commands
  that ties into the `InputBuilder` helper.
- Bumped version to 0.1.5.

## [0.1.4] - Input builder class
- Added ``InputBuilder`` that records body initialization actions for
  ``dynamics.dyn_manager``.
- Updated documentation and bumped version to 0.1.4.

## [0.1.3] - Logging and events
- Added wrappers for `trick.add_data_record_group` and event scheduling with
  timestamped logging.
- Bumped version to 0.1.3.

## [0.1.2] - State and gravity helpers
- Added translation and rotation state utilities with unit handling.
- Added gravity configuration helpers including spherical harmonics.

## [0.1.1] - Vehicle helpers
- Added `JeodHelperError` exception class.
- Implemented `create_dyn_body`, `set_mass_properties`, and `attach_body` with logging.

## [0.1.0] - Initial release
- Package scaffold with version metadata.
