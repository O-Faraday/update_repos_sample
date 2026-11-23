# update_repos_sample

A synthetic Databricks project to test the dbx_modernizer agent.
It is built to contain known problems: [EXPECTED.md](EXPECTED.md) lists what
the agent should find, file by file. Every name, endpoint, URL and credential
is fake.

## Layout

```
databricks.yml            bundle, variables, targets dev (default) and prod
resources/                jobs, pipeline, schema and volume (included)
src/common/               names and the chat model, shared by the notebooks
src/ingest/               batch, HTTP and streaming loads
src/genai/                vector search, model calls, ai_query
src/legacy/               deprecated patterns, and a copy of them
src/pipeline/             a serverless pipeline (SQL)
manual/                   a job meant to be created by hand, outside the bundle
data/                     demo tables, UC functions and a raw file (catalog demo)
```

## Deploy (no schedule, nothing runs)

```bash
# Set the catalog of your workspace locally (not committed):
mkdir -p .databricks/bundle/dev
echo '{"catalog": "<catalog>"}' > .databricks/bundle/dev/variable-overrides.json
databricks bundle deploy -t dev --profile <profile>
```

Deploying creates the jobs, the pipeline, a schema and a volume; none of
them is scheduled. Then create the job outside the bundle from
`manual/job_created_by_hand.json` (replace the notebook path by the bundle's
files path):

```bash
databricks jobs create --json @manual/job_created_by_hand.json --profile <profile>
```

Load the demo data of `data/` (data/README.md): the code reads and writes
`demo.update_repos_sample`.

Point the agent's `source_root` to the bundle's files path
(`/Workspace/Users/<you>/.bundle/update_repos_sample/dev/files`) and its
`project_schemas` to `demo.update_repos_sample` and the deployed schema.
