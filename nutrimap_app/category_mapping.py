
import numpy as np
import pandas as pd

def assign_food_group(row):
    """
    Classify a food into a coarse food group using only nutrient data (per 100 g).

    Expected columns:
      - energy_kcal_calculated
      - protein_g
      - carbs_g
      - fiber_g
      - fat_g
      - satfat_g

    Returns:
      category: str
    """

    kcal     = float(row.get("energy_kcal_calculated", 0.0))
    protein  = float(row.get("protein_g", 0.0))
    carbs    = float(row.get("carbs_g", 0.0))
    fiber    = float(row.get("fiber_g", 0.0))
    fat      = float(row.get("fat_g", 0.0))
    satfat   = float(row.get("satfat_g", 0.0))

    # Safe denominators
    kcal_safe  = max(kcal, 1e-6)
    carbs_safe = max(carbs, 1e-6)

    # Ratios
    Pshare = 4 * protein / kcal_safe
    Cshare = 4 * carbs   / kcal_safe
    Fshare = 9 * fat     / kcal_safe

    # ------------------------
    # 1) Oils & fats
    # ------------------------
    if fat >= 80 or Fshare >= 0.85:
        return "oils_fats"

    # ------------------------
    # 2) Nuts & seeds
    # ------------------------
    if 40 <= fat < 80 and protein >= 10 and fiber >= 5:
        return "nuts_seeds"

    # ------------------------
    # 3) Dairy (lean vs fatty) – WITHOUT sodium
    # ------------------------
    dairy_candidate = (
        protein >= 3 and
        carbs  >= 3 and
        satfat  >= 1.5
    )

    if dairy_candidate:
        # Lean dairy (milk, yogurt, skyr)
        if fat < 5 and satfat < 3 and kcal <= 120:
            return "dairy_lean"

        # Fatty dairy (cheese, cream)
        if fat >= 15 or satfat >= 5 or kcal >= 200:
            return "dairy_fatty"

        # Between → assign by kcal/fat
        if fat <= 8 and kcal <= 150:
            return "dairy_lean"
        else:
            return "dairy_fatty"

    # ------------------------
    # 4) Legumes / pulses (canned and dried)
    # ------------------------

    # CANNED/COOKED LEGUMES:
    canned_legume = (
        5  <= protein <= 12 and
        10 <= carbs   <= 25 and
        fiber >= 3 and
        fat   < 10 and
        60 <= kcal <= 180
    )

    # DRIED/VERY DENSE LEGUMES:
    dried_legume = (
        protein >= 15 and
        carbs   >= 30 and
        fiber   >= 10 and
        fat     < 15 and
        kcal    >= 250
    )

    if canned_legume or dried_legume:
        return "legumes_pulses"

    # ------------------------
    # 5) Protein foods (meat, poultry, fish, eggs)
    # ------------------------
    protein_food_candidate = (protein >= 15 and carbs < 5)

    if protein_food_candidate:
        # Eggs
        if (8 <= fat <= 12 and 2 <= satfat <= 4 and 130 <= kcal <= 180):
            return "eggs"

        # Fish / seafood
        if fat <= 15 and satfat <= 3 and kcal <= 180:
            return "fish_seafood"

        # Poultry
        if fat <= 10 and satfat <= 4:
            return "poultry"

        # Red / processed meat
        if fat > 10 or satfat > 4:
            return "meat_red"

    # ------------------------
    # 6) Sweets / snacks
    # ------------------------
    if  carbs >= 20 and kcal >= 250:
        return "sweets_snacks"

    # ------------------------
    # 7) Fruit
    # ------------------------
    if (
        carbs >= 8 and
        fat < 5 and
        fiber >= 1.5 and
        kcal < 120
    ):
        return "fruit_sweet"

    # ------------------------
    # 8) Non-starchy vegetables
    # ------------------------
    if (
        kcal < 80 and
        carbs < 15 and
        fiber >= 2
    ):
        return "nonstarchy_veg"

    # ------------------------
    # 9) Starchy vegetables
    # ------------------------
    if (
        15 <= carbs <= 30 and
        60 <= kcal <= 130 and
        fiber >= 2
    ):
        return "starchy_veg"

    # ------------------------
    # 10) Grain / starch (single group)
    # ------------------------
    if (
        carbs >= 45 and
        fat < 10 and
        kcal >= 200
    ):
        return "grain_starch"

    # ------------------------
    # 11) Fallback
    # ------------------------
    return "mixed/other"