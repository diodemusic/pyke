# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

### Deprecated

### Security

---

## [v3.0.0] - 2026-02-08

### Removed

- Removed pydantic models in favour of lists and dicts

---

## [v2.1.1] - 2025-11-13

### Added

- Added support for all `DataDragon` CDN endpoints
- Added tests for all `DataDragon` CDN endpoints
- Added `create_cdn_tests.py` generator
- Added `[project.optional-dependencies]` for proper dev dependency separation

### Changed

- Changed `_BaseDataDragonClient` and all cdn calls in ddragon to use `_data_dragon_cdn_request` instead of `_data_dragon_request`
- Changed pipeline to run matrix at max parallel 1
- Moved dev dependencies (pytest, mypy, black, etc.) to optional `[dev]` group
- Production dependencies now only include `requests` and `pydantic`
- `python-dotenv` moved to dev dependencies (user's choice for env management)

### Fixed

- Fixed duplicate `self.champion` assignment in `main.py:95`
- Fixed dead code in `league.py:81-84` that was rebuilding the same list twice

### Removed

- Removed two broken ddragon cdn endpoints (`itemmodifiers`, `missionassets`)
- Removed dead code in `league.py:81-84`

## [2.1.0] - 2025-11-01

### Added

- Added Data Dragon support with `DataDragon` class in `main.py:69-74`
- Added `_BaseDataDragonClient` for Data Dragon HTTP handling in `_base_data_dragon_client.py:15-68`
- Added automatic latest version resolution in `_base_data_dragon_client.py:40-50`
  - Fetches latest version from Data Dragon API when `version=None`
  - Graceful error handling for version fetch failures
- Added `VersionsEndpoint` with `get_all_versions()` in `ddragon/versions.py:8`
- Added `ChampionsEndpoint` with `get_all_champions(locale)` in `ddragon/champions.py:12`
- Added comprehensive `Locale` enum with 25+ supported locales in `enums/locale.py`
  - Snake_case naming (e.g., `Locale.united_kingdom`, `Locale.korea`)
- Added Data Dragon usage example in `examples/ddragon.py`

---

## [2.0.0] - 2025-10-31

### Changed

- Replaced print() with logging in `_base_client.py`
- Replaced for loops with list comprehensions

### Removed

- Removed tournament endpoints `tournament.py` and `tournament_stub.py`

---

## [1.4.1] - 2025-10-30

### Added

- Initial changelog setup
- Added retry logic with exponential backoff for server errors in `_base_client.py:178-194`
- Added configurable timeout in `_base_client.py:125`
- Added configurable retry parameters to `Pyke` constructor in `main.py`
- Added intelligent backoff strategies:
  - 504 Gateway Timeout: 10s base exponential backoff (10s, 20s, 40s)
  - 502/503 Server Errors: 5s base exponential backoff (5s, 10s, 20s)

### Changed

- Filter None params explicitly in `match.py:52-59`
- Changed ValueError to JSONDecodeError in `_base_client.py:109`
- Changed default timeout from 30s to 60s for slow endpoints
- Separated retry logic: rate limit (429) and server errors (502/503/504) now use independent retry counters
- Updated `_BaseApiClient.__init__()` to accept separate retry configuration parameters
- Updated timeout test to reflect new 60s default in `tests/test_timeout.py`

### Fixed

- Fixed type annotation mismatch in `clash.py:97,106`
- Fixed return type in match endpoint `match.py:64`
- Fixed type coercion in `champion_mastery.py:106`
- Fixed mutable default arguments in `base_client.py:158,164`
- Fixed league_exp parameter name in `league_exp.py:38`
- Fixed region enum case consistency in `region.py:10`
- Fixed fragile header parsing in `_base_client.py:44-84`
- Fixed infinite retry issue for 502/503/504 errors in `_base_client.py`

### Removed

- Removed dead code in `clash.py:91`
- Removed retry on 502 in `_base_client.py:145`
- Removed unused `Mock` import from `tests/test_timeout.py`

---

## Category Guidelines:

- **Added**: New features, endpoints, or functionality
- **Changed**: Changes to existing functionality (breaking or non-breaking)
- **Fixed**: Bug fixes, type corrections, parameter fixes
- **Removed**: Removed features, dead code removal
- **Deprecated**: Features marked for removal in future versions
- **Security**: Security fixes or improvements

## Semantic Versioning Quick Reference:

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes
- **MINOR** (1.0.0 → 1.1.0): New features (backwards compatible)
- **PATCH** (1.0.0 → 1.0.1): Bug fixes (backwards compatible)
