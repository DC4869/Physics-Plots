# JSON Configuration Guide

## Project Structure

```json
{
  "id": "project-id",
  "name": "Project Display Name",
  "description": "Brief project description",
  "subpages": [...]
}
```

Note: `id` much match the name of a directory under `src/pages`. 

## Subpage Configuration

```json
{
  "id": "subpage-id",
  "name": "Subpage Display Name",
  "defaultGridCols": 4,
  "plots": [...]
}
```

- `defaultGridCols`: Number of columns for multi-plot grid view (1-6)

Note: `id` much match the name of a `.astro` page in `/src/pages/<project-id>/`; e.g.: `/src/pages/<project-id>/<subpage-id>.astro`

## Plot Types

### 1. Single File Plot

```json
{
  "id": "plot-id",
  "title": "Plot Title",
  "description": "Plot description",
  "axes": { "x": "x-axis label", "y": "y-axis label" },
  "file": "/plots/path/to/plot.pdf"
}
```

### 2. Multi-File Plot

```json
{
  "id": "plot-id",
  "title": "Plot Title",
  "description": "Plot description",
  "axes": { "x": "x-axis label", "y": "y-axis label" },
  "files": [
    "/plots/path/to/plot1.pdf",
    "/plots/path/to/plot2.pdf"
  ]
}
```

### 3. Multi-File Plot with Column Headers

```json
{
  "id": "plot-id",
  "title": "Plot Title",
  "description": "Plot description",
  "axes": { "x": "x-axis label", "y": "y-axis label" },
  "columnHeaders": [
    { "afterIndex": 0, "text": "First Section" },
    { "afterIndex": 5, "text": "Second Section" }
  ],
  "files": [...]
}
```

- `afterIndex`: 0-based position before which header appears
- Header spans full grid width

### 4. Grid Layout Plot

```json
{
  "id": "plot-id",
  "title": "Plot Title",
  "description": "Plot description",
  "axes": { "x": "x-axis label", "y": "y-axis label" },
  "gridLayout": {
    "rowHeader": "Row Label",
    "colHeader": "Column Label",
    "rows": ["Row 1", "Row 2"],
    "cols": ["Col 1", "Col 2", "Col 3"],
    "files": [
      ["/plots/r1c1.pdf", "/plots/r1c2.pdf", "/plots/r1c3.pdf"],
      ["/plots/r2c1.pdf", "/plots/r2c2.pdf", "/plots/r2c3.pdf"]
    ]
  }
}
```

- Creates a table with labeled rows and columns
- `files` is a 2D array matching row/column structure

## Notes

- Supports both PDF and image files (png, jpg, jpeg, gif, webp, svg)
- All file paths are relative to `/public/` directory
- Use consistent naming conventions for easier maintenance
