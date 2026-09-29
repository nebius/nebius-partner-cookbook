# External follow-ups from first-user feedback

These items are not owned by this repository and require the corresponding product or documentation team.

| Owner | Follow-up | Evidence required for closure |
|---|---|---|
| Token Factory Docs | Replace retired models in Python, JavaScript, and cURL quickstarts; correct the authentication wording. | All samples use a model returned by `/v1/models`; authentication failures are grammatical and actionable. |
| Token Factory Product/SRE | Investigate intermittent multi-minute serverless inference latency from the supplied request traces. | Root-cause note, measured latency distribution, and a supportable timeout/retry recommendation. |
| Token Factory DevRel | Lead evaluation messaging with OpenAI-compatible inference and configuration-only provider switching. | Updated quickstart and partner-evaluation copy. |
| Tavily Product/Docs | Clarify date-filter strictness and make score/domain controls prominent for news grounding. | Reproduction of stale/social results plus documented filtering behavior. |

The repository-side mitigations are the scheduled model-availability check, explicit client timeouts and retries, safe development diagnostics, and Recipe 03 post-filtering.
Do not publish customer benchmark results or traces without explicit permission, and retain sample-size and scorer caveats when permission is granted.
