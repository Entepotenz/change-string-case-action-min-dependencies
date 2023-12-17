# change-string-case-action-min-dependencies
Github Action: Make a string lowercase, uppercase, or capitalized

this runs in pure python without any additional packages or dependencies!

 ## features:
 - support for UTF-8 strings
 - minimal dependencies (small footprint)
 - this action has tests to guarantee a smooth experience for you

## What do you mean by "minimal dependencies"
- using only simple standard python3
- here a list of typical advantages for this approach:
    - no dependency on a specific execution environment
        - no need to update the action
    - less code -> less bugs -> less security issues
        - total number of code lines: 14

## inspiration for this project:
from this project: https://github.com/ASzc/change-string-case-action

# usage

# Change String Case GitHub Action

This action accepts any string, and outputs three different versions of that string:

- lowercase (`XyZzY` -> `xyzzy`)
- uppercase (`XyZzY` -> `XYZZY`)
- capitalized (`Xyzzy` -> `Xyzzy`)

You can access the outputted strings through the job outputs context. See docs [here](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjobs_idoutputs), or the Example Usage section below.

## Inputs

### `string`

**Required** The string you want manipulated

## Outputs

### `lowercase`

```python
lowercase="${{ inputs.string }}".lower()
```

Example: `XyZzY` -> `xyzzy`

### `uppercase`

```python
uppercase="${{ inputs.string }}".upper()
```

Example: `XyZzY` -> `XYZZY`

### `capitalized`

```python
lowercase="${{ inputs.string }}".lower()
uppercase="${{ inputs.string }}".upper()
capitalized=f'{uppercase[:1]}{lowercase[1:]}'
```

Example: `XyZzY` -> `Xyzzy`

## Example Usage

```yaml
name: SomeWorkflow
jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - id: string
        uses: Entepotenz/change-string-case-action@v1
        with:
          string: XyZzY
      - id: step2
        run: echo ${{ steps.string.outputs.lowercase }}
      - id: step3
        run: echo ${{ steps.string.outputs.uppercase }}
      - id: step4
        run: echo ${{ steps.string.outputs.capitalized }}
```
