// Bootstrap state for window.SENTINEL_DATA. Every slice is hydrated from the
// backend on mount (see useForgeData in app-forge.jsx); evalResults starts
// empty so a failed /api/eval-results fetch shows the loading/empty state
// instead of silently rendering stale mock numbers as real data.
window.SENTINEL_DATA = {
  evalResults: {},

  // The question raced in the Compare tab when /api/dataset is unavailable —
  // drawn from negation_gap.
  raceQuestion: {
    id: "q-042",
    category: "negation_gap",
    difficulty: "hard",
    sop_id: "SOP-ISEC-008",
    sopTitle: "Cryptographic Controls and Key Management",
    regulations_involved: ["HIPAA Security Rule", "SOC 2 CC6.1"],
    expected_compliance_level: "non_compliant",
    question: "Review SOP-ISEC-008 (Cryptographic Controls and Key Management). Does it satisfy 45 CFR 164.312(a)(2)(iv) — encryption and decryption of ePHI — and SOC 2 CC6.1 logical access controls? Identify any specific safeguards that are missing or vague.",
  },
};
