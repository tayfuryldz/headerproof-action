# HeaderProof Action

Official composite action for running HeaderProof in CI.

```yaml
- uses: TayfurYldz/headerproof-action@v1
  with:
    target: https://example.com
    severity: high,medium
    output: headerproof.sarif
```

The action preserves HeaderProof exit semantics. Set `fail-on-findings: "false"` when a finding should be exported without failing the step.
