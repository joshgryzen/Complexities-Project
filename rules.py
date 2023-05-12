import numpy as np

# Rule 110
rule_110 = np.zeros((2, 2, 2), dtype=int)
rule_110[0, 0, 0] = 0
rule_110[0, 0, 1] = 1
rule_110[0, 1, 0] = 1
rule_110[0, 1, 1] = 1
rule_110[1, 0, 0] = 0
rule_110[1, 0, 1] = 1
rule_110[1, 1, 0] = 1
rule_110[1, 1, 1] = 0

# rule 30
rule_30 = np.zeros((2, 2, 2), dtype=int)
rule_30[0, 0, 0] = 0
rule_30[0, 0, 1] = 1
rule_30[0, 1, 0] = 1
rule_30[0, 1, 1] = 1
rule_30[1, 0, 0] = 1
rule_30[1, 0, 1] = 0
rule_30[1, 1, 0] = 0
rule_30[1, 1, 1] = 0

# rule 158
rule_158 = np.zeros((2, 2, 2), dtype=int)
rule_158[0, 0, 0] = 0
rule_158[0, 0, 1] = 1
rule_158[0, 1, 0] = 1
rule_158[0, 1, 1] = 1
rule_158[1, 0, 0] = 1
rule_158[1, 0, 1] = 0
rule_158[1, 1, 0] = 0
rule_158[1, 1, 1] = 1

# rule 150
rule_150 = np.zeros((2, 2, 2), dtype=int)
rule_150[0, 0, 0] = 0
rule_150[0, 0, 1] = 1
rule_150[0, 1, 0] = 1
rule_150[0, 1, 1] = 0
rule_150[1, 0, 0] = 1
rule_150[1, 0, 1] = 0
rule_150[1, 1, 0] = 0
rule_150[1, 1, 1] = 1

# rule 182
rule_182 = np.zeros((2, 2, 2), dtype=int)
rule_182[0, 0, 0] = 0
rule_182[0, 0, 1] = 1
rule_182[0, 1, 0] = 1
rule_182[0, 1, 1] = 0
rule_182[1, 0, 0] = 1
rule_182[1, 0, 1] = 1
rule_182[1, 1, 0] = 0
rule_182[1, 1, 1] = 1

# rule 90
rule_90 = np.zeros((2, 2, 2), dtype=int)
rule_90[0, 0, 0] = 0
rule_90[0, 0, 1] = 1
rule_90[0, 1, 0] = 0
rule_90[0, 1, 1] = 1
rule_90[1, 0, 0] = 1
rule_90[1, 0, 1] = 0
rule_90[1, 1, 0] = 1
rule_90[1, 1, 1] = 0

# rule 62
rule_62 = np.zeros((2, 2, 2), dtype=int)
rule_62[0, 0, 0] = 0
rule_62[0, 0, 1] = 1
rule_62[0, 1, 0] = 1
rule_62[0, 1, 1] = 1
rule_62[1, 0, 0] = 1
rule_62[1, 0, 1] = 1
rule_62[1, 1, 0] = 0
rule_62[1, 1, 1] = 0

# rule 126
rule_126 = np.zeros((2, 2, 2), dtype=int)
rule_126[0, 0, 0] = 0
rule_126[0, 0, 1] = 1
rule_126[0, 1, 0] = 1
rule_126[0, 1, 1] = 1
rule_126[1, 0, 0] = 1
rule_126[1, 0, 1] = 1
rule_126[1, 1, 0] = 1
rule_126[1, 1, 1] = 0

# rule 54
rule_54 = np.zeros((2, 2, 2), dtype=int)
rule_54[0, 0, 0] = 0
rule_54[0, 0, 1] = 1
rule_54[0, 1, 0] = 1
rule_54[0, 1, 1] = 0
rule_54[1, 0, 0] = 1
rule_54[1, 0, 1] = 1
rule_54[1, 1, 0] = 0
rule_54[1, 1, 1] = 0

# rule 94
rule_94 = np.zeros((2, 2, 2), dtype=int)
rule_94[0, 0, 0] = 0
rule_94[0, 0, 1] = 1
rule_94[0, 1, 0] = 1
rule_94[0, 1, 1] = 1
rule_94[1, 0, 0] = 1
rule_94[1, 0, 1] = 0
rule_94[1, 1, 0] = 1
rule_94[1, 1, 1] = 0

# idk what rule this is but its cool
# rule = np.zeros((2, 2, 2), dtype=int)
# rule[0, 0, 0] = 0
# rule[0, 0, 1] = 1
# rule[0, 1, 0] = 1
# rule[0, 1, 1] = 0
# rule[1, 0, 0] = 1
# rule[1, 0, 1] = 0
# rule[1, 1, 0] = 1
# rule[1, 1, 1] = 0

rules = {
    "Rule 110": rule_110,
    "Rule 30": rule_30,
    "Rule 158": rule_158,
    "Rule 150": rule_150,
    "Rule 182": rule_182,
    "Rule 90": rule_90,
    "Rule 62": rule_62,
    "Rule 126": rule_126,
    "Rule 54": rule_54,
    "Rule 94": rule_94,
}
