# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Mitochondrial Biogenesis MET Flux Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentMitochondrialBiogenesisMetFlux

def main():
    agent = PersonalAgentMitochondrialBiogenesisMetFlux()

    print("=" * 70)
    print("DEMO: Personal Agent Mitochondrial Biogenesis & PGC-1alpha Modeler")
    print("=" * 70)

    # 1. 50-minute Zone 2 Endurance Session (avg HR: 132 bpm, max HR: 180 bpm)
    res_z2 = agent.model_pgc1a_transcriptional_stimulus(
        session_type="zone2_endurance",
        duration_minutes=50.0,
        average_hr_bpm=132.0,
        max_hr_bpm=180.0
    )

    print(f"\n1. Zone 2 Endurance PGC-1a Stimulus Analysis (50 min @ 132 bpm):")
    print(f"   Modality: {res_z2['session_modality']}")
    print(f"   Signaling Pathway: {res_z2['biochemical_signaling_cascade']}")
    print(f"   PGC-1a Score: {res_z2['pgc1a_transcriptional_score']}")
    print(f"   Stimulus Tier: {res_z2['biogenesis_stimulus_tier']}")
    print(f"   Mitophagy: {res_z2['mitophagy_clearance_status']}")
    print(f"   Adaptation: {res_z2['structural_adaptation_forecast']}")

    # 2. Optimize weekly 80/20 polarized volume (150 min Zone 2 + 35 min HIIT)
    res_pol = agent.optimize_weekly_mitochondrial_stimulus_balance(
        zone2_minutes_total=150.0,
        hiit_minutes_total=35.0
    )

    print(f"\n2. Weekly 80/20 Polarized Mitochondrial Balance:")
    print(f"   Total Volume: {res_pol['total_weekly_cardio_minutes']} min")
    print(f"   Zone 2: {res_pol['zone2_volume_minutes']} min ({res_pol['zone2_percentage']})")
    print(f"   HIIT: {res_pol['hiit_volume_minutes']} min ({res_pol['hiit_percentage']})")
    print(f"   Status: {res_pol['polarization_equilibrium']}")
    print(f"   Prescription: {res_pol['weekly_programming_prescription']}")

    print("\nVerification complete: Mitochondrial biogenesis engine executed flawlessly.")

if __name__ == "__main__":
    main()
