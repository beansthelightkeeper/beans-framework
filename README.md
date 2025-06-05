# Beans Framework Cleanup Guide

This repository now includes a `.gitignore` file to prevent common temporary files from being committed. If you previously committed macOS artifact files such as `.DS_Store`, remove them with the following command:

```bash
find . -name '.DS_Store' -delete
```

Likewise, to remove log files that are no longer needed, run:

```bash
find . -name '*.log' -delete
```

After cleaning up, verify that no undesired files remain with `git status` and commit the changes.
