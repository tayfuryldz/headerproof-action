# HeaderProof Action

Official composite action for running HeaderProof in CI.

```yaml
- uses: TayfurYldz/headerproof-action@v1
  with:
    target: https://example.com
    severity: high,medium
    output: headerproof.sarif
```

The action is versioned independently from the HeaderProof scanner. The `v1` major tag tracks compatible v1 action releases, while the `version` input selects the HeaderProof scanner release (`latest` by default).

The action preserves HeaderProof exit semantics: `0` no verified finding, `1` verified finding, `2` scan error, and `130` operator interruption. Set `fail-on-findings: "false"` when a finding should be exported without failing the step.
