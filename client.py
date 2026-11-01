# -*- coding: utf-8 -*-
"""
Personal Agent Mitochondrial Biogenesis MET Flux Client
Zero-dependency PGC-1alpha transcriptional induction modeler, CaMK vs. AMPK pathway
partitioner, and 80/20 polarized mitochondrial density training optimizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentMitochondrialBiogenesisMetFlux:
    """
    Quantifies cellular mitochondrial adaptations, tracking PGC-1alpha transcriptional upregulation,
    differentiating CaMK/p38 MAPK continuous volume signaling from AMPK sprint signaling.
    """

    def model_pgc1a_transcriptional_stimulus(
        self,
        session_type: str = "zone2_endurance",
        duration_minutes: float = 45.0,
        average_hr_bpm: float = 135.0,
        max_hr_bpm: float = 185.0
    ) -> Dict[str, Any]:
        """
        Models Peroxisome Proliferator-Activated Receptor Gamma Coactivator 1-alpha (PGC-1a)
        transcriptional activation, the master regulator of mitochondrial biogenesis and cristae density.
        """
        stype = str(session_type).lower()
        dur = max(5.0, min(240.0, float(duration_minutes)))
        avg_hr = max(60.0, min(220.0, float(average_hr_bpm)))
        mhr = max(120.0, min(230.0, float(max_hr_bpm)))

        intensity_pct = avg_hr / mhr

        if "sprint" in stype or "hiit" in stype or "sit" in stype or intensity_pct >= 0.85:
            # High-intensity interval / sprint mode: AMPK pathway dominant
            # Driven by high cellular AMP:ATP ratio and severe glycogen depletion
            pathway = "AMPK (AMP-Activated Protein Kinase) Phosphorylation"
            mechanic = "Acute energy charge depletion triggers rapid nuclear translocation of PGC-1a."
            # High intensity saturates quickly: max stimulus reached in 15-25 minutes
            raw_stimulus = (intensity_pct * 65.0) + min(35.0, dur * 1.4)
            mitophagy_rate = "High: Vigorous fragmentation and autophagic clearance of damaged mitochondria."
            mitochondrial_adaptation = "Increased mitochondrial enzyme efficiency, electron transport chain protein density, and cristae folding."
        else:
            # Low-intensity steady state / Zone 2: CaMK & p38 MAPK pathway dominant
            # Driven by continuous cytosolic calcium [Ca2+] flux and sustained lipid oxidation
            pathway = "CaMK (Calmodulin-Dependent Protein Kinase) & p38 MAPK Activation"
            mechanic = "Sustained calcium oscillation promotes transcription factor binding to mitochondrial promoters."
            # Low intensity requires duration: ramps linearly up to 90 minutes
            raw_stimulus = (intensity_pct * 30.0) + min(65.0, (dur / 90.0) * 65.0)
            mitophagy_rate = "Moderate: Steady turnover with zero excessive free-radical oxidative damage."
            mitochondrial_adaptation = "Expanded total mitochondrial volume, capillary network angiogenesis, and increased fat oxidation capacity."

        pgc1a_score = round(min(100.0, max(10.0, raw_stimulus)), 1)

        # Post-exercise PGC-1a mRNA expression peak window (typically 2 - 6 hours post-workout)
        if pgc1a_score >= 75.0:
            tier = "Robust Mitochondrial Biogenesis Signal (High PGC-1a Induction)"
            recovery_hours = 24.0 if "zone2" in stype else 48.0
        elif pgc1a_score >= 45.0:
            tier = "Moderate Mitochondrial Maintenance Signal"
            recovery_hours = 18.0
        else:
            tier = "Sub-Threshold Stimulus (Minimal Biogenesis Triggered)"
            recovery_hours = 12.0

        return {
            "session_modality": "High-Intensity Interval (AMPK Pathway)" if "sprint" in stype or intensity_pct >= 0.85 else "Zone 2 Low-Intensity (CaMK Pathway)",
            "duration_minutes": dur,
            "average_heart_rate_bpm": avg_hr,
            "cardiac_intensity_percentage": f"{round(intensity_pct * 100, 1)}% Max HR",
            "biochemical_signaling_cascade": pathway,
            "pgc1a_transcriptional_score": f"{pgc1a_score} / 100",
            "biogenesis_stimulus_tier": tier,
            "mitophagy_clearance_status": mitophagy_rate,
            "structural_adaptation_forecast": mitochondrial_adaptation,
            "cellular_recovery_window_hours": recovery_hours
        }

    def optimize_weekly_mitochondrial_stimulus_balance(
        self,
        zone2_minutes_total: float,
        hiit_minutes_total: float
    ) -> Dict[str, Any]:
        """
        Applies Dr. Stephen Seiler's 80/20 Polarized Training model to balance
        Zone 2 volume (structural mitochondrial network) with HIIT/SIT (efficiency).
        """
        z2 = max(0.0, float(zone2_minutes_total))
        hiit = max(0.0, float(hiit_minutes_total))
        total = z2 + hiit

        if total == 0:
            return {"error": "Total training volume is zero."}

        z2_pct = round((z2 / total) * 100.0, 1)
        hiit_pct = round((hiit / total) * 100.0, 1)

        # Polarized 80/20 benchmark evaluation
        if 75.0 <= z2_pct <= 85.0:
            distribution_status = "Optimal 80/20 Polarized Distribution (Peak Mitochondrial Density & Longevity)"
            guidance = "Perfect equilibrium. Maximum PGC-1a biogenesis with zero autonomic overtraining."
        elif z2_pct < 70.0:
            distribution_status = "Over-Indexed on High Intensity (Excessive Sympathetic / Cortisol Strain)"
            guidance = "Shift 30-40 minutes from HIIT to pure Zone 2 to prevent autonomic plateau and glycogen depletion."
        else:
            distribution_status = "Pure Aerobic Base (Minimal High-Velocity Cristae Stress)"
            guidance = "Add one weekly 15-minute 4x4 VO2max session to activate the acute AMPK-PGC-1a biogenesis arm."

        return {
            "total_weekly_cardio_minutes": total,
            "zone2_volume_minutes": z2,
            "zone2_percentage": f"{z2_pct}% (Target: 80%)",
            "hiit_volume_minutes": hiit,
            "hiit_percentage": f"{hiit_pct}% (Target: 20%)",
            "polarization_equilibrium": distribution_status,
            "weekly_programming_prescription": guidance
        }
